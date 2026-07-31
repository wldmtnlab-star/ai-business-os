# Worker Specification

Version: Draft v1

---

# Overview

A Worker represents a role within an AI-native organization.

Workers perform tasks, apply organizational knowledge, and execute Playbooks.

A Worker is not an AI model.

A Worker defines **who** performs the work, not **how** the AI generates responses.

---

# Purpose

Workers encapsulate organizational responsibilities.

A Worker may represent:

- Designer
- Marketing Specialist
- Customer Support
- Sales Representative
- Product Manager
- Project Manager
- Software Engineer

Workers SHOULD be reusable across multiple Organizations.

---

# Resource Definition

Every Worker resource MUST include:

- apiVersion
- kind
- metadata
- spec

Example:

```yaml
apiVersion: aibos.dev/v1

kind: Worker

metadata:

  name: designer

  version: 1.0.0

spec:

  role: UI/UX Designer

  goal: Create beautiful and usable interfaces.
```

---

# apiVersion

Defines the specification version.

```yaml
apiVersion: aibos.dev/v1
```

---

# kind

The resource type.

```text
Worker
```

---

# Metadata

Required:

| Field | Description |
|--------|-------------|
| name | Worker name |
| version | Version |

Optional:

| Field | Description |
|--------|-------------|
| description | Description |
| author | Author |
| tags | Tags |

---

# Specification

The spec section defines the Worker.

---

## Role

Defines who the Worker is.

Example:

```yaml
role: Marketing Specialist
```

---

## Goal

The Worker's primary objective.

Example:

```yaml
goal: Increase customer engagement.
```

---

## Responsibilities

Primary duties.

Example:

```yaml
responsibilities:

  - Write product descriptions

  - Review branding

  - Optimize SEO
```

---

## Capabilities

Worker skills.

Example:

```yaml
capabilities:

  - copywriting

  - seo

  - branding
```

---

## Knowledge

Referenced Knowledge resources.

Example:

```yaml
knowledge:

  - knowledge/branding.md

  - knowledge/products.md
```

Workers SHOULD consume Knowledge instead of embedding large amounts of information directly.

---

## Tools

Available tools.

Example:

```yaml
tools:

  - search

  - image-generator

  - markdown
```

Tool names are implementation-dependent.

---

## Constraints

Behavioral limitations.

Example:

```yaml
constraints:

  - Never invent product specifications.

  - Follow the brand guide.

  - Ask for clarification if required information is missing.
```

---

# Design Principles

Workers SHOULD be:

- reusable
- composable
- specialized
- knowledge-driven
- provider agnostic

Workers SHOULD NOT contain workflow logic.

Workflow belongs to Playbooks.

---

# Validation Rules

Every Worker MUST include:

- apiVersion
- kind
- metadata.name
- metadata.version
- spec.role
- spec.goal

---

# Example

```yaml
apiVersion: aibos.dev/v1

kind: Worker

metadata:

  name: designer

  version: 1.0.0

spec:

  role: Graphic Designer

  goal: Produce high-quality visual assets.

  responsibilities:

    - Design posters

    - Design logos

  capabilities:

    - illustration

    - branding

  knowledge:

    - knowledge/branding.md

  tools:

    - image-generator

    - markdown

  constraints:

    - Follow the brand guide.
```