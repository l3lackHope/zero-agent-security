import unittest
from simulator import ReliableLeadIntake

BASE = {
    "event_id": "evt-001",
    "email": "Buyer@Example.com",
    "company": "Example Co",
    "consent": True,
    "payment_status": "current",
    "approval_1": True,
    "approval_2": True,
}

class ReliabilityTests(unittest.TestCase):
    def test_valid_two_approval_path_reaches_boundary_once(self):
        s = ReliableLeadIntake()
        r = s.handle(BASE.copy())
        self.assertEqual((r.http_status, r.disposition, r.side_effects), (202, "ready_for_side_effect", 1))

    def test_duplicate_never_repeats_side_effect(self):
        s = ReliableLeadIntake()
        first = s.handle(BASE.copy())
        second = s.handle(BASE.copy())
        self.assertEqual(first.side_effects, 1)
        self.assertEqual((second.disposition, second.side_effects), ("duplicate_ignored", 0))

    def test_missing_second_approval_holds(self):
        s = ReliableLeadIntake()
        p = BASE.copy()
        p["approval_2"] = False
        r = s.handle(p)
        self.assertEqual((r.disposition, r.side_effects), ("held", 0))

    def test_overdue_payment_holds(self):
        s = ReliableLeadIntake()
        p = BASE.copy()
        p["payment_status"] = "overdue"
        r = s.handle(p)
        self.assertEqual((r.disposition, r.side_effects), ("held", 0))

    def test_invalid_payload_rejected_before_state_change(self):
        s = ReliableLeadIntake()
        p = BASE.copy()
        p.pop("email")
        r = s.handle(p)
        self.assertEqual((r.http_status, r.disposition, r.side_effects), (400, "validation_failed", 0))
        self.assertNotIn("evt-001", s.seen)

if __name__ == "__main__":
    unittest.main()
