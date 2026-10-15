#!/usr/bin/env python3
"""account_list_check.py: coverage, source and verification checks for account research.

Standard library only, no network, writes no files.

Inputs:
  --list      the user's account list: a text file with one account per line, or a CSV
              with an "account" column
  --research  the research table, a CSV with these columns:
                account,field,value,source,status,verified_by,checked_on
              status       verified | unverified | not found
              source       one or more public links, separated by " | " or ";",
                           or the user's file and row ("file: crm-export.csv row 12")
              verified_by  the connector that verified the row (for example the user's CRM
                           for the user's own records, or an enrichment tool whose row a
                           second source in the source column confirms), or empty when
                           verified on the web
  --ban       domains the user banned, comma separated (for example "example-screener.com")
  --min-web   web sources needed to call a row verified without a connector (default 2)
  --enrichment names of enrichment or technographic tools, comma separated (for example
              "ToolA,ToolB"); a row verified_by one of them must also carry at least one
              web source in the source column that is not on the tool's own site, because an
              enrichment row alone is a lead

What it checks:
  - every account on the list has at least one row (coverage), and rows for accounts
    that are not on the list
  - possible duplicates on the list (same name once legal suffixes are removed)
  - every row has a status; "not found" rows carry no value; a verified or unverified row
    carries a value (N/A, NA, none, unknown, TBD or a lone dash counts as empty); every row
    names its field
  - an empty account list, or a research table with no rows, is a problem
  - a verified row has a connector named, or at least --min-web links from different
    domains; a row verified by a tool named in --enrichment also needs a web source
  - no row uses a banned domain, written as a link or as a bare site name
  - then prints two lists: verified rows and unverified rows, per account

Exit code: 0 when no problem was found, 1 when a problem was found, 2 when a file could
not be read.
"""
import argparse
import csv
import io
import json
import re
import sys
from urllib.parse import urlparse

SUFFIXES = {"limited", "ltd", "pvt", "private", "inc", "incorporated", "llc", "llp", "corp", "corporation",
            "plc", "co", "company", "gmbh", "sa", "ag", "bv", "technologies", "technology", "solutions",
            "systems", "software", "esolutions", "group", "holdings", "the"}
STATUSES = {"verified", "unverified", "not found"}
# S6 (1.0.2): a value that only says it is missing counts as empty, as an empty value does
EMPTY_WORDS = {"n/a", "na", "none", "unknown", "tbd", "-", "\u2013", "\u2014"}
COLUMNS = ["account", "field", "value", "source", "status", "verified_by", "checked_on"]


