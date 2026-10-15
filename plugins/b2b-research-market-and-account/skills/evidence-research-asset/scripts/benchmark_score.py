#!/usr/bin/env python3
"""benchmark_score.py: score companies against a fixed set of yes or no criteria, the same way every run.

Standard library only, no network, writes no files.

Inputs:
  --criteria  CSV: criterion_id,question,points   (fixed before any company is scored)
  --evidence  CSV: company,criterion_id,answer,source,tier,cut
              answer  yes | no | not found
              source  the public link that shows the answer (needed for a yes)
              tier    publishable | directional | anecdotal
              cut     optional group the study will report (for example a region or a vertical)
  --publishable-only   count a yes only when its tier is publishable
  --min-per-cut N      the user's minimum number of companies per reported cut

Scoring: a yes with a public link earns the criterion's points; a yes without a link earns 0
and is listed as a problem; no and not found earn 0. A company missing a row for any
criterion is listed as not fully scored. Companies are sorted by score, then by name, and the
tiers are always listed publishable, directional, anecdotal, so the same input always prints
the same table and the same --json.

Problems also include: points that are not a finite number (NaN or Infinity count as 0), the
same criterion_id twice in the criteria (the first row is kept, never silently replaced), no
criteria, no evidence rows, points too large to add up (they count as 0), and a row with a
missing cell. --json prints strict JSON (no NaN or Infinity). Negative points are accepted as
written.

Exit code: 0 when every company is fully scored with no problem, 1 otherwise, 2 when a file
could not be read.
"""
import argparse
import csv
import io
import json
import math
import sys

ANSWERS = {"yes", "no", "not found"}
TIERS = ("publishable", "directional", "anecdotal")   # a fixed order, so --json prints the same bytes every run


def utf8_output():
    """Write UTF-8, so a rupee sign, a Unicode minus or a curly quote never stops the script on a Windows console or pipe
    set to code page 1252 (S2, version 1.0.2). A stream that cannot be reconfigured (a test buffer) is left as it is."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def load(text, need):
    reader = csv.DictReader(io.StringIO(text))
    missing = [c for c in need if c not in (reader.fieldnames or [])]
    if missing:
        raise ValueError("missing columns %s" % ", ".join(missing))
    return list(reader)


def score(criteria_rows, evidence_rows, publishable_only=False, min_per_cut=0):
    problems = []
    crit = {}
    if not criteria_rows:
        problems.append("no criteria: fix the criteria before any company is scored")
    if not evidence_rows:
        problems.append("no evidence rows: nothing was scored")
    for r in criteria_rows:
        cid = (r.get("criterion_id") or "").strip()
        if cid in crit:
            problems.append("criterion %s appears twice in the criteria; the first row is kept, give each criterion its own id" % cid)
            continue
        try:
            crit[cid] = float(r.get("points") or "")
        except ValueError:
            problems.append("criterion %s: points '%s' is not a number" % (cid, r.get("points") or ""))
            crit[cid] = 0.0
            continue
        if not math.isfinite(crit[cid]):
            problems.append("criterion %s: points '%s' is not a finite number; it counts as 0" % (cid, r["points"]))
            crit[cid] = 0.0
    if not math.isfinite(sum(abs(v) for v in crit.values())):
        problems.append("the points are too large to add up; use smaller points (every criterion counts as 0 until then)")
        crit = {k: 0.0 for k in crit}
    companies = {}
    cuts = {}
    for i, r in enumerate(evidence_rows, 2):
        comp = (r.get("company") or "").strip()
        cid = (r.get("criterion_id") or "").strip()
        ans = (r.get("answer") or "").strip().lower()
        tier = (r.get("tier") or "").strip().lower()
        src = (r.get("source") or "").strip()
        c = companies.setdefault(comp, {"score": 0.0, "seen": set(), "tiers": {t: 0 for t in TIERS}})
        if (r.get("cut") or "").strip():
            cuts.setdefault(r["cut"].strip(), set()).add(comp)
        if cid not in crit:
            problems.append("row %d %s: criterion %s is not in the criteria" % (i, comp, cid))
            continue
        if cid in c["seen"]:
            problems.append("row %d %s: criterion %s answered twice" % (i, comp, cid))
            continue
        c["seen"].add(cid)
        if ans not in ANSWERS:
            problems.append("row %d %s / %s: answer '%s'; use yes, no or not found" % (i, comp, cid, ans))
            continue
        if tier and tier not in TIERS:
            problems.append("row %d %s / %s: tier '%s'; use publishable, directional or anecdotal" % (i, comp, cid, tier))
        elif tier:
            c["tiers"][tier] += 1
        if ans == "yes":
            if not (src.startswith("http://") or src.startswith("https://")):
                problems.append("row %d %s / %s: yes without a public link scores 0" % (i, comp, cid))
                continue
            if publishable_only and tier != "publishable":
                continue
            c["score"] += crit[cid]
    table = []
    for comp, c in companies.items():
        missing = sorted(set(crit) - c["seen"])
        if missing:
            problems.append("%s: not fully scored, no row for %s" % (comp, ", ".join(missing)))
        table.append({"company": comp, "score": c["score"], "max": sum(crit.values()),
                      "missing": missing, "tiers": c["tiers"]})
    table.sort(key=lambda t: (-t["score"], t["company"].lower()))
    low = []
    if min_per_cut:
        for cut, comps in sorted(cuts.items()):
            if len(comps) < min_per_cut:
                low.append("%s: %d companies, below the minimum of %d; base too low to report this cut" % (cut, len(comps), min_per_cut))
    return {"table": table, "problems": problems, "low_cuts": low}


def render(res):
    lines = ["Scores (same input, same order, every run):"]
    for t in res["table"]:
        tiers = ", ".join("%s %d" % (k, t["tiers"][k]) for k in ("publishable", "directional", "anecdotal"))
        lines.append("  %s: %g of %g  [%s]%s" % (t["company"], t["score"], t["max"], tiers,
                                                 "  NOT FULLY SCORED" if t["missing"] else ""))
    for l in res["low_cuts"]:
        lines.append("Cut: " + l)
    if res["problems"]:
        lines.append("Problems: %d" % len(res["problems"]))
        lines.extend("  " + p for p in res["problems"])
    else:
        lines.append("Problems: none")
    return "\n".join(lines)


def main(argv=None):
    utf8_output()
    ap = argparse.ArgumentParser(description="Score companies against a fixed set of yes or no criteria.")
    ap.add_argument("--criteria", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--publishable-only", action="store_true")
    ap.add_argument("--min-per-cut", type=int, default=0)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        with open(a.criteria, encoding="utf-8") as fh:
            criteria = load(fh.read(), ["criterion_id", "question", "points"])
        with open(a.evidence, encoding="utf-8") as fh:
            evidence = load(fh.read(), ["company", "criterion_id", "answer", "source", "tier"])
    except (OSError, UnicodeDecodeError, ValueError) as e:
        print("Could not read: %s" % e)
        return 2
    res = score(criteria, evidence, a.publishable_only, a.min_per_cut)
    print(json.dumps(res, indent=2, allow_nan=False) if a.json else render(res))
    return 1 if (res["problems"] or res["low_cuts"]) else 0


if __name__ == "__main__":
    sys.exit(main())
