# Reliability Proof — Test Results

Date: 2026-09-25

This file records a local regression run of the deterministic simulator committed in this directory.

Command:

`python -m unittest discover -s tests -v`

Observed result:

- duplicate execution does not repeat the side-effect boundary: PASS
- invalid input is rejected before state mutation: PASS
- missing second approval is held safely: PASS
- overdue payment state is held safely: PASS
- valid paid + two-approval path reaches the side-effect boundary exactly once: PASS

Summary: **5 tests passed, 0 failed.**

Important limitation: these tests exercise the deterministic simulator, not a live third-party system and not an n8n production deployment. The adjacent `workflow.json` is a credential-free reference workflow. A client deployment still requires environment-specific import validation, credentials, retry/backoff configuration, Error Trigger/alerting, and integration tests against the actual downstream APIs.
