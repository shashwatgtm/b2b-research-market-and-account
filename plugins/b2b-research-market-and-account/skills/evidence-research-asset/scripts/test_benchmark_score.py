#!/usr/bin/env python3
"""Tests for benchmark_score.py. Run: python3 test_benchmark_score.py -v"""
import csv
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import benchmark_score as rs  # noqa: E402

CRITERIA = "criterion_id,question,points\nQ1,Publishes a security page,2\nQ2,Names a certification on its own site,1\n"
EVID = (
    "company,criterion_id,answer,source,tier,cut\n"
    "Beta,Q1,yes,https://beta.example/security,publishable,India\n"
    "Beta,Q2,no,,publishable,India\n"
    "Alpha,Q1,yes,https://alpha.example/trust,publishable,India\n"
    "Alpha,Q2,yes,https://alpha.example/cert,directional,India\n"
)


def rows(text):
    return list(csv.DictReader(io.StringIO(text)))


class BenchmarkTests(unittest.TestCase):
    def test_scores_and_order(self):
        r = rs.score(rows(CRITERIA), rows(EVID))
        self.assertEqual([(t["company"], t["score"]) for t in r["table"]], [("Alpha", 3.0), ("Beta", 2.0)])
        self.assertEqual(r["problems"], [])

    def test_same_output_every_run(self):
        a = rs.render(rs.score(rows(CRITERIA), rows(EVID)))
        b = rs.render(rs.score(rows(CRITERIA), list(reversed(rows(EVID)))))
        self.assertEqual(a, b)

    def test_publishable_only(self):
        r = rs.score(rows(CRITERIA), rows(EVID), publishable_only=True)
        self.assertEqual(dict((t["company"], t["score"]) for t in r["table"])["Alpha"], 2.0)

    def test_yes_without_link(self):
        ev = EVID.replace("https://alpha.example/cert", "their site")
        r = rs.score(rows(CRITERIA), rows(ev))
        self.assertTrue(any("without a public link" in p for p in r["problems"]))
        self.assertEqual(dict((t["company"], t["score"]) for t in r["table"])["Alpha"], 2.0)

    def test_missing_and_unknown_criterion(self):
        ev = "company,criterion_id,answer,source,tier,cut\nGamma,Q1,no,,anecdotal,\nGamma,Q9,yes,https://g.example,publishable,\n"
        r = rs.score(rows(CRITERIA), rows(ev))
        self.assertTrue(any("not fully scored" in p for p in r["problems"]))
        self.assertTrue(any("not in the criteria" in p for p in r["problems"]))

    def test_min_per_cut(self):
        r = rs.score(rows(CRITERIA), rows(EVID), min_per_cut=3)
        self.assertTrue(any("base too low" in l for l in r["low_cuts"]))

    def test_bad_answer_and_tier(self):
        ev = "company,criterion_id,answer,source,tier,cut\nAlpha,Q1,maybe,,guess,\n"
        r = rs.score(rows(CRITERIA), rows(ev))
        self.assertTrue(any("answer 'maybe'" in p for p in r["problems"]))

    def test_main(self):
        d = tempfile.mkdtemp()
        rp, ep = os.path.join(d, "r.csv"), os.path.join(d, "e.csv")
        with open(rp, "w", encoding="utf-8") as fh:
            fh.write(CRITERIA)
        with open(ep, "w", encoding="utf-8") as fh:
            fh.write(EVID)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = rs.main(["--criteria", rp, "--evidence", ep])
        self.assertEqual(code, 0)
        self.assertIn("Alpha: 3 of 3", buf.getvalue())

    def test_main_bad_columns(self):
        d = tempfile.mkdtemp()
        rp, ep = os.path.join(d, "r.csv"), os.path.join(d, "e.csv")
        with open(rp, "w", encoding="utf-8") as fh:
            fh.write("id,points\nQ1,1\n")
        with open(ep, "w", encoding="utf-8") as fh:
            fh.write(EVID)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = rs.main(["--criteria", rp, "--evidence", ep])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
