#!/usr/bin/env python3
"""claims_scan.py: seed a claims register and run the date checks on a text.

What it does (standard library only, no network, writes no files):
  1. Splits the text into sentences and lists every sentence that carries a
     checkable claim: a number, money, percentage, date, superlative, an
     attribution ("according to", "as per", "reports") or a quote. Each one gets
     an id (C1, C2, ...) so a claims register can be built from the list.
  2. Flags attributions with no named source ("research shows", "studies show").
  3. Checks every weekday written next to a date (for example "Wednesday,
     13 August 2026") against the calendar.
  4. With --year, flags dates in an earlier year, because documents meant to be
     current often carry last year's date by mistake. History is fine; the flag
     only asks for a look.
  5. Lists long and short dashes (and spaced hyphens used as dashes).
  6. With --tone, lists banned words and patterns from the voice check.

Usage:
  python3 claims_scan.py draft.txt
  python3 claims_scan.py draft.txt --year 2026 --tone
  cat draft.txt | python3 claims_scan.py - --json

Exit code: 0 when no date problem, dash or banned word was found, 1 otherwise,
2 when the file could not be read.
The claim list itself never changes the exit code: claims are for checking.
"""
import argparse
import datetime as _dt
import json
import re
import sys

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
WEEKDAY_ABBR = {w[:3]: w for w in WEEKDAYS}
MONTHS = ["january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december"]
MONTH_ABBR = {m[:3]: i + 1 for i, m in enumerate(MONTHS)}
MONTH_ABBR["sept"] = 9

WD = r"(?P<wd>mon(?:day)?|tue(?:s|sday)?|wed(?:nesday)?|thu(?:r|rs|rsday)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?)"
MON = r"(?P<mon>jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
DAY = r"(?P<day>\d{1,2})(?:st|nd|rd|th)?"
YEAR = r"(?P<year>\d{4})"

# Weekday before the date: "Thursday, 13 August 2026", "Thu 13 Aug 2026", "Thursday, August 13, 2026"
WD_BEFORE_DMY = re.compile(WD + r"\.?,?\s+" + DAY + r"\s+(?:of\s+)?" + MON + r"\.?,?\s+" + YEAR, re.I)
WD_BEFORE_MDY = re.compile(WD + r"\.?,?\s+" + MON + r"\.?\s+" + DAY + r",?\s+" + YEAR, re.I)
# Weekday after the date: "13 August 2026 (Thursday)", "August 13, 2026, a Thursday"
DMY_WD_AFTER = re.compile(DAY + r"\s+(?:of\s+)?" + MON + r"\.?,?\s+" + YEAR + r"\s*(?:\(|,\s*(?:a|which is a|is a)?\s*)" + WD, re.I)
MDY_WD_AFTER = re.compile(MON + r"\.?\s+" + DAY + r",?\s+" + YEAR + r"\s*(?:\(|,\s*(?:a|which is a|is a)?\s*)" + WD, re.I)
# Any date, for the year check
ANY_DMY = re.compile(r"\b" + DAY + r"\s+(?:of\s+)?" + MON + r"\.?,?\s+" + YEAR + r"\b", re.I)
ANY_MDY = re.compile(r"\b" + MON + r"\.?\s+" + DAY + r",?\s+" + YEAR + r"\b", re.I)
ISO = re.compile(r"\b(?P<year>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})\b")

NUMBER = re.compile(r"(?<![A-Za-z])[₹$€£]?\s?\d[\d,]*(?:\.\d+)?\s?(?:%|percent|per cent|million|billion|crore|cr|lakh|bn|mn|k|x)?(?![A-Za-z])", re.I)
MONEY = re.compile(r"[₹$€£]|\b(?:rs\.?|inr|usd|eur|gbp)\b", re.I)
SUPERLATIVE = re.compile(r"(#\s?1\b|\bnumber one\b|\bfirst\b|\bonly\b|\blargest\b|\bbiggest\b|\bleading\b|\bbest\b|\btop\b|\bfastest\b|\bmost\b|\blowest\b|\bhighest\b|\bunique\b|\bno\.? 1\b)", re.I)
ATTRIBUTION = re.compile(r"\b(according to|as per|per the|reports?|reported|says|said|states|stated|survey|study|studies|research|data shows?|found that|estimates?)\b", re.I)
UNNAMED = re.compile(r"\b(research shows|studies show|studies have shown|experts say|data shows|reports suggest|it is said|many believe|according to research|according to studies|according to experts)\b", re.I)
QUOTE = re.compile(r"[\"“][^\"”]{3,}[\"”]")
DASHES = re.compile(r"[\u2012\u2013\u2014\u2015]|\s--?\s")

