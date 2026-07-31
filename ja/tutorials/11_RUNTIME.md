# Runtime

Runtimeは、AIBOSの実行エンジンです。

Knowledge、

Workers、

Playbooks、

Organization。

これらは定義であり、

それだけでは何も実行されません。

Runtimeは、

それらを読み込み、

適切な順序で実行し、

AIへ仕事を依頼します。

---

# What is Runtime?

Runtimeとは、

**Organizationを動かすためのエンジン**

です。

```
Organization

↓

Runtime

↓

LLM

↓

Result
```

Runtimeは、

人とAIの橋渡しを行います。

---

# Responsibilities

Runtimeには、

大きく5つの役割があります。

## 1. Load Organization

Organization全体を読み込みます。

```
knowledge/

workers/

playbooks/
```

必要な情報を取得します。

---

## 2. Resolve Dependencies

Playbookを確認し、

必要なWorkerを特定します。

例えば、

```
Designer

Writer

Reviewer
```

が必要なら、

Runtimeが自動で読み込みます。

---

## 3. Load Knowledge

Workerが必要とするKnowledgeだけを取得します。

例えば、

Designerなら、

```
brand.md

style-guide.md
```

Writerなら、

```
products.md

brand.md
```

不要な情報は読み込みません。

---

## 4. Execute Workflow

Playbookの順番に沿って、

Workerを実行します。

```
Research

↓

Design

↓

Writing

↓

Review

↓

Publish
```

各Workerの成果物は、

次のWorkerへ渡されます。

---

## 5. Return Results

最終成果物を返します。

例えば、

```
Image Prompt

Title

Description

Tags
```

あるいは、

```
Proposal

Source Code

Presentation

Article
```

など。

---

# Runtime Flow

Runtime全体の流れは、

次のようになります。

```
Organization

↓

Playbook

↓

Resolve Workers

↓

Load Knowledge

↓

Execute Workers

↓

Collect Results

↓

Output
```

---

# Example

例えば、

商品制作では、

```
aibos run create-product
```

を実行すると、

Runtimeは、

```
Playbook

↓

Designer

↓

Writer

↓

SEO

↓

Reviewer
```

を順番に呼び出します。

最終的に、

```
Product Package
```

を生成します。

---

# Runtime is Stateless

Runtimeは、

知識を保持しません。

Knowledgeは、

Organization側が管理します。

Runtimeは、

毎回、

最新のKnowledgeを読み込みます。

これにより、

Knowledgeを更新するだけで、

AIの振る舞いも改善できます。

---

# Human in the Loop

Runtimeは、

人のレビューも実行できます。

```
Designer

↓

Human Approval

↓

Writer
```

承認が必要な場合は、

Runtimeが停止し、

人の判断を待ちます。

その後、

処理を再開します。

---

# Multi-LLM Support

Runtimeは、

特定のAIモデルに依存しません。

例えば、

```
GPT

Claude

Gemini

Local LLM
```

など、

様々なLLMを利用できます。

Organizationは、

Runtimeを変更することなく、

利用するモデルを切り替えられます。

---

# Future Runtime

将来的には、

Runtimeは以下の機能を提供します。

- CLI
- REST API
- Webhook
- Scheduler
- Event Trigger
- Queue
- Memory
- Monitoring
- Logging

Runtimeは、

AIBOS全体の基盤となる実行環境へ進化します。

---

# Principles

Runtimeは、

できるだけシンプルであることを目指します。

Runtime自身は、

ビジネスロジックを持ちません。

ビジネスロジックは、

Playbookにあります。

知識は、

Knowledgeにあります。

役割は、

Workerにあります。

Runtimeは、

それらを正しく実行することだけに集中します。

---

# Summary

Runtimeは、

Organizationを実行するエンジンです。

Knowledgeを読み、

Workersを呼び出し、

Playbookを実行し、

AIへ仕事を依頼します。

Runtimeは、

AIBOSにおける唯一の実行コンポーネントです。

---

# Next Step

Runtimeの仕組みを理解したら、

実際にAIBOSを操作してみましょう。

→ 12_CLI.md