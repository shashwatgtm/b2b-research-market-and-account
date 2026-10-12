#!/usr/bin/env python3
"""Tests for number_lock.py. Run: python3 test_number_lock.py -v"""
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import number_lock as nl  # noqa: E402

LOCK = (
    "id,label,value,source\n"
    "L1,detections,265.52 million,https://example.org/report p.12\n"
    "L2,sector share,14.22%,https://example.org/report p.39\n"
    "L3,revenue,Rs 51.4 crore,https://example.org/filing\n"
)


class NumberLockTests(unittest.TestCase):
    def setUp(self):
        self.lock = nl.read_lock(LOCK)

    def test_parse_units(self):
        self.assertEqual(nl.parse_value("265.52M")[:2], (265.52, "million"))
        self.assertEqual(nl.parse_value("14.22 percent")[:2], (14.22, "%"))
        self.assertEqual(nl.parse_value("₹51.4 Cr")[:2], (51.4, "crore"))
        self.assertEqual(nl.parse_value("8,000+")[:2], (8000.0, ""))

    def test_exact_match_any_writing(self):
        r = nl.scan_asset("a", "We saw 265.52M detections; 14.22 percent in one sector; revenue ₹51.4 Cr.", self.lock)
        self.assertEqual([m[1] for m in r["matched"]], ["L1", "L2", "L3"])
        self.assertEqual(r["unlocked"], [])

    def test_near_and_unlocked(self):
        r = nl.scan_asset("b", "India saw 265.5 million detections and 77% agreed.", self.lock)
        self.assertEqual(r["near"][0][1], "L1")
        self.assertEqual(r["unlocked"], ["77%"])

    def test_currency_differs(self):
        r = nl.scan_asset("e", "Revenue was $51.4 crore. Revenue was 51.4 crore.", self.lock)
        self.assertEqual(len(r["near"]), 1)
        self.assertIn("currency differs", r["near"][0][2])
        self.assertEqual([m[1] for m in r["matched"]], ["L3"])

    def test_skips_years_dates_and_small(self):
        r = nl.scan_asset("c", "In 2026, on 13 August 2026, Part 2 of 5.", self.lock, allow_small=10)
        self.assertEqual(r["unlocked"], [])
        strict = nl.scan_asset("c", "Part 2 of 5.", self.lock)
        self.assertEqual(strict["unlocked"], ["2", "5"])

    def test_weekday(self):
        r = nl.scan_asset("d", "Published Wednesday, 13 August 2026.", self.lock)
        self.assertEqual(len(r["weekday_problems"]), 1)
        ok = nl.scan_asset("d", "Published Thursday, 13 August 2026.", self.lock)
        self.assertEqual(ok["weekday_problems"], [])

    def test_bad_lock(self):
        with self.assertRaises(ValueError):
            nl.read_lock("id,label,value\nL1,x,1\n")
        with self.assertRaises(ValueError):
            nl.read_lock("id,label,value,source\nL1,x,none,y\n")

    def test_main_two_assets(self):
        d = tempfile.mkdtemp()
        paths = {}
        for name, text in (("lock.csv", LOCK), ("post.md", "265.52 million detections."),
                           ("deck.md", "265 million attacks.")):
            paths[name] = os.path.join(d, name)
            with open(paths[name], "w", encoding="utf-8") as fh:
                fh.write(text)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = nl.main(["--lock", paths["lock.csv"], paths["post.md"], paths["deck.md"]])
        out = buf.getvalue()
        self.assertEqual(code, 1)
        self.assertIn("near L1", out)
        self.assertIn("L1 detections = 265.52 million: %s" % paths["post.md"], out)

    def test_main_clean(self):
        d = tempfile.mkdtemp()
        lp, ap = os.path.join(d, "lock.csv"), os.path.join(d, "a.md")
        with open(lp, "w", encoding="utf-8") as fh:
            fh.write(LOCK)
        with open(ap, "w", encoding="utf-8") as fh:
            fh.write("265.52 million detections; 14.22% share.")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = nl.main(["--lock", lp, ap])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
