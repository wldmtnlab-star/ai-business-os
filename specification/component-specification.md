# Component Specification

Version: Draft v1

---

# Overview

A Component is the fundamental building block of the AI Business OS Specification.

All AIBOS resources are Components.

This specification defines the common structure and behavior shared by every resource type.

---

# Purpose

Component Specification provides:

- Common metadata
- Versioning
- Resource identification
- Validation rules
- Lifecycle expectations

Every resource inherits these definitions.

---

# Resource Model

Every Component MUST contain:

```yaml
apiVersion:
kind:
metadata:
```

Additional fields are defined by each individual resource specification.

---

# apiVersion

Identifies the specification version implemented by the resource.

Example:

```yaml
apiVersion: aibos.dev/v1
```

Breaking changes MUST introduce a new apiVersion.

---

# kind

Identifies the resource type.

Examples include:

- Organization
- Knowledge
- Worker
- Playbook

Future resource types MAY include:

- Team
- Department
- Memory
- Tool
- Plugin
- Event

---

# Metadata

Every Component MUST include a metadata object.

## Required Fields

| Field | Description |
|--------|-------------|
| name | Unique resource name |
| version | Resource version |

---

## Optional Fields

| Field | Description |
|--------|-------------|
| description | Human-readable description |
| author | Resource author |
| owner | Owning organization or person |
| homepage | Project URL |
| license | License identifier |
| tags | Classification tags |
| created | Creation date |
| updated | Last updated |

Example:

```yaml
metadata:

  name: designer

  version: 1.0.0

  description: Graphic Designer Worker

  tags:

    - design

    - branding
```

---

# Naming Rules

Resource names SHOULD:

- use lowercase
- use kebab-case
- remain stable
- be unique within an Organization

Examples:

Good

```
designer

customer-support

brand-guide
```

Avoid

```
Designer01

MyWorker

temp
```

---

# Versioning

Resources SHOULD follow Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Example:

```
1.0.0

1.2.3

2.0.0
```

---

# Identity

A Component is uniquely identified by:

```
apiVersion

kind

metadata.name

metadata.version
```

---

# Validation Rules

Every Component MUST satisfy:

- apiVersion exists
- kind exists
- metadata exists
- metadata.name exists
- metadata.version exists

Validation MUST fail if any required field is missing.

---

# Lifecycle

Every Component follows the same lifecycle.

```
Created
      │
      ▼
Validated
      │
      ▼
Loaded
      │
      ▼
Referenced
      │
      ▼
Executed (optional)
      │
      ▼
Archived
```

Not every Component is executable.

Only Playbooks are directly executed by the Runtime.

---

# Compatibility

Future versions SHOULD remain backward compatible whenever possible.

Breaking changes MUST increment the major specification version.

---

# Extensibility

Additional metadata fields MAY be introduced by future specification versions.

Runtime implementations SHOULD ignore unknown optional fields unless explicitly required.

---

# Summary

The Component Specification defines the common contract shared by every AIBOS resource.

All higher-level specifications inherit this foundation.