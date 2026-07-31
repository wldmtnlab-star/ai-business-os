# Runtime Specification

## Status

Draft

Version: 1.0

---

# Overview

Runtimeは、

Organizationを実行するための標準実装です。

Runtimeは、

Knowledge、

Workers、

Playbooks

を読み込み、

LLMへ適切なコンテキストを渡します。

Runtime自身は、

ビジネスロジックを持ちません。

---

# Responsibilities

Runtime MUST:

- Load an Organization
- Resolve Component dependencies
- Load required Knowledge
- Execute Playbooks
- Invoke Workers
- Return Outputs

Runtime MUST NOT:

- Modify Knowledge
- Rewrite Playbooks
- Change Worker definitions

---

# Runtime Flow

```

Load Organization

↓

Validate

↓

Resolve Dependencies

↓

Load Knowledge

↓

Execute Workflow

↓

Collect Outputs

↓

Return Result

```

---

# Execution Context

Runtime SHOULD generate a single execution context containing:

- Organization Metadata
- Selected Playbook
- Required Workers
- Required Knowledge
- Runtime Configuration

---

# Human Checkpoints

Runtime MUST support pausing execution.

```

Designer

↓

Human Approval

↓

Writer

```

Execution resumes after approval.

---

# LLM Providers

Runtime MUST be provider-agnostic.

Supported providers MAY include:

- OpenAI
- Anthropic
- Google
- Local Models

---

# Configuration

Runtime SHOULD load configuration from:

```

organization.yaml

```

Runtime MAY support:

```

.env

config.yaml

```

---

# Validation

Before execution,

Runtime MUST validate:

- Organization exists
- Playbook exists
- Worker references
- Knowledge references

Execution MUST fail on validation errors.

---

# Outputs

Runtime returns structured outputs.

Example

```yaml
status: success

outputs:

title:

description:

image:

tags:
```

---

# Extensibility

Runtime SHOULD support:

- Plugins
- Hooks
- Middleware
- Custom Providers

---

# Summary

Runtime is the execution engine of AIBOS.

It connects Organizations,

Knowledge,

Workers,

and Playbooks,

into executable AI workflows.