# モジュール2: クラウドセキュリティの基礎(AWS/Azure)

## 日本語

### 学ぶこと

AWSやAzure(自分でサーバーを持たずに、必要な分だけ借りて使えるクラウドサービス)でよく起きる「設定ミス」のパターンと、その見つけ方・考え方を学びます。特に、クラウドならではの2つの仕組み、「誰が何をできるかの管理(IAM)」と「データの公開範囲の設定」に絞って扱います。

### 前提知識

- AWSまたはAzureで何かリソース(サーバーの代わりになる「仮想マシン」や、ファイルを置く「ストレージ」など)を作ったことがある程度でOKです。なくても、用語はこのページの中で説明します

### よくある設定ミスのパターン

- **過剰な権限**: IAM(Identity and Access Management = 「誰が、何に対して、何をしてよいか」を管理する仕組み)の「ロール」や「ユーザー」(アクセスする側の単位)に、`*`(すべての操作を許可するという意味の記号。つまり「フルアクセス」)の権限が付与されている
- **公開範囲の誤り**: ストレージ(ファイルを保存しておく領域。AWSでは「S3バケット」、Azureでは「Blob Storage」と呼ばれます)が、意図せず誰でも見られる状態(公開設定)になっている
- **削除されない認証情報**: 退職した人や、使われなくなったプログラム用アカウント(サービスアカウント)の「アクセスキー」(ログインパスワードのようなもの)が、消されずに残っている
- **ログの未取得**: 「誰が何をしたか」を記録する機能(AWSでは CloudTrail、Azureでは Activity Log と呼ばれます)が無効になっている、または記録を残しておく期間が短すぎる

### ハンズオン(ダミー設定)

以下はIAMポリシー(「誰が何をできるか」を定義する設定ファイル)の例です。JSON(設定を書くための、よく使われる記法)という形式で書かれていますが、読めなくても問題ありません。Claudeに読ませて説明してもらう前提です(実際のアカウント情報は使わないでください)。

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

### Claudeへの質問例

[templates/ja/secure-config-review-prompt.md](../../templates/ja/secure-config-review-prompt.md) をベースに、以下のような依頼をしてみましょう。「最小権限の原則」とは、「必要な操作だけを許可し、それ以上の権限は与えない」という考え方のことです。

```
このIAMポリシーのリスクを指摘し、最小権限の原則(必要な操作だけを許可する考え方)に
沿った改善案を提示してください。一般的なベストプラクティスの観点から説明してください。
```

### 次のステップ

次は [モジュール3: インシデント対応の基礎](../03-incident-response-basics/README.md) に進みましょう。

---

## English

### What you'll learn

Common misconfiguration patterns on AWS and Azure (cloud services that let you rent computing resources instead of owning your own servers), and how to spot them. This module focuses on two cloud-specific mechanisms: controlling who can do what (IAM) and controlling who can see your data (storage exposure settings).

### Prerequisites

Having created some resource on AWS or Azure before (a virtual server, or a storage area for files) is enough — if not, every term is explained inline below.

### Common misconfiguration patterns

- **Overly broad permissions**: IAM (Identity and Access Management — the system that controls who can do what) grants a "role" or "user" (the unit being granted access) the permission `*`, a symbol meaning "every action allowed" — i.e. full access
- **Wrong exposure scope**: storage (a place to keep files — called an "S3 bucket" on AWS, "Blob Storage" on Azure) accidentally set to be viewable by anyone (made public)
- **Stale credentials**: an "access key" (like a login password, but for a program rather than a person) left behind for a former employee or an unused service account (an account meant for a program, not a human)
- **Missing audit logs**: the feature that records who did what (CloudTrail on AWS, Activity Log on Azure) disabled, or its retention period set too short

### Hands-on (dummy config)

Below is an example IAM policy (a configuration file that defines who can do what). It's written in JSON (a common format for writing configuration), but you don't need to be able to read it yourself — the point is to have Claude explain it to you (never use real account details):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

### Example prompt for Claude

Based on [templates/en/secure-config-review-prompt.md](../../templates/en/secure-config-review-prompt.md), try this. "Principle of least privilege" just means "only allow what's actually needed, and nothing more":

```
Point out the risks in this IAM policy, and propose a fix that follows the
principle of least privilege (only allow what's actually needed). Explain it
in terms of general best practice.
```

### Next step

Move on to [Module 3: Incident Response Basics](../03-incident-response-basics/README.md).
