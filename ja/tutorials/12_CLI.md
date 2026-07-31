# CLI

AIBOS CLIは、

Organizationを操作するためのコマンドラインツールです。

CLIを使うことで、

Organizationの作成、

Workerの追加、

Playbookの実行などを簡単に行えます。

---

# Philosophy

CLIは、

AIBOSを扱うための共通インターフェースです。

できるだけ、

覚えやすく、

予測しやすいコマンドを目指しています。

---

# Initialize

新しいOrganizationを作成します。

```bash
aibos init
```

実行すると、

```
my-organization/

knowledge/

workers/

playbooks/

README.md
```

など、

基本構成が生成されます。

---

# Run a Playbook

Playbookを実行します。

```bash
aibos run create-product
```

Runtimeが、

Organizationを読み込み、

必要なWorkerを実行します。

---

# List Workers

登録済みWorkerを表示します。

```bash
aibos worker list
```

例

```
Designer

Writer

SEO

Reviewer
```

---

# Create Worker

新しいWorkerを作成します。

```bash
aibos worker create
```

または、

```bash
aibos worker create designer
```

テンプレートが生成されます。

---

# List Knowledge

Knowledge一覧を表示します。

```bash
aibos knowledge list
```

---

# Create Knowledge

Knowledgeを追加します。

```bash
aibos knowledge create brand
```

生成されるファイル

```
knowledge/

brand.md
```

---

# List Playbooks

Playbook一覧を表示します。

```bash
aibos playbook list
```

---

# Create Playbook

```bash
aibos playbook create create-product
```

テンプレートを生成します。

---

# Validate

Organization全体をチェックします。

```bash
aibos validate
```

例

```
✓ Organization

✓ Workers

✓ Knowledge

✓ Playbooks
```

問題があれば、

詳細が表示されます。

---

# Doctor

環境を診断します。

```bash
aibos doctor
```

例

```
Runtime

LLM

Configuration

API Keys

Dependencies
```

---

# Configuration

設定を表示します。

```bash
aibos config
```

---

# Example

商品制作を実行します。

```bash
aibos run create-product
```

Runtimeが、

```
Brand

↓

Designer

↓

Writer

↓

SEO

↓

Reviewer
```

を実行し、

成果物を生成します。

---

# Future Commands

将来的には、

以下のコマンドを予定しています。

```bash
aibos login

aibos publish

aibos pull

aibos update

aibos registry search

aibos team list

aibos cloud deploy

aibos monitor

aibos logs
```

---

# Design Principles

CLIは、

Runtimeの薄いラッパーです。

CLI自身は、

ビジネスロジックを持ちません。

Organizationの操作だけを担当します。

---

# Summary

CLIは、

AIBOSを操作するための入口です。

Organizationを作り、

Playbookを実行し、

Runtimeを呼び出すための、

もっとも基本的なツールになります。

---

# Next Step

ここまでで、

AIBOSの全体像を理解しました。

次は、

各コンポーネントの詳細仕様をまとめた

Referenceへ進みます。

→ Reference Documentation