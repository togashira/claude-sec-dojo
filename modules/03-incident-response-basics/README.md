# モジュール3: インシデント対応の基礎

## 日本語

### 学ぶこと

セキュリティインシデント(「侵入された」「情報が漏れたかもしれない」など、セキュリティ上の問題が起きた、または起きた疑いがある状態のことをこう呼びます)が起きたときに、現場のエンジニアが最初に行うべき「状況の整理」と「報告」の進め方を学びます。実際の対応手順(問題の拡大を止める「封じ込め」、元の状態に戻す「復旧」など)は組織ごとのルールに従う必要があるため、ここでは「情報整理の型」を扱います。

### 前提知識

特にありません。モジュール1・2を終えていると理解しやすくなります。

### 初動で整理すべきこと(型)

1. **何が起きたか(事実)**: いつ、どこで、何が検知されたか
2. **影響範囲**: 影響を受けている可能性のあるシステム・データ・利用者
3. **すでに分かっている原因の仮説**: 断定せず「可能性」として
4. **すでに取った対応**: 誰が何をしたか
5. **次に必要な判断・エスカレーション先**: 自分だけで決めずに、上位の判断者や専門チームに引き上げる(これを「エスカレーション」と言います)必要がある場合、誰の判断が必要か

### ハンズオン(ダミーシナリオ)

以下のようなダミーの状況メモをClaudeに読ませてみましょう。

```
23:40 監視アラートで fw01 からの認証失敗が通常の20倍に増加していることを検知。
23:45 対象IPレンジ(203.0.113.0/24)からの通信であることを確認。
23:50 一時的に該当IPレンジをファイアウォールでブロック。
00:10 ブロック後、異常な認証失敗は収束。影響を受けたアカウントは現時点で不明。
```

### Claudeへの質問例

[templates/ja/incident-report-prompt.md](../../templates/ja/incident-report-prompt.md) をベースに、以下のような依頼をしてみましょう。

```
このメモを元に、上司・関係者に共有するための初動報告書を作成してください。
「事実」と「推測」を明確に分け、まだ確認できていない点は
「未確認事項」として明記してください。
```

### 次のステップ

次は [モジュール4: セキュア設定レビュー](../04-secure-config-review/README.md) に進みましょう。

---

## English

### What you'll learn

How a frontline engineer should organize facts and write a report in the first moments of a security incident — a state where something security-related has gone wrong, or is suspected to have (an intrusion, a possible data leak, etc.). Actual response procedures ("containment" — stopping the problem from spreading, "recovery" — getting back to normal, etc.) must follow your organization's own rules, so this module focuses purely on the "shape" of information organizing.

### Prerequisites

None specifically, though finishing Modules 1 and 2 first will help.

### What to organize first (the shape)

1. **What happened (facts)**: when, where, what was detected
2. **Scope of impact**: which systems/data/users may be affected
3. **Working hypotheses about the cause**: framed as possibilities, not conclusions
4. **Actions already taken**: who did what
5. **What decision or escalation is needed next**: if this needs to be raised to someone more senior or a specialist team rather than decided alone (that's what "escalation" means), whose call is it

### Hands-on (dummy scenario)

Feed Claude a dummy situation note like this one:

```
23:40 Monitoring alert: auth failures from fw01 spiked to 20x normal.
23:45 Confirmed traffic is coming from IP range 203.0.113.0/24.
23:50 Temporarily blocked that IP range at the firewall.
00:10 After the block, abnormal auth failures subsided. Affected accounts unknown so far.
```

### Example prompt for Claude

Based on [templates/en/incident-report-prompt.md](../../templates/en/incident-report-prompt.md), try:

```
Using this note, draft an initial incident report to share with management
and stakeholders. Clearly separate facts from speculation, and list anything
not yet confirmed under "open items".
```

### Next step

Move on to [Module 4: Secure Configuration Review](../04-secure-config-review/README.md).
