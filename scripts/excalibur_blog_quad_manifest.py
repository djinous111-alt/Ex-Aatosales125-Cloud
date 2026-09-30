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


def scene_hint_for_type(type_id: str, h2: str) -> str:
    """AVTO SALES niche defaults — never seed Wordstat/SEO-laptop myths."""
    hints = {
        "comparison_table_ui": f"Таблица сравнения: Япония / Корея / Китай или документы vs риск — «{h2}»; NO Wordstat NO Metrika",
        "workflow_diagram": f"Схема шагов: таможня → документы → ГИБДД / проверка до депозита — «{h2}»; NO SEO tools",
        "checklist_board": f"Printable чеклист по документам/проверке авто — «{h2}»; NO Wordstat",
        "schema_faq_ui": f"FAQ accordion UI про авто/растаможку — «{h2}»",
        "tool_screenshot": f"Fake UI: Encar / аукционный лист / каталог avto-sales125.ru — «{h2}»; NEVER Wordstat/Metrika",
        "infographic_card": f"Карточка фактов про авто из Азии / документы — «{h2}»",
    }
    return hints.get(type_id, f"Полезная иллюстрация про авто/документы — «{h2}»")


def alt_for_type(type_id: str, h2: str, types_catalog: dict) -> str:
    label = ((types_catalog.get("types") or {}).get(type_id) or {}).get("label_ru") or type_id
    return f"{label}: {h2}"


def compact_topic(value: object, limit: int = 80) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def default_cover_hook(article_topic: str, meta: dict) -> str:
    """AVTO SALES pain hook — never seed SEO/Wordstat myths."""
    primary = (meta.get("primary_query") or meta.get("h1") or article_topic or "").strip()
    short = compact_topic(primary, 70)
    if short:
        return f"Пропустили шаг — и «{short}» превратился в отказ?"
    return "Документы вроде есть — а в ГИБДД разворачивают?"


def build_manifest(article_dir: Path, root: Path, preserve: dict | None) -> dict[str, Any]:
    meta_path = article_dir / "article.meta.json"
    meta = load_json(meta_path) if meta_path.is_file() else {}
    types_catalog = load_json(root / "memory/cover/inline-visual-types.json")
    h2s = extract_h2_titles(article_dir / "article.html")
    topic_id = meta.get("topic_id") or article_dir.name.split("-")[0]
    article_topic = meta.get("h1") or article_dir.name

    old_cover = ((preserve or {}).get("slots") or {}).get("cover") or {}
    default_cover_scene = (
        "EXACT face+glasses from reference; OUTFIT under weather/topic from article "
        "(rain jacket / winter coat / smart casual — NOT reference hoodie/tank); "
        f"pose/props under hook for «{compact_topic(article_topic)}»; "
        "Vladivostok/port/customs/docs vibe when relevant; "
        "NO Wordstat NO Metrika NO SEO laptop myths; corner footer avto-sales125.ru"
    )
    cover = {
        "quadrant": "top_left",
        "role": "cover_meme_hero",
        "alt": old_cover.get("alt") or f"Обложка: {article_topic}",
        "scene_hint": old_cover.get("scene_hint") or default_cover_scene,
        "meme_caption_ru": old_cover.get("meme_caption_ru") or "без сюрпризов на таможне",
    }

    used: set[str] = set()
    slots: dict[str, Any] = {"cover": cover}
    for idx, slot_key in enumerate(("inline_1", "inline_2", "inline_3"), start=1):
        h2 = h2s[idx - 1] if idx - 1 < len(h2s) else f"Секция {idx}"
        visual_type = pick_visual_type(h2, types_catalog, used)
        used.add(visual_type)
        old = ((preserve or {}).get("slots") or {}).get(slot_key) or {}
        slots[slot_key] = {
            "quadrant": DEFAULT_SLOT_MAP[slot_key],
            "h2_anchor": old.get("h2_anchor") or h2,
            "visual_type": visual_type,
            "scene_hint": old.get("scene_hint")
            or scene_hint_for_type(visual_type, old.get("h2_anchor") or h2),
            "alt": alt_for_type(visual_type, old.get("h2_anchor") or h2, types_catalog),
        }

    cover_hook = (preserve or {}).get("cover_hook") or default_cover_hook(article_topic, meta)

    return {
        "topic_id": topic_id,
        "canvas_file": "cover/canvas-quad.png",
        "layout": "2x2",
        "pipeline": "quad_canvas_1x_mcp",
        "style_preset": "digital_meme_collage_ru",
        "style_file": "memory/cover/quad-style-digital-meme-collage-ru.json",
        "blog_hero": "memory/cover/blog-hero.json",
        "inline_types_catalog": "memory/cover/inline-visual-types.json",
        "cover_hook": cover_hook,
        "mcp_note": "ONE gpt-image-2 call with input_urls=[reference_url_hosted], then split",
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
