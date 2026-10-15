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

    def test_enrichment_row_needs_second_source(self):
        alone = ac.check(["Alpha"], rows("Alpha,CRM in use,ProductX,enrichment export row 4,verified,ToolA,2026-10-12\n"), enrichment=["ToolA"])
        self.assertTrue(any("enrichment tool" in p for p in alone["problems"]))
        confirmed = ac.check(["Alpha"], rows("Alpha,CRM in use,ProductX,https://alpha.example.org/careers,verified,ToolA,2026-10-12\n"), enrichment=["ToolA"])
        self.assertFalse(any("enrichment tool" in p for p in confirmed["problems"]))

    def test_enrichment_tools_own_site_is_not_a_second_source(self):
        r = ac.check(["Alpha"], rows("Alpha,CRM in use,ProductX,https://toola.example.com/companies/alpha,verified,ToolA,2026-10-12\n"), enrichment=["ToolA"])
        self.assertTrue(any("enrichment tool" in p for p in r["problems"]))

    def test_own_crm_record_not_treated_as_enrichment(self):
        r = ac.check(["Alpha"], rows("Alpha,Customer status,Customer,file: crm-export.csv row 3,verified,OurCRM,2026-10-12\n"), enrichment=["ToolA"])
        self.assertEqual(r["problems"], [])

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

    # Run 31C, Codex finding F003: an empty population and empty rows are problems, never "Problems: none"
    def test_empty_list_and_empty_table_are_problems(self):
        r = ac.check([], [])
        self.assertTrue(any("account list is empty" in p for p in r["problems"]))
        self.assertTrue(any("research table has no rows" in p for p in r["problems"]))

    def test_table_with_no_rows_is_a_problem(self):
        r = ac.check(["Alpha"], [])
        self.assertTrue(any("research table has no rows" in p for p in r["problems"]))

    def test_verified_or_unverified_row_with_empty_value(self):
        v = ac.check(["Alpha"], rows("Alpha,HQ,,https://a.org | https://b.org,verified,,2026-10-14\n"))
        self.assertTrue(any("verified row has no value" in p for p in v["problems"]))
        u = ac.check(["Alpha"], rows("Alpha,HQ,,https://a.org,unverified,,2026-10-14\n"))
        self.assertTrue(any("unverified row has no value" in p for p in u["problems"]))
        nf = ac.check(["Alpha"], rows("Alpha,HQ,,,not found,,2026-10-14\n"))
        self.assertEqual(nf["problems"], [])

    def test_row_with_empty_field_name(self):
        r = ac.check(["Alpha"], rows("Alpha,,City,https://a.org | https://b.org,verified,,2026-10-14\n"))
        self.assertTrue(any("has no field name" in p for p in r["problems"]))

    def test_reconciliation_probe_row(self):
        r = ac.check(["Account A"], rows("Account A,,,https://a.example/x | https://b.example/y,verified,,2026-10-14\n"))
        self.assertTrue(any("has no field name" in p for p in r["problems"]))
        self.assertTrue(any("verified row has no value" in p for p in r["problems"]))

    def test_main_empty_files_exit_1(self):
        d = tempfile.mkdtemp()
        lp, rp = os.path.join(d, "list.txt"), os.path.join(d, "research.csv")
        with open(lp, "w", encoding="utf-8") as fh:
            fh.write("")
        with open(rp, "w", encoding="utf-8") as fh:
            fh.write(HEAD + "\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = ac.main(["--list", lp, "--research", rp])
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

    def test_account_name_with_rupee_and_quotes(self):
        name = "Caf\u00e9 \u201cAlpha\u201d \u20b9 Ltd"
        p = _run_cp1252("account_list_check.py", ["--list", "{0}", "--research", "{1}"],
                        [("list.txt", name + "\n"),
                         ("r.csv", HEAD + "\n" + name + ",revenue,\u20b951.4 crore,https://a.example/x,verified,,2026-10-14\n")])
        self.assert_utf8_output(p, name)


class PlaceholderValueTests(unittest.TestCase):
    """S6, run 32A: a verified or unverified row whose value is N/A, NA, n/a, none, unknown, TBD or a lone dash counts as
    empty, exactly as an empty value does (F003)."""

    def test_placeholder_values_count_as_empty(self):
        for value in ["N/A", "NA", "n/a", "none", "None", "unknown", "Unknown", "TBD", "tbd", "-", " N/A ", "\u2013", "\u2014"]:
            for status in ("verified", "unverified"):
                r = ac.check(["Alpha"], rows("Alpha,HQ,%s,https://a.org | https://b.org,%s,,2026-10-14\n" % (value, status)))
                self.assertTrue(any("%s row has no value" % status in p for p in r["problems"]), (value, status, r["problems"]))

    def test_real_values_that_contain_those_words_are_kept(self):
        for value in ["None Ltd", "Unknown Capital", "TBD Labs", "NASSCOM member", "-5%"]:
            r = ac.check(["Alpha"], rows("Alpha,HQ,%s,https://a.org | https://b.org,verified,,2026-10-14\n" % value))
            self.assertFalse(any("has no value" in p for p in r["problems"]), (value, r["problems"]))

    def test_not_found_row_unchanged(self):
        nf = ac.check(["Alpha"], rows("Alpha,HQ,,,not found,,2026-10-14\n"))
        self.assertEqual(nf["problems"], [])


if __name__ == "__main__":
    unittest.main()
