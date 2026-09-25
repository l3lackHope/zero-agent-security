# ZERO — Defensive Agent Security Grant Proposal

## Project
ZERO is an early-stage open-source adversarial regression tester for AI-agent workflows.

It focuses on a specific defensive problem: individually permitted actions can combine across time, state, approvals, and delegation to produce an operator-defined forbidden outcome.

Examples of defensive invariants:
- cumulative spend must remain under an operator-defined limit;
- sensitive data must not reach unauthorized destinations;
- an approval token must not be reusable outside its intended state;
- a delegated or child agent must not exceed the authority of its parent;
- production-impacting actions must preserve required human approval.

## Why this matters
Traditional allow/deny checks and single-action tests can miss failures that emerge only after multiple individually valid steps. Agentic systems increasingly interact with money, customer data, infrastructure, email, and other consequential systems.

ZERO is intended to help developers test those multi-step behaviors before production and turn discoveries into regression cases.

## Defensive scope
ZERO is for local, mock, sandbox, testnet, or otherwise explicitly authorized environments only. It is not intended for unauthorized production testing.

The project does not rely on speculative vulnerability claims. A valid finding must include a reproducible trace, the violated invariant, impact, and a regression test.

## Current evidence
The repository contains synthetic benchmarks covering cumulative spend, delegated/shared budgets, approval reuse, and multi-node/stateful action chains.

The project is pre-revenue and early-stage. Existing benchmarks are development evidence, not claims about third-party production vulnerabilities.

## Proposed grant project
Build an open benchmark and regression suite for stateful agent authorization failures.

Planned deliverables:
1. A machine-readable invariant format for business and authorization constraints.
2. A reference runner that explores multi-step state/action traces.
3. Open synthetic benchmark scenarios for spend, data movement, approval lifecycle, delegation, and irreversible actions.
4. Reproducible finding artifacts: trace, state transitions, violated invariant, remediation notes, and regression case.
5. Example adapters for common agent/tool schemas such as MCP or OpenAPI-style tool definitions.
6. Documentation for running the suite locally without production credentials.
7. A public evaluation methodology that distinguishes tested coverage, passed paths, untested paths, and residual uncertainty.

## Public benefit
The benchmark, reference scenarios, and evaluation methodology are intended to be released openly so teams can test agent workflows before production and improve secure-by-design development practices.

## Proposed 10,000 USD work package
If direct funding is available:
- engineering and benchmark development: $6,000
- test infrastructure and evaluation: $2,000
- documentation, examples, and public release: $1,000
- independent validation / contingency: $1,000

If support is provided as API credits instead, the project scope would shift compute-heavy portions toward systematic trace generation, evaluation, and benchmark expansion.

## Milestones
### Milestone 1 — Invariant + trace format
Define stable schemas and baseline benchmark corpus.

### Milestone 2 — Stateful exploration
Implement multi-step state/action exploration with reproducible evidence output.

### Milestone 3 — Regression and adapters
Add regression generation and reference tool-schema adapters.

### Milestone 4 — Public evaluation release
Publish benchmark methodology, limitations, examples, and results.

## Success criteria
- reproducible open benchmark suite;
- multiple stateful failure classes represented;
- deterministic regression cases for discovered synthetic failures;
- clear coverage and residual-uncertainty reporting;
- documentation sufficient for another developer to run the suite locally.

## Repository
https://github.com/l3lackHope/zero-agent-security

## Status
Early-stage, open-source, pre-revenue.
