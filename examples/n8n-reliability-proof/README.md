# n8n Automation Reliability Proof

A small, transparent reference artifact showing the engineering approach used for automation work.

It is **not a client case study** and does not claim production usage.

## What it demonstrates

- webhook intake with explicit validation
- normalization before business logic
- idempotency / duplicate suppression before consequential actions
- two independent approval gates
- payment-status gate
- a clear side-effect boundary
- explicit safe-hold behavior instead of silently continuing
- synthetic regression tests for duplicate, approval, payment, and invalid-input cases

## What it intentionally does not do

The reference workflow stops before a real CRM/email/payment action. A client build would put the external action after the side-effect boundary, use n8n credentials rather than hard-coded secrets, configure retry/backoff where appropriate, and attach a dedicated Error Trigger workflow/alerting path.

## Files

- `workflow.json` — importable n8n reference workflow (no credentials)
- `simulator.py` — deterministic model of the business gates
- `tests/test_simulator.py` — synthetic regression tests
- `sample_payloads/` — example inputs

## Validation

Run locally:

`python -m unittest discover -s tests -v`

Expected current result: **5 tests pass**.

The simulator exists so the business invariants can be regression-tested without requiring an n8n account or third-party API credentials.
