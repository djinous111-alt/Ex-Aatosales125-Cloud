#!/usr/bin/env python3
"""Fill quad-manifest.json: cover hook + inline visual_type per H2 (one quad canvas)."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

# Reuse type picker from visual manifest module inline
TYPE_PRIORITY = [
    "comparison_table_ui",
    "workflow_diagram",
    "checklist_board",
    "schema_faq_ui",
    "tool_screenshot",
    "infographic_card",
]
DEFAULT_SLOT_MAP = {
    "cover": "top_left",
    "inline_1": "top_right",
    "inline_2": "bottom_left",
    "inline_3": "bottom_right",
}


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def extract_h2_titles(article_html: Path) -> list[str]:
    if not article_html.is_file():
        return []
    text = article_html.read_text(encoding="utf-8")
    titles: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", text, flags=re.I | re.S):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        if title.lower() in {"частые вопросы", "faq"}:
            break
        titles.append(title)
    return titles


def score_type(h2: str, type_def: dict) -> int:
    hay = h2.lower()
    score = 0
    for kw in type_def.get("keywords") or []:
        if kw.strip().lower() in hay:
            score += 2
    return score


def pick_visual_type(h2: str, types_catalog: dict, used: set[str]) -> str:
    types = types_catalog.get("types") or {}
    scored: list[tuple[int, str]] = []
    for type_id, type_def in types.items():
        scored.append((score_type(h2, type_def), type_id))
    scored.sort(key=lambda item: (-item[0], TYPE_PRIORITY.index(item[1]) if item[1] in TYPE_PRIORITY else 99))
    for score, type_id in scored:
        if score > 0 and type_id not in used:
            return type_id
    for type_id in TYPE_PRIORITY:
        if type_id not in used:
            return type_id
    return TYPE_PRIORITY[0]


def scene_hint_for_type(type_id: str, h2: str, topic_hint: str = "") -> str:
    """Build inline scene from article H2/topic — never inject legacy SEO/Wordstat stubs."""
    topic = (topic_hint or "").strip()
    topic_bit = f"; тема: {topic[:80]}" if topic else ""
    hints = {
        "comparison_table_ui": f"Таблица сравнения по критериям из «{h2}»{topic_bit}",
        "workflow_diagram": f"Пошаговая схема действий: «{h2}»{topic_bit}",
        "checklist_board": f"Чеклист до решения/оплаты: «{h2}»{topic_bit}",
        "schema_faq_ui": f"FAQ/карточка ответов: «{h2}»{topic_bit}",
        "tool_screenshot": f"Fake UI/скрин инструмента по «{h2}»{topic_bit}",
        "infographic_card": f"Карточка фактов: «{h2}»{topic_bit}",
    }
    return hints.get(type_id, f"Полезная иллюстрация: «{h2}»{topic_bit}")


def alt_for_type(type_id: str, h2: str, types_catalog: dict) -> str:
    label = ((types_catalog.get("types") or {}).get(type_id) or {}).get("label_ru") or type_id
    return f"{label}: {h2}"


def build_manifest(article_dir: Path, root: Path, preserve: dict | None) -> dict[str, Any]:
    meta_path = article_dir / "article.meta.json"
    meta = load_json(meta_path) if meta_path.is_file() else {}
    types_catalog = load_json(root / "memory/cover/inline-visual-types.json")
    h2s = extract_h2_titles(article_dir / "article.html")
    topic_id = meta.get("topic_id") or article_dir.name.split("-")[0]
    article_topic = meta.get("h1") or article_dir.name

    old_cover = ((preserve or {}).get("slots") or {}).get("cover") or {}
    default_cover_scene = (
        "reference face + glasses; outfit: navy/charcoal softshell jacket OR heavyweight crewneck "
        "(NO hoodie, NO hood, NO cap); new pose/gesture; no headphones; topic-specific fake UI + meme cutout"
    )
    # On --merge, drop legacy SEO/Wordstat/hoodie stubs from a previous article.
    preserved_scene = str(old_cover.get("scene_hint") or "")
    stale_scene = any(
        token in preserved_scene.lower()
        for token in ("hoodie", "худи", "wordstat", "vordstat", "seoshnik", "seo vs geo", "15k ключей")
    )
    cover_scene = preserved_scene if preserved_scene and not stale_scene else default_cover_scene
    preserved_caption = str(old_cover.get("meme_caption_ru") or "")
    stale_caption = any(token in preserved_caption.lower() for token in ("15k", "wordstat", "ключей — 0"))
    cover = {
        "quadrant": "top_left",
        "role": "cover_meme_hero",
        "alt": old_cover.get("alt") or f"Обложка: {article_topic}",
        "scene_hint": cover_scene,
        "meme_caption_ru": preserved_caption if preserved_caption and not stale_caption else "До депозита — чеклист",
    }

    used: set[str] = set()
    slots: dict[str, Any] = {"cover": cover}
    for idx, slot_key in enumerate(("inline_1", "inline_2", "inline_3"), start=1):
        h2 = h2s[idx - 1] if idx - 1 < len(h2s) else f"Секция {idx}"
        visual_type = pick_visual_type(h2, types_catalog, used)
        used.add(visual_type)
        old = ((preserve or {}).get("slots") or {}).get(slot_key) or {}
        anchor = old.get("h2_anchor") or h2
        old_hint = str(old.get("scene_hint") or "")
        stale_inline = any(
            token in old_hint.lower()
            for token in ("seo vs geo", "wordstat", "longread: интент", "json-ld schema ui", "seo-инструмента")
        )
        slots[slot_key] = {
            "quadrant": DEFAULT_SLOT_MAP[slot_key],
            "h2_anchor": anchor,
            "visual_type": visual_type,
            "scene_hint": (
                old_hint
                if old_hint and not stale_inline
                else scene_hint_for_type(visual_type, anchor, article_topic)
            ),
            "alt": alt_for_type(visual_type, anchor, types_catalog),
        }

    old_hook = str((preserve or {}).get("cover_hook") or "")
    stale_hook = any(token in old_hook.lower() for token in ("seo-текст", "seo текст", "workflow?"))
    cover_hook = old_hook if old_hook and not stale_hook else f"{article_topic}: ловушка до депозита?"

    return {
        "topic_id": topic_id,
        "canvas_file": "cover/canvas-quad.png",
        "layout": "2x2",
        "pipeline": "quad_canvas_1x_mcp",
        "style_preset": "digital_meme_collage_ru",
        "style_file": "memory/cover/quad-style-digital-meme-collage-ru.json",
        "blog_hero": "memory/cover/blog-hero.json",
        "inline_types_catalog": "memory/cover/inline-visual-types.json",
        "outfit_lock": "softshell_or_crewneck",
        "cover_hook": cover_hook,
        "mcp_note": "Prefer Kie async API (scripts/excalibur_blog_kie_gpt_image2_api.py); sync MCP gpt-image-2 is legacy fallback",
        "slots": slots,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--out", default="cover/quad-manifest.json")
    ap.add_argument("--merge", action="store_true")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = article_dir / out_path

    preserve = load_json(out_path) if args.merge and out_path.is_file() else None
    manifest = build_manifest(article_dir, root, preserve)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(out_path, manifest)
    print(f"OK manifest={out_path}")
    for key in ("inline_1", "inline_2", "inline_3"):
        s = manifest["slots"][key]
        print(f"  {key}: {s['visual_type']} -> {s['h2_anchor']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
