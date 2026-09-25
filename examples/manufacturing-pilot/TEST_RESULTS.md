# Test Results

Date: 2026-09-25

Local deterministic regression run:

`python -m unittest discover -s tests -v`

Observed:

- OEE calculation + healthy classification: PASS
- duplicate event suppression: PASS
- critical line alert decision: PASS
- missing field rejection: PASS
- invalid numeric rejection: PASS

**5 passed, 0 failed.**

Synthetic evidence from the test data:

- LINE-A OEE: **85.42%** -> healthy
- LINE-C OEE: **54.69%** -> critical -> alert

Limitation: this validates the deterministic core logic only. The n8n workflow is credential-free reference material and still needs environment-specific import/integration testing before production use.