BANNED_WORDS = [
    "game-changer", "game changer", "game-changing", "game changing", "leverage", "dive in", "dive deep", "delve",
    "tapestry", "elevate", "elevated", "unlock", "seamless", "seamlessly", "landed hard", "resonated",
    "struck a chord", "genuine unlock", "genuinely", "honestly", "straightforward", "revolutionize",
    "revolutionise", "revolutionary", "supercharge", "harness", "empower", "in today's world",
    "ever-evolving", "next level", "it's important to note", "testament to", "the rise of",
    "keep coming back to", "sat with me", "rubric", "move the needle", "here's the thing",
    "groundbreaking", "transformative", "comprehensive", "robust", "dynamic", "holistic", "synergy",
    "paradigm shift", "thought leader", "next-level", "humbled to share",
]
PATTERNS = [
    (re.compile(r"\b(?:it|this|that)(?:'s| is| was) not [^.!?]{1,60}[.!?]\s+(?:it|this|that)(?:'s| is| was) ", re.I), "\"It is not X. It is Y\" contrast pattern"),
    (re.compile(r"!"), "exclamation mark"),
    (re.compile(r"\bstart(?:ing)? (?:on|from) monday\b", re.I), "\"start on Monday\" line"),
]


def utf8_output():
    """Write UTF-8, so a rupee sign, a Unicode minus or a curly quote never stops the script on a Windows console or pipe
    set to code page 1252 (S2, version 1.0.2). A stream that cannot be reconfigured (a test buffer) is left as it is."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def split_sentences(text):
    parts = []
    for block in re.split(r"\n\s*\n|\n(?=\s*[-*\d]+[.)]?\s)|\n", text):
        block = block.strip()
        if not block:
            continue
        for s in re.split(r"(?<=[.!?])\s+(?=[\"“(\[]?[A-Z0-9₹$])", block):
            s = s.strip()
            if s:
                parts.append(s)
    return parts


def _month(name):
    return MONTH_ABBR.get(name.lower()[:4] if name.lower().startswith("sept") else name.lower()[:3])


def _weekday(name):
    n = name.lower()
    for w in WEEKDAYS:
        if w.startswith(n[:3]):
            return w
    return None


def date_problems(text):
    out = []
    seen = set()
    for rx in (WD_BEFORE_DMY, WD_BEFORE_MDY, DMY_WD_AFTER, MDY_WD_AFTER):
        for m in rx.finditer(text):
            if m.span() in seen:
                continue
            seen.add(m.span())
            try:
                d = _dt.date(int(m.group("year")), _month(m.group("mon")), int(m.group("day")))
            except (ValueError, TypeError):
                out.append({"text": m.group(0), "problem": "not a real date"})
                continue
            written = _weekday(m.group("wd"))
            actual = WEEKDAYS[d.weekday()]
            if written != actual:
                out.append({"text": m.group(0), "problem": "that date is a %s, not a %s" % (actual.capitalize(), written.capitalize())})
    return out


def all_dates(text):
    found = []
    for rx in (ANY_DMY, ANY_MDY):
        for m in rx.finditer(text):
            try:
                d = _dt.date(int(m.group("year")), _month(m.group("mon")), int(m.group("day")))
            except (ValueError, TypeError):
                found.append((m.group(0), None))
                continue
            found.append((m.group(0), d))
    for m in ISO.finditer(text):
        try:
            found.append((m.group(0), _dt.date(int(m.group("year")), int(m.group("m")), int(m.group("d")))))
        except ValueError:
            found.append((m.group(0), None))
    return found


def year_checks(text, year):
    out = []
    for raw, d in all_dates(text):
        if d is None:
            out.append({"text": raw, "problem": "not a real date"})
        elif d.year < year:
            out.append({"text": raw, "problem": "year %d is before %d: fine if this is history, wrong if this document is meant to be current" % (d.year, year)})
    return out


def claim_types(sentence):
    types = []
    if MONEY.search(sentence):
        types.append("money")
    if re.search(r"\d", sentence):
        if re.search(r"%|\bper ?cent\b", sentence, re.I):
            types.append("percentage")
        if ANY_DMY.search(sentence) or ANY_MDY.search(sentence) or ISO.search(sentence):
            types.append("date")
        if not types or types == ["money"] or "number" not in types:
            types.append("number")
    if SUPERLATIVE.search(sentence):
        types.append("superlative")
    if ATTRIBUTION.search(sentence):
        types.append("attribution")
    if QUOTE.search(sentence):
        types.append("quote")
    seen = []
    for t in types:
        if t not in seen:
            seen.append(t)
    return seen


def scan(text, year=None, tone=False):
    claims = []
    unnamed = []
    for s in split_sentences(text):
        t = claim_types(s)
        if t:
            claims.append({"id": "C%d" % (len(claims) + 1), "types": t, "sentence": s})
            if UNNAMED.search(s):
                unnamed.append({"id": claims[-1]["id"], "sentence": s})
    dashes = []
    for i, line in enumerate(text.splitlines(), 1):
        for m in DASHES.finditer(line):
            start = max(0, m.start() - 20)
            dashes.append({"line": i, "context": line[start:m.end() + 20]})
    banned = []
    if tone:
        # Curly apostrophes (text pasted from Word or a phone) are read as straight ones,
        # so "it’s important to note" is caught like "it's important to note".
        low = text.lower().replace("\u2019", "'").replace("\u2018", "'")
        for w in BANNED_WORDS:
            for m in re.finditer(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
                line = low.count("\n", 0, m.start()) + 1
                banned.append({"line": line, "word": w})
        for rx, label in PATTERNS:
            for m in rx.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                banned.append({"line": line, "word": label})
        banned.sort(key=lambda b: (b["line"], b["word"]))
    return {
        "claims": claims,
        "unnamed_sources": unnamed,
        "date_problems": date_problems(text),
        "year_checks": year_checks(text, year) if year else [],
        "dashes": dashes,
        "banned": banned,
    }


def render(result):
    lines = []
    lines.append("Claims to check: %d" % len(result["claims"]))
    for c in result["claims"]:
        lines.append("  %s [%s] %s" % (c["id"], ", ".join(c["types"]), c["sentence"]))
    if result["unnamed_sources"]:
        lines.append("Attribution with no named source:")
        for u in result["unnamed_sources"]:
            lines.append("  %s %s" % (u["id"], u["sentence"]))
    if result["date_problems"]:
        lines.append("Date problems:")
        for d in result["date_problems"]:
            lines.append("  '%s': %s" % (d["text"], d["problem"]))
    else:
        lines.append("Date problems: none found (weekdays written next to dates match the calendar)")
    if result["year_checks"]:
        lines.append("Year checks:")
        for d in result["year_checks"]:
            lines.append("  '%s': %s" % (d["text"], d["problem"]))
    if result["dashes"]:
        lines.append("Dashes: %d" % len(result["dashes"]))
        for d in result["dashes"]:
            lines.append("  line %d: ...%s..." % (d["line"], d["context"]))
    else:
        lines.append("Dashes: none")
    if result["banned"]:
        lines.append("Banned words and patterns: %d" % len(result["banned"]))
        for b in result["banned"]:
            lines.append("  line %d: %s" % (b["line"], b["word"]))
    return "\n".join(lines)


def main(argv=None):
    utf8_output()
    ap = argparse.ArgumentParser(description="Seed a claims register and check dates, weekdays and dashes.")
    ap.add_argument("path", help="text file to scan, or - for standard input")
    ap.add_argument("--year", type=int, help="the current year; dates in earlier years are flagged for a look")
    ap.add_argument("--tone", action="store_true", help="also list banned words and patterns")
    ap.add_argument("--json", action="store_true", help="print JSON instead of text")
    a = ap.parse_args(argv)
    if a.path == "-":
        text = sys.stdin.read()
    else:
        try:
            with open(a.path, encoding="utf-8") as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError) as e:
            print("Could not read %s: %s" % (a.path, e))
            return 2
    result = scan(text, a.year, a.tone)
    print(json.dumps(result, ensure_ascii=False, indent=2) if a.json else render(result))
    bad = result["date_problems"] or result["dashes"] or result["banned"]
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
