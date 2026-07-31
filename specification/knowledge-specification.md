# Knowledge Specification

Version: Draft v1

---

# Overview

A Knowledge resource represents structured organizational knowledge that can be shared, reused, and consumed by AI Workers.

Knowledge is the foundation of AI Business OS.

Unlike prompts, Knowledge is persistent, versionable, and reusable across multiple Workers and Playbooks.

---

# Purpose

Knowledge captures information that defines how an organization thinks and operates.

Examples include:

- Company information
- Brand guidelines
- Writing style
- Product catalog
- Policies
- Procedures
- Frequently Asked Questions
- Domain expertise

Knowledge SHOULD remain independent from any specific Worker or Playbook.

---

# Resource Definition

Every Knowledge resource MUST include:

- apiVersion
- kind
- metadata
- content

Example:

```yaml
apiVersion: aibos.dev/v1

kind: Knowledge

metadata:

  name: company-profile

  version: 1.0.0

content: |
  Nagi Print Studio specializes in Japanese-inspired printable wall art...
```

---

# apiVersion

Defines the specification version.

Example:

```yaml
apiVersion: aibos.dev/v1
```

---

# kind

The resource type.

For this specification the value MUST be:

```text
Knowledge
```

---

# Metadata

Required fields:

| Field | Description |
|--------|-------------|
| name | Unique knowledge name |
| version | Version |

Optional fields:

| Field | Description |
|--------|-------------|
| description | Human-readable description |
| category | Classification |
| author | Author |
| tags | Search tags |
| updated | Last update |

Example:

```yaml
metadata:

  name: brand-guide

  version: 1.0.0

  category: branding
```

---

# Content

Knowledge content is stored in Markdown.

Example:

```yaml
content: |

  # Brand Identity

  Primary Color

  Typography

  Tone of Voice
```

Markdown allows:

- headings
- lists
- tables
- code blocks
- links
- images

---

# Design Principles

Knowledge SHOULD be:

- reusable
- versioned
- portable
- human-readable
- AI-friendly

Knowledge SHOULD NOT include execution logic.

---

# Scope

Knowledge defines **facts**, not **actions**.

Examples:

✓ Company overview

✓ Product information

✓ Design guidelines

✓ Customer personas

✗ Workflow execution

✗ Decision logic

✗ Runtime configuration

---

# Validation Rules

Every Knowledge resource MUST contain:

- apiVersion
- kind
- metadata.name
- metadata.version
- content

---

# Best Practices

Prefer multiple small Knowledge resources instead of one large document.

Good:

- company.md
- branding.md
- faq.md
- products.md

Avoid:

- everything.md

---

# Example

```yaml
apiVersion: aibos.dev/v1

kind: Knowledge

metadata:

  name: writing-style

  version: 1.0.0

content: |

  # Tone

  Friendly

  Professional

  Clear

  # Writing Rules

  - Short paragraphs
  - Active voice
  - Avoid jargon
```