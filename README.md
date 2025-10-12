# Amplifier × AI Cage (“Spell Platform”) 開発環境

このリポジトリは、Microsoft Amplifier の AI 開発環境と  
`NishizukaKoichi/ai-cage-driven-dev` が提供する **Claude Code × Codex CLI** の二重運用フレームを統合したもの。  
Amplifier の豊富なサブエージェントと知識管理を土台に、Spell Platform 向けの拘束条件つき開発ループを構築する。

---

## 主な構成要素

- `docs/amplifier_core/` – 元 Amplifier のエージェント規約や README を保管
- `AGENTS.md` – Claude / Codex 双方の起動プロンプトと統合運用ルール
- `PLANS.md` – 現行スプリントの目的・非目的・意思決定ログ
- `docs/spec/Spell-Platform_v1.4.0.md` – Spell Platform 仕様書（一次参照）
- `frontend/`, `backend/` – Spell Platform 向け UI / API 実装
- `amplifier/`, `tools/`, `.ai/` など – Amplifier のコア機能・サブエージェント・知識抽出パイプライン
- `scripts/` – UI スナップ生成や review 集約など ai-cage 由来の自動化スクリプト

---

## セットアップ

前提: Python 3.11+, UV, Node.js, pnpm, Git, VS Code (推奨) が導入済みであること。

```bash
make install        # Amplifier 依存 + frontend/backend 依存をまとめてインストール
```

### 推奨設定

1. `cp .env.example .env` して Amplifier のデータ/コンテンツ保存先を編集（OneDrive 等で集中管理可能）
2. Claude Code 側で chrome-devtools-mcp を有効化し、`AGENTS.md` の指示をセッション冒頭で貼り付け
3. Codex CLI 側でも `AGENTS.md` の実装担当テンプレを貼り、`make test` → `make ui:snap` → `make review` のループを確立

---

## 主要コマンド

Amplifier 由来のコマンドに加え、Spell Platform 向けのショートカットが組み込まれている。

| コマンド | 内容 |
| --- | --- |
| `make install` | Amplifier の Python 依存と、`frontend`/`backend` の依存をまとめてセットアップ |
| `make test` | Amplifier コアの pytest + Spell Platform の FE/BE テストを連続実行 |
| `make ui:snap` | `scripts/gen_ui_previews.py` とフロントエンドのスナップテストを実行し、差分レポートを生成 |
| `make review` | lint / typecheck / 依存監査 / セキュリティチェックをまとめて実行（FE/BE 双方） |
| `make cage:fe-*` / `make cage:be-*` | Spell Platform 向けに分割された細粒度コマンド（詳細は `Makefile` 参照） |
| `make knowledge-update` | Amplifier の知識抽出パイプラインを実行 |
| `make worktree <name>` | Amplifier の並列ワークツリーを作成（Spell Platform データディレクトリ共有を推奨） |

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

- Amplifier Vision: `AMPLIFIER_VISION.md`
- Amplifier の元 README: `docs/amplifier_core/README_CORE.md`
- Claude 専用哲学/サブエージェント一覧: `docs/amplifier_core/AGENTS_CORE.md`
- Spell Platform 仕様書: `docs/spec/Spell-Platform_v1.4.0.md`
- セッションの意思決定ログ: `PLANS.md`
- Chrome DevTools MCP 連携や UI スナップ関連: `scripts/`

---

## 貢献ポリシー

現在はリポジトリ統合直後の実験段階。  
PR は 1 目的 1 本・500 行以下を目安とし、`PLANS.md` に根拠と判断ログを必ず記録する。  
Amplifier の学習系コマンドは破壊的変更が起こり得るため、`make knowledge-update` などを実行する際は  
事前にバックアップと `.env` の保存先確認を行うこと。
