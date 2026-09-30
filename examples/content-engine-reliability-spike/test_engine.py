import unittest

from engine import BudgetExceeded, ContentEngine


def item(source="rss1", ext="1", title="Hello",
         body="This is a sufficiently long body for deterministic gate testing."):
    return {"source_id": source, "external_id": ext, "title": title, "body": body}


class ContentEngineTests(unittest.TestCase):
    def setUp(self):
        self.engine = ContentEngine(
            [{"id": "rss1", "enabled": True}, {"id": "off", "enabled": False}],
            monthly_cap=10,
        )

    def test_duplicate_blocked(self):
        self.assertEqual(len(self.engine.ingest("r1", [item()])), 1)
        self.assertEqual(len(self.engine.ingest("r2", [item()])), 0)

    def test_disabled_source_skipped(self):
        self.assertEqual(self.engine.ingest("r", [item(source="off")]), [])

    def test_missing_required_rejected(self):
        x = item()
        x["body"] = ""
        self.assertEqual(self.engine.ingest("r", [x]), [])

    def test_budget_cap_blocks_generation(self):
        accepted = self.engine.ingest("r", [item()])[0]
        self.engine.generate("r", accepted, 8)
        with self.assertRaises(BudgetExceeded):
            self.engine.generate("r", accepted, 3)

    def test_deterministic_gate_pass(self):
        accepted = self.engine.ingest("r", [item()])[0]
        draft = self.engine.generate("r", accepted, 1)
        passed, _ = self.engine.gates("r", draft, "sufficiently")
        self.assertTrue(passed)

    def test_source_registry_change_needs_no_pipeline_edit(self):
        self.engine.add_source({"id": "new", "enabled": True})
        self.assertEqual(len(self.engine.ingest("r", [item(source="new", ext="2")])), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
