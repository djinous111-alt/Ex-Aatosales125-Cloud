#!/usr/bin/env python3
"""Smoke checks for AS10 fixer durable fixes (no network, no publish)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def check_topic_ids() -> None:
    from excalibur_topic_ids import format_topic_id, next_topic_id, parse_topic_id

    assert parse_topic_id("AS10") == ("AS", 10)
    assert parse_topic_id("B09") == ("B", 9)
    assert parse_topic_id("XX1") is None
    assert format_topic_id("AS", 11) == "AS11"
    assert next_topic_id(["AS08", "AS10", "B99"], preferred_prefix="AS") == "AS11"
    print("OK topic_ids AS|B")


def check_tech_markers() -> None:
    from excalibur_blog_research_notes_gate import is_technical_topic

    auto_ctx = {
        "topic": {
            "h1": "Как выбрать Hyundai Avante из Кореи по мощности и комплектации",
            "primary_query": "hyundai avante из кореи комплектации",
            "secondary_queries": ["мощность avante", "трим комплектации"],
            "search_intent": "how_to",
            "slug": "hyundai-avante-iz-korei-kak-vybrat-2026",
        }
    }
    assert is_technical_topic(auto_ctx, "github_evidence: n/a\nreader_pain: депозит\n") is False
    assert is_technical_topic(auto_ctx, "reader_pain: депозит без проверки\n") is False

    tech_ctx = {
        "topic": {
            "h1": "Как подключить MCP API к Cursor AI агенту",
            "primary_query": "mcp api cursor agent",
            "secondary_queries": ["rag workflow"],
            "search_intent": "how_to",
            "slug": "mcp-api-cursor",
        }
    }
    assert is_technical_topic(tech_ctx, "нужен github evidence из репозиториев") is True
    print("OK research tech markers (Hyundai/комплектации/github_evidence label not technical)")


def check_utility_empty_markers_skip() -> None:
    from excalibur_blog_utility_gate import count_markers

    # Empty list must yield zero without raising; gate skips min when list empty.
    assert count_markers("боль результат получите", []) == 0
    assert count_markers("боль и проблема, получите результат", ["боль", "проблем", "результат"]) >= 2
    print("OK utility marker counting")


def check_kie_cli_flags() -> None:
    import subprocess

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/excalibur_blog_kie_gpt_image2_api.py"), "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    assert "--min-credits" in proc.stdout
    assert "--credits-only" in proc.stdout
    print("OK kie --min-credits CLI")


def check_llms_no_blog_path() -> None:
    import subprocess

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/excalibur_blog_llms_generator.py"), "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert "--blog-dir" in proc.stdout
    assert "--blog-path" not in proc.stdout
    print("OK llms CLI --blog-dir only")


def check_credit_parser() -> None:
    from excalibur_blog_kie_gpt_image2_api import parse_credit_balance

    assert parse_credit_balance({"code": 200, "data": {"credit": 3.5}}) == 3.5
    assert parse_credit_balance({"data": -0.11}) == -0.11
    print("OK kie credit parser")


def main() -> int:
    check_topic_ids()
    check_tech_markers()
    check_utility_empty_markers_skip()
    check_kie_cli_flags()
    check_llms_no_blog_path()
    check_credit_parser()
    print("SUMMARY all smoke checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
