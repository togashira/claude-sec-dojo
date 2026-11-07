# モジュール1: ネットワークログ分析の基礎

## 日本語

### 学ぶこと

ネットワーク機器(ルーター・スイッチ・ファイアウォールなど)のログから、「通常の動き」と「怪しい動き」を見分ける考え方を学びます。ログを1行ずつ手で追うのではなく、Claudeに読み込ませて要点を抽出する流れを体験します。

### 前提知識

- syslogやアクセスログがどんなものか、見たことがある程度でOKです
- 特定ベンダー(Cisco/Juniper等)の専門知識は不要です

### 見るべき観点(考え方)

- **量の変化**: 普段と比べて接続数・エラー数が急増/急減していないか
- **時間帯の違和感**: 業務時間外の管理者ログインなど、通常と違うタイミングのアクセスはないか
- **送信元の違和感**: 見慣れないIPレンジ・海外アドレスからのアクセスが連続していないか
- **繰り返しの失敗**: 短時間で同じ宛先への認証失敗が連続していないか(総当たり攻撃の可能性)

### ハンズオン(ダミーデータ)

以下のようなダミーのログを用意し、Claudeに読み込ませてみましょう(実際のログは使わないでください)。

```
2026-11-01 02:13:04 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:05 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:06 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:07 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 09:02:11 fw01 AUTH_OK    src=10.0.1.23   user=tanaka
2026-11-01 09:15:40 fw01 CONN_OK    src=10.0.1.23   dst=10.0.2.5 port=443
```

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

How to tell "normal" traffic apart from "suspicious" traffic in network device logs (routers, switches, firewalls). Instead of reading every line by hand, you'll practice feeding logs to Claude and extracting what matters.

### Prerequisites

- You've seen a syslog or access log before — that's enough
- No vendor-specific expertise (Cisco/Juniper, etc.) required

### What to look for (the mindset)

- **Volume changes**: a sudden spike or drop in connection/error counts vs. normal
- **Odd timing**: admin logins outside business hours, or other access at unusual times
- **Odd source**: a run of access from unfamiliar IP ranges or unexpected countries
- **Repeated failures**: repeated auth failures against the same target in a short window (possible brute force)

### Hands-on (dummy data)

Use dummy log lines like the ones below and feed them to Claude (never use real logs):

```
2026-11-01 02:13:04 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:05 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:06 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 02:13:07 fw01 AUTH_FAIL src=203.0.113.44 user=admin
2026-11-01 09:02:11 fw01 AUTH_OK    src=10.0.1.23   user=tanaka
2026-11-01 09:15:40 fw01 CONN_OK    src=10.0.1.23   dst=10.0.2.5 port=443
```

### Example prompt for Claude

Based on [templates/en/log-analysis-prompt.md](../../templates/en/log-analysis-prompt.md), try something like:

```
From this log, pick out up to 3 behaviors you consider abnormal, and for each one
note what might be happening and what to check next. Present these as
possibilities, not conclusions.
```

### Next step

Move on to [Module 2: Cloud Security Basics](../02-cloud-security-basics/README.md).
