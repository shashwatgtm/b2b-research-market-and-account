#!/usr/bin/env python3
"""number_lock.py: check that every asset uses the locked numbers, written the same way.

Standard library only, no network, writes no files.

Inputs:
  --lock   the number lock sheet, a CSV with columns id,label,value,source
           value is written as the asset should write it: "265.52 million", "14.22%",
           "Rs 51.4 crore", "8 million"
  assets   one or more text or Markdown files (the post, the deck text, the page, the PDF text)

What it reports, per asset:
  - each number that matches a lock row (by value and unit)
  - each number that is close to a lock value (within 1 percent, same unit): a rounded or
    retyped form; write it as on the sheet, or add the rounded form to the sheet as its own row
  - each number that is not on the lock sheet at all
  - a number that matches a lock value but is written in another currency
    (for example "$51.4 crore" against "Rs 51.4 crore"), reported as a near match
  - each weekday written next to a date that does not match the calendar
Then, per lock row, which assets use it.

A minus sign directly before a number makes it negative ("-14.22%" is not "14.22%"): the
Unicode minus, or an ASCII hyphen that does not follow a digit, a letter, a percent sign or
a point (so "**-14.22%**", ":-14.22%" and "(-14.22%)" are negative). A hyphen between two
numbers ("10-12", "12%-14%") is a range, not a sign.

Years (1900 to 2099 with no unit) and numbers inside dates are skipped, except a four digit
number that equals a lock value or is followed by the word that follows a lock value
("2024 accounts" next to a lock row "2,024 accounts"): that is a count and is checked.
Plain integers from 0 up to --allow-small (default 0) are skipped, for structure such as
"Part 2 of 5".

Exit code: 0 when every number is on the sheet and every weekday is right, 1 otherwise,
2 when a file could not be read.
"""
import argparse
import csv
import datetime as _dt
import io
import json
import re
import sys

UNIT_MAP = {
    "%": "%", "percent": "%", "per cent": "%",
    "million": "million", "mn": "million", "m": "million",
    "billion": "billion", "bn": "billion", "b": "billion",
    "crore": "crore", "cr": "crore", "lakh": "lakh", "lakhs": "lakh",
    "thousand": "thousand", "k": "thousand", "x": "x",
}
NUM = re.compile(
    r"(?<![\w.])(?P<cur>[₹$€£]|rs\.?\s?|inr\s?|usd\s?)?(?P<num>\d(?:[\d,]*\d)?(?:\.\d+)?)"
    r"(?:\s?(?P<unit>%|percent|per cent|million|billion|crore|lakhs?|thousand|mn|bn|cr|k|m|b|x)(?![a-z]))?", re.I)

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
WD = r"(?P<wd>mon(?:day)?|tue(?:s|sday)?|wed(?:nesday)?|thu(?:r|rs|rsday)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?)"
MON = r"(?P<mon>jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
DAY = r"(?P<day>\d{1,2})(?:st|nd|rd|th)?"
YEAR = r"(?P<year>\d{4})"
DATE_FORMS = [
    re.compile(WD + r"\.?,?\s+" + DAY + r"\s+" + MON + r"\.?,?\s+" + YEAR, re.I),
    re.compile(WD + r"\.?,?\s+" + MON + r"\.?\s+" + DAY + r",?\s+" + YEAR, re.I),
    re.compile(DAY + r"\s+" + MON + r"\.?,?\s+" + YEAR + r"\s*(?:\(|,\s*(?:a\s+)?)" + WD, re.I),
]
ANY_DATE = [
    re.compile(r"\b" + DAY + r"\s+" + MON + r"\.?,?\s+" + YEAR + r"\b", re.I),
    re.compile(r"\b" + MON + r"\.?\s+" + DAY + r",?\s+" + YEAR + r"\b", re.I),
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    re.compile(r"\b" + MON + r"\.?\s+" + YEAR + r"\b", re.I),
]


MINUS = "\u2212"


