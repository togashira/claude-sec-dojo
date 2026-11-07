# Contributing / コントリビュートガイド

## 日本語

このプロジェクトへの貢献を歓迎します。以下のような貢献を想定しています。

- 新しいプロンプトテンプレートの追加(`templates/ja/` と `templates/en/` の両方に対応する内容を追加してください)
- ガイド・ユースケースの追加・改善(`docs/ja/` と `docs/en/`)
- 実際に動くツールの追加・改善(`tools/`)
- 誤字脱字・翻訳の修正

### 進め方

1. 本リポジトリをフォークする
2. 変更用のブランチを作成する(例: `add-okr-template`)
3. 変更を行う。日本語版と英語版の両方を用意するのが望ましいですが、片方のみでも歓迎します(その場合、翻訳が不足している旨をPRに明記してください)
4. Pull Requestを作成する

### プロンプトテンプレートを追加する場合

- `templates/ja/` に日本語版、`templates/en/` に英語版のファイルを、同じファイル名で追加してください
- どんな場面で使うか、想定する入力・出力を簡単に書いてください
- 機密情報(実際の社名・個人名・財務データなど)をサンプルに含めないでください

## English

Contributions are welcome, including:

- New prompt templates (please add matching content under both `templates/ja/` and `templates/en/`)
- New or improved guides and use cases (`docs/ja/` and `docs/en/`)
- New or improved working tools (`tools/`)
- Typo fixes and translation improvements

### Workflow

1. Fork this repository
2. Create a branch for your change (e.g. `add-okr-template`)
3. Make your change. Providing both Japanese and English versions is preferred, but a single-language contribution is also welcome — note in the PR that translation is pending
4. Open a Pull Request

### Adding a prompt template

- Add a Japanese version under `templates/ja/` and an English version under `templates/en/` with the same filename
- Briefly describe the intended use case and expected input/output
- Do not include real company names, personal data, or financial figures in examples
