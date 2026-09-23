# ZERO Early Pilot

ZERO is looking for a small number of real agent workflows to stress-test before production.

## Good pilot fit
Your agent can do at least one consequential thing: spend money, send external messages/data, modify records, call write-capable APIs, delegate to another agent, or change production state.

## What to send
A sanitized MCP/OpenAPI/tool schema plus 1–5 outcomes that must never happen.

Do **not** send secrets, credentials, customer data, production tokens, or private keys.

## What ZERO returns
- a reproducible multi-step action trace when a forbidden outcome is found;
- the state/sequence that made the bypass possible;
- a suggested regression rule to prevent recurrence.

## Cost
First pilot scan: free during validation.

There is no checkout and no payment collection in this repository. The purpose of the pilot is to learn whether the result is useful enough that teams want repeat scans.
