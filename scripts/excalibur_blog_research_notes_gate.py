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


# Do NOT include allowed search_intent labels like "workflow" — that false-marks
# non-IT how-to/workflow guides (auto import, checklists) as technical_topic.
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
    "автоматизац",
    "нейросет",
)


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


def is_technical_topic(context: dict[str, Any], notes: str) -> bool:
    """Detect tech niche topics. Short markers must be whole words:

    substring ``ai`` matches ``reader_pain`` and ``ии`` matches common Russian
    endings (``комплектации``, ``России``), falsely forcing GitHub evidence for
    non-tech niches (auto import, etc.).

    ``search_intent`` is intentionally excluded: values like ``workflow`` /
    ``how_to`` are editorial labels, not tech-stack signals.
    """
    topic = context.get("topic") or {}
    blob = " ".join(
        str(topic.get(key) or "")
        for key in ("h1", "primary_query", "secondary_queries", "slug")
    ).lower()
    blob += " " + notes[:2000].lower()
    for marker in TECH_MARKERS:
        if len(marker) <= 3:
            if re.search(rf"(?<![a-zа-яё0-9_]){re.escape(marker)}(?![a-zа-яё0-9_])", blob, flags=re.I):
                return True
        elif marker in blob:
            return True
    return False


def count_accessed_at(text: str) -> int:
    """Count source access stamps: ``accessed_at:`` keys and ISO dates in tables
    whose header includes an ``accessed_at`` column.
    """
    text_lower = text.lower()
    key_count = len(re.findall(r"\baccessed_at\b\s*:", text_lower))
    if not re.search(r"\|[^\n]*\baccessed_at\b[^\n]*\|", text_lower):
        return key_count
    date_in_table_rows = len(
        re.findall(r"^\s*\|[^\n]*\b20\d{2}-\d{2}-\d{2}\b", text, flags=re.M)
    )
    return max(key_count, date_in_table_rows)


def count_pain_solution_map_rows(text: str) -> int:
    """Count data rows under ## pain_solution_map.

    Prefer section table rows over requiring the words pain/solution/result on
    every row (agents may use Russian column labels only in the header).
    """
    match = re.search(
        r"##\s*\d*\.?\s*pain[_\s-]*solution[_\s-]*map\b([\s\S]*?)(?=\n##\s|\Z)",
        text,
        flags=re.I,
    )
    section = match.group(1) if match else ""
    if section:
        rows = 0
        for line in section.splitlines():
            if not re.match(r"^\s*\|", line):
                continue
            if re.match(r"^\s*\|[\s:\-|]+\|\s*$", line):
                continue
            cells = [c.strip().lower() for c in line.strip().strip("|").split("|")]
            nonempty = [c for c in cells if c]
            if not nonempty:
                continue
            label_hits = sum(
                1
                for c in nonempty
                if any(
                    tok in c
                    for tok in (
                        "pain",
                        "боль",
                        "solution",
                        "решение",
                        "result",
                        "результат",
                        "outcome",
                    )
                )
            )
            # Header row: mostly label cells, no concrete content digits/URLs.
            if label_hits >= max(2, len(nonempty) - 1) and not re.search(
                r"\d|http", line, flags=re.I
            ):
                continue
            rows += 1
        if rows:
            return rows
    # Fallback: legacy keyword-in-row heuristic across the whole notes file.
    return len(
        re.findall(
            r"^\s*\|.*(?:боль|pain|решение|solution|result|результат).*",
            text.lower(),
            flags=re.M,
        )
    )


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
    accessed_count = count_accessed_at(text)
    source_rows = len(re.findall(r"^\s*\|.*https?://", text, flags=re.M))
    pain_map_rows = count_pain_solution_map_rows(text)
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


def run_self_tests() -> int:
    """Regression: auto-import Russian notes must not be classified as technical."""
    auto_notes = (
        "reader_pain: ошибка выбора комплектации Kia K5 из России\n"
        "покупатель смотрит комплектации и мощность на Encar\n"
    )
    auto_ctx = {
        "topic": {
            "h1": "Kia K5 из Кореи: как выбрать комплектацию",
            "primary_query": "киа к5 из кореи",
            "slug": "kia-k5-iz-korei-kak-vybrat-2026",
            "search_intent": "workflow",
        }
    }
    if is_technical_topic(auto_ctx, auto_notes):
        print("SELF-TEST FAIL: auto topic falsely marked technical_topic", file=sys.stderr)
        return 1

    workflow_only_ctx = {
        "topic": {
            "h1": "Авто из Кореи под заказ: чек-лист",
            "primary_query": "авто из кореи под заказ",
            "slug": "avto-iz-korei-pod-zakaz-2026",
            "search_intent": "workflow",
        }
    }
    if is_technical_topic(workflow_only_ctx, "читатель выбирает авто и считает пошлину\n"):
        print(
            "SELF-TEST FAIL: search_intent=workflow alone must not set technical_topic",
            file=sys.stderr,
        )
        return 1

    tech_notes = "настройка mcp agent api и github actions для cursor\n"
    tech_ctx = {
        "topic": {
            "h1": "Как подключить MCP к Cursor",
            "primary_query": "mcp cursor api",
            "slug": "mcp-cursor-api",
            "search_intent": "how_to",
        }
    }
    if not is_technical_topic(tech_ctx, tech_notes):
        print("SELF-TEST FAIL: tech topic not detected", file=sys.stderr)
        return 1

    table = (
        "| source | url | accessed_at |\n"
        "| --- | --- | --- |\n"
        "| Kia | https://example.com/a | 2026-07-22 |\n"
        "| Drom | https://example.com/b | 2026-07-22 |\n"
    )
    if count_accessed_at(table) < 2:
        print("SELF-TEST FAIL: accessed_at table dates not counted", file=sys.stderr)
        return 1

    pain_section = (
        "## pain_solution_map\n"
        "| боль | решение | результат |\n"
        "| --- | --- | --- |\n"
        "| выбрал 180 л.с. | отсейте мотор ≤160 | проходите по утилю |\n"
        "| не знает trim | сравните Prestige/Noblesse | ясный чек-лист |\n"
        "| LPG путаница | сверьте паспорт | без сюрприза на таможне |\n"
    )
    if count_pain_solution_map_rows(pain_section) < 3:
        print("SELF-TEST FAIL: pain_solution_map rows undercounted", file=sys.stderr)
        return 1

    print("Research Notes Gate self-test: PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate research-notes.md freshness and depth")
    ap.add_argument("--article-dir", type=Path, default=None)
    ap.add_argument("-o", "--output", type=Path, default=None)
    ap.add_argument("--self-test", action="store_true", help="Run marker/regression self-tests")
    args = ap.parse_args()

    if args.self_test:
        return run_self_tests()
    if args.article_dir is None:
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
