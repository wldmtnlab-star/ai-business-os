# Create Your First Knowledge

Knowledgeは、AIBOSの中核となるコンポーネントです。

Knowledgeとは、

**組織が持つ知識をAIが理解できる形で管理する仕組み**

です。

人が何年もかけて蓄積した知識を、

AIと共有できる資産へ変えていきます。

---

# What is Knowledge?

Knowledgeには、

例えば以下のような情報を保存します。

- ブランド
- 商品
- サービス
- 会社概要
- ミッション
- デザインルール
- 営業資料
- FAQ
- 技術資料
- 用語集

Knowledgeは、

単なるメモではありません。

AIが仕事をするための

**組織の知識ベース**

です。

---

# Create Your First Knowledge

```
knowledge/

brand.md
```

---

# Example

```markdown
# Brand

Name

NagiPrintStudio

Mission

Create peaceful Japanese-inspired digital art.

Target

Global Etsy customers.

Style

Minimal

Zen

Nature

Warm

Modern Japanese
```

これだけでも、

AIはブランドを理解できます。

---

# Multiple Knowledge Files

Knowledgeは、

小さく分割します。

例えば、

```
knowledge/

brand.md

products.md

services.md

company.md

vision.md

faq.md

style-guide.md

seo.md
```

このような構成になります。

---

# Why Split?

Knowledgeを分割すると、

Runtimeは

必要な情報だけを読み込めます。

例えば、

Designer Workerなら、

```
brand.md

style-guide.md
```

だけ読めば十分です。

一方、

Sales Workerなら、

```
company.md

services.md

faq.md
```

を利用します。

つまり、

Knowledgeは

Workerごとに最適化できます。

---

# Knowledge is Reusable

Knowledgeは、

複数のWorkerから利用できます。

```
Brand

↓

Designer

Writer

SEO

Reviewer
```

同じブランド情報を、

全員が共有できます。

---

# Best Practices

Knowledgeを書くときは、

次のことを意識します。

✅ 一つのテーマにつき一つのファイル

✅ 更新しやすい

✅ 人にも読みやすい

✅ AIにも理解しやすい

Knowledgeは、

組織の「唯一の真実（Single Source of Truth）」になることを目指します。

---

# Example Structure

```
knowledge/

brand.md

company.md

products.md

services.md

customers.md

vision.md

style-guide.md

marketing.md

seo.md

faq.md
```

---

# Human First

Knowledgeは、

AIのためだけではありません。

人も読み、

人も更新し、

人も改善します。

その結果、

AIも成長します。

Knowledgeは、

組織全体で育てていく資産です。

---

# Summary

Knowledgeは、

組織の知識を管理するコンポーネントです。

Worker

Playbook

Runtime

すべてがKnowledgeを利用します。

AIBOSでは、

Knowledgeこそが最も重要な資産です。

---

# Next Step

次は、

Playbookを作成します。

Knowledgeが

「何を知っているか」

なら、

Playbookは

「どう仕事を進めるか」

を定義します。

→ 08_CREATE_YOUR_FIRST_PLAYBOOK.md