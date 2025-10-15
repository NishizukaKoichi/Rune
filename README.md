# Rune

このリポジトリは、**Claude Code（総監督）× Codex CLI（実装担当）** の二重体制により、
どんなソフトウェアでも「計画 → 実装 → テスト → レビュー」を安全に自動運転できるよう設計された開発環境です。

---

## 主な構成要素

- `docs/amplifier_core/` – コアエージェント規約や README を保管
- `AGENTS.md` – Claude / Codex 両エージェント向けの起動プロンプトと運用ルール
- `PLANS.md` – 現行スプリントの目的・非目的・意思決定ログ
- `docs/spec/PROJECT_SPEC.md` – プロジェクトの一次仕様（※名称はプロジェクトに合わせて差し替え可）
- `frontend/`, `backend/` – フロントエンド／バックエンド向けの雛形。不要なら削除・置換してよい
- `amplifier/`, `tools/`, `.ai/` など – コア機能・サブエージェント・知識抽出パイプライン
- `scripts/` – UI スナップ生成や review 集約などの自動化スクリプト

---

## セットアップ

前提: Python 3.11+, UV, Node.js, pnpm, Git, VS Code (推奨) が導入済みであること。

```bash
make install        # 依存パッケージをまとめてインストール
```

### 推奨設定

1. `cp .env.example .env` してデータ/コンテンツ保存先を編集（OneDrive 等で集中管理可能）
2. Claude Code 側で chrome-devtools-mcp を有効化し、`AGENTS.md` の指示をセッション冒頭で貼り付け
3. Codex CLI 側でも `AGENTS.md` の実装担当テンプレを貼り、`make test` → `make ui:snap` → `make review` のループを確立

---

## 主要コマンド

| コマンド | 内容 |
| --- | --- |
| `make install` | Python 依存と、`frontend`/`backend` の依存をまとめてセットアップ |
| `make test` | コアの pytest と、フロントエンド／バックエンドテストを連続実行 |
| `make ui:snap` | `scripts/gen_ui_previews.py` とフロントエンドのスナップテストを実行し、差分レポートを生成 |
| `make review` | lint / typecheck / 依存監査 / セキュリティチェックをまとめて実行 |
| `make cage:fe-*` / `make cage:be-*` | フロント/バックエンド個別のショートカット（詳細は `Makefile` 参照） |
| `make knowledge-update` | 知識抽出パイプラインを実行 |
| `make worktree <name>` | 並列ワークツリーを作成（`.env` で共有データディレクトリを設定可能） |

---

## Claude / Codex の運用フロー

1. Claude セッション開始時に `AGENTS.md` 掲載の総監督プロンプトを貼り、`PLANS.md` と仕様書の要約から着手。  
2. `make test` で赤テストを確認し、`PLANS.md` の「進捗・意思決定ログ」に最短緑化プランを追記。  
3. UI が絡む場合は `make ui:snap` → 差分分類 → Claude が Codex へ依頼テンプレで指示。  
4. Codex は最小差分で実装・テスト・レビューを完遂し、根拠節を添えてログ化。  
5. Claude が `make review` の結果を確認、blocking=0 になるまでループ。  
6. 完了後は PR を小粒度で作成し、仕様根拠と検証手順を添えて提出。

---

## 参考ドキュメント

- Vision: `AMPLIFIER_VISION.md`
- コア README: `docs/amplifier_core/README_CORE.md`
- Claude 専用哲学/サブエージェント一覧: `docs/amplifier_core/AGENTS_CORE.md`
- プロジェクト仕様の雛形: `docs/spec/PROJECT_SPEC.md`（必要に応じて置き換え）
- セッションの意思決定ログ: `PLANS.md`
- Chrome DevTools MCP 連携や UI スナップ関連: `scripts/`

---

## 貢献ポリシー

PR は 1 目的 1 本・500 行以下を目安とし、`PLANS.md` に根拠と判断ログを必ず記録する。
学習系コマンドは破壊的変更が起こり得るため、`make knowledge-update` などを実行する際は
事前にバックアップと `.env` の保存先確認を行うこと。
