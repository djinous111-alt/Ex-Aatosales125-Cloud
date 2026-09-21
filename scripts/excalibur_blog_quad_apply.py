#!/usr/bin/env python3
"""Download ONE quad canvas URL, save canvas-quad.png, run split + optional inject."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from asset_download import download_url_bytes  # noqa: E402


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--url", default="", help="MCP/Kie result URL (or read cover/quad-mcp-result.json)")
    ap.add_argument(
        "--local-canvas",
        default="",
        help=(
            "Path to an already-generated local canvas PNG (GenerateImage / resized fallback). "
            "Skips URL download; copies/resizes path into cover/canvas-quad.png then splits."
        ),
    )
    ap.add_argument("--inject-html", action="store_true")
    ap.add_argument("--output-size", default="1200x675")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)

    canvas_path = cover_dir / "canvas-quad.png"
    local_canvas = (args.local_canvas or "").strip()
    url = args.url.strip()

    if local_canvas:
        src = Path(local_canvas)
        if not src.is_absolute():
            src = root / src
        if not src.is_file():
            # Also try relative to article_dir / cover
            alt = article_dir / local_canvas
            src = alt if alt.is_file() else cover_dir / local_canvas
        if not src.is_file():
            print(f"❌ QUAD APPLY BLOCKER: --local-canvas not found: {local_canvas}", file=sys.stderr)
            return 1
        if src.resolve() != canvas_path.resolve():
            shutil.copy2(src, canvas_path)
        print(f"OK local-canvas → {canvas_path}")
        result_json = cover_dir / "quad-mcp-result.json"
        result_json.write_text(
            json.dumps(
                {
                    "url": "",
                    "source": "local-canvas",
                    "local_canvas": str(src),
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    else:
        if not url:
            result_path = cover_dir / "quad-mcp-result.json"
            if result_path.is_file():
                url = (json.loads(result_path.read_text(encoding="utf-8")).get("url") or "").strip()
        if not url:
            print(
                "❌ QUAD APPLY BLOCKER: pass --url, cover/quad-mcp-result.json, or --local-canvas",
                file=sys.stderr,
            )
            return 1

        data, _evidence = download_url_bytes(url)
        canvas_path.write_bytes(data)
        print(f"OK canvas={canvas_path}")

        result_json = cover_dir / "quad-mcp-result.json"
        result_json.write_text(json.dumps({"url": url}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    cmd = [
        sys.executable,
        str(root / "scripts" / "excalibur_blog_cover_quad_split.py"),
        "--article-dir",
        str(article_dir),
        "--manifest",
        "cover/quad-manifest.json",
        "--canvas",
        str(canvas_path),
        "--output-size",
        args.output_size,
    ]
    if args.inject_html:
        cmd.append("--inject-html")
    proc = subprocess.run(cmd, cwd=str(root))
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