def utf8_output():
    """Write UTF-8, so a rupee sign, a Unicode minus or a curly quote never stops the script on a Windows console or pipe
    set to code page 1252 (S2, version 1.0.2). A stream that cannot be reconfigured (a test buffer) is left as it is."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def _negative(text, start):
    """True when a minus sign sits directly before the number that starts at start."""
    if start == 0:
        return False
    before = text[start - 1]
    if before == MINUS:
        return True
    return before == "-" and (start == 1 or not (text[start - 2].isalnum() or text[start - 2] in "%."))


def parse_value(text):
    """Return (float, unit, currency) for the first number in text, or None."""
    m = NUM.search(text or "")
    if not m:
        return None
    return _from_match(m)


def _from_match(m):
    num = float(m.group("num").replace(",", ""))
    if _negative(m.string, m.start()):
        num = -num
    unit = (m.group("unit") or "").lower()
    unit = UNIT_MAP.get(unit, unit)
    cur = (m.group("cur") or "").strip().lower().rstrip(".")
    cur = {"₹": "inr", "rs": "inr", "$": "usd", "€": "eur", "£": "gbp"}.get(cur, cur)
    return num, unit, cur


def date_spans(text):
    spans = []
    for rx in ANY_DATE:
        spans.extend(m.span() for m in rx.finditer(text))
    return spans


def weekday_problems(text):
    out = []
    for rx in DATE_FORMS:
        for m in rx.finditer(text):
            try:
                d = _dt.date(int(m.group("year")), MONTHS.index(m.group("mon").lower()[:3]) + 1, int(m.group("day")))
            except ValueError:
                out.append("'%s': not a real date" % m.group(0))
                continue
            written = [w for w in WEEKDAYS if w.startswith(m.group("wd").lower()[:3])][0]
            actual = WEEKDAYS[d.weekday()]
            if written != actual:
                out.append("'%s': that date is a %s" % (m.group(0), actual.capitalize()))
    return out


def read_lock(text):
    reader = csv.DictReader(io.StringIO(text))
    need = ["id", "label", "value", "source"]
    missing = [c for c in need if c not in (reader.fieldnames or [])]
    if missing:
        raise ValueError("lock sheet is missing columns %s" % ", ".join(missing))
    lock = []
    for r in reader:
        pv = parse_value(r["value"])
        if pv is None:
            raise ValueError("lock row %s has no number in value '%s'" % (r["id"], r["value"]))
        m = NUM.search(r["value"])
        after = re.match(r"\s*([a-z]+)", r["value"][m.end():], re.I)
        lock.append({"id": r["id"].strip(), "label": r["label"].strip(), "value": r["value"].strip(),
                     "num": pv[0], "unit": pv[1], "cur": pv[2], "source": r["source"].strip(),
                     "word": after.group(1).lower() if after else ""})
    return lock


def scan_asset(name, text, lock, allow_small=0):
    found, near, unlocked = [], [], []
    spans = date_spans(text)
    for m in NUM.finditer(text):
        if any(a <= m.start() < b for a, b in spans):
            continue
        num, unit, cur = _from_match(m)
        raw = m.group(0).strip()
        if num < 0:
            raw = text[m.start() - 1] + raw
        if not unit and 1900 <= num <= 2099 and float(num).is_integer() and "," not in m.group("num"):
            nxt = re.match(r"\s*([a-z]+)", text[m.end():], re.I)
            count = any(l["num"] == num and not l["unit"] for l in lock) or bool(
                nxt and any(l["word"] and l["word"] == nxt.group(1).lower() and not l["unit"] for l in lock))
            if not count:
                continue
        if not unit and not cur and float(num).is_integer() and 0 <= num <= allow_small:
            continue
        exact = [l for l in lock if l["num"] == num and l["unit"] == unit]
        clash = [l for l in exact if cur and l["cur"] and cur != l["cur"]]
        if clash:
            near.append((raw, clash[0]["id"], clash[0]["value"] + " (the currency differs)"))
            continue
        if exact:
            found.append((raw, exact[0]["id"]))
            continue
        close = [l for l in lock if l["unit"] == unit and l["num"] and abs(num - l["num"]) / abs(l["num"]) <= 0.01]
        if close:
            near.append((raw, close[0]["id"], close[0]["value"]))
        else:
            unlocked.append(raw)
    return {"asset": name, "matched": found, "near": near, "unlocked": unlocked,
            "weekday_problems": weekday_problems(text)}


def render(results, lock):
    lines = []
    bad = False
    for r in results:
        lines.append("Asset: %s" % r["asset"])
        lines.append("  matched: %s" % (", ".join("%s (%s)" % x for x in r["matched"]) or "none"))
        for raw, lid, val in r["near"]:
            bad = True
            lines.append("  near %s: '%s' is close to '%s'; write it as on the sheet or lock the rounded form" % (lid, raw, val))
        for raw in r["unlocked"]:
            bad = True
            lines.append("  not on the lock sheet: '%s'" % raw)
        for w in r["weekday_problems"]:
            bad = True
            lines.append("  weekday: %s" % w)
    lines.append("Lock rows used:")
    for l in lock:
        users = [r["asset"] for r in results if any(x[1] == l["id"] for x in r["matched"])]
        lines.append("  %s %s = %s: %s" % (l["id"], l["label"], l["value"], ", ".join(users) or "not used"))
    lines.append("Result: %s" % ("problems found" if bad else "every number is on the lock sheet and every weekday is right"))
    return "\n".join(lines), bad


def main(argv=None):
    utf8_output()
    ap = argparse.ArgumentParser(description="Check assets against a number lock sheet.")
    ap.add_argument("--lock", required=True)
    ap.add_argument("assets", nargs="+")
    ap.add_argument("--allow-small", type=int, default=0)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        with open(a.lock, encoding="utf-8") as fh:
            lock = read_lock(fh.read())
        texts = []
        for p in a.assets:
            with open(p, encoding="utf-8") as fh:
                texts.append((p, fh.read()))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        print("Could not read: %s" % e)
        return 2
    results = [scan_asset(p, t, lock, a.allow_small) for p, t in texts]
    out, bad = render(results, lock)
    print(json.dumps(results, ensure_ascii=False, indent=2) if a.json else out)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
