# Architecture

AIBOSは、組織をAIと協働できる形へ設計するためのモジュラーアーキテクチャを採用しています。

各コンポーネントは独立しており、必要に応じて自由に組み合わせることができます。

```
                AIBOS

                   │

    ┌──────────────┼──────────────┐

Knowledge      Workers      Playbooks

    └──────────────┼──────────────┘
                   │
               Runtime
                   │
      GPT / Claude / Gemini / ...
```

---

# Repository Structure

AIBOSでは、標準的なリポジトリ構成を採用します。

```
ai-business-os/

├── knowledge/
│
├── workers/
│
├── playbooks/
│
├── runtime/
│
├── examples/
│
├── docs/
│
├── ja/
│
└── README.md
```

各ディレクトリには明確な責務があります。

---

# knowledge/

Knowledgeは組織の知識を管理します。

例：

```
knowledge/

company.md

brand.md

products.md

design-guidelines.md

customers.md

faq.md
```

Runtimeは必要なKnowledgeだけを読み込みます。

---

# workers/

WorkersはAIの役割を定義します。

```
workers/

designer.md

writer.md

engineer.md

sales.md

reviewer.md
```

Workerには、

- Role
- Goal
- Responsibilities
- Constraints
- Skills

などを記述します。

---

# playbooks/

Playbooksは業務プロセスを定義します。

例：

```
playbooks/

create-lp.md

etsy-product.md

code-review.md

sales-proposal.md
```

Playbookは、

AIが仕事を進めるための標準手順です。

---

# runtime/

Runtimeは、

Knowledge

Workers

Playbooks

を読み込み、

LLMへ渡します。

```
Knowledge
      │
Workers
      │
Playbooks
      │
Runtime
      │
LLM
```

Runtimeは、

どのLLMでも動作できることを目標としています。

例えば、

- OpenAI
- Anthropic
- Google
- OpenRouter
- Local LLM

など。

---

# examples/

実際の利用例を配置します。

```
examples/

NagiPrintStudio/

Marketing/

SoftwareDevelopment/

CustomerSupport/
```

AIBOSは、

実例から学べることを重視しています。

---

# docs/

英語版ドキュメントです。

```
docs/

Getting Started

Architecture

Runtime

Workers

Playbooks
```

OSSとして世界中の開発者が利用できるよう整備します。

---

# ja/

日本語ドキュメントです。

```
ja/

README

01_WHAT_IS_AI_BUSINESS_OS

02_CORE_CONCEPTS

03_ARCHITECTURE

...
```

日本語利用者向けの公式ガイドです。

---

# Design Principles

AIBOSは、以下の設計思想を大切にしています。

## Modular

すべて独立している。

---

## Reusable

一度作れば、

何度でも利用できる。

---

## Composable

自由に組み合わせられる。

---

## Portable

特定のAIへ依存しない。

---

## Human-Led

最終的な意思決定は人が行う。

---

# Future Vision

現在のAIBOSは、

Knowledge

Workers

Playbooks

Runtime

を中心に構成されています。

将来的には、

```
Portal

Cloud

Marketplace

Organizations

Teams

Monitoring

Analytics
```

などのコンポーネントも追加予定です。

---

# Summary

AIBOSは、

知識、

役割、

業務、

実行環境

を分離することで、

柔軟で拡張性の高いAIネイティブ組織を実現します。

```
Knowledge

+

Workers

+

Playbooks

+

Runtime

=

AI Business OS
```