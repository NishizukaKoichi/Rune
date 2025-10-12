#!/usr/bin/env python3
"""
レビュー統合：静的解析/依存/セキュリティ/循環/複雑度の収集と要約。
CIログで読みやすい形に整形する。blocking条件の例も提示。
"""
import json
import random

report = {
    "lint": "ok",
    "typecheck": "ok",
    "deps": {"unused": [], "vulns": []},
    "security": {"bandit": "ok"},
    "complexity": {"avg_cyclomatic": 3.1},
    "cycles": {"found": 0},
}

# 実装では各ツールのJSON出力を読み込む
blocking = []
if report["cycles"]["found"] > 0:
    blocking.append("循環参照あり")

if report["security"]["bandit"] != "ok":
    blocking.append("セキュリティ検査でHigh以上")

print("=== Review Report ===")
print(json.dumps(report, indent=2, ensure_ascii=False))
print("=====================")
if blocking:
    print("BLOCKING:", blocking)
else:
    print("BLOCKING: 0")
