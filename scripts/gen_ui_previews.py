#!/usr/bin/env python3
"""
UIプレビュー画像生成スクリプト（例）
- Reactアプリをローカルで起動し、主要ルートのスクショを撮る想定。
- 実運用では Playwright/Puppeteer を呼び出して各ビューポートで撮影する。
"""
import os
import sys
import json
import time
import subprocess
import pathlib

ROUTES = [
    {"name": "home-desktop", "url": "http://localhost:3000/", "width": 1366, "height": 768},
    {"name": "home-mobile", "url": "http://localhost:3000/", "width": 390, "height": 844},
]

OUT_DIR = pathlib.Path("frontend/__previews__")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def ensure_dev():
    """Placeholder for ensuring dev server is running.

    In production, this would start/verify the dev server is healthy.
    """
    # TODO: Implement dev server health check
    return True


def capture(route):
    # 実務では playwright CLI を使う
    # ここはダミー画像生成の例（pngバイナリは省略せず…と言いたいが生成実装は環境依存のためテキストメタで代替）
    p = OUT_DIR / f"{route['name']}.meta.json"
    meta = {
        "url": route["url"],
        "width": route["width"],
        "height": route["height"],
        "timestamp": time.time(),
    }
    p.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"[preview] wrote {p}")


def main():
    ensure_dev()
    for r in ROUTES:
        capture(r)
    print("[preview] done")


if __name__ == "__main__":
    main()
