# WhatsApp Lead Qualification + Human Handoff Proof

Self-directed portfolio proof. **Not client production history.**

This is a runnable reliability-focused workflow simulator for the failure modes that repeatedly appear in paid n8n / CRM / WhatsApp automation briefs.

## What it demonstrates

- webhook-style event intake
- delivery/read receipt filtering
- payload validation
- deterministic idempotency
- duplicate-side-effect prevention
- lead intent classification
- low-confidence / sensitive / explicit-human handoff
- CRM-style upsert behavior
- bounded retries for transient provider failures
- operator alerts for permanent or exhausted failures
- structured audit logging
- safe replay behavior

## Run it

```bash
cd examples/whatsapp-human-handoff-proof
python test_workflow.py
```

Current validation: **9/9 acceptance tests pass.**

See [ACCEPTANCE_REPORT.md](./ACCEPTANCE_REPORT.md) for the tested behaviors and proof limitations.

## Files

- `workflow.py` — runnable workflow simulator
- `test_workflow.py` — acceptance tests
- `ACCEPTANCE_REPORT.md` — validation evidence and commercial relevance

## Production boundary

A real deployment would replace the in-memory CRM and messaging provider with the customer's approved WhatsApp Business provider, CRM/API, secure credential store, persistence layer, monitoring and deployment environment.

No secrets belong in exported workflow files. Consequential outbound actions should preserve an explicit approval or handoff boundary appropriate to the client's risk tolerance.
