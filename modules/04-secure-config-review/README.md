# モジュール4: セキュア設定レビュー

## 日本語

### 学ぶこと

サーバーやネットワーク機器の設定ファイル、IaC(Infrastructure as Code。サーバーやネットワークの設定を、手作業ではなくコードとして書いて管理する方法。Terraformなどのツールが有名です)のコードを、セキュリティの観点でレビューする考え方を学びます。モジュール2のクラウド設定レビューを、より広い範囲(サーバーの基本ソフト(OS)の設定、ネットワーク機器設定、IaC全般)に広げます。

### 前提知識

モジュール1・2を終えていることを推奨します。設定ファイル(機械の動作を決めるための、人が書いたテキスト)を読んだ経験があれば十分です。

### レビューの観点

- **デフォルト設定のまま残っていないか**: 出荷時のままのパスワード、使っていないのに開いたままのポート(通信の出入り口の番号)など
- **不要に広い許可**: `0.0.0.0/0`(「インターネット上のすべての場所から」という意味です)からの全ポート許可など、必要以上に広い通信許可
- **暗号化・通信の保護**: 通信内容がそのまま読める「平文」のプロトコル(通信のやり方の規格。telnetや、暗号化されていないHTTPなど)が使われていないか
- **最小権限**: サービス・ユーザーに必要以上の権限が与えられていないか

### ハンズオン(ダミー設定)

以下はセキュリティグループ(「このポートは、このIPアドレスからだけ通信を許可する」といったルールの集まり。クラウドの通信制御の仕組みです)の設定例です(擬似コードで、実際に動くコードではありません)。Claudeに読ませてみましょう。

```
Rule 1: Allow TCP 22  from 0.0.0.0/0   (SSH=遠隔操作用の通信。全世界からアクセス可能)
Rule 2: Allow TCP 3389 from 0.0.0.0/0  (RDP=Windowsの遠隔操作用の通信。全世界からアクセス可能)
Rule 3: Allow TCP 443 from 0.0.0.0/0   (HTTPS=暗号化されたWebアクセス)
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

How to review server/network device config files and IaC code (Infrastructure as Code — writing infrastructure settings as code instead of configuring things by hand; Terraform is a well-known tool for this) from a security angle. This extends Module 2's cloud config review to a broader scope: the server's base software (OS) settings, network device configs, and IaC in general.

### Prerequisites

Finishing Modules 1 and 2 is recommended. Having read a config file (plain text a person writes to control how a machine behaves) before is enough.

### What to review for

- **Leftover defaults**: a password left at its out-of-the-box default, an unused port (a numbered "door" for network traffic) left open
- **Overly broad access**: rules like "allow all ports from `0.0.0.0/0`" (meaning "from anywhere on the internet") that are wider than needed
- **Encryption / protection in transit**: "plaintext" protocols (a protocol is just a set of rules for how two machines talk — telnet, or unencrypted HTTP, are examples) where the content can be read as-is by anyone watching the traffic
- **Least privilege**: services/users granted more access than they need

### Hands-on (dummy config)

Below is an example security group (a cloud mechanism for traffic rules like "only allow this port from this IP range") config, written as pseudocode (not real, runnable code). Feed it to Claude:

```
Rule 1: Allow TCP 22  from 0.0.0.0/0   (SSH - remote login. Open to the whole internet)
Rule 2: Allow TCP 3389 from 0.0.0.0/0  (RDP - Windows remote login. Open to the whole internet)
Rule 3: Allow TCP 443 from 0.0.0.0/0   (HTTPS - encrypted web traffic)
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