def utf8_output():
    """Write UTF-8, so a rupee sign, a Unicode minus or a curly quote never stops the script on a Windows console or pipe
    set to code page 1252 (S2, version 1.0.2). A stream that cannot be reconfigured (a test buffer) is left as it is."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def norm(name):
    words = re.sub(r"[^a-z0-9 ]+", " ", (name or "").lower()).split()
    while words and words[-1] in SUFFIXES:
        words.pop()
    while words and words[0] == "the":
        words.pop(0)
    return " ".join(words)


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def parse_list(text):
    lines = [l for l in text.splitlines() if l.strip()]
    if lines and "account" in [c.strip().lower() for c in next(csv.reader([lines[0]]))]:
        reader = csv.DictReader(io.StringIO(text))
        key = [k for k in reader.fieldnames if k.strip().lower() == "account"][0]
        return [r[key].strip() for r in reader if (r.get(key) or "").strip()]
    return [l.strip() for l in lines]


def domains(source):
    out = []
    for part in re.split(r"\s*\|\s*|\s*;\s*", source or ""):
        part = part.strip()
        if part.startswith("http://") or part.startswith("https://"):
            host = urlparse(part).hostname or ""
            host = host[4:] if host.startswith("www.") else host
            out.append(host)
    return out


BARE_HOST = re.compile(r"^(?:www\.)?([a-z0-9-]+(?:\.[a-z0-9-]+)+)(?:/\S*)?$", re.I)


def all_hosts(source):
    """Hosts in links and in bare site names ("screener.in/company/x"), for the banned check only."""
    out = list(domains(source))
    for part in re.split(r"\s*\|\s*|\s*;\s*", source or ""):
        part = part.strip()
        m = BARE_HOST.match(part)
        if m and not part.lower().startswith(("http://", "https://")):
            out.append(m.group(1).lower())
    return out


def check(accounts, rows, banned=(), min_web=2, enrichment=()):
    problems = []
    enrichment = [e.strip().lower() for e in enrichment if e.strip()]
    banned = [b.strip().lower().lstrip(".") for b in banned if b.strip()]
    seen = {}
    dups = []
    for a in accounts:
        k = norm(a)
        if k in seen:
            dups.append((seen[k], a))
        else:
            seen[k] = a
    for first, second in dups:
        problems.append("possible duplicate on the list: '%s' and '%s' (check by hand)" % (first, second))
    if not accounts:
        problems.append("the account list is empty: add the accounts to research before calling the list done")
    if not rows:
        problems.append("the research table has no rows: every account needs at least one row, a not found row included")
    covered = {}
    extra = set()
    for i, r in enumerate(rows, 2):
        acc = (r.get("account") or "").strip()
        k = norm(acc)
        status = (r.get("status") or "").strip().lower()
        src = (r.get("source") or "").strip()
        value = (r.get("value") or "").strip()
        field = (r.get("field") or "").strip() or "(no field)"
        if not (r.get("field") or "").strip():
            problems.append("row %d %s: has no field name; name the field the value answers" % (i, acc))
        if k not in seen:
            extra.add(acc)
        covered.setdefault(k, []).append(r)
        if status not in STATUSES:
            problems.append("row %d %s / %s: status '%s'; use verified, unverified or not found" % (i, acc, field, status))
        if status == "not found" and value:
            problems.append("row %d %s / %s: marked not found but has a value" % (i, acc, field))
        if status in ("verified", "unverified") and not value:
            problems.append("row %d %s / %s: %s row has no value; give the value or mark it not found" % (i, acc, field, status))
        elif status in ("verified", "unverified") and value.lower() in EMPTY_WORDS:
            problems.append("row %d %s / %s: %s row has no value ('%s' counts as empty); give the value or mark it not found" % (i, acc, field, status, value))
        if status in ("verified", "unverified") and not src:
            problems.append("row %d %s / %s: has no source" % (i, acc, field))
        doms = domains(src)
        for d in all_hosts(src):
            for b in banned:
                if d == b or d.endswith("." + b):
                    problems.append("row %d %s / %s: uses banned source %s" % (i, acc, field, d))
        if status == "verified":
            connector = (r.get("verified_by") or "").strip()
            if not connector and len(set(doms)) < min_web:
                problems.append("row %d %s / %s: verified needs a connector or %d web sources from different domains (has %d)" % (
                    i, acc, field, min_web, len(set(doms))))
            tool_key = re.sub(r"[^a-z0-9]", "", connector.lower())
            independent = [d for d in doms if not tool_key or tool_key not in re.sub(r"[^a-z0-9]", "", d.lower())]
            if connector and connector.lower() in enrichment and not independent:
                problems.append("row %d %s / %s: verified by an enrichment tool (%s) needs a second source in the source column "
                                "(the account's own page, a filing, a joint case study or another independent source; a page on the tool's own site does not count)" % (i, acc, field, connector))
    missing = [a for a in accounts if norm(a) not in covered]
    for a in missing:
        problems.append("not covered: %s has no rows" % a)
    for a in sorted(extra):
        problems.append("row for an account not on the list: %s" % a)
    lists = {"verified": {}, "unverified": {}}
    for k, rs in covered.items():
        name = seen.get(k, rs[0].get("account", k))
        for r in rs:
            st = (r.get("status") or "").strip().lower()
            bucket = "verified" if st == "verified" else "unverified"
            lists[bucket].setdefault(name, []).append("%s (%s)" % ((r.get("field") or "").strip(), st or "no status"))
    unique = len(seen)
    return {
        "accounts_on_list": len(accounts), "unique_accounts": unique,
        "covered": len([k for k in seen if k in covered]),
        "missing": missing, "problems": problems, "lists": lists,
    }


def render(res):
    lines = ["Coverage: %d of %d unique accounts have rows (%d names on the list)" % (
        res["covered"], res["unique_accounts"], res["accounts_on_list"])]
    for title in ("verified", "unverified"):
        lines.append("%s list:" % title.capitalize())
        if not res["lists"][title]:
            lines.append("  (none)")
        for acc in sorted(res["lists"][title]):
            lines.append("  %s: %s" % (acc, "; ".join(res["lists"][title][acc])))
    if res["problems"]:
        lines.append("Problems: %d" % len(res["problems"]))
        for p in res["problems"]:
            lines.append("  " + p)
    else:
        lines.append("Problems: none")
    return "\n".join(lines)


def main(argv=None):
    utf8_output()
    ap = argparse.ArgumentParser(description="Coverage, source and verification checks for account research.")
    ap.add_argument("--list", required=True, dest="list_path")
    ap.add_argument("--research", required=True)
    ap.add_argument("--ban", default="", help="banned domains, comma separated")
    ap.add_argument("--min-web", type=int, default=2)
    ap.add_argument("--enrichment", default="", help="enrichment or technographic tool names, comma separated")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        accounts = parse_list(read_text(a.list_path))
        text = read_text(a.research)
    except (OSError, UnicodeDecodeError) as e:
        print("Could not read a file: %s. Stop and ask the user for a readable copy; do not fill rows from memory." % e)
        return 2
    reader = csv.DictReader(io.StringIO(text))
    missing_cols = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
    if missing_cols:
        print("Could not read the research table: missing columns %s" % ", ".join(missing_cols))
        return 2
    res = check(accounts, list(reader), a.ban.split(","), a.min_web, a.enrichment.split(","))
    print(json.dumps(res, indent=2) if a.json else render(res))
    return 1 if res["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
