#!/usr/bin/env python3
"""Validate Excalibur BLOG research notes for freshness and depth."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from excalibur_repo_paths import repo_relative


TECH_MARKERS = (
    "ai",
    "ии",
    "agent",
    "агент",
    "mcp",
    "api",
    "cursor",
    "make",
    "n8n",
    "github",
    "docker",
    "rag",
    "workflow",
    "автоматизац",
    "нейросет",
)

# Word-ish boundary: avoid substring hits like ai∈reader_pain / pain, ии∈японии.
_TECH_BOUNDARY = r"0-9A-Za-zА-Яа-яЁё_"


REQUIRED_FIELDS = (
    "research_date",
    "accessed_at",
    "reader_pain",
    "reader_outcome",
    "success_criteria",
    "voice_angle",
    "reader_story",
    "surprising_fact",
    "pain_solution_map",
    "github_evidence",
    "action_outline",
    "utility_verdict: PASS",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_urls(text: str) -> list[str]:
    urls = re.findall(r"https?://[^\s<>)\"']+", text)
    return [url.rstrip(".,;:") for url in urls]


def count_action_items(text: str) -> int:
    match = re.search(r"##\s*\d*\.?\s*action_outline\b([\s\S]*?)(?=\n##\s|\Z)", text, flags=re.I)
    section = match.group(1) if match else text
    numbered = re.findall(r"^\s*(?:\d+[\).]|[-*])\s+\S+", section, flags=re.M)
    return len(numbered)


def has_wordstat(text_lower: str) -> bool:
    return "wordstat" in text_lower or "вордстат" in text_lower or "wordstat_get_top_requests" in text_lower


def _marker_matches(marker: str, blob: str) -> bool:
    """True when marker appears as its own token, not as a substring of a longer word."""
    escaped = re.escape(marker.lower())
    pattern = rf"(?<![{_TECH_BOUNDARY}]){escaped}(?![{_TECH_BOUNDARY}])"
    return re.search(pattern, blob, flags=re.IGNORECASE) is not None


# Alias for self-tests / older call sites (INC-20261019-0913).
def _tech_marker_hit(marker: str, blob: str) -> bool:
    return _marker_matches(marker, blob)


def _strip_research_field_labels(notes_sample: str) -> str:
    """Remove required field labels/headings so they cannot false-trigger TECH_MARKERS."""
    cleaned = notes_sample
    for field in REQUIRED_FIELDS:
        if field == "utility_verdict: PASS":
            cleaned = re.sub(
                r"utility[_\s-]*verdict\s*:\s*pass",
                " ",
                cleaned,
                flags=re.I,
            )
            continue
        field_pattern = re.escape(field).replace("_", r"[_\s-]")
        cleaned = re.sub(
            rf"^\s*##\s*\d*\.?\s*{field_pattern}\b",
            " ",
            cleaned,
            flags=re.I | re.M,
        )
        cleaned = re.sub(rf"\b{field_pattern}\b\s*:", " ", cleaned, flags=re.I)
    return cleaned


def is_technical_topic(context: dict[str, Any], notes: str) -> bool:
    topic = context.get("topic") or {}
    blob = " ".join(
        str(topic.get(key) or "")
        for key in ("h1", "primary_query", "secondary_queries", "search_intent", "slug")
    ).lower()
    # Scan a notes sample, but strip structural labels (reader_pain, github_evidence, …).
    notes_sample = _strip_research_field_labels(notes[:2000].lower())
    blob += " " + notes_sample
    return any(_marker_matches(marker, blob) for marker in TECH_MARKERS)


def field_present(text_lower: str, field: str) -> bool:
    if field == "utility_verdict: PASS":
        return bool(re.search(r"utility[_\s-]*verdict\s*:\s*pass", text_lower, flags=re.I))
    if field in {"action_outline", "github_evidence", "pain_solution_map"}:
        field_pattern = re.escape(field).replace("_", r"[_\s-]")
        return bool(re.search(rf"^\s*##\s*\d*\.?\s*{field_pattern}\b", text_lower, flags=re.I | re.M))
    field_pattern = re.escape(field).replace("_", r"[_\s-]")
    return bool(re.search(rf"\b{field_pattern}\b\s*:", text_lower, flags=re.I))


def validate_research_notes(article_dir: Path) -> dict[str, Any]:
    root = project_root()
    notes_path = article_dir / "research-notes.md"
    context_path = article_dir / "research-context.json"
    errors: list[str] = []
    warnings: list[str] = []

    if not notes_path.is_file():
        return {
            "gate": "research-notes",
            "status": "BLOCK",
            "article_dir": repo_relative(article_dir, root),
            "errors": ["research-notes.md not found"],
            "warnings": [],
            "metrics": {},
        }
    if not context_path.is_file():
        errors.append("research-context.json not found")
        context: dict[str, Any] = {}
    else:
        context = load_json(context_path)

    text = notes_path.read_text(encoding="utf-8")
    text_lower = text.lower()
    ctx = context.get("date_context") or {}
    today_iso = str(ctx.get("today_iso") or "")
    year = str(ctx.get("year") or "")
    prefer_after = str((ctx.get("freshness_window") or {}).get("prefer_sources_after") or "")

    urls = extract_urls(text)
    domains = Counter(urlparse(url).netloc.lower().removeprefix("www.") for url in urls)
    github_urls = [url for url in urls if "github.com" in url.lower()]
    official_doc_urls = [
        url
        for url in urls
        if any(token in url.lower() for token in ("/docs", "developers.", "developer.", "help.", "learn."))
    ]
    accessed_count = len(re.findall(r"\baccessed_at\b\s*:", text_lower))
    source_rows = len(re.findall(r"^\s*\|.*https?://", text, flags=re.M))
    pain_map_rows = len(re.findall(r"^\s*\|.*(?:боль|pain|решение|solution|result|результат).*", text_lower, flags=re.M))
    action_items = count_action_items(text)

    for field in REQUIRED_FIELDS:
        if not field_present(text_lower, field):
            errors.append(f"missing required research field: {field}")

    if today_iso and today_iso not in text:
        errors.append(f"research_date must match current context today_iso={today_iso}")
    if today_iso and accessed_count < 5:
        errors.append(f"too few source access dates: accessed_at={accessed_count} < 5")
    if len(urls) < 8:
        errors.append(f"too few source URLs: {len(urls)} < 8")
    if len(domains) < 5:
        errors.append(f"too few independent source domains: {len(domains)} < 5")
    if source_rows < 5:
        warnings.append(f"source table looks thin: URL rows={source_rows} < 5")
    if not has_wordstat(text_lower):
        errors.append("missing Wordstat section or explicit Wordstat auth warning")
    if action_items < 5:
        errors.append(f"action_outline too short: {action_items} < 5")
    if pain_map_rows < 3:
        errors.append(f"pain_solution_map too thin: rows={pain_map_rows} < 3")
    if "⚠️ wordstat auth warning" in text_lower and "показы" not in text_lower:
        warnings.append("Wordstat auth warning present; exact demand volumes were not verified")

    technical = is_technical_topic(context, text)
    if technical and len(github_urls) < 3:
        errors.append(f"technical topic requires GitHub evidence: github_urls={len(github_urls)} < 3")
    if technical and not official_doc_urls:
        warnings.append("technical topic has no obvious official docs/developer documentation URL")

    if year and year not in text:
        warnings.append(f"current year {year} is not visible in research notes")
    if prefer_after and prefer_after not in text:
        warnings.append(f"freshness window prefer_sources_after={prefer_after} is not cited")

    status = "PASS" if not errors else "BLOCK"
    return {
        "gate": "research-notes",
        "status": status,
        "article_dir": repo_relative(article_dir, root),
        "notes": repo_relative(notes_path, root),
        "context": repo_relative(context_path, root),
        "errors": errors,
        "warnings": warnings,
        "metrics": {
            "today_iso": today_iso,
            "prefer_sources_after": prefer_after,
            "source_urls": len(urls),
            "source_domains": len(domains),
            "source_table_rows": source_rows,
            "accessed_at": accessed_count,
            "github_urls": len(github_urls),
            "official_doc_urls": len(official_doc_urls),
            "action_outline_items": action_items,
            "pain_solution_rows": pain_map_rows,
            "technical_topic": technical,
        },
    }


def _self_test() -> int:
    """Regression: ai⊂pain / reader_pain label must not mark AVTO topics technical."""
    assert _tech_marker_hit("ai", "ai agent workflow") is True
    assert _tech_marker_hit("ai", "reader_pain: новичок боится депозита") is False
    assert _tech_marker_hit("api", "rest api docs") is True
    assert _tech_marker_hit("api", "capibara") is False

    notes = (
        "research_date: 2026-10-19\n"
        "reader_pain: новичок не знает комплектации Seltos до депозита\n"
        "reader_outcome: чеклист комплектаций\n"
        "success_criteria: беру / жду / отказываюсь\n"
        "voice_angle: спокойный практик\n"
        "reader_story: заказ через Encar\n"
        "surprising_fact: комплектация без нужной опции\n"
        "accessed_at: 2026-10-19\n"
    )
    context = {
        "topic": {
            "h1": "Kia Seltos из Кореи: комплектации и ловушки",
            "primary_query": "киа селтос из кореи",
            "slug": "kia-seltos-iz-korei-komplektatsii-lovushki-2026",
            "search_intent": "checklist",
            "secondary_queries": ["комплектации seltos"],
        }
    }
    assert is_technical_topic(context, notes) is False

    tech_notes = "reader_pain: не умею подключить AI agent к MCP"
    tech_ctx = {
        "topic": {
            "h1": "Как подключить AI agent к MCP",
            "primary_query": "ai agent mcp",
            "slug": "ai-agent-mcp",
            "search_intent": "how_to",
            "secondary_queries": ["cursor mcp"],
        }
    }
    assert is_technical_topic(tech_ctx, tech_notes) is True
    print("PASS research_notes_gate --self-test")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate research-notes.md freshness and depth")
    ap.add_argument("--article-dir", type=Path, default=None)
    ap.add_argument("-o", "--output", type=Path, default=None)
    ap.add_argument("--self-test", action="store_true", help="Run TECH_MARKERS word-boundary regression")
    args = ap.parse_args()

    if args.self_test:
        return _self_test()

    if not args.article_dir:
        ap.error("--article-dir is required unless --self-test")

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    report = validate_research_notes(article_dir)

    if args.output:
        # Bare filename → article_dir. Path with directories → repo-root relative.
        if args.output.is_absolute():
            output = args.output
        else:
            rel = args.output.as_posix()
            if "/" in rel or rel.startswith(".."):
                output = root / args.output
            else:
                output = article_dir / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Research Notes Gate: {report['status']}")
    for error in report.get("errors") or []:
        print(f"ERROR: {error}", file=sys.stderr)
    for warning in report.get("warnings") or []:
        print(f"WARN: {warning}", file=sys.stderr)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
