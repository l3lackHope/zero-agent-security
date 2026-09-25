# FRED Paid-Test Matching Proof

A self-directed, credential-free reference built to match the public paid-test shape advertised by FRED.ai for an n8n / Make automation engineer.

This is **not client production work** and does not imply FRED.ai approval or employment.

## Buyer-requested shape mirrored

Webhook → validate required fields → reject bad input → duplicate/loop guard → prepare Google Sheets row → notification boundary → explicit failure alert path.

## What this proof demonstrates

- required-field and email validation before side effects
- stable `event_id` duplicate suppression / safe stopping
- one normalized row contract suitable for Google Sheets
- one notification contract suitable for Slack or email
- visible failure path rather than silent success
- credential-free n8n JSON for review/import
- deterministic regression simulator and tests

## Test evidence

The deterministic simulator was executed locally on 2026-09-25.

Result: **5/5 checks passed**:
1. valid event completes with one Sheet write + one notification
2. duplicate event produces no repeated side effects
3. invalid email fails before side effects
4. Sheet failure raises one failure alert and does not notify success
5. notification failure preserves the prior Sheet write and raises one failure alert

## Production boundary

The reference workflow intentionally does not contain Google/Slack credentials. A paid test in the buyer's environment would use buyer-owned credentials and would be validated end-to-end against their acceptance criteria.
