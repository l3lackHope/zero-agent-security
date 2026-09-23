import unittest
import zero

class ZeroTests(unittest.TestCase):
    def setUp(self):
        self.cfg,self.actions=zero.load("examples/purchasing.json")

    def test_finds_cumulative_spend(self):
        f=zero.explore(self.cfg,self.actions,2)
        self.assertTrue(any(any(v["type"]=="cumulative_spend" for v in x["violations"]) for x in f))

    def test_finds_private_exfiltration(self):
        f=zero.explore(self.cfg,self.actions,2)
        self.assertTrue(any(any(v["type"]=="private_data_exfiltration" for v in x["violations"]) for x in f))

if __name__=="__main__": unittest.main()
