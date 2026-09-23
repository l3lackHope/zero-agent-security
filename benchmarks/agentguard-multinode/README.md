# External Benchmark 003 — Multi-node guardrail staleness

Target for design comparison: `Caua-ferraz/AgentGuard`.

Date: 2026-09-23

## Why this benchmark matters

AgentGuard documents a deliberate multi-node trade-off: rate/cost state is reconciled in the background, so distributed limits are bounded-overshoot rather than globally strict. It also documents a short cross-node window in which a consumed one-shot approval may still be honored by another node before reconciliation.

Those are documented limitations, **not ZERO-discovered vulnerabilities**.

They are valuable benchmark material because ZERO is intended to reason about forbidden outcomes that emerge from time + state + multiple actors/nodes, rather than single isolated calls.

## Model

We model two nodes with stale local views of a shared $500 ceiling.

Sequence:

1. node A observes $0 and admits $300;
2. before reconciliation, node B also observes $0 and admits $300;
3. shared intended outcome becomes $600;
4. policy invariant `shared_spend <= $500` is violated.

A second future case will model one-shot approval consumption racing across two nodes.

## Success criterion for ZERO

ZERO should be able to describe the violation as a temporal/stateful trace and distinguish it from a conventional isolated-call test.

This benchmark is synthetic and safe: no target service is executed, no network requests are made, and no third-party system is attacked.
