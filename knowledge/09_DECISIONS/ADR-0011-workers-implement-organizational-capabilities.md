---
id: ADR-0011

title: Workers Implement Organizational Capabilities

status: Accepted

date: YYYY-MM-DD

---

# ADR-0011

# Workers Implement Organizational Capabilities

## Context

Organizational capabilities define what an organization is able to accomplish.

However, capabilities are abstract by nature and cannot produce outcomes on their own.

Execution requires an operational implementation that applies capabilities consistently and produces accountable artifacts.

AI Business OS separates the definition of organizational capabilities from their execution to ensure that capabilities remain stable while implementation can evolve over time.

---

## Decision

Workers are adopted as the executable implementations of organizational capabilities.

Capabilities define *what* the organization can do.

Workers define *how* those capabilities are executed.

Workers execute shared Playbooks to transform organizational capabilities into meaningful outcomes.

The implementation of a Worker may be Human, AI, or Hybrid without changing the underlying organizational capability.

---

## Consequences

### Positive

- Organizational capabilities remain independent of technology.
- Human and AI implementations share the same execution model.
- Workers can evolve without redefining organizational capabilities.
- New technologies can be adopted without redesigning the operating model.
- Organizational execution becomes modular and adaptable.

### Trade-offs

- Organizations must clearly distinguish capabilities from implementations.
- Worker definitions require ongoing governance.
- Additional architectural discipline is needed to preserve this separation.

---

## Principle

Capabilities define intent.

Playbooks define execution.

Workers implement capabilities.

Artifacts deliver value.

---

Capabilities become real through execution.

Human-Led.

AI-Amplified.