# Example: NagiPrintStudio

このドキュメントでは、AIBOSを実際のビジネスへ適用した例として、

**NagiPrintStudio**

を紹介します。

NagiPrintStudioは、和をテーマにしたデジタルアートを販売するEtsyショップです。

AIBOSでは、このショップ運営をAIと協働するワークフローとして設計しています。

---

# Goal

目的は、

商品制作を完全自動化することではありません。

人が世界観や方向性を決め、

AIが制作・文章・SEOなどを支援することです。

```
Human
    ↓
Direction

AI
    ↓
Execution
```

---

# Organization

NagiPrintStudioでは、

以下のような組織を設計しています。

```
Knowledge

↓

Workers

↓

Playbooks

↓

Runtime

↓

LLM
```

---

# Knowledge

Knowledgeには、

ショップに関する情報を保存します。

例えば、

```
Brand

Products

Art Style

Target Audience

SEO Rules

Etsy Policies

Color Palette

Prompt Library
```

などです。

AIは、

これらを読んでブランドを理解します。

---

# Workers

NagiPrintStudioでは、

複数のWorkerが協力します。

```
Designer

Writer

SEO Specialist

Reviewer
```

例えば、

Designer Workerは、

画像生成プロンプトを作ります。

Writer Workerは、

商品説明を書きます。

SEO Workerは、

タグを考えます。

Reviewer Workerは、

品質を確認します。

---

# Playbooks

Playbookには、

商品制作フローを書きます。

```
Generate Product

↓

Create Concept

↓

Generate Prompt

↓

Create Image

↓

Write Title

↓

Write Description

↓

Generate Tags

↓

Review

↓

Publish
```

AIは、

このPlaybookに沿って仕事を進めます。

---

# Runtime

Runtimeは、

必要な情報を集めます。

```
Knowledge

+

Designer Worker

+

Etsy Product Playbook

↓

GPT

↓

Result
```

Runtimeが、

どのKnowledgeを読むか、

どのWorkerを使うか、

どのPlaybookを実行するか、

を管理します。

---

# Result

最終的に、

以下の成果物が完成します。

```
Product Concept

Image Prompt

Product Image

Title

Description

Tags

SEO Keywords
```

これらは、

ブランドの世界観を維持したまま生成されます。

---

# Benefits

AIBOSを導入することで、

- ブランドの一貫性を維持できる
- 作業品質を標準化できる
- 制作時間を短縮できる
- 新しいWorkerを追加できる
- Playbookを改善し続けられる

といったメリットがあります。

---

# Future

将来的には、

Runtimeから、

```
aibos run nagi product
```

のようなコマンドを実行するだけで、

商品制作全体を支援できるようになることを目指しています。

---

# Human-Led.

NagiPrintStudioでは、

人が、

- ブランドを育てる
- 世界観を決める
- 商品を選ぶ

AIが、

- アイデアを広げる
- 制作を支援する
- 品質を高める

という役割分担を採用しています。

AIBOSは、

AIに仕事を任せるためではなく、

**人の創造性を増幅するため**に設計されています。

---

# Summary

NagiPrintStudioは、

AIBOSを実際のビジネスへ適用した最初のケーススタディです。

ここで得られた知見は、

Web制作、

マーケティング、

営業、

ソフトウェア開発など、

さまざまな分野へ応用できると考えています。