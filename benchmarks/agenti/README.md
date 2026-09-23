# External Benchmark 001 — Agenti MCP payment tool

Target: `nirholas/agenti` (public repository)

Date: 2026-09-23

## Why this target

Agenti exposes an MCP `pay` tool that can automatically handle x402 payments. This is a useful real-world benchmark for ZERO because a model can invoke a financially consequential tool.

## Observed public interface

At the inspected revision, the MCP `pay` tool accepts:
- URL
- optional EVM private key
- HTTP method
- optional body

The inspected MCP wrapper does not expose a per-call amount ceiling, cumulative session/day budget, or explicit human-approval field in that tool schema.

This is **not a vulnerability claim**. Spending constraints may exist elsewhere in the SDK/protocol/deployment. ZERO must verify the full payment path before reporting a finding.

## ZERO hypothesis

Outcome to test:

> An agent must not spend more than an operator-defined cumulative budget without human approval.

Adversarial paths to explore:
1. repeated individually valid paid requests;
2. retries/redirect-like flows that could trigger more than one authorization;
3. delegation where multiple agents share the same funded identity;
4. payment requests whose individual amount is acceptable but cumulative spend is not.

## Evidence standard

ZERO will only call this a finding if it can reproduce a prohibited outcome in a safe local/test environment and identify the exact action/state sequence. No mainnet funds or third-party systems should be touched.

## Why this matters for market validation

If ZERO can turn this public tool definition into a reproducible stateful regression test, we have a concrete artifact to show a maintainer instead of sending generic sales outreach.
