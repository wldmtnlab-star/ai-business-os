# Organization Specification

Version: Draft v1

---

# Overview

An Organization is the root resource in AIBOS.

It defines the structure, capabilities, and execution context of an AI-native organization.

Every AIBOS project MUST contain exactly one Organization definition.

---

# Purpose

An Organization serves as the entry point for the Runtime.

It declares:

- organizational metadata
- available Knowledge
- available Workers
- available Playbooks
- runtime configuration

The Runtime MUST load the Organization before loading any other resources.

---

# Resource Definition

Every Organization MUST include:

- apiVersion
- kind
- metadata
- spec

Example:

```yaml
apiVersion: aibos.dev/v1
kind: Organization

metadata:
  name: nagi-print-studio
  version: 1.0.0

spec:
  knowledge:
    - knowledge/company.md

  workers:
    - workers/designer.md

  playbooks:
    - playbooks/create-product.md
```

---

# apiVersion

Defines the specification version.

Example:

```yaml
apiVersion: aibos.dev/v1
```

Future incompatible changes MUST introduce a new apiVersion.

---

# kind

The resource type.

For this specification the value MUST be:

```text
Organization
```

---

# Metadata

Metadata identifies the organization.

Required fields:

| Field | Description |
|--------|-------------|
| name | Unique organization name |
| version | Organization version |

Optional fields:

| Field | Description |
|--------|-------------|
| description | Human readable description |
| owner | Organization owner |
| homepage | Project URL |
| license | License |
| tags | Classification tags |

Example:

```yaml
metadata:
  name: nagi-print-studio
  version: 1.0.0
  description: AI-powered Etsy print shop
```

---

# Specification

The spec section defines the operational resources.

## Knowledge

List of Knowledge resources.

```yaml
knowledge:
  - knowledge/company.md
  - knowledge/style-guide.md
```

---

## Workers

List of Worker resources.

```yaml
workers:
  - workers/designer.md
  - workers/marketing.md
```

---

## Playbooks

List of Playbook resources.

```yaml
playbooks:
  - playbooks/create-product.md
```

---

# Runtime

Optional runtime configuration.

Example:

```yaml
runtime:

  provider: openai

  model: gpt-5.5

  temperature: 0.3
```

Runtime implementations MAY ignore unsupported settings.

---

# Validation Rules

The Runtime MUST verify:

- apiVersion exists
- kind equals Organization
- metadata.name exists
- metadata.version exists
- spec exists

If validation fails, execution MUST stop.

---

# Execution Flow

The Runtime SHOULD execute resources in this order:

1. Load Organization
2. Load Knowledge
3. Load Workers
4. Load Playbooks
5. Initialize Runtime
6. Execute requested Playbook

---

# Design Principles

Organizations should be:

- modular
- versioned
- portable
- provider agnostic
- human readable

---

# Example

```yaml
apiVersion: aibos.dev/v1

kind: Organization

metadata:

  name: nagi-print-studio

  version: 1.0.0

spec:

  knowledge:

    - knowledge/company.md

    - knowledge/branding.md

  workers:

    - workers/designer.md

    - workers/copywriter.md

  playbooks:

    - playbooks/create-product.md

runtime:

  provider: openai

  model: gpt-5.5
```