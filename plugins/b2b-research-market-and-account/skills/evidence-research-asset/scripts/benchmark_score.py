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
criterion is listed as not fully scored. Companies are sorted by score, then by name, so the
same input always prints the same table.

Exit code: 0 when every company is fully scored with no problem, 1 otherwise, 2 when a file
could not be read.
"""
import argparse
import csv
import io
import json
import sys

ANSWERS = {"yes", "no", "not found"}
TIERS = {"publishable", "directional", "anecdotal"}


def load(text, need):
    reader = csv.DictReader(io.StringIO(text))
    missing = [c for c in need if c not in (reader.fieldnames or [])]
    if missing:
        raise ValueError("missing columns %s" % ", ".join(missing))
    return list(reader)


def score(criteria_rows, evidence_rows, publishable_only=False, min_per_cut=0):
    problems = []
    crit = {}
    for r in criteria_rows:
        cid = r["criterion_id"].strip()
        try:
            crit[cid] = float(r["points"])
        except ValueError:
            problems.append("criterion %s: points '%s' is not a number" % (cid, r["points"]))
            crit[cid] = 0.0
    companies = {}
    cuts = {}
    for i, r in enumerate(evidence_rows, 2):
        comp = r["company"].strip()
        cid = r["criterion_id"].strip()
        ans = r["answer"].strip().lower()
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
    print(json.dumps(res, indent=2) if a.json else render(res))
    return 1 if (res["problems"] or res["low_cuts"]) else 0


if __name__ == "__main__":
    sys.exit(main())
