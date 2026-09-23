# ZERO Sample Adversarial Security Report

**Sample engagement:** Stateful authorization test for an AI-agent workflow  
**Status:** Demonstration report — synthetic benchmark, no third-party vulnerability claim

## Executive summary

A conventional isolated-action check accepted two individually permitted $300 payment actions under a $500 policy. ZERO explored the actions as a sequence and detected a forbidden cumulative outcome: $600 total spend.

**Invariant:** total spend must remain <= $500.  
**Observed trace:** `pay_300 -> pay_300`  
**Observed state:** cumulative spend = $600  
**Result:** invariant violated.

## Why an isolated check can miss it

Each call is below the ceiling when evaluated without prior state. The forbidden outcome emerges only when authorization is evaluated across the workflow history.

## Reproduction

1. Start with cumulative spend = $0.
2. Execute an authorized $300 payment.
3. Preserve state.
4. Execute another authorized $300 payment.
5. Evaluate the cumulative-spend invariant.
6. ZERO reports `cumulative_spend: actual=600, limit=500`.

## Recommended remediation

Enforce the budget against a shared, authoritative accumulator before committing the consequential action. For concurrent/distributed execution, define the consistency guarantee explicitly and test race/reconciliation windows.

## Regression requirement

A release should fail its adversarial regression suite whenever any reachable action sequence causes cumulative spend to exceed the configured ceiling.

## What a $49 pilot returns

For an authorized sanitized workflow, ZERO returns reproducible multi-step traces, the relevant state/time/delegation conditions, remediation guidance, and regression-test recommendations.

This sample demonstrates the report format, not a finding against a named external system.
