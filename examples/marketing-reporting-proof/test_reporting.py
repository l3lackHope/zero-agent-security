import unittest
from reporting import normalize, wow_change, build_summary, run_weekly_report

class ReportingTests(unittest.TestCase):
    def test_normalize_two_sources(self):
        rows = normalize("Client A","2026-W39",{"spend":100,"leads":10,"conversions":2},{"leads":4,"conversions":1})
        self.assertEqual(len(rows),2)
        self.assertEqual(sum(r.leads for r in rows),14)

    def test_wow_positive(self):
        self.assertEqual(wow_change(120,100),20.0)

    def test_wow_zero_base(self):
        self.assertEqual(wow_change(5,0),100.0)

    def test_summary_contains_all_metrics(self):
        s = build_summary({"spend":120,"leads":12,"conversions":3},{"spend":100,"leads":10,"conversions":2})
        self.assertIn("spend",s)
        self.assertIn("leads",s)
        self.assertIn("conversions",s)

    def test_report_is_email_ready(self):
        r = run_weekly_report("Client A","2026-W39",{"spend":100,"leads":10,"conversions":2},{"leads":4,"conversions":1},{"spend":80,"leads":12,"conversions":2})
        self.assertTrue(r["email_ready"])
        self.assertIsNone(r["error_alert"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
