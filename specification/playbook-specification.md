# Playbook Specification

Version: Draft v1

---

# Overview

A Playbook defines a repeatable organizational workflow.

A Playbook orchestrates Workers, Knowledge, and execution steps to accomplish a specific business objective.

Playbooks describe **what should happen**, not how an AI model internally generates responses.

---

# Purpose

Playbooks standardize business processes.

Examples include:

- Create a product listing
- Respond to customer inquiries
- Publish a blog article
- Review a design
- Generate a proposal
- Onboard a new employee

A Playbook SHOULD be reusable across organizations whenever possible.

---

# Resource Definition

Every Playbook resource MUST include:

- apiVersion
- kind
- metadata
- spec

Example:

```yaml
apiVersion: aibos.dev/v1

kind: Playbook

metadata:

  name: create-product

  version: 1.0.0

spec:

  objective: Publish a new Etsy product.

  workers:

    - designer

    - copywriter

  steps:

    - id: design

      worker: designer

      action: Create product images.

    - id: description

      worker: copywriter

      action: Write product description.
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

```
Playbook
```

---

# Metadata

Required fields:

| Field | Description |
|--------|-------------|
| name | Playbook name |
| version | Version |

Optional:

| Field | Description |
|--------|-------------|
| description | Description |
| author | Author |
| tags | Classification tags |

---

# Specification

## Objective

Business goal.

```yaml
objective: Publish a product.
```

---

## Workers

Workers participating in the Playbook.

```yaml
workers:

  - designer

  - copywriter
```

---

## Inputs

Optional input parameters.

```yaml
inputs:

  productName:

    type: string

  category:

    type: string
```

---

## Outputs

Expected outputs.

```yaml
outputs:

  images

  description

  tags
```

---

## Steps

Execution sequence.

Example:

```yaml
steps:

  - id: design

    worker: designer

    action: Create product images.

  - id: copy

    worker: copywriter

    action: Write product description.
```

Steps SHOULD execute sequentially unless otherwise specified by the Runtime.

---

## Success Criteria

Defines completion requirements.

```yaml
success:

  - Images created

  - Description approved
```

---

# Design Principles

Playbooks SHOULD be:

- reusable
- deterministic
- human-readable
- modular

Playbooks SHOULD NOT contain organizational knowledge.

Playbooks SHOULD reference Workers and Knowledge instead.

---

# Validation Rules

Every Playbook MUST contain:

- apiVersion
- kind
- metadata.name
- metadata.version
- spec.objective
- spec.steps

---

# Example

```yaml
apiVersion: aibos.dev/v1

kind: Playbook

metadata:

  name: create-product

  version: 1.0.0

spec:

  objective: Publish Etsy Product

  workers:

    - designer

    - copywriter

  inputs:

    title:

      type: string

  outputs:

    - images

    - description

  steps:

    - id: design

      worker: designer

      action: Generate artwork.

    - id: description

      worker: copywriter

      action: Create listing description.

  success:

    - Product assets completed
```