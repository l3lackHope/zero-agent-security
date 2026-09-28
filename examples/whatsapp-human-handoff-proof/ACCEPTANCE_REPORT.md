# Acceptance Report

Self-directed portfolio proof. Not client production history.

## Validation run

Command:

```bash
python test_workflow.py
```

Result:

- 9 tests executed
- 9 passed
- 0 failed

## Behaviors covered

1. Normal lead completes.
2. Duplicate message is blocked before a second CRM write or outbound message.
3. Delivery/read receipts are ignored.
4. Missing required fields are rejected before side effects.
5. Explicit human request stops automation and hands off.
6. Low-confidence input hands off.
7. Retryable provider failure recovers.
8. Permanent provider failure surfaces an operator alert.
9. Retry exhaustion surfaces an operator alert.

## Commercial relevance

This proof targets the exact failure modes buyers repeatedly request in WhatsApp, CRM and n8n automation work: idempotency, safe replay, retries, failure visibility, human handoff and auditable decisions.

## Limits

The provider and CRM are simulated in-memory components. This is deliberately not presented as client production history or as a live WhatsApp Business integration.
