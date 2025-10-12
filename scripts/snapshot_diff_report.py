#!/usr/bin/env python3
"""
スナップショット差分の要約。
Jestの結果や __snapshots__ の更新状況を拾い、PLANS.md向けに整形。
"""
import re
import pathlib
import sys

SNAP_DIR = pathlib.Path("frontend/__tests__/__snapshots__")


def main():
    if not SNAP_DIR.exists():
        print("[snap] no snapshots dir found")
        return
    snaps = list(SNAP_DIR.glob("*.snap"))
    print("=== Snapshot Summary ===")
    for s in snaps:
        data = s.read_text(encoding="utf-8", errors="ignore")
        # 実運用では差分解析を行う。ここではファイル名列挙で可視性を担保。
        print(f"- {s.name}: {len(data)} bytes")
    print("========================")


if __name__ == "__main__":
    main()
