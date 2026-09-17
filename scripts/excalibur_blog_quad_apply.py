#!/usr/bin/env python3
"""Download ONE quad canvas URL (or use local canvas), save canvas-quad.png, run split + optional inject."""

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


def resolve_local_canvas(root: Path, article_dir: Path, canvas_local: str) -> Path:
    candidate = Path(canvas_local)
    if candidate.is_absolute() and candidate.is_file():
        return candidate
    for base in (article_dir, article_dir / "cover", root, root / "memory" / "cover" / "assets"):
        path = base / candidate if not candidate.is_absolute() else candidate
        if path.is_file():
            return path
    raise FileNotFoundError(f"local canvas not found: {canvas_local}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--url", default="", help="MCP/Kie result URL (or read cover/quad-mcp-result.json)")
    ap.add_argument(
        "--canvas-local",
        default="",
        help="Emergency path: use local PNG/JPEG as canvas instead of downloading a URL",
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
    result_json = cover_dir / "quad-mcp-result.json"

    canvas_local = args.canvas_local.strip()
    url = args.url.strip()
    if canvas_local:
        local_path = resolve_local_canvas(root, article_dir, canvas_local)
        if local_path.resolve() != canvas_path.resolve():
            shutil.copyfile(local_path, canvas_path)
        print(f"OK canvas-local={local_path} -> {canvas_path}")
        meta = {
            "url": "",
            "source": "canvas_local",
            "canvas_local": str(local_path),
        }
        if result_json.is_file():
            try:
                existing = json.loads(result_json.read_text(encoding="utf-8"))
                if isinstance(existing, dict):
                    meta = {**existing, **meta}
            except json.JSONDecodeError:
                pass
        result_json.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        if not url:
            if result_json.is_file():
                url = (json.loads(result_json.read_text(encoding="utf-8")).get("url") or "").strip()
        if not url:
            print(
                "❌ QUAD APPLY BLOCKER: pass --url, cover/quad-mcp-result.json, or --canvas-local",
                file=sys.stderr,
            )
            return 1

        data, _evidence = download_url_bytes(url)
        canvas_path.write_bytes(data)
        print(f"OK canvas={canvas_path}")
        result_json.write_text(json.dumps({"url": url}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    cmd = [
        sys.executable,
        str(root / "scripts" / "excalibur_blog_cover_quad_split.py"),
        "--article-dir",
        str(article_dir),
        "--manifest",
        "cover/quad-manifest.json",
        "--output-size",
        args.output_size,
    ]
    if args.inject_html:
        cmd.append("--inject-html")
    proc = subprocess.run(cmd, cwd=str(root))
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
