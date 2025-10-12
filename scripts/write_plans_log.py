#!/usr/bin/env python3
"""
PLANS.mdに進捗・意思決定ログを追記する簡易スクリプト。
CIやAIから呼び出して履歴を"必ず"残す。
"""
import sys
import datetime
import pathlib

PLANS = pathlib.Path("PLANS.md")


def main(msg: str):
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    block = f"\n- **{stamp}**  {msg}\n"
    data = PLANS.read_text(encoding="utf-8")
    anchor = "## 5. 進捗・意思決定ログ（AIは必ず更新）"
    if anchor in data:
        data = data.replace(anchor, anchor + block, 1)
        PLANS.write_text(data, encoding="utf-8")
        print("[plans] appended log")
    else:
        print("[plans] anchor not found", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: write_plans_log.py 'message'")
        sys.exit(1)
    main(sys.argv[1])
