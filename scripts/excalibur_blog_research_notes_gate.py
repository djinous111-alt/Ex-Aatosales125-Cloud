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


# Match as whole tokens only (word-boundary). Substring matches caused false
# technical classification: "ai" inside "pain", "ии" inside "комплектации".
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

# Auto-import / dealer utility niches are never forced to GitHub evidence.
AUTO_NICHE_MARKERS = (
    "encar",
    "hyundai",
    "toyota",
    "kia",
    "santa fe",
    "tucson",
    "аукцион",
    "растамож",
    "комплектац",
    "автоимпорт",
    "из кореи",
    "из японии",
    "из китая",
    "utilzbor",
    "утильсбор",
    "carhistory",
    "trust encar",
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


def _token_present(blob: str, marker: str) -> bool:
    """True if marker appears as a whole token (Unicode-aware word boundary)."""
    if not marker:
        return False
    # Prefix markers (автоматизац / нейросет) — match start of a word.
    if marker.endswith(("ац", "ет")) and len(marker) >= 6:
        return bool(re.search(rf"(?<![\w]){re.escape(marker)}", blob, flags=re.I | re.UNICODE))
    return bool(re.search(rf"(?<![\w]){re.escape(marker)}(?![\w])", blob, flags=re.I | re.UNICODE))


def topic_blob(context: dict[str, Any], notes: str) -> str:
    topic = context.get("topic") or {}
    blob = " ".join(
        str(topic.get(key) or "")
        for key in ("h1", "primary_query", "secondary_queries", "search_intent", "slug")
    ).lower()
    blob += " " + notes[:2000].lower()
    return blob


def is_auto_niche(context: dict[str, Any], notes: str) -> bool:
    blob = topic_blob(context, notes)
    return any(marker in blob for marker in AUTO_NICHE_MARKERS)


def is_technical_topic(context: dict[str, Any], notes: str) -> bool:
    if is_auto_niche(context, notes):
        return False
    blob = topic_blob(context, notes)
    return any(_token_present(blob, marker) for marker in TECH_MARKERS)


def count_accessed_at(text: str) -> int:
    """Count accessed_at labels and markdown-table column dates."""
    text_lower = text.lower()
    colon_hits = len(re.findall(r"\baccessed_at\b\s*:", text_lower))
    table_hits = 0
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if "|" in line and re.search(r"\baccessed_at\b", line, flags=re.I):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            col = next(
                (idx for idx, c in enumerate(cells) if re.search(r"\baccessed_at\b", c, flags=re.I)),
                None,
            )
            if col is None:
                i += 1
                continue
            i += 1
            if i < len(lines) and re.match(r"^\s*\|?\s*[-:| ]+\s*\|?\s*$", lines[i]):
                i += 1
            while i < len(lines) and "|" in lines[i]:
                row_cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if col < len(row_cells) and re.match(r"^\d{4}-\d{2}-\d{2}$", row_cells[col]):
                    table_hits += 1
                i += 1
            continue
        i += 1
    return colon_hits + table_hits


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
    auto_niche = is_auto_niche(context, text)
    if technical and len(github_urls) < 3:
        errors.append(f"technical topic requires GitHub evidence: github_urls={len(github_urls)} < 3")
    if technical and not official_doc_urls:
        warnings.append("technical topic has no obvious official docs/developer documentation URL")
    if auto_niche and not technical and len(github_urls) < 3:
        warnings.append(
            "auto/dealer niche: GitHub evidence optional; github_urls not required "
            f"(found {len(github_urls)})"
        )

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
            "auto_niche": auto_niche,
        },
    }


def run_self_test() -> int:
    """Lightweight regression checks for TECH_MARKERS and accessed_at counting."""
    failures: list[str] = []

    # Substring traps must NOT classify as technical
    fake_ctx = {
        "topic": {
            "h1": "Hyundai Santa Fe из Кореи: как выбрать комплектацию",
            "primary_query": "как выбрать комплектацию hyundai santa fe из кореи",
            "slug": "hyundai-santa-fe-iz-korei-komplektatsii-lovushki-2026",
            "search_intent": "how_to",
        }
    }
    notes = (
        "reader_pain: покупатель теряет деньги на комплектации\n"
        "reader_outcome: сможет проверить см³ до депозита\n"
    )
    if is_technical_topic(fake_ctx, notes):
        failures.append("Santa Fe / комплектации / reader_pain wrongly marked technical")
    if not is_auto_niche(fake_ctx, notes):
        failures.append("Santa Fe should be auto_niche")

    tech_ctx = {
        "topic": {
            "h1": "Как подключить MCP API к Cursor agent",
            "primary_query": "mcp api cursor agent",
            "slug": "mcp-api-cursor-agent",
            "search_intent": "how_to",
        }
    }
    if not is_technical_topic(tech_ctx, "github evidence for rag workflow"):
        failures.append("MCP/API/Cursor topic should be technical")

    table = """
| source | url | accessed_at | why |
| --- | --- | --- | --- |
| a | https://example.com/a | 2026-10-20 | x |
| b | https://example.com/b | 2026-10-20 | y |
| c | https://example.com/c | 2026-10-20 | z |
| d | https://example.com/d | 2026-10-20 | w |
| e | https://example.com/e | 2026-10-20 | v |
"""
    if count_accessed_at(table) < 5:
        failures.append(f"table accessed_at count expected >=5 got {count_accessed_at(table)}")

    colon_block = "\n".join(f"source_access_{i}: accessed_at: 2026-10-20" for i in range(5))
    if count_accessed_at(colon_block) < 5:
        failures.append(f"colon accessed_at count expected >=5 got {count_accessed_at(colon_block)}")

    if failures:
        for item in failures:
            print(f"SELF-TEST FAIL: {item}", file=sys.stderr)
        return 1
    print("Research Notes Gate self-test: PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate research-notes.md freshness and depth")
    ap.add_argument("--article-dir", type=Path, default=None)
    ap.add_argument("-o", "--output", type=Path, default=None)
    ap.add_argument("--self-test", action="store_true", help="Run TECH_MARKERS / accessed_at regressions")
    args = ap.parse_args()

    if args.self_test:
        return run_self_test()

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
