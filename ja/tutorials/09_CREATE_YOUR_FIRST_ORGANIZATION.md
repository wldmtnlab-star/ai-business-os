# Create Your First Organization

ここまでで、AIBOSの3つの主要コンポーネントを作成しました。

- Knowledge
- Workers
- Playbooks

次は、それらを一つにまとめた **Organization** を作成します。

Organizationは、AIBOSにおける最上位の概念です。

---

# What is an Organization?

現実の会社には、

- ブランド
- 社員
- 業務フロー

があります。

AIBOSでは、それぞれ次のように対応します。

| Real Organization | AIBOS |
|-------------------|--------|
| Company Knowledge | Knowledge |
| Employees | Workers |
| Business Processes | Playbooks |

これらをまとめたものが **Organization** です。

---

# Folder Structure

最もシンプルなOrganizationは次のようになります。

```text
my-organization/

├── knowledge/
│   ├── brand.md
│   ├── company.md
│   └── products.md
│
├── workers/
│   ├── designer.md
│   ├── writer.md
│   └── reviewer.md
│
├── playbooks/
│   └── create-product.md
│
└── README.md
```

これだけで一つのOrganizationです。

---

# Organization = Business

Organizationは、

単なるフォルダではありません。

**一つの事業そのもの**を表現します。

例えば、

```
NagiPrintStudio
```

```
Marketing Agency
```

```
Software Company
```

```
Restaurant
```

```
Consulting Firm
```

どれもOrganizationとして表現できます。

---

# How Components Work Together

商品制作を例にすると、

```text
Brand Knowledge
        │
        ▼
Designer Worker
        │
        ▼
Writer Worker
        │
        ▼
Reviewer Worker
        │
        ▼
Completed Product
```

Playbookは、

この流れを定義しています。

Runtimeは、

このPlaybookを実行します。

---

# Reusability

Organizationの大きな特徴は、

コンポーネントを自由に組み合わせられることです。

例えば、

```
Designer Worker
```

は、

複数のPlaybookで利用できます。

```
Create Product

Create Blog

Create LP

Create Banner
```

Knowledgeも同様です。

```
brand.md
```

は、

Designer、

Writer、

SEO Workerなど、

様々なWorkerが共有できます。

---

# Version Control

Organization全体は、

Gitで管理できます。

```
Git Repository

↓

Knowledge

Workers

Playbooks
```

変更履歴を残し、

チーム全員で改善を続けられます。

これは、

ソフトウェア開発でいう

**Infrastructure as Code**

と同じ考え方です。

AIBOSでは、

これを

> **Organizations as Code**

と呼びます。

---

# Organizations as Code

Organizationは、

ドキュメントではありません。

設計図でもありません。

Organizationそのものが、

実行可能な資産です。

```
Design

↓

Version

↓

Share

↓

Improve

↓

Run
```

これが、

Organizations as Codeの考え方です。

---

# Human-Led

Organizationの目的は、

AIへ仕事を丸投げすることではありません。

人が方向性を決め、

AIが実行を支援し、

人が改善を続けます。

Organizationは、

人とAIが協働するための基盤です。

---

# Summary

Organizationは、

Knowledge

Workers

Playbooks

を一つにまとめた最上位コンポーネントです。

AIBOSでは、

Organizationを中心に設計することで、

あらゆる業種・チーム・プロジェクトを共通の構造で表現できます。

---

# Next Step

次は、

複数のWorkerが協力して仕事を進める

**AI Team**

を作成します。

→ 10_BUILD_YOUR_FIRST_AI_TEAM.md