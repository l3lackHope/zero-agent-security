# WhatsApp Lead Qualification + Human Handoff Proof

Self-directed portfolio proof. Not client production history.

This example demonstrates a reliability-first WhatsApp-style automation pattern for service businesses and agency white-label work: webhook intake, receipt filtering, validation, idempotency, lead qualification, human handoff, CRM upsert, retry handling, audit logging, and safe replay.

## Acceptance tests

- Duplicate message ID never creates a second downstream side effect.
- Delivery/read receipt is ignored.
- Missing sender or message ID is rejected before downstream writes.
- Explicit human request routes to human handoff.
- Low confidence routes to human handoff.
- Human-owned conversation blocks automated follow-up.
- Temporary API failure is retryable.
- Permanent failure emits an operator-facing alert event.
- Every branch emits a correlation ID and audit record.

## Production notes

A real deployment would use the customer's WhatsApp Business provider, CRM, and credential store. No secrets belong in exported workflow JSON. Consequential outbound messages should retain an approval/handoff boundary appropriate to the client's risk tolerance.
