import unittest
import zero

class DelegationBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.cfg, self.actions = zero.load("benchmarks/delegation/scenario.json")

    def test_each_child_action_is_individually_under_parent_budget(self):
        limit = self.cfg["rules"]["max_total_spend"]
        self.assertTrue(all(a.spend <= limit for a in self.actions))

    def test_cross_child_sequence_breaks_shared_parent_budget(self):
        findings = zero.explore(self.cfg, self.actions, 2)
        expected = ["child_a_pay_300", "child_b_pay_300"]
        self.assertTrue(any(
            f["trace"] == expected and
            any(v["type"] == "cumulative_spend" and v["actual"] == 600
                for v in f["violations"])
            for f in findings
        ))

if __name__ == "__main__":
    unittest.main()
