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

    # Run 31C, Codex finding F005: a minus sign directly before a number makes it negative
    def test_minus_sign_is_not_a_match(self):
        for text in ("-14.22% in one sector.", "Share fell -14.22% this year.", "Share fell −14.22% this year.", "Share (-14.22%) this year."):
            r = nl.scan_asset("m", text, self.lock)
            self.assertEqual(r["matched"], [], text)
            self.assertTrue(any(u.endswith("14.22%") and u[0] in "-−" for u in r["unlocked"]), (text, r))

    def test_hyphen_between_numbers_is_a_range_not_a_sign(self):
        r = nl.scan_asset("r", "A range of 13-14.22% across sectors.", self.lock)
        self.assertEqual([m[1] for m in r["matched"]], ["L2"])
        self.assertEqual(r["unlocked"], ["13"])

    def test_negative_lock_row(self):
        lock = nl.read_lock("id,label,value,source\nN1,change,-3.5%,https://example.org/r\n")
        self.assertEqual(lock[0]["num"], -3.5)
        self.assertEqual([m[1] for m in nl.scan_asset("n", "It moved -3.5% last year.", lock)["matched"]], ["N1"])
        self.assertEqual(nl.scan_asset("n", "It moved 3.5% last year.", lock)["matched"], [])

    def test_main_minus_sign_exit_1(self):
        d = tempfile.mkdtemp()
        lp, ap = os.path.join(d, "lock.csv"), os.path.join(d, "a.md")
        with open(lp, "w", encoding="utf-8") as fh:
            fh.write("id,label,value,source\nL1,growth,14.22%,https://example.org/r\n")
        with open(ap, "w", encoding="utf-8") as fh:
            fh.write("-14.22%")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = nl.main(["--lock", lp, ap])
        self.assertEqual(code, 1)
        self.assertNotIn("matched: 14.22%", buf.getvalue())

    # Run 31C auditor gap S1: a minus sign after markup or punctuation is still a sign; after a digit, a letter or a percent sign it is a range
    def test_minus_after_markup_or_punctuation(self):
        for text in ("**-14.22%** fell", "growth:-14.22%", '"-14.22%"', "up,-14.22%"):
            r = nl.scan_asset("p", text, self.lock)
            self.assertEqual(r["matched"], [], text)
        rng = nl.scan_asset("p", "between 12%-14.22% by sector", self.lock)
        self.assertEqual([m[1] for m in rng["matched"]], ["L2"])

    # Run 31C, Codex finding F005 (the year like count): a four digit count is checked against a lock row, not skipped as a year
    def test_year_like_count_next_to_lock_row(self):
        lock = nl.read_lock('id,label,value,source\nC1,accounts studied,"2,024 accounts",https://example.org/r\n')
        same = nl.scan_asset("y", "We studied 2024 accounts.", lock)
        self.assertEqual([m[1] for m in same["matched"]], ["C1"])
        typo = nl.scan_asset("y", "We studied 2042 accounts.", lock)
        self.assertEqual([n[1] for n in typo["near"]], ["C1"])
        year = nl.scan_asset("y", "In 2026 we studied the market.", lock)
        self.assertEqual((year["matched"], year["near"], year["unlocked"]), ([], [], []))


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

    def test_rupee_minus_and_quotes(self):
        p = _run_cp1252("number_lock.py", ["--lock", "{0}", "{1}"],
                        [("lock.csv", "id,label,value,source\nL1,revenue,Rs 51.4 crore,https://example.org/f\nL2,change,14.22%,https://example.org/g\n"),
                         ("asset.txt", "Revenue \u20b951.4 crore, a change of \u221214.22% \u201cas filed\u201d.\n")])
        self.assert_utf8_output(p, "\u20b951.4 crore")
        self.assertIn("\u221214.22%".encode("utf-8"), p.stdout)

    def test_rupee_json(self):
        p = _run_cp1252("number_lock.py", ["--lock", "{0}", "{1}", "--json"],
                        [("lock.csv", "id,label,value,source\nL1,revenue,Rs 51.4 crore,https://example.org/f\n"),
                         ("asset.txt", "Revenue \u20b951.4 crore.\n")])
        self.assert_utf8_output(p, "\u20b951.4 crore")


if __name__ == "__main__":
    unittest.main()
