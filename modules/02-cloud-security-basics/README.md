# モジュール2: クラウドセキュリティの基礎(AWS/Azure)

## 日本語

### 学ぶこと

AWSやAzureでよく起きる「設定ミス」のパターンと、その見つけ方・考え方を学びます。クラウド特有のサービス(IAM、ストレージ公開設定など)に絞って扱います。

### 前提知識

- AWSまたはAzureでリソース(EC2/VM、S3/Blob Storageなど)を作ったことがある程度でOKです

### よくある設定ミスのパターン

- **過剰な権限**: IAMロール・ユーザーに `*`(フルアクセス)権限が付与されている
- **公開範囲の誤り**: ストレージ(S3バケット、Blob Storage)が意図せず公開設定になっている
- **削除されない認証情報**: 退職者・使われていないサービスアカウントのアクセスキーが残っている
- **ログの未取得**: CloudTrail/Azure Activity Logなどの監査ログが無効、または保存期間が短すぎる

### ハンズオン(ダミー設定)

以下のようなダミーのIAMポリシー(JSON)をClaudeに読ませてみましょう(実際のアカウント情報は使わないでください)。

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

[templates/ja/secure-config-review-prompt.md](../../templates/ja/secure-config-review-prompt.md) をベースに、以下のような依頼をしてみましょう。

```
このIAMポリシーのリスクを指摘し、最小権限の原則に沿った改善案を提示してください。
一般的なベストプラクティスの観点から説明してください。
```

### 次のステップ

次は [モジュール3: インシデント対応の基礎](../03-incident-response-basics/README.md) に進みましょう。

---

## English

### What you'll learn

Common misconfiguration patterns on AWS and Azure, and how to spot them. This module focuses on cloud-specific services: IAM and storage exposure settings.

### Prerequisites

Having created a resource on AWS or Azure before (EC2/VM, S3/Blob Storage) is enough.

### Common misconfiguration patterns

- **Overly broad permissions**: an IAM role/user granted `*` (full access)
- **Wrong exposure scope**: storage (S3 bucket, Blob Storage) accidentally made public
- **Stale credentials**: access keys left behind for former employees or unused service accounts
- **Missing audit logs**: CloudTrail/Azure Activity Log disabled, or retention set too short

### Hands-on (dummy config)

Feed Claude a dummy IAM policy like this one (never use real account details):

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

Based on [templates/en/secure-config-review-prompt.md](../../templates/en/secure-config-review-prompt.md), try:

```
Point out the risks in this IAM policy, and propose a fix that follows the
principle of least privilege. Explain it in terms of general best practice.
```

### Next step

Move on to [Module 3: Incident Response Basics](../03-incident-response-basics/README.md).
