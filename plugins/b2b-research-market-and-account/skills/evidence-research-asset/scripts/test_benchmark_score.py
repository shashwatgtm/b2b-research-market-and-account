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

    # Run 31C, Codex finding F004: non finite points, duplicate ids and zero items are problems; --json is strict JSON
    def test_non_finite_points_are_problems(self):
        crit = "criterion_id,question,points\nc1,q,nan\nc2,q2,inf\nc3,q3,-Infinity\n"
        r = rs.score(rows(crit), rows("company,criterion_id,answer,source,tier,cut\nAlpha,c1,yes,https://a.example,publishable,\n"))
        for cid in ("c1", "c2", "c3"):
            self.assertTrue(any(("criterion %s" % cid) in p and "not a finite number" in p for p in r["problems"]), cid)
        import json as _json
        _json.dumps(r, allow_nan=False)   # raises ValueError if NaN or Infinity is left in the result

    def test_duplicate_criterion_id_is_a_problem_not_a_replace(self):
        crit = "criterion_id,question,points\nQ1,first,2\nQ1,second,5\n"
        r = rs.score(rows(crit), rows("company,criterion_id,answer,source,tier,cut\nAlpha,Q1,yes,https://a.example,publishable,\n"))
        self.assertTrue(any("criterion Q1" in p and "twice" in p for p in r["problems"]))
        self.assertEqual(r["table"][0]["score"], 2.0)
        self.assertEqual(r["table"][0]["max"], 2.0)

    def test_zero_criteria_or_zero_evidence_is_a_problem(self):
        none_crit = rs.score([], rows(EVID))
        self.assertTrue(any("no criteria" in p for p in none_crit["problems"]))
        none_ev = rs.score(rows(CRITERIA), [])
        self.assertTrue(any("no evidence rows" in p for p in none_ev["problems"]))
        both = rs.score([], [])
        self.assertGreaterEqual(len(both["problems"]), 2)

    def test_main_json_is_strict(self):
        d = tempfile.mkdtemp()
        rp, ep = os.path.join(d, "r.csv"), os.path.join(d, "e.csv")
        with open(rp, "w", encoding="utf-8") as fh:
            fh.write("criterion_id,question,points\nc1,q,nan\nc1,q2,inf\n")
        with open(ep, "w", encoding="utf-8") as fh:
            fh.write("company,criterion_id,answer,source,tier,cut\nAlpha,c1,yes,https://a.example,publishable,\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = rs.main(["--criteria", rp, "--evidence", ep, "--json"])
        self.assertEqual(code, 1)
        import json as _json

        def refuse(c):
            raise ValueError("non-finite constant %s" % c)
        _json.loads(buf.getvalue(), parse_constant=refuse)

    # Run 31C auditor gaps S3 and S4: points too large to add up, and rows with missing cells, are problems, never inf or a traceback
    def test_points_too_large_to_add_up(self):
        crit = "criterion_id,question,points\nc1,q,1e308\nc2,q2,1e308\n"
        r = rs.score(rows(crit), rows("company,criterion_id,answer,source,tier,cut\nAlpha,c1,yes,https://a.example,publishable,\nAlpha,c2,yes,https://a.example/2,publishable,\n"))
        self.assertTrue(any("too large" in p for p in r["problems"]))
        import json as _json
        _json.dumps(r, allow_nan=False)

    def test_rows_with_missing_cells(self):
        r = rs.score(rows("criterion_id,question,points\nc1,q\n"), rows("company,criterion_id,answer,source,tier,cut\nA,c1\n"))
        self.assertTrue(any("criterion c1" in p and "not a number" in p for p in r["problems"]))
        self.assertTrue(any("answer ''" in p for p in r["problems"]))

    def test_main_header_only_files_exit_1(self):
        d = tempfile.mkdtemp()
        rp, ep = os.path.join(d, "r.csv"), os.path.join(d, "e.csv")
        with open(rp, "w", encoding="utf-8") as fh:
            fh.write("criterion_id,question,points\n")
        with open(ep, "w", encoding="utf-8") as fh:
            fh.write("company,criterion_id,answer,source,tier,cut\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = rs.main(["--criteria", rp, "--evidence", ep])
        self.assertEqual(code, 1)
        self.assertNotIn("Problems: none", buf.getvalue())


def _run_cp1252(script_name, args, files):
    """S2, run 32A: run the script as a user on Windows would, with output set to code page 1252 (a console or pipe)."""
    import subprocess
    import tempfile
    d = tempfile.mkdtemp()
    paths = []
    for name, body in files:
        p = os.path.join(d, name)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
        paths.append(p)
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
    env = dict(os.environ, PYTHONIOENCODING="cp1252")
    return subprocess.run([sys.executable, script] + [a.format(*paths) for a in args], capture_output=True, env=env)


class CodePage1252Tests(unittest.TestCase):
    """S2, run 32A: a character outside plain ASCII (rupee sign, Unicode minus, curly quotes) is written as UTF-8 and the
    script never stops with an encoding error on a Windows console or pipe set to code page 1252."""

    def assert_utf8_output(self, p, expected):
        self.assertNotIn(b"Traceback", p.stderr, p.stderr.decode("utf-8", "replace"))
        self.assertNotIn(b"UnicodeEncodeError", p.stderr)
        self.assertIn(p.returncode, (0, 1))
        self.assertIn(expected.encode("utf-8"), p.stdout)

    def test_company_with_rupee_and_quotes(self):
        p = _run_cp1252("benchmark_score.py", ["--criteria", "{0}", "--evidence", "{1}"],
                        [("c.csv", "criterion_id,question,points\nQ1,Publishes a \u201csecurity\u201d page,1\n"),
                         ("e.csv", "company,criterion_id,answer,source,tier,cut\n\u201cAlpha\u201d \u20b9,Q1,yes,https://a.example/s,publishable,India\n")])
        self.assert_utf8_output(p, "\u201cAlpha\u201d \u20b9")


class TierOrderTests(unittest.TestCase):
    """Run 32A (coordinator review of run 31C): --json prints the tiers in one fixed order, whatever the hash seed."""

    def test_json_tier_order_fixed_across_hash_seeds(self):
        import subprocess
        d = tempfile.mkdtemp()
        rp, ep = os.path.join(d, "c.csv"), os.path.join(d, "e.csv")
        with open(rp, "w", encoding="utf-8") as fh:
            fh.write(CRITERIA)
        with open(ep, "w", encoding="utf-8") as fh:
            fh.write(EVID)
        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "benchmark_score.py")
        outs = set()
        for seed in range(8):
            env = dict(os.environ, PYTHONHASHSEED=str(seed))
            p = subprocess.run([sys.executable, script, "--criteria", rp, "--evidence", ep, "--json"], capture_output=True, env=env)
            outs.add(p.stdout)
            import json as _json
            for row in _json.loads(p.stdout.decode("utf-8"))["table"]:
                self.assertEqual(list(row["tiers"]), ["publishable", "directional", "anecdotal"])
        self.assertEqual(len(outs), 1)


if __name__ == "__main__":
    unittest.main()
