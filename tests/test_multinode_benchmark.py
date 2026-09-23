import unittest
import zero

class MultiNodeBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.cfg, self.actions = zero.load("benchmarks/agentguard-multinode/scenario.json")

    def test_isolated_admissions_are_below_shared_ceiling(self):
        ceiling = self.cfg["rules"]["max_total_spend"]
        self.assertTrue(all(a.spend <= ceiling for a in self.actions))

    def test_temporal_cross_node_trace_exceeds_shared_ceiling(self):
        findings = zero.explore(self.cfg, self.actions, 2)
        trace = ["node_a_admit_300_before_reconcile", "node_b_admit_300_before_reconcile"]
        self.assertTrue(any(
            f["trace"] == trace and
            any(v["type"] == "cumulative_spend" and v["actual"] == 600
                for v in f["violations"])
            for f in findings
        ))

if __name__ == "__main__":
    unittest.main()
