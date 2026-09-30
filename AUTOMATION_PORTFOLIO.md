# Kendo AI Automation — Technical Proof Portfolio

This repository contains **self-directed and qualification-oriented technical proofs**. Unless a folder explicitly says otherwise, these are **not presented as client production history**.

The goal is to make reliability, failure handling, scope discipline and handoff quality inspectable before a buyer grants production access.

## 1) WhatsApp Lead Qualification + Human Handoff

Path: `examples/whatsapp-human-handoff-proof/`

Demonstrates:
- event validation
- receipt filtering
- idempotency / duplicate blocking
- human handoff for sensitive or low-confidence cases
- CRM-style upsert
- retryable vs permanent failure behavior
- operator alerting
- audit logging

Validation: **9/9 acceptance tests pass.**

Best fit:
- service-business lead qualification
- WhatsApp intake
- CRM routing
- agency white-label delivery
- human-in-the-loop automation

## 2) Content Engine Reliability Spike

Path: `examples/content-engine-reliability-spike/`

Demonstrates:
- configuration-driven source registry
- source enable/disable without pipeline edits
- deterministic deduplication
- required-field validation
- run-level audit events
- spend / token budget caps
- deterministic quality gates
- acceptance-test evidence

Validation: **6/6 acceptance tests pass.**

Best fit:
- content automation
- scheduled generation systems
- RAG/content-pipeline preflight work
- production hardening
- stabilisation / observability discussions

## 3) n8n Reliability Proof

Path: `examples/n8n-reliability-proof/`

Focus:
- production-style reliability controls
- retry/error handling
- safe side effects
- monitoring / handoff thinking

Best fit:
- paid qualifications
- workflow rescue
- API/webhook hardening
- white-label overflow

## 4) Manufacturing Pilot

Path: `examples/manufacturing-pilot/`

Focus:
- bounded workflow proof for a manufacturing automation brief
- representative inputs and acceptance-oriented thinking

## 5) FRED Paid-Test Proof

Path: `examples/fred-paid-test/`

Focus:
- proof built around a public paid-test automation brief
- requirement matching instead of generic portfolio claims

## Delivery principles

- acceptance criteria before build
- explicit scope boundaries
- validation before consequential side effects
- idempotency where replay is possible
- bounded retries
- visible terminal failures
- human approval when mistakes matter
- written handoff / recovery notes
- no fabricated client history or performance claims

## Commercial path

The intended engagement model is:

**paid qualification → bounded pilot → implementation → stabilisation → maintenance / white-label repeat work**
