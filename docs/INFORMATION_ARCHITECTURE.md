# Information Architecture

While `ARCHITECTURE.md` explains how AI Business OS is designed, this document explains how the repository itself is organized to support that architecture.

> How the AI Business OS repository is organized.

AI Business OS is designed as a modular knowledge system.

Each directory, document, and layer has a single responsibility.

Together, they create a coherent operating system for organizations.

---

# Architecture Overview

```text
README
      │
      ▼
GETTING_STARTED
      │
      ▼
ARCHITECTURE
      │
      ▼
Core Components
      │
      ▼
Reference Organizations
      │
      ▼
Continuous Evolution
```

The repository is designed to help users move from understanding concepts to applying them in real organizations.

---

# Repository Structure

```text
/
├── docs/
├── knowledge/
├── playbooks/
├── workers/
├── standards/
├── templates/
├── examples/
├── adr/
└── README.md
```

Each directory represents a distinct capability within AI Business OS.

---

# Repository Layers

## Documentation

```text
docs/
```

Provides documentation for understanding, adopting, and contributing to AI Business OS.

Examples include:

- Getting Started
- Architecture
- Manifesto
- Constitution
- Roadmap

---

## Core Components

```text
knowledge/
playbooks/
workers/
standards/
templates/
```

These directories form the operational core of AI Business OS.

They define:

- What the organization knows
- How work is performed
- Who performs the work
- Shared standards
- Reusable templates

---

## Reference Organizations

```text
examples/
```

Reference Organizations demonstrate how AI Business OS can be implemented in different contexts.

Current example:

```text
examples/
└── digital-agency/
```

Each implementation adapts the core architecture while preserving its principles.

---

## Architecture Decisions

```text
adr/
```

Architecture Decision Records document significant design decisions.

They explain:

- Why a decision was made
- Alternatives considered
- Expected consequences

ADRs preserve architectural knowledge over time.

---

# Documentation Flow

The recommended reading order is:

```text
README
      │
      ▼
GETTING_STARTED
      │
      ▼
MANIFESTO
      │
      ▼
ARCHITECTURE
      │
      ▼
CONSTITUTION
      │
      ▼
Knowledge
      │
      ▼
Playbooks
      │
      ▼
Workers
      │
      ▼
Reference Organizations
```

Readers move from philosophy to implementation.

---

# Information Flow

Knowledge flows throughout the operating system.

```text
Purpose
      │
      ▼
Knowledge
      │
      ▼
Playbooks
      │
      ▼
Workers
      │
      ▼
Execution
      │
      ▼
Artifacts
      │
      ▼
Case Studies
      │
      ▼
Organizational Memory
      │
      ▼
Continuous Evolution
```

Every project enriches the repository.

Every contribution strengthens the operating system.

---

# Design Principles

The repository follows several guiding principles.

## Single Responsibility

Each directory exists for one primary purpose.

---

## Modular Design

Components can evolve independently while remaining connected.

---

## Knowledge First

Knowledge should be captured before it is automated.

---

## Reuse Over Duplication

Information should have one authoritative source.

Reference rather than duplicate.

---

## Continuous Evolution

Documentation evolves together with the operating system.

No document is ever considered complete.

---

# Relationship Between Components

```text
Documentation
        │
        ▼
Core Components
        │
        ▼
Reference Organizations
        │
        ▼
Real-world Execution
        │
        ▼
Continuous Learning
```

The repository itself reflects the architecture it describes.

---

# Closing

Information architecture is not about organizing files.

It is about organizing knowledge.

A well-structured repository enables organizations to learn faster, collaborate better, and evolve continuously.

---

# Intended Audience

This document is intended for:

- Contributors
- Maintainers
- Repository Architects
- Organizations extending AI Business OS

If you are using AI Business OS for the first time, begin with:

1. README
2. GETTING_STARTED
3. ARCHITECTURE

before reading this document.



**Human-Led.**

**AI-Amplified.**