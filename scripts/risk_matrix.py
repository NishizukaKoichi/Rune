#!/usr/bin/env python3
"""
差分サイズ/ファイル数/テスト失敗数/循環有無などから変更リスクを算出する。
PRの粒度が適切かを定量的に判断する補助指標。
"""
import random
import json

risk = {
    "diff_lines": 320,
    "files_changed": 14,
    "tests_failed": 0,
    "cycles_found": 0,
    "score": 0.37,  # 0(低)〜1(高)の仮スコア
}
print(json.dumps(risk, indent=2))
