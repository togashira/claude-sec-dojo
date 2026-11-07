# Contributing / コントリビュートガイド

## 日本語

このプロジェクトへの貢献を歓迎します。以下のような貢献を想定しています。

- 新しい学習モジュールの追加(`modules/`、日英バイリンガルで1ファイルにまとめる形式)
- 新しいプロンプトテンプレートの追加(`templates/ja/` と `templates/en/` の両方に対応する内容を追加)
- ガイドの追加・改善(`docs/ja/` と `docs/en/`)
- 実際に動くツールの追加・改善(`tools/`)
- 誤字脱字・翻訳の修正

### 重要な方針

- 本リポジトリは**防御(ディフェンシブ)・検知・学習目的**のコンテンツのみを扱います
- 実在のシステムへの攻撃手法、侵入テストの実践手順、悪用可能なエクスプロイトコードは受け入れません
- ハンズオンの例には、実データ・実在の脆弱性情報ではなく、学習用のダミーデータを使ってください

### 進め方

1. 本リポジトリをフォークする
2. 変更用のブランチを作成する(例: `add-cloud-iam-module`)
3. 変更を行う。モジュールやガイドは日英バイリンガルが望ましいですが、片方のみでも歓迎します(その場合、翻訳が不足している旨をPRに明記してください)
4. Pull Requestを作成する

### 学習モジュールを追加する場合

- `modules/<番号>-<topic>/README.md` に、日本語セクション→英語セクションの順でまとめてください(既存モジュールの構成を参考にしてください)
- 「学ぶこと」「前提知識」「ハンズオン」「Claudeへの質問例」を含めてください
- ハンズオンは、ローカル環境やダミーデータで安全に再現できるものにしてください

## English

Contributions are welcome, including:

- New learning modules (`modules/`, bilingual JA/EN in a single file)
- New prompt templates (please add matching content under both `templates/ja/` and `templates/en/`)
- New or improved guides (`docs/ja/` and `docs/en/`)
- New or improved working tools (`tools/`)
- Typo fixes and translation improvements

### Important policy

- This repository covers **defensive, detection, and learning-oriented content only**
- We do not accept attack techniques against real systems, penetration-testing walkthroughs, or weaponizable exploit code
- Hands-on examples must use dummy/learning data, not real data or real vulnerability details

### Workflow

1. Fork this repository
2. Create a branch for your change (e.g. `add-cloud-iam-module`)
3. Make your change. Bilingual JA/EN content is preferred for modules and guides, but a single-language contribution is also welcome — note in the PR that translation is pending
4. Open a Pull Request

### Adding a learning module

- Put it at `modules/<number>-<topic>/README.md`, with a Japanese section followed by an English section (follow the structure of existing modules)
- Include "What you'll learn", "Prerequisites", "Hands-on", and "Example prompts for Claude"
- Hands-on exercises should be safely reproducible with a local environment or dummy data
