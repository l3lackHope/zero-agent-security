# Nebius × NVIDIA Global AI Hackathon — ZERO Execution Track

Verified against the official rules on 2026-09-25.

## Entry strategy

Use ZERO as an existing project and make a **significant post-Aug-26 update** rather than pretending the project is new.

Target track: **Coding and Agentic Engineering**.

Working submission name: **ZERO Agent Reliability Lab**

## Required hackathon integration

The submitted build must:
- run on Nebius Token Factory or Nebius AI Cloud;
- use at least one NVIDIA open-source model;
- make a runtime call to Token Factory inference API OR run/deploy using Nebius AI Cloud compute;
- provide a working demo URL/test build;
- provide public open-source code with a visible OSI-style license;
- include setup instructions;
- include a <=3 minute public demo video;
- explain significant updates made during the submission period.

No claim of qualification is made until the required Nebius/NVIDIA runtime integration is actually tested.

## Significant update scope

Turn the current deterministic stateful path explorer into a hybrid **model-guided + deterministic** reliability tester.

1. Operator defines forbidden outcomes/invariants.
2. ZERO builds the state/action graph from tool definitions.
3. Deterministic exploration provides baseline coverage.
4. An NVIDIA model on Nebius prioritizes action/state combinations that appear semantically likely to violate an invariant.
5. The deterministic runner verifies every candidate trace.
6. Only reproducible traces become findings.
7. A regression case is emitted for each verified finding.
8. If no finding is produced, report tested coverage and residual uncertainty.

The model must never be treated as the verifier. It proposes candidates; deterministic replay remains authoritative.

## Why this fits the judging criteria

### Technological implementation
Nebius/NVIDIA is used for semantic trace prioritization, not a cosmetic chat wrapper.

### Design
The product flow is: define invariant → import tools → run test → inspect verified trace → export regression case.

### Potential impact
Target users are teams deploying tool-using agents that can spend money, send data, change systems, or cross approval boundaries.

### Quality of idea
The project focuses on failure modes that emerge only from combinations of actions, time, state, and delegation.

## Hard gates

Do not submit until:
- [ ] Nebius/Devpost registration completed by the entrant
- [ ] required terms reviewed/accepted by entrant
- [ ] Nebius credentials/credits available
- [ ] NVIDIA model runtime call verified
- [ ] existing project update is significant and documented
- [ ] public repo has acceptable open-source license
- [ ] working demo is available
- [ ] demo video is recorded and public
- [ ] submission wording contains no fabricated users/revenue/security findings

## Capital logic

Prize pool is not booked as capital until actually won/received.
Credits are runway, not revenue.
Any prize-related tax/identity paperwork remains an entrant action.
