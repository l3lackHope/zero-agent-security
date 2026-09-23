import unittest
import zero

class AgentiBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.cfg, self.actions = zero.load("benchmarks/agenti/scenario.json")

    def test_each_mock_payment_is_individually_within_budget(self):
        limit = self.cfg["rules"]["max_total_spend"]
        self.assertTrue(all(a.spend <= limit for a in self.actions))

    def test_stateful_explorer_finds_cumulative_budget_violation(self):
        findings = zero.explore(self.cfg, self.actions, 2)
        hit = [
            f for f in findings
            if f["trace"] == ["pay_mock_300", "pay_mock_300"]
            and any(v["type"] == "cumulative_spend" and v["actual"] == 600
                    for v in f["violations"])
        ]
        self.assertTrue(hit)

if __name__ == "__main__":
    unittest.main()
