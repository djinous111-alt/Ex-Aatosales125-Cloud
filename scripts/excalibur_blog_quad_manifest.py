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

AUTO_NICHE_MARKERS = (
    "авто",
    "машин",
    "япони",
    "коре",
    "кита",
    "растамож",
    "encar",
    "аукцион",
    "владивосток",
    "утильсбор",
    "vin",
    "эптс",
    "свх",
    "таможн",
    "авто-сейлс",
    "avto-sales",
    "avtosales",
)
SEO_NICHE_MARKERS = (
    "seo",
    "geo",
    "wordstat",
    "llms.txt",
    "cursor ai",
    "mcp",
    "нейросет",
    "ai-агент",
)


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


def detect_niche(meta: dict[str, Any], root: Path, article_topic: str, h2s: list[str]) -> str:
    parts = [
        str(meta.get("h1") or ""),
        str(meta.get("primary_query") or ""),
        str(meta.get("slug") or ""),
        str(meta.get("cover_alt") or ""),
        article_topic,
        " ".join(h2s[:4]),
    ]
    brief = root / "memory/brief/site-brief.md"
    if brief.is_file():
        parts.append(brief.read_text(encoding="utf-8")[:1200])
    blob = " ".join(parts).lower()
    auto_hits = sum(1 for m in AUTO_NICHE_MARKERS if m in blob)
    seo_hits = sum(1 for m in SEO_NICHE_MARKERS if m in blob)
    if auto_hits >= seo_hits and auto_hits > 0:
        return "auto_import"
    if seo_hits > auto_hits:
        return "seo"
    # Current channel default: Авто-Сейлс JP/KR/CN
    return "auto_import"


def scene_hint_for_type(type_id: str, h2: str, niche: str) -> str:
    if niche == "auto_import":
        hints = {
            "comparison_table_ui": (
                f"Чистая RU-таблица сравнения строк сметы (лот / логистика / таможня / РФ) — «{h2}»; "
                "без Wordstat/Metrika/SEO; без конкретных сумм"
            ),
            "workflow_diagram": (
                f"Схема 4 блоков со стрелками: Япония/Корея/Китай → море/порт → таможня → СБКТС/ЭПТС — «{h2}»; "
                "без Wordstat/Metrika"
            ),
            "checklist_board": (
                f"Printable чеклист до ставки/депозита (VIN, лист, курс, строки сметы) — «{h2}»; "
                "без Wordstat/Metrika"
            ),
            "schema_faq_ui": f"FAQ accordion про импорт авто / растаможку — «{h2}»; без SEO-аналитики",
            "tool_screenshot": (
                f"Fake UI: аукционный лист / Encar / каталог карточка — «{h2}»; "
                "NEVER Wordstat NEVER Metrika; суммы размыты"
            ),
            "infographic_card": f"Карточка фактов по импорту авто JP/KR/CN — «{h2}»; без SEO-инструментов",
        }
    else:
        hints = {
            "comparison_table_ui": f"Таблица SEO vs GEO: критерии, цели, человек vs AI — «{h2}»",
            "workflow_diagram": f"6 шагов longread: интент -> семантика -> outline -> lead -> факты -> FAQ — «{h2}»",
            "checklist_board": f"Printable чеклист перед публикацией — «{h2}»",
            "schema_faq_ui": f"FAQ accordion + JSON-LD schema UI — «{h2}»",
            "tool_screenshot": f"Скрин SEO-инструмента — «{h2}»",
            "infographic_card": f"Карточка фактов — «{h2}»",
        }
    return hints.get(type_id, f"Полезная иллюстрация — «{h2}»")


def alt_for_type(type_id: str, h2: str, types_catalog: dict) -> str:
    label = ((types_catalog.get("types") or {}).get(type_id) or {}).get("label_ru") or type_id
    return f"{label}: {h2}"


def default_cover_for_niche(niche: str, article_topic: str) -> dict[str, str]:
    if niche == "auto_import":
        return {
            "alt": f"Обложка Авто-Сейлс: {article_topic}",
            "scene_hint": (
                "reference EXACT face likeness; outfit under Vladivostok/port weather "
                "(NOT reference tank/t-shirt), NO cap NO hood, glasses on; "
                "auction sheet / Encar card / calculator props; torn-paper Cyrillic hook; "
                "DIY zine collage; corner footer ONLY avto-sales125.ru catalog site "
                "(NOT Telegram); NEVER Wordstat NEVER Metrika NEVER SEO analytics; "
                "NO concrete money amounts on image"
            ),
            "meme_caption_ru": "Цена лота — ещё не итог",
            "cover_hook": "Полная смета до ставки: лот ≠ итог под ключ",
        }
    return {
        "alt": f"Обложка: {article_topic}",
        "scene_hint": (
            "reference-лицо, белое плотное худи из толстой ткани, новая поза/жест/ракурс под крючок, "
            "без наушников/headset/earbuds, шок/ирония SEOшника, Wordstat + ноутбук"
        ),
        "meme_caption_ru": "15k ключей — 0 прочтений?",
        "cover_hook": "SEO-текст, который люди дочитают — миф или workflow?",
    }


def build_manifest(article_dir: Path, root: Path, preserve: dict | None) -> dict[str, Any]:
    meta_path = article_dir / "article.meta.json"
    meta = load_json(meta_path) if meta_path.is_file() else {}
    types_catalog = load_json(root / "memory/cover/inline-visual-types.json")
    h2s = extract_h2_titles(article_dir / "article.html")
    topic_id = meta.get("topic_id") or article_dir.name.split("-")[0]
    article_topic = meta.get("h1") or article_dir.name
    niche = detect_niche(meta, root, str(article_topic), h2s)
    niche_defaults = default_cover_for_niche(niche, str(article_topic))

    old_cover = ((preserve or {}).get("slots") or {}).get("cover") or {}
    cover = {
        "quadrant": "top_left",
        "role": "cover_meme_hero",
        "alt": old_cover.get("alt") or niche_defaults["alt"],
        "scene_hint": old_cover.get("scene_hint") or niche_defaults["scene_hint"],
        "meme_caption_ru": old_cover.get("meme_caption_ru") or niche_defaults["meme_caption_ru"],
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
            "scene_hint": scene_hint_for_type(visual_type, old.get("h2_anchor") or h2, niche),
            "alt": alt_for_type(visual_type, old.get("h2_anchor") or h2, types_catalog),
        }

    cover_hook = (preserve or {}).get("cover_hook") or niche_defaults["cover_hook"]

    return {
        "topic_id": topic_id,
        "niche": niche,
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
    print(f"OK manifest={out_path} niche={manifest.get('niche')}")
    for key in ("inline_1", "inline_2", "inline_3"):
        s = manifest["slots"][key]
        print(f"  {key}: {s['visual_type']} -> {s['h2_anchor']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
