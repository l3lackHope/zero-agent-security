# ZERO — Break Your AI Agent Before Production

ZERO is an early-stage adversarial security tester for AI agents and MCP-style tool workflows.

Instead of checking one tool call at a time, ZERO searches for **forbidden outcomes that emerge from sequences of individually allowed actions** — across state, time, approvals, and delegated agents.

## What ZERO is testing

Examples of failures we want to discover:

- cumulative spending that bypasses per-action limits
- private-data exfiltration through allowed read + send actions
- approval-token reuse
- privilege expansion through delegated/child agents
- production changes reached through multi-step action chains

## Prototype thesis

A conventional authorization test can say every individual action is allowed while the overall workflow still reaches a prohibited outcome.

Example:

```text
Policy: total purchases must stay <= $500/day

buy($300) -> allowed
buy($300) -> allowed

Outcome: $600/day -> policy violated
```

ZERO explores the stateful path, reports the violating sequence, and should eventually suggest the policy/control needed to prevent it.

## Status

**Pre-alpha / market validation.**

The current project is intentionally small. We are validating whether teams deploying write-capable AI agents have this problem before building dashboards, billing, or production infrastructure.

## Early access / pilot

If you are deploying an AI agent that can call tools, MCP servers, APIs, or perform consequential actions, open an issue in this repository describing the workflow you want stress-tested.

Useful inputs include:

- tool or MCP definitions
- OpenAPI schemas
- actions the agent is allowed to perform
- outcomes that must never happen

Do not post secrets, production credentials, customer data, or private API keys.

## Direction

The target workflow is:

```text
Agent / MCP / OpenAPI definition
        |
        v
ZERO adversarial explorer
        |
        +--> multi-step attack paths
        +--> state/time/delegation violations
        +--> reproducible traces
        +--> policy regression tests
```

## Project ZERO

This repository is part of Project ZERO: an AI-led experiment to discover, validate, and build a business from zero based on real market evidence.

No claim of product-market fit is being made yet. Market pull will be judged by concrete pilot requests, submitted workflows, repeat usage, and willingness to pay.
