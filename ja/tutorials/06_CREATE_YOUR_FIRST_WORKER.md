# Create Your First Worker

このガイドでは、AIBOSで最初のWorkerを作成します。

Workerとは、

**AIに役割（Role）を与える設計図**です。

Workerは人格ではありません。

組織の中で担当する役割を定義します。

---

# What is a Worker?

例えば会社には、

- Designer
- Sales
- Engineer
- Writer

など、

様々な役割があります。

AIBOSでも同じです。

AIへ

「あなたはデザイナーです。」

ではなく、

**デザイナーという役割を定義する**

という考え方になります。

---

# Create a Worker

workers/

```
designer.md
```

---

# Basic Template

```yaml
name: Designer

version: 1.0

description:
Creates visual designs while maintaining brand consistency.

goal:
Create high-quality designs.

responsibilities:

- Design
- Branding
- Creativity
- Visual Consistency
```

これだけでも、

Designer Workerになります。

---

# Add Skills

次に、

得意分野を書きます。

```yaml
skills:

- Graphic Design

- Typography

- Color Theory

- Layout

- Prompt Engineering
```

Workerは、

専門知識を持つことができます。

---

# Add Constraints

AIには、

守るべきルールがあります。

```yaml
constraints:

- Follow Brand Guidelines

- Never copy copyrighted works

- Maintain consistent visual identity
```

これにより、

品質を一定に保てます。

---

# Connect Knowledge

WorkerはKnowledgeを利用します。

```yaml
knowledge:

- brand.md

- products.md

- style-guide.md
```

Runtimeは、

必要なKnowledgeだけを読み込みます。

---

# Connect Playbooks

次に、

Playbookを接続します。

```yaml
playbooks:

- create-product.md

- create-lp.md

- social-post.md
```

同じDesigner Workerでも、

Playbookを変えるだけで、

仕事が変わります。

---

# Worker Independence

Workerは、

Playbookから独立しています。

例えば、

```
Designer

↓

LP

```

にも使えます。

```
Designer

↓

Etsy

```

にも使えます。

```
Designer

↓

Instagram
```

にも使えます。

だから、

再利用できます。

---

# Example

NagiPrintStudioでは、

```
Designer Worker

↓

Brand Knowledge

↓

Etsy Product Playbook

↓

Runtime

↓

GPT
```

という流れになります。

---

# Best Practices

Workerは、

役割だけを書きます。

仕事の流れは書きません。

仕事の流れは、

Playbookへ書きます。

知識は、

Knowledgeへ書きます。

役割だけを担当する。

それが、

Workerです。

---

# Summary

Workerは、

AIへ役割を与えるコンポーネントです。

Knowledge

+

Worker

+

Playbook

を組み合わせることで、

様々な業務へ対応できます。

---

# Next Step

次は、

Playbookを作成します。

Playbookを書くことで、

Workerは実際に仕事を進められるようになります。

→ 07_CREATE_YOUR_FIRST_PLAYBOOK.md