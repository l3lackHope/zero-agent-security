import unittest

from workflow import WhatsAppLeadWorkflow, SimulatedMessagingProvider


def event(message_id="m1", text="I need a price quote", event_type="message", sender="+15550001111"):
    return {"message_id": message_id, "sender": sender, "event_type": event_type, "text": text}


class WorkflowTests(unittest.TestCase):
    def test_normal_lead_completes(self):
        w = WhatsAppLeadWorkflow()
        result = w.process(event())
        self.assertEqual(result.status, "completed")
        self.assertEqual(w.crm.write_count, 1)
        self.assertEqual(len(w.provider.sent), 1)

    def test_duplicate_is_blocked_before_second_side_effect(self):
        w = WhatsAppLeadWorkflow()
        w.process(event())
        result = w.process(event())
        self.assertEqual(result.status, "duplicate_blocked")
        self.assertEqual(w.crm.write_count, 1)
        self.assertEqual(len(w.provider.sent), 1)

    def test_receipt_is_ignored(self):
        w = WhatsAppLeadWorkflow()
        result = w.process(event(event_type="read"))
        self.assertEqual(result.status, "ignored_receipt")
        self.assertEqual(w.crm.write_count, 0)

    def test_invalid_payload_rejected(self):
        w = WhatsAppLeadWorkflow()
        result = w.process({"message_id": "m1", "event_type": "message", "text": "hello"})
        self.assertEqual(result.status, "rejected_invalid")
        self.assertEqual(w.crm.write_count, 0)

    def test_explicit_human_request_stops_automation(self):
        w = WhatsAppLeadWorkflow()
        result = w.process(event(text="Please let me talk to a human agent"))
        self.assertEqual(result.status, "human_handoff")
        self.assertEqual(w.crm.write_count, 0)
        self.assertEqual(len(w.provider.sent), 0)

    def test_low_confidence_handoffs(self):
        w = WhatsAppLeadWorkflow()
        result = w.process(event(text="hi"))
        self.assertEqual(result.status, "human_handoff")

    def test_retryable_failure_recovers(self):
        w = WhatsAppLeadWorkflow(max_retries=2)
        w.provider = SimulatedMessagingProvider(["retryable", None])
        result = w.process(event())
        self.assertEqual(result.status, "completed")
        self.assertEqual(result.retries, 1)
        self.assertEqual(len(w.provider.sent), 1)

    def test_permanent_failure_alerts(self):
        w = WhatsAppLeadWorkflow()
        w.provider = SimulatedMessagingProvider(["permanent"])
        result = w.process(event())
        self.assertEqual(result.status, "operator_alert")
        self.assertEqual(len(w.provider.sent), 0)

    def test_retry_exhaustion_alerts(self):
        w = WhatsAppLeadWorkflow(max_retries=1)
        w.provider = SimulatedMessagingProvider(["retryable", "retryable"])
        result = w.process(event())
        self.assertEqual(result.status, "operator_alert")
        events = [e["event"] for e in w.audit.as_dicts()]
        self.assertIn("operator_alert", events)


if __name__ == "__main__":
    unittest.main(verbosity=2)
