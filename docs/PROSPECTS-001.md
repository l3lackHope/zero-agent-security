# Prospect Batch 001

Date: 2026-09-23

Goal: identify public projects where consequential MCP/agent actions make stateful adversarial testing easy to explain. This is a research shortlist, not a vulnerability list.

## Priority targets

1. **UseJunior/email-agent-mcp** — external email writes; sending is guarded by an explicit allowlist. Candidate question: can multi-step state or workflow composition reach an outcome the configured policy intended to prevent?
2. **trekmail/mcp-server** — explicit environment + per-call confirmation gates for sending and migration actions. Strong fit for approval/confirmation state testing.
3. **tokencanopy/e2a** — agent email with outbound actions and optional human-in-the-loop approval. Strong fit for approval lifecycle/state-machine regression.
4. **zavora-ai/mcp-email** — broad write/destructive surface including send, delete and batch operations. Candidate for composed-action and cumulative-impact policies.
5. **chronomcp/chronomcp** — transactional guard with human approval, irreversible actions and compensation. High-value benchmark for multi-step policy/transaction semantics.

## Outreach rule

Do not allege a vulnerability from documentation alone. First contact should offer a free fit assessment based on a sanitized workflow. A full authorized adversarial pilot is $49.

No automated spam, no unsolicited exploit execution, no credentials, and no production attacks.
