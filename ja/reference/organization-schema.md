# Organization Schema

Organizationは、AIBOSにおける最上位のコンポーネントです。

Knowledge、

Workers、

Playbooks

を一つにまとめ、

実行可能な組織を定義します。

Runtimeは、

Organizationを読み込んで実行します。

---

# Conformance

このドキュメントでは、

**MUST**
**SHOULD**
**MAY**

を RFC 2119 に従って使用します。

---

# Purpose

Organizationは、

現実の会社、

チーム、

プロジェクト、

ブランドなどを表現します。

例えば、

- NagiPrintStudio
- Marketing Agency
- Software Company
- Sales Team

など、

業種を問いません。

---

# Minimum Structure

Organizationは、

最低限、

以下のディレクトリを持つ必要があります。

```text
my-organization/

├── knowledge/
│
├── workers/
│
├── playbooks/
│
└── README.md
```

---

# Recommended Structure

より大きなOrganizationでは、

以下を推奨します。

```text
my-organization/

├── knowledge/
│
├── workers/
│
├── playbooks/
│
├── assets/
│
├── prompts/
│
├── tests/
│
├── docs/
│
└── README.md
```

---

# Metadata

Organizationは、

YAML Front Matterまたは

organization.yamlを利用できます。

例

```yaml
name: NagiPrintStudio

version: 1.0.0

description:
Japanese-inspired digital art business.

owner:
MTN Syndicate

license:
MIT
```

---

# Responsibilities

Organizationは、

以下を管理します。

- Knowledge
- Workers
- Playbooks
- Assets
- Configuration

Organization自身は、

業務ロジックを持ちません。

---

# Relationships

Organizationは、

すべてのComponentを統合します。

```text
Organization
│
├── Knowledge
│
├── Workers
│
├── Playbooks
│
└── Runtime
```

Runtimeは、

Organizationを単位として実行します。

---

# Multiple Organizations

一つのRepositoryで、

複数Organizationを管理できます。

例

```text
organizations/

├── nagi-print-studio/

├── web-agency/

└── marketing-lab/
```

Runtimeは、

対象Organizationを選択して実行します。

---

# Dependencies

Organizationは、

外部Componentを参照できます。

例えば、

```
Shared Brand

Shared Workers

Shared Playbooks
```

将来的には、

Registryから取得できるようになります。

---

# Versioning

Organizationは、

Semantic Versioningを推奨します。

```
1.0.0

1.1.0

2.0.0
```

---

# Distribution

Organizationは、

Git Repositoryとして配布できます。

例

```
github.com/example/nagi-print-studio
```

将来的には、

AIBOS Registryからも配布できます。

---

# Validation

Runtimeは、

Organization実行前に検証を行います。

例えば、

- 必須フォルダが存在する
- Playbookが存在する
- Worker参照が解決できる
- Knowledge参照が解決できる

問題があれば、

実行を停止します。

---

# Best Practices

- Organizationは小さく始める
- Componentを再利用する
- Gitで管理する
- READMEを書く
- バージョンを付ける

---

# Anti-Patterns

避けるべき例

❌ すべてを1ファイルへ書く

❌ WorkerへKnowledgeを書く

❌ Playbookへブランドを書く

❌ Runtime設定を書く

Organizationは、

Componentを整理する責務だけを持ちます。

---

# Summary

Organizationは、

AIBOSにおける実行単位です。

Knowledge、

Workers、

Playbooksをまとめ、

Runtimeへ提供します。

Organizationは、

現実の組織をデジタルで表現する最上位コンポーネントです。