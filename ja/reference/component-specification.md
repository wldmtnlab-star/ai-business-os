# Component Specification

Componentは、AIBOSを構成する最小単位です。

Knowledge、Worker、Playbook、Organizationなど、
すべてのComponentは、この仕様に従います。

---

# Purpose

Componentは、

- 再利用可能
- バージョン管理可能
- 人が読める
- AIが理解できる

ことを目的として設計されています。

---

# Component Types

現在、AIBOSでは以下のComponentを定義します。

| Component | Purpose |
|------------|----------|
| Knowledge | 知識 |
| Worker | 役割 |
| Playbook | 業務フロー |
| Organization | 全体構成 |

将来的には、

- Runtime
- Plugin
- Tool
- Memory

などもComponentとして追加される可能性があります。

---

# Metadata

すべてのComponentは、
共通のMetadataを持つことを推奨します。

```yaml
---
name:
version:
description:
owner:
tags:
created:
updated:
license:
---
```

---

# Required Metadata

最低限、

以下を定義します。

| Field | Level |
|--------|-------|
| name | MUST |
| description | MUST |

---

# Recommended Metadata

以下は推奨です。

| Field | Level |
|--------|-------|
| version | SHOULD |
| owner | SHOULD |
| tags | SHOULD |
| created | MAY |
| updated | MAY |
| license | MAY |

---

# Naming

Component名は、

- 読みやすい
- 一意
- 短い

ことを推奨します。

例

```
Designer

Brand

Create Product
```

---

# File Naming

ファイル名は、

kebab-caseを推奨します。

```
brand.md

create-product.md

style-guide.md
```

---

# Versioning

Componentは、

Semantic Versioningを推奨します。

例

```
1.0.0

1.2.0

2.0.0
```

---

# Ownership

Componentには、

管理者を定義できます。

例

```yaml
owner:

Marketing Team
```

---

# Tags

分類用タグを利用できます。

```yaml
tags:

- marketing

- design

- seo
```

---

# Documentation

Componentは、

人が読めることを重視します。

Markdown本文には、

背景

目的

例

注意事項

を書くことを推奨します。

---

# Single Responsibility

Componentは、

一つの責務だけを持ちます。

Knowledgeは、

Knowledgeだけ。

Workerは、

Workerだけ。

Playbookは、

Playbookだけ。

役割を混在させてはいけません。

---

# Composition

Componentは、

組み合わせて利用します。

```
Knowledge

+

Worker

+

Playbook

↓

Organization
```

AIBOSでは、

Componentを小さく保ち、

必要に応じて組み合わせることを推奨します。

---

# Version Control

すべてのComponentは、

Gitなどのバージョン管理システムで管理することを推奨します。

変更履歴は、

Organizationの進化そのものです。

---

# Summary

Componentは、

AIBOSを構成する基本単位です。

すべてのComponentは、

この仕様に従うことで、

相互運用性、

再利用性、

保守性を高めます。