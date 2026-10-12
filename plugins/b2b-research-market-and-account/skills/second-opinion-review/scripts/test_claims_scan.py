#!/usr/bin/env python3
"""Tests for claims_scan.py. Run: python3 test_claims_scan.py -v"""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import claims_scan as cs  # noqa: E402

DRAFT = (
    "The company grew revenue 20% to Rs 51.3 crore in the quarter. "
    "It now serves 10,000 clients and is India's largest platform. "
    "Results came out on Wednesday, 13 August 2026.\n\n"
    "Research shows most sellers switch tools every year. "
    "As per the filing, it onboarded 115 enterprise customers."
)


class ClaimsScanTests(unittest.TestCase):
    def test_claims_found_and_numbered(self):
        r = cs.scan(DRAFT)
        ids = [c["id"] for c in r["claims"]]
        self.assertEqual(ids, ["C1", "C2", "C3", "C4", "C5"])
        self.assertIn("money", r["claims"][0]["types"])
        self.assertIn("percentage", r["claims"][0]["types"])
        self.assertIn("superlative", r["claims"][1]["types"])
        self.assertIn("attribution", r["claims"][4]["types"])

    def test_decimal_does_not_split_sentence(self):
        r = cs.scan("Revenue was 51.4 crore. Profit was 4.7 crore.")
        self.assertEqual(len(r["claims"]), 2)
        self.assertIn("51.4", r["claims"][0]["sentence"])

    def test_unnamed_source_flagged(self):
        r = cs.scan(DRAFT)
        self.assertEqual(len(r["unnamed_sources"]), 1)
        self.assertTrue(r["unnamed_sources"][0]["sentence"].startswith("Research shows"))

    def test_weekday_wrong(self):
        r = cs.scan(DRAFT)
        self.assertEqual(len(r["date_problems"]), 1)
        self.assertIn("Thursday", r["date_problems"][0]["problem"])

    def test_weekday_right_and_other_forms(self):
        ok = cs.scan("Out on Thursday, 13 August 2026. Also Tue, Sep 5, 2023. And 9 December 2025 (Tuesday).")
        self.assertEqual(ok["date_problems"], [])
        bad = cs.scan("Out on August 13, 2026, a Monday.")
        self.assertEqual(len(bad["date_problems"]), 1)

    def test_impossible_date(self):
        r = cs.scan("Due Monday, 31 February 2026.")
        self.assertEqual(r["date_problems"][0]["problem"], "not a real date")

    def test_year_check(self):
        r = cs.scan("Dated 5 September 2023 and 11 October 2026 and 2025-12-09.", year=2026)
        flagged = [y["text"] for y in r["year_checks"]]
        self.assertIn("5 September 2023", flagged)
        self.assertIn("2025-12-09", flagged)
        self.assertNotIn("11 October 2026", flagged)

    def test_dashes(self):
        r = cs.scan("Revenue rose \u2014 fast. Range 25-30% is fine. A spaced - hyphen. A \u2013 short dash.")
        self.assertEqual(len(r["dashes"]), 3)

    def test_tone(self):
        r = cs.scan("We leverage a robust, seamless platform! It is not a tool. It is a system.", tone=True)
        words = [b["word"] for b in r["banned"]]
        for w in ("leverage", "robust", "seamless", "exclamation mark"):
            self.assertIn(w, words)
        self.assertTrue(any("contrast" in w for w in words))

    def test_tone_curly_apostrophes(self):
        r = cs.scan("It\u2019s important to note this. In today\u2019s world. Here\u2019s the thing.", tone=True)
        words = [b["word"] for b in r["banned"]]
        for w in ("it's important to note", "in today's world", "here's the thing"):
            self.assertIn(w, words)

    def test_main_exit_codes(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as fh:
            fh.write(DRAFT)
            path = fh.name
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cs.main([path, "--year", "2026"])
        os.unlink(path)
        self.assertEqual(code, 1)
        self.assertIn("Claims to check: 5", buf.getvalue())
        clean = io.StringIO()
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as fh:
            fh.write("Revenue was 51.4 crore on Thursday, 13 August 2026.")
            path = fh.name
        with redirect_stdout(clean):
            code = cs.main([path])
        os.unlink(path)
        self.assertEqual(code, 0)

    def test_unreadable_file(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cs.main(["/no/such/file.txt"])
        self.assertEqual(code, 2)
        self.assertIn("Could not read", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
