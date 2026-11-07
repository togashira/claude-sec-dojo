# モジュール4: セキュア設定レビュー

## 日本語

### 学ぶこと

サーバーやネットワーク機器の設定ファイル、IaC(Terraformなど)のコードを、セキュリティの観点でレビューする考え方を学びます。モジュール2のクラウド設定レビューを、より広い範囲(OS設定、ネットワーク機器設定、IaC全般)に広げます。

### 前提知識

モジュール1・2を終えていることを推奨します。設定ファイルを読んだ経験があれば十分です。

### レビューの観点

- **デフォルト設定のまま残っていないか**: デフォルトパスワード、不要なデフォルトポート開放など
- **不要に広い許可**: `0.0.0.0/0` からの全ポート許可など、必要以上に広い通信許可
- **暗号化・通信の保護**: 平文プロトコル(telnet, 平文HTTP等)が使われていないか
- **最小権限**: サービス・ユーザーに必要以上の権限が与えられていないか

### ハンズオン(ダミー設定)

以下のようなダミーのセキュリティグループ設定(擬似コード)をClaudeに読ませてみましょう。

```
Rule 1: Allow TCP 22  from 0.0.0.0/0   (SSH, 全世界からアクセス可能)
Rule 2: Allow TCP 3389 from 0.0.0.0/0  (RDP, 全世界からアクセス可能)
Rule 3: Allow TCP 443 from 0.0.0.0/0   (HTTPS)
```

### Claudeへの質問例

[templates/ja/secure-config-review-prompt.md](../../templates/ja/secure-config-review-prompt.md) をベースに、以下のような依頼をしてみましょう。

```
この設定をセキュリティの観点でレビューし、リスクの高いものから優先順位をつけて
指摘してください。それぞれについて、一般的な改善方針も提示してください。
```

### ここまでのまとめ

4つのモジュールを通じて、「ログから異常を見つける」「クラウド・設定のリスクを見つける」「インシデントを整理・報告する」という、現場で求められる基本サイクルを扱いました。次は [tools/log-triage-agent/](../../tools/log-triage-agent/) で、この一部を自動化する体験に進んでみてください。

---

## English

### What you'll learn

How to review server/network device config files and IaC code (Terraform, etc.) from a security angle. This extends Module 2's cloud config review to a broader scope: OS settings, network device configs, and IaC in general.

### Prerequisites

Finishing Modules 1 and 2 is recommended. Having read a config file before is enough.

### What to review for

- **Leftover defaults**: default passwords, unnecessary default ports left open
- **Overly broad access**: rules like "allow all ports from `0.0.0.0/0`" that are wider than needed
- **Encryption / protection in transit**: plaintext protocols (telnet, plain HTTP) still in use
- **Least privilege**: services/users granted more access than they need

### Hands-on (dummy config)

Feed Claude a dummy security-group config (pseudocode) like this:

```
Rule 1: Allow TCP 22  from 0.0.0.0/0   (SSH, open to the whole internet)
Rule 2: Allow TCP 3389 from 0.0.0.0/0  (RDP, open to the whole internet)
Rule 3: Allow TCP 443 from 0.0.0.0/0   (HTTPS)
```

### Example prompt for Claude

Based on [templates/en/secure-config-review-prompt.md](../../templates/en/secure-config-review-prompt.md), try:

```
Review this configuration from a security angle, and flag issues in priority
order from highest risk to lowest. For each one, suggest a general direction
for remediation.
```

### Wrapping up

Across these four modules, you've covered the basic cycle a frontline engineer needs: finding anomalies in logs, finding risk in cloud/config settings, and organizing/reporting an incident. Next, try [tools/log-triage-agent/](../../tools/log-triage-agent/) to get a taste of automating part of this.
