#!/usr/bin/env python3
"""Stamp catalog corner brand onto cover.png when the model omitted it.

Used after quad split. Does NOT regenerate the image — only a light PIL overlay.
Default brand text comes from memory/cover/blog-hero.json cover_corner_brand.text.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_brand_text(root: Path, override: str) -> str:
    if override.strip():
        return override.strip()
    hero_path = root / "memory/cover/blog-hero.json"
    if hero_path.is_file():
        hero = json.loads(hero_path.read_text(encoding="utf-8"))
        brand = hero.get("cover_corner_brand") or {}
        if isinstance(brand, dict) and brand.get("text"):
            return str(brand["text"]).strip()
    return "avto-sales125.ru"


def stamp_corner(cover_path: Path, text: str, *, force: bool = False) -> bool:
    img = Image.open(cover_path).convert("RGBA")
    # Cheap skip: if brand already clearly present as pixels we still may stamp;
    # agents pass --force when visual QA confirmed missing text.
    if not force:
        # Always stamp lightly — overlay is idempotent-ish (bottom-right strip).
        pass

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    font_size = max(18, img.width // 55)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    except OSError:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except OSError:
            font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad = max(8, font_size // 2)
    x = img.width - tw - pad * 2
    y = img.height - th - pad * 2
    # Soft dark plate for readability on white collage
    plate = [x - pad, y - pad // 2, x + tw + pad, y + th + pad // 2]
    draw.rectangle(plate, fill=(20, 20, 20, 150))
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 230))
    out = Image.alpha_composite(img, overlay).convert("RGB")
    out.save(cover_path)
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Stamp catalog corner brand on cover.png")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--text", default="", help="Override brand text (default: blog-hero cover_corner_brand)")
    ap.add_argument("--force", action="store_true", help="Stamp even if unsure text is missing")
    ap.add_argument("--cover", default="cover/cover.png")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_path = article_dir / args.cover
    if not cover_path.is_file():
        print(f"❌ STAMP BLOCKER: missing {cover_path}", file=sys.stderr)
        return 1

    text = load_brand_text(root, args.text)
    stamp_corner(cover_path, text, force=True if args.force else True)
    print(f"OK stamped corner brand={text!r} on {cover_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
