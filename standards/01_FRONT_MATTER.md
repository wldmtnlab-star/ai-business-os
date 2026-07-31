# AI Business OS Standard

# 01_FRONT_MATTER

Version: 1.0

---

# Purpose

Every document within AI Business OS begins with a standardized Front Matter.

The Front Matter provides structured metadata that helps both humans and AI understand the document before reading its content.

It improves consistency, discoverability, version control, and long-term maintainability.

---

# Philosophy

The content explains the knowledge.

The Front Matter explains the document.

Every document should answer two questions immediately:

- What is this document?
- How should it be used?

---

# Standard Format

```yaml
---
id: company

title: Company

type: Knowledge

layer: Knowledge

version: 1.0

status: Active

owner: Human

updated: YYYY-MM-DD

reviewed: YYYY-MM-DD

tags:
  - company
  - organization

related:
  - 05_PROJECTS.md
  - 08_DECISIONS.md
---
```

---

# Field Definitions

## id

A unique identifier.

Rules

- lowercase
- kebab-case or snake_case
- never changes

Example

```yaml
id: company
```

---

## title

Human-readable title.

Example

```yaml
title: Company
```

---

## type

Defines the document category.

Allowed values

- Standard
- Knowledge
- Playbook
- Architecture
- Constitution
- Manifesto
- Brand
- Decision
- Reference

Example

```yaml
type: Knowledge
```

---

## layer

Defines the Business OS layer.

Allowed values

- Foundation
- Identity
- Knowledge
- Execution
- Review
- Evolution
- Standards

Example

```yaml
layer: Knowledge
```

---

## version

Document version.

Semantic Versioning is recommended.

Example

```yaml
version: 1.0
```

---

## status

Current lifecycle status.

Allowed values

- Draft
- Review
- Active
- Deprecated
- Archived

Example

```yaml
status: Active
```

---

## owner

Primary maintainer.

Allowed values

- Human
- AI Worker
- Team Name
- Role

Example

```yaml
owner: Executive AI
```

---

## updated

Date of the latest content update.

Format

```text
YYYY-MM-DD
```

---

## reviewed

Date of the latest review.

Example

```yaml
reviewed: 2026-07-28
```

---

## tags

Search keywords.

Example

```yaml
tags:
  - ai
  - business
  - knowledge
```

---

## related

Related documents.

Only reference documents.

Never duplicate content.

Example

```yaml
related:
  - 02_FOUNDATION.md
  - 03_ARCHITECTURE.md
```

---

# Design Rules

## Rule 1

Every document must include Front Matter.

---

## Rule 2

Front Matter should describe the document, not its content.

---

## Rule 3

Metadata must remain concise.

---

## Rule 4

Content belongs below the Front Matter.

Never duplicate metadata.

---

## Rule 5

The Front Matter should remain stable even when the document evolves.

Only update fields when necessary.

---

# Example

```yaml
---
id: brand

title: Brand Identity

type: Brand

layer: Identity

version: 1.0

status: Active

owner: Human

updated: 2026-07-28

reviewed: 2026-07-28

tags:
  - brand
  - identity

related:
  - 02_FOUNDATION.md
---
```

---

# Architect Notes

A good Front Matter allows AI to understand the purpose of a document before processing its content.

It serves as the table of contents for machines while remaining readable for humans.

As AI Business OS grows, this standard should evolve carefully.

Backward compatibility should be preserved whenever possible.

---

## Human-Led.

## AI-Amplified.