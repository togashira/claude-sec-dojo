# weekly-report-agent

箇条書きの活動メモから週次レポートを自動生成する、最小限のサンプルツールです。
A minimal sample tool that turns bullet-point activity notes into a weekly report automatically.

## 日本語

### これは何か

`templates/ja/weekly-report-prompt.md` のプロンプトを、コマンド1つで実行できるようにしたサンプルです。箇条書きのメモファイルを渡すと、Claude APIを呼び出して週次報告書を生成し、標準出力(または指定したファイル)に出力します。

プログラミング未経験の方は、まず [docs/ja/getting-started.md](../../docs/ja/getting-started.md) でチャット版の使い方を確認することをおすすめします。このツールは「もう少し自動化したい」という段階向けです。

### セットアップ

```bash
cd tools/weekly-report-agent
pip install -r requirements.txt
cp .env.example .env
# .env を開き、ANTHROPIC_API_KEY にご自身のAPIキーを設定する
```

APIキーは [Anthropic Console](https://console.anthropic.com) で取得できます。

### 使い方

```bash
# notes.txt に箇条書きの今週のメモを書いておく
python agent.py notes.txt

# 出力をファイルに保存する場合
python agent.py notes.txt --output report.md

# トーンを指定する場合
python agent.py notes.txt --tone "です・ます調、簡潔に"
```

### 注意事項

- このツールはAPI呼び出しのたびに料金が発生します。料金は[Anthropic公式サイト](https://www.anthropic.com)でご確認ください
- 生成された内容は必ず人間が確認してから使用してください
- 機密情報を含むメモを扱う場合は、社内のセキュリティ方針に従ってください

## English

### What this is

A runnable version of the prompt in `templates/en/weekly-report-prompt.md`. Give it a file of bullet-point notes and it calls the Claude API to generate a weekly report, printed to stdout (or saved to a file).

If you have no programming background, start with the chat-based workflow in [docs/en/getting-started.md](../../docs/en/getting-started.md) first. This tool is for when you're ready to automate a bit further.

### Setup

```bash
cd tools/weekly-report-agent
pip install -r requirements.txt
cp .env.example .env
# Open .env and set ANTHROPIC_API_KEY to your own API key
```

Get an API key from the [Anthropic Console](https://console.anthropic.com).

### Usage

```bash
# Put this week's bullet-point notes in notes.txt
python agent.py notes.txt

# Save output to a file instead of printing it
python agent.py notes.txt --output report.md

# Specify a tone
python agent.py notes.txt --tone "concise, professional"
```

### Notes

- Every run of this tool calls the API and incurs cost — see [Anthropic's pricing page](https://www.anthropic.com) for current rates
- Always have a human review the generated report before using it
- Follow your company's security policy when handling notes that contain sensitive information
