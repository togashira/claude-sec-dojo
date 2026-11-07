# log-triage-agent

ログファイルを渡すと、Claude APIを使って異常の可能性がある挙動を抽出する最小限のサンプルツールです。
A minimal sample tool that feeds a log file to the Claude API and extracts possibly-anomalous behavior.

## 日本語

### これは何か

`templates/ja/log-analysis-prompt.md` のプロンプトを、コマンド1つで実行できるようにしたサンプルです。ログファイルを渡すと、Claude APIを呼び出して「通常と異なると考えられる挙動」のリストを生成し、標準出力(または指定したファイル)に出力します。

[modules/01-network-log-analysis/](../../modules/01-network-log-analysis/README.md) を終えてから使うことを想定しています。

### セットアップ

```bash
cd tools/log-triage-agent
pip install -r requirements.txt
cp .env.example .env
# .env を開き、ANTHROPIC_API_KEY にご自身のAPIキーを設定する
```

APIキーは [Anthropic Console](https://console.anthropic.com) で取得できます。

### 使い方

```bash
# サンプルのダミーログで試す
python agent.py sample-access.log

# 出力をファイルに保存する場合
python agent.py sample-access.log --output findings.md

# 英語で出力する場合
python agent.py sample-access.log --lang en
```

### 注意事項(必ず読んでください)

- **実際の本番ログを入力しないでください。** 本ツールはダミーデータでの学習・検証を想定しています。実ログには個人情報・機密情報が含まれる可能性があります
- このツールはAPI呼び出しのたびに料金が発生します。料金は[Anthropic公式サイト](https://www.anthropic.com)でご確認ください
- 出力される「異常の可能性」は候補であり、誤検知を含みます。必ず人間が確認してから対応してください
- 本ツールは検知の下書きを支援するものであり、SIEM等の専門ツールの代替ではありません

## English

### What this is

A runnable version of the prompt in `templates/en/log-analysis-prompt.md`. Give it a log file and it calls the Claude API to produce a list of possibly-anomalous behavior, printed to stdout (or saved to a file).

Intended to be used after finishing [modules/01-network-log-analysis/](../../modules/01-network-log-analysis/README.md).

### Setup

```bash
cd tools/log-triage-agent
pip install -r requirements.txt
cp .env.example .env
# Open .env and set ANTHROPIC_API_KEY to your own API key
```

Get an API key from the [Anthropic Console](https://console.anthropic.com).

### Usage

```bash
# Try it with the included dummy log
python agent.py sample-access.log

# Save output to a file instead of printing it
python agent.py sample-access.log --output findings.md

# Output in Japanese
python agent.py sample-access.log --lang ja
```

### Notes (please read)

- **Never feed this tool a real production log.** It's meant for learning and testing with dummy data — real logs can contain personal or sensitive information
- Every run of this tool calls the API and incurs cost — see [Anthropic's pricing page](https://www.anthropic.com) for current rates
- The "possible anomalies" it outputs are candidates and can include false positives — always have a human review them before acting
- This tool assists with a first-pass draft; it is not a substitute for a dedicated SIEM or security tool
