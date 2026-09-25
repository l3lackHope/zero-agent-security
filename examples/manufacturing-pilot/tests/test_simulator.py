import unittest
from simulator import ManufacturingPilot

HEALTHY = {
    "event_id": "shift-001",
    "line_id": "LINE-A",
    "planned_minutes": 480,
    "run_minutes": 450,
    "ideal_cycle_seconds": 30,
    "total_units": 850,
    "good_units": 820,
}

CRITICAL = {
    "event_id": "shift-002",
    "line_id": "LINE-C",
    "planned_minutes": 480,
    "run_minutes": 350,
    "ideal_cycle_seconds": 45,
    "total_units": 400,
    "good_units": 350,
}

class ManufacturingPilotTests(unittest.TestCase):
    def test_oee_calculation_and_healthy_classification(self):
        r = ManufacturingPilot().process(HEALTHY.copy())
        self.assertEqual(r.oee_pct, 85.42)
        self.assertEqual((r.status, r.alert), ("healthy", False))

    def test_duplicate_event_is_suppressed(self):
        p = ManufacturingPilot()
        p.process(HEALTHY.copy())
        r = p.process(HEALTHY.copy())
        self.assertEqual((r.status, r.alert, r.duplicate), ("duplicate_ignored", False, True))

    def test_critical_line_triggers_alert(self):
        r = ManufacturingPilot().process(CRITICAL.copy())
        self.assertEqual(r.oee_pct, 54.69)
        self.assertEqual((r.status, r.alert), ("critical", True))

    def test_missing_field_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing_field"):
            ManufacturingPilot().process({"event_id": "x"})

    def test_invalid_numeric_is_rejected(self):
        p = HEALTHY.copy()
        p["planned_minutes"] = 0
        with self.assertRaisesRegex(ValueError, "invalid_numeric"):
            ManufacturingPilot().process(p)

if __name__ == "__main__":
    unittest.main()
