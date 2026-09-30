# Content Engine Reliability Spike

Self-directed technical proof. **Not client production history.**

This small runnable project demonstrates production-minded controls that appear repeatedly in higher-value automation briefs:

- configuration-driven source registry
- source enable/disable without pipeline code edits
- deterministic deduplication / idempotency
- required-field validation before downstream work
- run-level audit events
- token / model-spend budget cap
- deterministic quality gates
- repeatable acceptance tests

## Run

```bash
cd examples/content-engine-reliability-spike
python test_engine.py
```

Current validation: **6/6 tests pass.**

## Why it exists

Higher-value automation buyers are often evaluating whether a workflow can survive retries, duplicate inputs, configuration changes, budget ceilings, and handoff to another operator—not just whether the happy path works.

This spike is intentionally small and inspectable. It demonstrates those controls without claiming a production client deployment.

## Production boundary

A real delivery would replace the in-memory registry and state with client-owned infrastructure, wire real source adapters and model APIs, persist audit rows, and deploy through the client's CI/CD and credential-management process.
