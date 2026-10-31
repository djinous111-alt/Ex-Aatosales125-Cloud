#!/usr/bin/env python3
"""Smoke regressions for durable pipeline pins that rebrand/sync often wipe."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def load(name: str):
    path = SCRIPTS / name
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    errors: list[str] = []

    llms = load("excalibur_blog_llms_generator.py")
    url = llms.article_public_url("", "/", "vw-tharu-test")
    if url != "/vw-tharu-test/":
        errors.append(f"llms empty site-base + blog-path / expected /vw-tharu-test/, got {url!r}")
    legacy = llms.article_public_url("https://example.com", "/blog/", "vw-tharu-test")
    if legacy != "https://example.com/blog/vw-tharu-test/":
        errors.append(f"llms legacy blog-path failed: {legacy!r}")

    inter = load("excalibur_blog_interlinker.py")
    href = inter.article_href("/", "vw-tharu-test")
    if href != "/vw-tharu-test/":
        errors.append(f"interlinker href expected /vw-tharu-test/, got {href!r}")

    gate = load("excalibur_blog_research_notes_gate.py")
    auto_ctx = {
        "topic": {
            "h1": "Volkswagen Tharu из Китая: комплектации и ловушки",
            "primary_query": "как выбрать фольксваген тару из китая",
            "secondary_queries": ["комплектации tharu", "reader_pain checklist"],
            "search_intent": "how_to",
            "slug": "vw-tharu-iz-kitaya-komplektatsii-lovushki-2026",
        }
    }
    notes = (
        "# Volkswagen Tharu\n"
        "reader_pain: дорогая ошибка в комплектации\n"
        "## github_evidence\n"
        "- https://github.com/example/repo\n"
    )
    if gate.is_technical_topic(auto_ctx, notes):
        errors.append("TECH_MARKERS false-positive on комплектации / reader_pain auto topic")

    tech_ctx = {
        "topic": {
            "h1": "Как подключить MCP и Cursor agent к n8n",
            "primary_query": "cursor mcp n8n workflow",
            "secondary_queries": ["openai api"],
            "search_intent": "how_to",
            "slug": "cursor-mcp-n8n",
        }
    }
    if not gate.is_technical_topic(tech_ctx, "# MCP guide\n"):
        errors.append("TECH_MARKERS missed real technical topic")

    cover = load("excalibur_blog_cover_quad_prompt.py")
    if not hasattr(cover, "outfit_lock_from_hero"):
        errors.append("cover missing outfit_lock_from_hero")
    hero = {"outfit_rule": "softshell; NO hoodie", "cover_corner_brand": {"text": "example.ru"}}
    lock = cover.outfit_lock_from_hero(hero, "rain fog port")
    if "white hoodie" in lock.lower() and "no hoodie" not in lock.lower():
        errors.append(f"outfit lock still forces white hoodie: {lock!r}")

    pub = (SCRIPTS / "excalibur_blog_wp_publish.py").read_text(encoding="utf-8")
    if "reconstruct_publish_output_from_rest" not in pub:
        errors.append("publish missing REST reconstruct helper")

    for rel in (
        "scripts/excalibur_git.sh",
        "scripts/excalibur_blog_filter_commit_secret_env.sh",
        "scripts/excalibur_blog_filter_secret_names.sh",
    ):
        if not (ROOT / rel).is_file():
            errors.append(f"missing {rel}")

    today_src = (SCRIPTS / "excalibur_blog_today.py").read_text(encoding="utf-8")
    if r"((?:AS|B)\d+)" not in today_src:
        errors.append("today.py missing AS|B topic regex")

    if errors:
        print("FAIL fixer regression smoke:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("OK fixer regression smoke")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
