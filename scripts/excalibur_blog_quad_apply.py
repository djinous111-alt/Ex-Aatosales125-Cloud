#!/usr/bin/env python3
"""Download ONE quad canvas URL, save canvas-quad.png, run split + optional inject."""

from __future__ import annotations

import argparse
import json
import os
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


def normalize_canvas_to_recommended(canvas_path: Path, target: tuple[int, int] = (2048, 1152)) -> None:
    """Center-crop to 16:9 and resize — emergency GenerateImage often returns 3:2."""
    try:
        from PIL import Image
    except ImportError:
        print("WARN Pillow missing: skip canvas normalize to 2048x1152", file=sys.stderr)
        return
    tw, th = target
    target_aspect = tw / th
    with Image.open(canvas_path) as im:
        im = im.convert("RGBA")
        w, h = im.size
        if (w, h) == (tw, th):
            return
        current = w / h if h else 0
        if current > target_aspect:
            new_w = int(round(h * target_aspect))
            left = max(0, (w - new_w) // 2)
            box = (left, 0, left + new_w, h)
        else:
            new_h = int(round(w / target_aspect))
            top = max(0, (h - new_h) // 2)
            box = (0, top, w, top + new_h)
        cropped = im.crop(box).resize((tw, th), Image.Resampling.LANCZOS)
        cropped.save(canvas_path, format="PNG", optimize=True)
        print(f"OK canvas normalized {w}x{h} → {tw}x{th}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--url", default="", help="MCP result URL (or read cover/quad-mcp-result.json)")
    ap.add_argument(
        "--canvas",
        default="",
        help="Local canvas PNG path (emergency GenerateImage); skips URL download",
    )
    ap.add_argument("--inject-html", action="store_true")
    ap.add_argument("--output-size", default="1200x675")
    ap.add_argument(
        "--normalize-canvas",
        action="store_true",
        default=True,
        help="Center-crop+resize canvas to 2048x1152 before split (default on)",
    )
    ap.add_argument(
        "--no-normalize-canvas",
        action="store_false",
        dest="normalize_canvas",
        help="Keep source canvas dimensions",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)

    canvas_path = cover_dir / "canvas-quad.png"
    local_canvas = args.canvas.strip()
    url = args.url.strip()

    if local_canvas:
        src = Path(local_canvas)
        if not src.is_absolute():
            src = root / src
        if not src.is_file():
            # Also accept path relative to article_dir / cover
            alt = article_dir / local_canvas
            src = alt if alt.is_file() else cover_dir / local_canvas
        if not src.is_file():
            print(f"❌ QUAD APPLY BLOCKER: local canvas not found: {local_canvas}", file=sys.stderr)
            return 1
        if src.resolve() != canvas_path.resolve():
            canvas_path.write_bytes(src.read_bytes())
        print(f"OK canvas=local:{src}")
        result_payload = {"url": "", "local_canvas": str(src), "source": "local"}
    else:
        if not url:
            result_path = cover_dir / "quad-mcp-result.json"
            if result_path.is_file():
                url = (json.loads(result_path.read_text(encoding="utf-8")).get("url") or "").strip()
        if not url:
            print(
                "❌ QUAD APPLY BLOCKER: pass --url, --canvas, or cover/quad-mcp-result.json",
                file=sys.stderr,
            )
            return 1
        data, _evidence = download_url_bytes(url)
        canvas_path.write_bytes(data)
        print(f"OK canvas={canvas_path}")
        result_payload = {"url": url, "source": "url"}

    if args.normalize_canvas:
        normalize_canvas_to_recommended(canvas_path)

    result_json = cover_dir / "quad-mcp-result.json"
    result_json.write_text(json.dumps(result_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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
