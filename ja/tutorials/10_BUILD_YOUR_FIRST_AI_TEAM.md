# Build Your First AI Team

ここまでで、

- Knowledge
- Workers
- Playbooks
- Organization

を作成しました。

次は、

複数のWorkerが協力して仕事を進める

**AI Team**

を構築します。

---

# Why AI Teams?

現実の会社では、

一人ですべての仕事をすることはありません。

例えば、

新しい商品を販売するときには、

```
Designer

↓

Writer

↓

SEO

↓

Reviewer
```

のように、

複数の専門家が協力します。

AIBOSでも同じ考え方を採用します。

---

# One AI vs AI Team

一人のAIに、

「全部やって」

と依頼すると、

役割が混ざり、

品質も安定しません。

```
One AI

↓

Design

Writing

SEO

Review

Publish
```

一方、

AI Teamでは、

役割を分けます。

```
Designer

↓

Writer

↓

SEO

↓

Reviewer
```

それぞれが、

専門家として仕事を担当します。

---

# Example Team

NagiPrintStudioでは、

以下のようなチームを構成しています。

```
Designer

・商品コンセプト

・画像生成プロンプト

↓

Writer

・商品タイトル

・商品説明

↓

SEO Specialist

・タグ

・SEOキーワード

↓

Reviewer

・ブランドチェック

・品質確認
```

---

# Shared Knowledge

全員が、

同じKnowledgeを利用します。

```
Brand

Products

Style Guide

Target Audience
```

これにより、

ブランドの一貫性を維持できます。

---

# Playbook

Playbookは、

チーム全体の仕事を定義します。

```
Research

↓

Design

↓

Writing

↓

SEO

↓

Review

↓

Publish
```

Workerは、

自分の担当だけを実行します。

---

# Human Checkpoints

重要な場面では、

人がレビューします。

```
Research

↓

Designer

↓

👤 Human Approval

↓

Writer

↓

Reviewer

↓

Publish
```

AIBOSは、

完全自動化を目的としていません。

重要な意思決定は、

常に人が行います。

---

# Scaling

AI Teamは、

自由に拡張できます。

例えば、

```
Marketing Team

Designer

Writer

SEO

SNS

Reviewer
```

あるいは、

```
Development Team

Architect

Backend

Frontend

QA

Reviewer
```

業種に応じて、

自由に構成できます。

---

# Reusability

Workerは、

他のチームでも再利用できます。

例えば、

```
Writer
```

は、

Marketing Teamでも、

Sales Teamでも、

Customer Support Teamでも利用できます。

Workerは、

Organization全体の共有資産です。

---

# Team Structure

AIBOSでは、

チームは次のように構成されます。

```
Knowledge

↓

Workers

↓

Playbook

↓

AI Team

↓

Runtime

↓

LLM
```

Runtimeは、

Playbookに従って、

必要なWorkerを順番に実行します。

---

# Summary

AI Teamとは、

役割を持ったWorkerが協力して仕事を進める仕組みです。

AIBOSでは、

一人の万能AIではなく、

複数の専門AIが協働することで、

品質、

再利用性、

保守性を高めています。

---

# Next Step

ここまでで、

AIBOSの基本設計は完成しました。

次は、

RuntimeがどのようにOrganizationを実行するのかを学びます。

→ 11_RUNTIME.md