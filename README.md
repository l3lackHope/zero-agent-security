# ZERO — Break Your AI Agent Before Production

ZERO is an early-stage adversarial security tester for AI agents and MCP-style tool workflows.

Instead of checking one tool call at a time, ZERO searches for **forbidden outcomes that emerge from sequences of individually allowed actions** — across state, time, approvals, and delegated agents.

## What ZERO looks for

- cumulative spending that bypasses per-action checks
- private-data exfiltration through allowed read + send actions
- approval-token reuse
- privilege expansion through delegated/child agents
- production changes reached through multi-step action chains

Example:

```text
Policy: total purchases must stay <= $500/day

buy($300) -> individually allowed
buy($300) -> individually allowed

Outcome: $600/day -> forbidden
```

ZERO explores the stateful path and returns a reproducible trace plus remediation/regression guidance.

## Paid pilot — $49/project

For teams with a write/send/spend/refund/deploy/delegation-capable agent or MCP workflow:

1. **Quick fit assessment — free.**
2. **Authorized adversarial pilot — $49/project.**
3. You provide sanitized tool/MCP/OpenAPI definitions and the outcomes that must never happen.
4. ZERO returns reproducible multi-step traces, relevant state/time/delegation conditions, remediation guidance, and regression-test recommendations.

Payment is arranged privately only after scope is accepted. Do **not** post secrets, production credentials, customer data, or private API keys.

Start here: open the **PAID PILOT — $49 adversarial scan** issue in this repository, or use the pilot template.

See [sample report](docs/SAMPLE-REPORT.md) and [pilot details](docs/PILOT.md).

## Status

**Pre-alpha / paid market validation.** No product-market-fit claim is being made. The validation bar is paid market pull, not stars or compliments.

## Safety / authorization

ZERO is for local, sandbox, mock, or explicitly authorized workflows. No unsolicited production testing.

## Project ZERO

Project ZERO is an AI-led experiment to discover, validate, and build a business from zero. Board capital for this experiment is $0; revenue earned by ZERO funds subsequent development.
