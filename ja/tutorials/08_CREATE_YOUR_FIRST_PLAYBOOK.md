# Create Your First Playbook

Playbookは、

**仕事の進め方（Workflow）**を定義するコンポーネントです。

Knowledgeが

「何を知っているか」

なら、

Playbookは

**「どのように仕事を進めるか」**

を定義します。

---

# What is a Playbook?

組織では、

どんな仕事にも手順があります。

例えば、

商品制作なら、

```
企画

↓

デザイン

↓

レビュー

↓

公開
```

営業なら、

```
ヒアリング

↓

提案

↓

見積

↓

契約

↓

フォロー
```

Playbookは、

こうした業務フローをAIへ伝えるための仕組みです。

---

# Create Your First Playbook

```
playbooks/

create-product.md
```

---

# Example

```markdown
# Create Product

1.

Read Brand Knowledge

2.

Generate Product Concept

3.

Create Image Prompt

4.

Generate Product Image

5.

Write Title

6.

Write Description

7.

Generate Tags

8.

Review

9.

Publish
```

これだけでも、

AIは仕事の流れを理解できます。

---

# Playbook is Workflow

Playbookは、

**チェックリスト**

ではありません。

**業務フロー**

です。

例えば、

```
Research

↓

Planning

↓

Design

↓

Review

↓

Delivery
```

AIは、

この順番に沿って仕事を進めます。

---

# Connect Workers

Playbookは、

複数のWorkerを利用できます。

```
Designer

↓

Writer

↓

SEO

↓

Reviewer
```

つまり、

一人のAIではなく、

チームとして仕事を進められます。

---

# Connect Knowledge

Playbookは、

必要なKnowledgeも指定します。

例えば、

```
Brand

Product

SEO Rules

Style Guide
```

Runtimeは、

必要なKnowledgeだけを読み込みます。

---

# Example Flow

```
Knowledge

↓

Designer Worker

↓

Writer Worker

↓

SEO Worker

↓

Reviewer Worker

↓

Completed Product
```

これが、

一つのPlaybookになります。

---

# Best Practices

Playbookを書くときは、

次のことを意識します。

✅ 手順を明確にする

✅ Workerを分離する

✅ Knowledgeを使い回す

✅ 一つの目的に集中する

Playbookは、

シンプルなほど再利用しやすくなります。

---

# Multiple Playbooks

例えば、

```
playbooks/

create-product.md

create-lp.md

create-blog.md

code-review.md

sales-proposal.md

customer-support.md
```

など。

業務ごとにPlaybookを分けます。

---

# Human Checkpoint

AIBOSでは、

重要なポイントで

人がレビューできます。

例えば、

```
Research

↓

Design

↓

👤 Human Review

↓

Revision

↓

Publish
```

AIだけで進める必要はありません。

人とAIが協働することが、

AIBOSの基本思想です。

---

# Summary

Playbookは、

業務プロセスを定義するコンポーネントです。

Knowledge

+

Workers

+

Playbooks

これらを組み合わせることで、

AIは組織のルールに従って仕事を進められるようになります。

---

# Next Step

Knowledge

Workers

Playbooks

この3つが揃いました。

次は、

これらを一つにまとめた

**Organization**

を作成します。

→ 09_CREATE_YOUR_FIRST_ORGANIZATION.md