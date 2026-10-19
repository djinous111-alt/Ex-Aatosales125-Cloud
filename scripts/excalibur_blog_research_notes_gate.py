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


# Whole-token / stem markers only. Plain substring falsely hits field names
# like reader_pain ("ai") and ordinary Cyrillic words with "ии".
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

# Stem prefixes: match at token start, allow suffix continuation.
TECH_STEM_MARKERS = frozenset({"автоматизац", "нейросет"})

_WORD_CHAR = r"0-9A-Za-zА-Яа-яЁё_"


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


def _tech_marker_re(marker: str) -> re.Pattern:
    escaped = re.escape(marker.lower())
    if marker in TECH_STEM_MARKERS:
        return re.compile(rf"(?<![{_WORD_CHAR}]){escaped}", re.I)
    return re.compile(rf"(?<![{_WORD_CHAR}]){escaped}(?![{_WORD_CHAR}])", re.I)


def marker_hits_blob(blob: str, marker: str) -> bool:
    return bool(_tech_marker_re(marker).search(blob))


def is_technical_topic(context: dict[str, Any], notes: str) -> bool:
    topic = context.get("topic") or {}
    blob = " ".join(
        str(topic.get(key) or "")
        for key in ("h1", "primary_query", "secondary_queries", "search_intent", "slug")
    ).lower()
    # Prefer topic card signals; only skim notes for explicit tech tokens, not field labels.
    notes_head = notes[:2000].lower()
    # Strip known research field labels that embed Latin "ai" / similar substrings.
    for field in ("reader_pain", "pain_solution_map", "reader_outcome", "success_criteria"):
        notes_head = notes_head.replace(field, " ")
    blob += " " + notes_head
    return any(marker_hits_blob(blob, marker) for marker in TECH_MARKERS)


def self_test() -> None:
    """Regression checks for TECH_MARKERS word-boundary matching."""
    cases = [
        ({"topic": {"h1": "Как растаможить авто", "slug": "kak-rastamozhit"}}, "reader_pain: боится депозит\npain_solution_map: …", False),
        ({"topic": {"h1": "Объявлении на сайте", "primary_query": "объявлении"}}, "обычный текст без tech", False),
        ({"topic": {"h1": "AI agent MCP workflow", "slug": "ai-agent"}}, "github evidence", True),
        ({"topic": {"h1": "n8n API docker", "slug": "n8n-api"}}, "", True),
        ({"topic": {"h1": "Cursor RAG", "slug": "cursor-rag"}}, "", True),
    ]
    failures: list[str] = []
    for context, notes, expect in cases:
        got = is_technical_topic(context, notes)
        if got != expect:
            failures.append(f"expected {expect} got {got} for {context!r} / {notes[:40]!r}")
    # Direct false-positive probes
    if marker_hits_blob("reader_pain: x", "ai"):
        failures.append("ai must not match inside reader_pain")
    if marker_hits_blob("объявлении", "ии"):
        failures.append("ии must not match inside объявлении")
    if marker_hits_blob("комплектации", "ии"):
        failures.append("ии must not match inside комплектации")
    if is_technical_topic(
        {"topic": {"h1": "Hyundai Tucson комплектации из Кореи", "slug": "hyundai-tucson-komplektatsii"}},
        "how_to import checklist for buyers",
    ):
        failures.append("auto комплектации topic must not be technical_topic")
    if not marker_hits_blob("use ai tools", "ai"):
        failures.append("ai must match as whole token")
    if failures:
        raise AssertionError("research_notes_gate self-test failed:\n- " + "\n- ".join(failures))


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


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate research-notes.md freshness and depth")
    ap.add_argument("--article-dir", type=Path, default=None)
    ap.add_argument("-o", "--output", type=Path, default=None)
    ap.add_argument("--self-test", action="store_true", help="Run TECH_MARKERS word-boundary regression checks")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        print("Research Notes Gate self-test: PASS")
        return 0

    if not args.article_dir:
        ap.error("--article-dir is required unless --self-test")

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    report = validate_research_notes(article_dir)

    if args.output:
        output = args.output if args.output.is_absolute() else article_dir / args.output
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
