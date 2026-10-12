#!/usr/bin/env python3
"""Tests for account_list_check.py. Run: python3 test_account_list_check.py -v"""
import csv
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import account_list_check as ac  # noqa: E402

HEAD = ",".join(ac.COLUMNS)


def rows(text):
    return list(csv.DictReader(io.StringIO(HEAD + "\n" + text)))


class AccountTests(unittest.TestCase):
    def test_norm_suffixes(self):
        self.assertEqual(ac.norm("Alpha Technologies Limited"), "alpha")
        self.assertEqual(ac.norm("The Alpha Corporation"), "alpha")
        self.assertEqual(ac.norm("Alpha eSolutions Ltd."), "alpha")

    def test_duplicates(self):
        r = ac.check(["Alpha", "Alpha Corporation", "Beta"], rows(
            "Alpha,HQ,City,https://a.org | https://b.org,verified,,2026-10-11\n"
            "Beta,HQ,,,not found,,2026-10-11\n"))
        self.assertTrue(any("possible duplicate" in p for p in r["problems"]))
        self.assertEqual(r["unique_accounts"], 2)

    def test_coverage_missing_and_extra(self):
        r = ac.check(["Alpha", "Beta"], rows("Alpha,HQ,City,https://a.org,unverified,,2026-10-11\nGamma,HQ,City,https://g.org,unverified,,\n"))
        self.assertIn("Beta", r["missing"])
        self.assertTrue(any("not on the list: Gamma" in p for p in r["problems"]))

    def test_verified_rule(self):
        one = ac.check(["Alpha"], rows("Alpha,HQ,City,https://a.org,verified,,2026-10-11\n"))
        self.assertTrue(any("verified needs" in p for p in one["problems"]))
        same_domain = ac.check(["Alpha"], rows("Alpha,HQ,City,https://a.org/x | https://www.a.org/y,verified,,\n"))
        self.assertTrue(any("verified needs" in p for p in same_domain["problems"]))
        two = ac.check(["Alpha"], rows("Alpha,HQ,City,https://a.org | https://b.org,verified,,\n"))
        self.assertEqual(two["problems"], [])
        conn = ac.check(["Alpha"], rows("Alpha,HQ,City,file: crm.csv row 3,verified,user CRM,\n"))
        self.assertEqual(conn["problems"], [])

    def test_banned_domain(self):
        r = ac.check(["Alpha"], rows("Alpha,Revenue,10,https://www.screener-example.in/x | https://a.org,unverified,,\n"),
                     banned=["screener-example.in"])
        self.assertTrue(any("banned source" in p for p in r["problems"]))

    def test_banned_bare_site_name(self):
        r = ac.check(["Alpha"], rows("Alpha,Revenue,10,screener-example.in/company/alpha,unverified,,\n"),
                     banned=["screener-example.in"])
        self.assertTrue(any("banned source" in p for p in r["problems"]))
        ok = ac.check(["Alpha"], rows("Alpha,HQ,City,file: crm.csv row 3,unverified,,\n"), banned=["screener-example.in"])
        self.assertEqual(ok["problems"], [])

    def test_not_found_with_value_and_bad_status(self):
        r = ac.check(["Alpha"], rows("Alpha,ERP,SAP,,not found,,\nAlpha,Cloud,,https://a.org,maybe,,\n"))
        self.assertTrue(any("not found but has a value" in p for p in r["problems"]))
        self.assertTrue(any("status 'maybe'" in p for p in r["problems"]))

    def test_no_source(self):
        r = ac.check(["Alpha"], rows("Alpha,HQ,City,,unverified,,\n"))
        self.assertTrue(any("has no source" in p for p in r["problems"]))

    def test_two_lists(self):
        r = ac.check(["Alpha"], rows("Alpha,HQ,City,https://a.org | https://b.org,verified,,\nAlpha,ERP,,,not found,,\n"))
        self.assertIn("Alpha", r["lists"]["verified"])
        self.assertIn("Alpha", r["lists"]["unverified"])

    def test_list_csv_and_main(self):
        d = tempfile.mkdtemp()
        lp = os.path.join(d, "list.csv")
        rp = os.path.join(d, "research.csv")
        with open(lp, "w", encoding="utf-8") as fh:
            fh.write("account,region\nAlpha,India\nBeta,India\n")
        with open(rp, "w", encoding="utf-8") as fh:
            fh.write(HEAD + "\nAlpha,HQ,City,https://a.org | https://b.org,verified,,\nBeta,HQ,,,not found,,\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = ac.main(["--list", lp, "--research", rp])
        self.assertEqual(code, 0)
        self.assertIn("Coverage: 2 of 2", buf.getvalue())

    def test_unreadable(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = ac.main(["--list", "/no/list.txt", "--research", "/no/r.csv"])
        self.assertEqual(code, 2)
        self.assertIn("do not fill rows from memory", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
