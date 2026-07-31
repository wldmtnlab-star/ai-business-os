# Quick Start

このガイドでは、AI Business OS（AIBOS）の基本的な考え方を短時間で体験します。

AIBOSは現在も開発中ですが、Knowledge・Workers・Playbooksを使った設計思想は、今すぐ試すことができます。

---

# Step 1. リポジトリを取得する

```bash
git clone https://github.com/<your-account>/ai-business-os.git

cd ai-business-os
```

---

# Step 2. リポジトリ構成を確認する

```
ai-business-os/

knowledge/

workers/

playbooks/

examples/

runtime/

docs/

ja/
```

AIBOSは、

- Knowledge
- Workers
- Playbooks

を中心に構成されています。

---

# Step 3. Knowledgeを作る

例として、

ブランド情報を作成します。

```
knowledge/

brand.md
```

```markdown
# Brand

Name

NagiPrintStudio

Mission

Peaceful Japanese-inspired digital art.

Target

Global Etsy Customers

Style

Minimal
Japanese
Zen
```

Knowledgeは、

AIへ渡す組織の知識です。

---

# Step 4. Workerを作る

```
workers/

designer.md
```

```markdown
# Worker

Designer

Goal

Create beautiful products.

Responsibilities

Design

Brand consistency

Creativity
```

Workerは、

AIの役割を定義します。

---

# Step 5. Playbookを作る

```
playbooks/

etsy-product.md
```

```markdown
# Etsy Product Workflow

1.

Read Brand

2.

Generate Concept

3.

Create Prompt

4.

Write Title

5.

Write Description

6.

Generate Tags
```

Playbookは、

仕事の進め方を定義します。

---

# Step 6. これらをAIへ渡す

現在は、

Knowledge

+

Worker

+

Playbook

を読み込み、

ChatGPTやClaudeなどへ入力することでAIBOSを体験できます。

```
Knowledge

+

Worker

+

Playbook

↓

ChatGPT
```

---

# Runtime（開発中）

将来的には、

以下のようなコマンドで実行できるようになる予定です。

```bash
aibos run designer
```

または、

```bash
aibos run etsy-product
```

Runtimeが自動的に

- Knowledge
- Worker
- Playbook

を読み込み、

最適なLLMへ渡して実行します。

---

# Example

例えば、

```
Knowledge

↓

NagiPrintStudio

↓

Designer Worker

↓

Etsy Product Playbook

↓

Runtime

↓

GPT-5

↓

Product Created
```

という流れになります。

---

# What's Next?

Quick Startが完了したら、

次は実際のプロジェクト例を見てみましょう。

- NagiPrintStudio
- Web Design
- Marketing
- Software Development

実際の利用例を見ることで、

AIBOSの考え方をより深く理解できます。

---

# Congratulations!

これで、

あなたはAIBOSの基本的な考え方を体験しました。

次は、

実際のプロジェクトでKnowledge・Workers・Playbooksを作成し、

AI Native Organizationを設計してみましょう。