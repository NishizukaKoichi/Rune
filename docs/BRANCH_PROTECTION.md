# ブランチ保護設定ガイド

このドキュメントでは、`main` ブランチの保護設定を行う手順を説明します。
これにより、素手では檻を越えられない最終防衛ラインが完成します。

## 設定URL

https://github.com/NishizukaKoichi/ai-cage-driven-dev/settings/branches

## 推奨設定

### 1. Require a pull request before merging
- ✅ **有効化**
- 設定:
  - Required approvals: **1**
  - Dismiss stale pull request approvals when new commits are pushed: ✅
  - Require review from Code Owners: ✅

### 2. Require status checks to pass before merging
- ✅ **有効化**
- 必須チェック（以下を選択）:
  - ✅ `CI / build-test-review`
  - ✅ `Guard - Makefile & Workflow Integrity / guard-checks`
  - ✅ `CodeQL Security Analysis / analyze (javascript)`
  - ✅ `CodeQL Security Analysis / analyze (python)`
- 設定:
  - Require branches to be up to date before merging: ✅

### 3. Require conversation resolution before merging
- ✅ **有効化**
- レビューコメントがすべて解決されるまでマージ不可

### 4. Require linear history
- ✅ **有効化** (推奨)
- マージコミット禁止、Squash/Rebaseのみ許可
- 履歴が一本線になり、追跡が容易

### 5. Require deployments to succeed before merging
- ⬜ **無効** (デプロイ環境がない場合)
- 本番デプロイがある場合は検討

### 6. Lock branch
- ⬜ **無効** (通常は不要)
- 完全に読み取り専用にする場合のみ

### 7. Do not allow bypassing the above settings
- ✅ **有効化**
- 管理者も含めて全員がルールに従う

### 8. Restrict who can push to matching branches
- ⬜ **任意**
- 特定のユーザー/チームのみpush許可する場合

## 設定後の確認

設定完了後、以下を確認：

```bash
# 1. 直接pushが拒否されることを確認
git checkout main
echo "test" >> test.txt
git add test.txt
git commit -m "test"
git push origin main
# → エラー: protected branch hook declined

# 2. PRを通せば問題なくマージできることを確認
git checkout -b test/branch-protection
git push origin test/branch-protection
# GitHub UIでPRを作成 → CI通過 → レビュー → マージ成功
```

## トラブルシューティング

### 「Status check not found」エラー

ワークフローが一度も実行されていない場合、チェック項目が表示されません。
以下の手順で解決：

1. PRを1つ作成してCIを実行
2. 実行後、Settings → Branches → Status checksに項目が表示される
3. 必須チェックを選択

### 自分自身がマージできない

"Do not allow bypassing" を有効にすると、管理者も含めて全員がPR+レビューが必要になります。
これは意図した動作です。セキュリティのため維持を推奨。

## 運用のコツ

- **小さなPR**を心がける（差分500行以下）
- **Draft PR**を活用してCI確認
- **Auto-merge**でパッチ/マイナー更新を自動化
- **CODEOWNERS**で自動レビュー依頼

---

設定完了後、PLANS.mdの進捗ログに記録してください。
