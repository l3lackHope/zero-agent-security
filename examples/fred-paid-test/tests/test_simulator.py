import unittest
from simulator import PaidTestWorkflow

VALID = {"event_id":"evt-001","name":"Ada","email":"ada@example.com"}

class PaidTestWorkflowTests(unittest.TestCase):
    def test_valid_event_completes_once(self):
        r = PaidTestWorkflow().handle(VALID.copy())
        self.assertEqual((r.disposition,r.sheet_writes,r.notifications,r.failure_alerts),
                         ("completed",1,1,0))

    def test_duplicate_is_safe_noop(self):
        w = PaidTestWorkflow()
        w.handle(VALID.copy())
        r = w.handle(VALID.copy())
        self.assertEqual((r.disposition,r.sheet_writes,r.notifications),
                         ("duplicate_ignored",0,0))

    def test_bad_email_rejected_before_side_effect(self):
        p = VALID.copy()
        p["email"] = "invalid"
        r = PaidTestWorkflow().handle(p)
        self.assertEqual((r.http_status,r.sheet_writes,r.notifications),
                         (400,0,0))

    def test_sheet_failure_alerts_and_stops(self):
        r = PaidTestWorkflow().handle(VALID.copy(), sheet_ok=False)
        self.assertEqual((r.disposition,r.sheet_writes,r.notifications,r.failure_alerts),
                         ("sheet_failed",0,0,1))

    def test_notification_failure_alerts_without_rewriting_sheet(self):
        r = PaidTestWorkflow().handle(VALID.copy(), notify_ok=False)
        self.assertEqual((r.disposition,r.sheet_writes,r.notifications,r.failure_alerts),
                         ("notification_failed",1,0,1))

if __name__ == "__main__":
    unittest.main()
