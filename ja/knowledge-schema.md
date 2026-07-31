# Knowledge Schema

Knowledgeは、Organizationが持つ知識を定義するコンポーネントです。

AIBOSでは、Knowledgeを人とAIの両方が理解しやすいMarkdown形式で管理します。

---

# Philosophy

Knowledgeは、

- 人が読める
- AIが理解できる
- Gitで管理できる
- 再利用できる

ことを目的としています。

Knowledgeは、Organizationの「Single Source of Truth」です。

---

# File Format

KnowledgeはMarkdownファイルとして保存します。

```
knowledge/

brand.md
```

```
knowledge/

products.md
```

```
knowledge/

faq.md
```

---

# Front Matter

必要に応じてYAML Front Matterを利用できます。

```markdown
---
title: Brand
version: 1.0
owner: Marketing Team
updated: 2026-07-31
tags:
  - brand
  - marketing
---

# Brand

...
```

Front Matterは任意ですが、利用を推奨します。

---

# Recommended Structure

Knowledgeには決まった形式はありません。

ただし、以下のような構成を推奨します。

```markdown
# Title

## Overview

概要

## Details

詳細

## Rules

ルール

## Examples

例

## References

参考情報
```

---

# Naming

ファイル名は

```
kebab-case
```

を推奨します。

例

```
style-guide.md

brand-guidelines.md

customer-personas.md
```

---

# Scope

Knowledgeは、

1ファイル1テーマを推奨します。

良い例

```
brand.md

products.md

seo.md
```

悪い例

```
all-information.md
```

---

# Writing Style

Knowledgeは、

AIへの命令ではありません。

組織の知識を書きます。

例えば、

❌

```
Always create beautiful images.
```

ではなく、

✅

```
The brand emphasizes calm, minimalist Japanese aesthetics inspired by nature.
```

事実・方針・ルールを書くことを推奨します。

---

# Relationships

Knowledgeは、

複数のWorkerから共有されます。

```
Brand

├── Designer

├── Writer

├── SEO

└── Reviewer
```

---

# Versioning

KnowledgeはGitで管理します。

変更履歴は、

Organizationの成長の記録になります。

---

# Best Practices

- 一つのテーマにつき一つのファイル
- Markdownで記述する
- 命令ではなく知識を書く
- 長すぎる場合は分割する
- Gitで変更履歴を管理する

---

# Anti-Patterns

避けるべき例

❌ 1万行の巨大ファイル

❌ Worker向けの指示を書く

❌ Playbookを書く

❌ 業務フローを書く

Knowledgeは、

知識だけを保持します。

---

# Example

```
knowledge/

brand.md

products.md

style-guide.md

faq.md
```

---

# Summary

Knowledgeは、

Organizationの知識を保持するための標準フォーマットです。

Knowledgeは、

Workerでも、

Playbookでもありません。

Organization全体で共有される知識資産です。