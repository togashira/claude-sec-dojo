# Claude経営 (ClaudeManagement)

**Claudeを使って経営・マネジメントをするための、初心者向けオープンソースプロジェクト。**
世界中の経営者・マネージャー・個人事業主が、Claude(Anthropic社のAIモデル)を日々の経営判断や業務に活用できるようにするための、ガイド・プロンプトテンプレート・実動くツールをまとめています。

[English version here](README.en.md)

## これは何か

経営者やマネージャーは、意思決定・レポート作成・会議の要約・戦略レビューなど、言葉を扱う仕事に多くの時間を使っています。Claudeはこうした仕事の「下書き・整理・たたき台作り」を強力に支援できますが、多くの人は「どう使えばいいかわからない」「プロンプトの書き方がわからない」という壁にぶつかります。

このリポジトリは、**プログラミング未経験でも使える**ことを前提に、以下を提供します。

- 経営でClaudeを使うための**ガイド** ([docs/](docs/ja/))
- そのままコピーして使える**プロンプトテンプレート** ([templates/](templates/ja/))
- 実際に動く**簡単なツール**(週報・レポート自動生成など) ([tools/](tools/))

## クイックスタート

1. [docs/ja/getting-started.md](docs/ja/getting-started.md) を読む(Claudeとは何か、何から始めるか)
2. [templates/ja/](templates/ja/) からよく使うプロンプトをコピーして、[claude.ai](https://claude.ai) や Claude Code に貼り付けて使う
3. もう少し自動化したくなったら [tools/weekly-report-agent/](tools/weekly-report-agent/) のサンプルを動かしてみる

## リポジトリ構成

```
docs/        使い方ガイド・ユースケース集 (ja/ と en/)
templates/   コピペで使えるプロンプトテンプレート (ja/ と en/)
tools/       実際に動く小さなツール・エージェントのサンプル
```

## 対象読者

- 初めてAIを経営に取り入れようとしている経営者・マネージャー
- 社内でClaude活用を広めたい情報システム担当者
- プログラミング未経験〜初心者のエンジニア

## コントリビュート

改善提案・新しいプロンプト・ユースケースの追加は歓迎します。[CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## ライセンス

[MIT License](LICENSE)
