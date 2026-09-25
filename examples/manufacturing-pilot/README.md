# Manufacturing Automation Pilot — Synthetic Proof

Built to match a real buyer pattern: a small n8n + AI/API manufacturing pilot that turns production data into a report/alert while handling validation, duplicate events, and failure boundaries.

This is **self-directed synthetic proof**, not a client case study and not a production deployment.

## Demonstrates

- one structured production-data input
- validation before calculation
- deterministic OEE calculation
- duplicate-event suppression with `event_id`
- critical / warning / healthy classification
- alert decision for critical OEE
- credential-free n8n reference workflow
- regression-tested core logic

## Synthetic fields

`event_id`, `line_id`, `planned_minutes`, `run_minutes`, `ideal_cycle_seconds`, `total_units`, `good_units`

## Current thresholds

- critical: OEE < 65%
- warning: 65% <= OEE < 85%
- healthy: OEE >= 85%

Thresholds are placeholders for a pilot. A real plant should define thresholds from its operating rules.

## Validation evidence

Run:

`python -m unittest discover -s tests -v`

Current local result: **5 tests passed, 0 failed**.

The proof uses no production credentials or customer data.
