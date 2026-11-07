# モジュール1: ネットワークログ分析の基礎

## 日本語

### 学ぶこと

ネットワーク機器(ルーター・スイッチ・ファイアウォールなど。社内の通信を中継したり、不要な通信を止めたりする機械です)のログ(いつ・誰が・何をしたかが自動で記録されたテキスト)から、「通常の動き」と「怪しい動き」を見分ける考え方を学びます。ログを1行ずつ手で追うのではなく、Claudeに読み込ませて要点を抽出する流れを体験します。

### 前提知識

- ログ(syslogやアクセスログと呼ばれる、機械が自動で残す記録)がどんなものか、見たことがある程度でOKです。わからなくても、後の「ハンズオン」を見れば実例が出てきます
- 特定ベンダー(Cisco/Juniper等、ネットワーク機器を作っている会社)の専門知識は不要です

### 見るべき観点(考え方)

- **量の変化**: 普段と比べて接続数・エラー数が急増/急減していないか
- **時間帯の違和感**: 業務時間外の管理者ログインなど、通常と違うタイミングのアクセスはないか
- **送信元の違和感**: 見慣れないIPレンジ(インターネット上の住所のようなもの。例えば `203.0.113.0〜203.0.113.255` のようなまとまり)・海外のIPアドレスからのアクセスが連続していないか
- **繰り返しの失敗**: 短時間で同じ宛先へのログイン失敗が連続していないか(パスワードを片っ端から試す「総当たり攻撃」の可能性があります)

### ハンズオン(ダミーデータ)

以下はログの一例です(実際のシステムのログではなく、学習用に作った架空のデータです)。各行の意味は、

- `AUTH_FAIL` = ログイン試行が失敗した、`AUTH_OK` = ログインに成功した
- `src=` = アクセスしてきた側のIPアドレス(送信元)
- `dst=` = アクセスされた側のIPアドレス(宛先)、`port=` = 使われた通信の種類(443は暗号化されたWebアクセスによく使われる番号)

という意味です。覚える必要はなく、このページを見ながら読めれば十分です。

```
2026-11-01 02:13:04 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:05 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:06 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:07 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 09:02:11 fw01 AUTH_OK    src=10.0.1.23   user=tanaka
2026-11-01 09:15:40 fw01 CONN_OK    src=10.0.1.23   dst=10.0.2.5 port=443
```

これを実際にClaudeに貼り付けなくても、次の「Claudeへの質問例」を読むだけでも、どんな視点でログを読めばいいかが分かるようになっています。

### Claudeへの質問例

[templates/ja/log-analysis-prompt.md](../../templates/ja/log-analysis-prompt.md) をベースに、以下のような依頼をしてみましょう。

```
このログから、通常と異なると考えられる挙動を3つまでピックアップし、
それぞれ「何が起きている可能性があるか」「次に確認すべきこと」を挙げてください。
断定はせず、可能性として提示してください。
```

### 次のステップ

次は [モジュール2: クラウドセキュリティの基礎](../02-cloud-security-basics/README.md) に進みましょう。

---

## English

### What you'll learn

How to tell "normal" traffic apart from "suspicious" traffic in network device logs. A network device is a machine that routes traffic or blocks unwanted traffic — a router, switch, or firewall. A log is just a text record a machine automatically keeps of what happened and when. Instead of reading every line by hand, you'll practice feeding logs to Claude and extracting what matters.

### Prerequisites

- You've seen a log (sometimes called a "syslog" or "access log" — just a machine's automatic record) before — that's enough. If you haven't, the hands-on example below shows you one
- No vendor-specific expertise (Cisco/Juniper — companies that make network devices — etc.) required

### What to look for (the mindset)

- **Volume changes**: a sudden spike or drop in connection/error counts vs. normal
- **Odd timing**: admin logins outside business hours, or other access at unusual times
- **Odd source**: a run of access from an unfamiliar IP range (a block of internet "addresses", e.g. everything from `203.0.113.0` to `203.0.113.255`) or an unexpected country
- **Repeated failures**: repeated login failures against the same target in a short window (this pattern is called a "brute force" attempt — trying many passwords quickly)

### Hands-on (dummy data)

Below is an example log — not from a real system, just invented for learning. What each part means:

- `AUTH_FAIL` = a login attempt failed, `AUTH_OK` = a login succeeded
- `src=` = the IP address of whoever is connecting in (the source)
- `dst=` = the IP address being connected to (the destination), `port=` = which kind of connection was used (443 is commonly used for encrypted web traffic)

You don't need to memorize this — just use it as a reference while reading.

```
2026-11-01 02:13:04 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:05 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:06 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:07 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 09:02:11 fw01 AUTH_OK    src=10.0.1.23   user=tanaka
2026-11-01 09:15:40 fw01 CONN_OK    src=10.0.1.23   dst=10.0.2.5 port=443
```

Even without pasting this into Claude yourself, reading the example prompt below shows you what angle to read a log from.

### Example prompt for Claude

Based on [templates/en/log-analysis-prompt.md](../../templates/en/log-analysis-prompt.md), try something like:

```
From this log, pick out up to 3 behaviors you consider abnormal, and for each one
note what might be happening and what to check next. Present these as
possibilities, not conclusions.
```

### Next step

Move on to [Module 2: Cloud Security Basics](../02-cloud-security-basics/README.md).
