# Attack Catalog

ZERO prioritizes outcome-level failures that ordinary per-action authorization can miss.

## Stateful limit bypass
Repeated individually allowed actions cross a cumulative budget, rate, or quota.

## Data-flow composition
An allowed read followed by an allowed external send creates a prohibited disclosure.

## Approval reuse
A human approval intended for one action or transaction is replayed or reused.

## Delegation expansion
A child/delegated agent obtains or exercises authority beyond its parent.

## Action chaining
Several low-risk operations compose into a high-impact state change.

The catalog is intentionally narrow while market validation is running. New attack classes should be added because of real pilot evidence, not feature speculation.
