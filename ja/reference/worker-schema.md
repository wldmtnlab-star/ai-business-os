# Worker Schema

Workerは、Organization内で特定の役割を担当するコンポーネントです。

Workerは知識（Knowledge）を保持せず、
業務フロー（Playbook）も持ちません。

Workerは、

**「どのような役割を担うか」**

だけを定義します。

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

WorkerはMarkdownで保存します。

```
workers/

designer.md

writer.md

reviewer.md
```

Workerは **Markdown MUST** です。

---

# Front Matter

WorkerはYAML Front Matterを持つことを推奨します。

```markdown
---
name: Designer
version: 1.0
description: Creates visual designs.
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
| goal | MUST |

例

```yaml
name: Designer

description:
Creates visual designs.

goal:
Design beautiful and consistent products.
```

---

# Optional Fields

必要に応じて、

以下を追加できます。

```yaml
version:

owner:

skills:

constraints:

knowledge:

playbooks:

tags:
```

これらはすべて **MAY** です。

---

# Skills

Workerが持つ専門能力です。

例

```yaml
skills:

- Graphic Design

- Typography

- Branding

- Prompt Engineering
```

Runtimeは、

将来的にSkillを利用して、

Workerを自動選択できる可能性があります。

---

# Constraints

Workerが守るべきルールです。

例

```yaml
constraints:

- Follow brand guidelines

- Never copy copyrighted works

- Use concise language
```

Constraintsは、

Knowledgeとは異なります。

Knowledgeは事実。

Constraintsは行動ルールです。

---

# Knowledge Dependencies

Workerは、

必要なKnowledgeを宣言できます。

```yaml
knowledge:

- brand.md

- style-guide.md

- products.md
```

Runtimeは、

必要なKnowledgeのみを読み込みます。

---

# Compatible Playbooks

Workerは、

対応するPlaybookを宣言できます。

```yaml
playbooks:

- create-product

- create-banner

- create-lp
```

これはドキュメント用途であり、

Runtimeが利用するかどうかは実装に依存します。

---

# Responsibilities

Workerは、

担当業務のみを定義します。

例えば、

Designerなら、

- Visual Design
- Branding
- Layout

など。

Playbookを書くべきではありません。

---

# What a Worker Should NOT Contain

Workerには、

以下を書いてはいけません。

❌ Organization全体の説明

❌ 業務フロー

❌ ブランド情報

❌ 商品情報

❌ FAQ

これらはKnowledgeまたはPlaybookに記述します。

---

# Relationships

```
Knowledge

↓

Worker

↓

Playbook

↓

Runtime
```

Workerは、

KnowledgeとPlaybookの橋渡しを行います。

---

# Best Practices

- 一つの役割に集中する
- 小さく作る
- 再利用可能にする
- 他Workerへ依存しない
- Knowledgeを直接コピーしない

---

# Example

```yaml
---
name: SEO Specialist

version: 1.0

description:
Optimizes content for search visibility.

goal:
Improve discoverability while maintaining quality.

skills:

- SEO

- Keyword Research

- Metadata

knowledge:

- seo.md

- brand.md

constraints:

- Never use keyword stuffing

- Preserve natural language
---
```

---

# Summary

Workerは、

Organizationの中で役割を担当するコンポーネントです。

Workerは、

知識ではなく、

役割を定義します。

Knowledge、

Playbook、

Runtimeと組み合わせることで、

AI Teamを構成します。