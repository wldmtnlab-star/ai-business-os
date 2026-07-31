# Playbook Schema

Playbookは、Organizationにおける業務フローを定義するコンポーネントです。

Playbookは、

**「どのように仕事を進めるか」**

を定義します。

Playbook自身は知識を持ちません。

また、Workerの役割も定義しません。

Playbookは、

KnowledgeとWorkersを組み合わせ、

業務を実行する流れを定義します。

---

# Conformance

このドキュメントでは、

**MUST**
**SHOULD**
**MAY**

を RFC 2119 に従って使用します。

| Keyword | Meaning |
|----------|---------|
| MUST | 必須 |
| SHOULD | 強く推奨 |
| MAY | 任意 |

---

# File Format

PlaybookはMarkdownファイルとして保存します。

```
playbooks/

create-product.md

customer-support.md

release-product.md
```

---

# Front Matter

YAML Front Matterの利用を推奨します。

```yaml
---
name: Create Product

version: 1.0

description:
Generate a complete Etsy product.

owner:
Marketing Team
---
```

---

# Required Fields

最低限、

以下を定義します。

| Field | Level |
|--------|-------|
| name | MUST |
| description | MUST |

---

# Recommended Sections

Playbookは、

以下の構成を推奨します。

```markdown
# Overview

## Goal

## Inputs

## Workflow

## Outputs

## Human Checkpoints

## Error Handling
```

---

# Inputs

Playbookは、

必要なKnowledgeやWorkerを明示します。

例

```yaml
knowledge:

- brand.md

- products.md

workers:

- designer

- writer

- seo

- reviewer
```

---

# Workflow

Workflowは、

Playbookの中心です。

例

```
Read Brand

↓

Create Concept

↓

Generate Prompt

↓

Create Image

↓

Write Description

↓

Generate SEO Tags

↓

Review

↓

Publish
```

Workflowは、

順序が重要です。

---

# Outputs

Playbookは、

期待する成果物を定義します。

例

```yaml
outputs:

- title

- description

- image

- tags
```

---

# Human Checkpoints

人による確認ポイントを定義できます。

例

```
Concept

↓

👤 Human Approval

↓

Generate Images
```

Runtimeは、

ここで停止し、

承認を待機できます。

---

# Error Handling

Playbookは、

異常時の対応方針を定義できます。

例

```yaml
on_error:

retry: 2

fallback:
reviewer
```

Runtimeが対応可能な場合は、

この情報を利用できます。

---

# Best Practices

- 一つの目的に集中する
- Workflowは短く保つ
- Workerを細かく分ける
- Human Reviewを適切に配置する
- 再利用できる設計にする

---

# Anti-Patterns

避けるべき例

❌ ブランド情報を書く

❌ Workerの詳細を書く

❌ 長すぎるWorkflow

❌ 一つのPlaybookで全業務を扱う

---

# Relationships

```
Knowledge

↓

Workers

↓

Playbook

↓

Runtime
```

Playbookは、

KnowledgeとWorkerを統合する役割を持ちます。

---

# Example

```yaml
---
name: Create Etsy Product

version: 1.0

description:
Generate a complete Etsy product.

knowledge:

- brand.md

- style-guide.md

workers:

- designer

- writer

- seo

- reviewer

outputs:

- image

- title

- description

- tags
---
```

---

# Summary

Playbookは、

Organizationの業務フローを定義するコンポーネントです。

Knowledgeが

「何を知っているか」

Workerが

「誰が担当するか」

なら、

Playbookは

**「どのように仕事を進めるか」**

を定義します。