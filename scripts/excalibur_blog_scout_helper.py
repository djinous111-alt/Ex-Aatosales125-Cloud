#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DENYLIST_PATH = Path("shared/wp-slug-denylist.json")


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_published_topics(root: Path) -> set[str]:
    ledger_path = root / "shared/published-articles.md"
    published = set()
    if not ledger_path.is_file():
        return published
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| 20"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 5 and cells[4].lower() in {"published", "in_progress", "draft_ready"}:
                published.add(cells[1].upper())
    return published


def load_active_article_topics(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = re.match(r"(B\d+)-", path.name, flags=re.IGNORECASE)
        if match:
            active.add(match.group(1).upper())
    return active


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in re.finditer(r"##\s+(B\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+B|\Z)", text, re.DOTALL):
        topic_id = match.group(1).upper()
        block = match.group(2)

        def field(name: str) -> str:
            m = re.search(rf"(?:-|\*)\s*\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            if not m:
                m = re.search(rf"\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            return m.group(1).strip() if m else ""

        topics.append(
            {
                "topic_id": topic_id,
                "primary_query": field("primary_query"),
                "slug": field("slug"),
                "priority": field("priority"),
            }
        )
    return topics


def normalize_and_tokenize(text: str) -> set[str]:
    text = text.lower()
    text = re.sub(r"[^\w\s\-]", " ", text)
    words = text.split()
    tokens = set()
    for w in words:
        w_clean = w.strip()
        if not w_clean or w_clean in {"в", "на", "и", "или", "с", "по", "для", "как", "что", "это"}:
            continue
        tokens.add(w_clean[:5] if len(w_clean) > 4 else w_clean)
    return tokens


def check_overlap(new_query: str, existing_topics: list[dict[str, str]], reserved_ids: set[str]) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    warnings = []

    for t in existing_topics:
        ext_tokens = normalize_and_tokenize(t["primary_query"])
        if not new_tokens or not ext_tokens:
            continue
        intersection = len(new_tokens.intersection(ext_tokens))
        union = len(new_tokens.union(ext_tokens))
        similarity = intersection / union

        status = "reserved" if t["topic_id"] in reserved_ids else "in_pool"

        if t["primary_query"].strip().lower() == new_query.strip().lower():
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "message": (
                        f"EXACT MATCH found with topic {t['topic_id']} ({status})! "
                        f"Primary query: '{t['primary_query']}'"
                    ),
                }
            )
        elif similarity >= 0.35:
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": t["topic_id"],
                    "similarity": round(similarity, 2),
                    "status": status,
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with topic "
                        f"{t['topic_id']} ({status}). Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def denylist_file(root: Path) -> Path:
    return root / DENYLIST_PATH


def load_denylist(root: Path) -> dict[str, Any]:
    path = denylist_file(root)
    if not path.is_file():
        return {
            "generated_at": "",
            "source": "missing",
            "count": 0,
            "slugs": [],
        }
    data = json.loads(path.read_text(encoding="utf-8"))
    slugs = data.get("slugs") or []
    if not isinstance(slugs, list):
        slugs = list(slugs)
    data["slugs"] = [str(s).strip().lower() for s in slugs if str(s).strip()]
    data["count"] = len(data["slugs"])
    return data


def save_denylist(root: Path, data: dict[str, Any]) -> Path:
    path = denylist_file(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    slugs = sorted({str(s).strip().lower() for s in (data.get("slugs") or []) if str(s).strip()})
    payload = {
        "generated_at": data.get("generated_at")
        or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": data.get("source") or "manual",
        "wp_total_reported": data.get("wp_total_reported", len(slugs)),
        "site_host_redacted": True,
        "count": len(slugs),
        "slugs": slugs,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def public_site_base() -> str:
    for key in ("PUBLIC_SITE_URL", "WP_SITE_URL", "WP_HOME"):
        value = (os.environ.get(key) or "").strip().rstrip("/")
        if value:
            return value
    return ""


def fetch_wp_slugs(site_base: str, *, per_page: int = 100, max_pages: int = 50) -> list[str]:
    if not site_base:
        raise RuntimeError("PUBLIC_SITE_URL/WP_SITE_URL required for --rebuild-denylist")
    slugs: list[str] = []
    page = 1
    while page <= max_pages:
        url = f"{site_base}/wp-json/wp/v2/posts?per_page={per_page}&page={page}&_fields=slug"
        req = urllib.request.Request(url, headers={"User-Agent": "ExcaliburBlogScoutHelper/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                chunk = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 400 and page > 1:
                break
            raise
        if not isinstance(chunk, list) or not chunk:
            break
        for item in chunk:
            slug = str((item or {}).get("slug") or "").strip().lower()
            if slug:
                slugs.append(slug)
        if len(chunk) < per_page:
            break
        page += 1
    return sorted(set(slugs))


def rebuild_denylist(root: Path) -> dict[str, Any]:
    site = public_site_base()
    slugs = fetch_wp_slugs(site)
    data = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "wp/v2/posts REST PUBLIC_SITE_URL (all pages per_page=100)",
        "wp_total_reported": len(slugs),
        "site_host_redacted": True,
        "slugs": slugs,
    }
    path = save_denylist(root, data)
    return {"path": str(path.relative_to(root)).replace("\\", "/"), "count": len(slugs)}


_FUZZY_STOP_TOKENS = {
    "2024",
    "2025",
    "2026",
    "avto",
    "auto",
    "iz",
    "kak",
    "dlya",
    "chto",
    "yaponii",
    "yaponiya",
    "yaponiya",
    "korei",
    "koreya",
    "kitaya",
    "kitaj",
    "rossii",
    "vladivostok",
    "komplektatsii",
    "lovushki",
    "gajd",
    "chek",
    "list",
}


def fuzzy_slug_hits(candidate: str, slugs: list[str], *, limit: int = 10) -> list[str]:
    """Fuzzy hits on distinctive model/brand tokens only (not iz-yaponii/2026)."""
    cand = candidate.strip().lower()
    if not cand:
        return []
    tokens = [
        t
        for t in re.split(r"[-_\s]+", cand)
        if len(t) >= 4 and t not in _FUZZY_STOP_TOKENS and not t.isdigit()
    ]
    hits: list[str] = []
    for slug in slugs:
        if slug == cand:
            hits.append(slug)
            continue
        # Substring only when candidate itself is short/distinctive.
        if len(cand) >= 12 and (cand in slug or slug in cand):
            hits.append(slug)
            continue
        if tokens and sum(1 for tok in tokens if tok in slug) >= max(1, min(2, len(tokens))):
            # Require ≥2 distinctive tokens when available (e.g. honda+vezel).
            needed = 2 if len(tokens) >= 2 else 1
            if sum(1 for tok in tokens if tok in slug) >= needed:
                hits.append(slug)
        if len(hits) >= limit:
            break
    return hits[:limit]


def check_slug(root: Path, slug: str, *, live_rest: bool = True) -> dict[str, Any]:
    cand = slug.strip().lower().strip("/")
    denylist = load_denylist(root)
    slugs = denylist.get("slugs") or []
    exact = cand in set(slugs)
    fuzzy = fuzzy_slug_hits(cand, slugs)
    live_empty: bool | None = None
    live_error = None
    if live_rest:
        site = public_site_base()
        if site:
            url = f"{site}/wp-json/wp/v2/posts?slug={urllib.parse.quote(cand)}&_fields=id,slug"
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "ExcaliburBlogScoutHelper/1.0"})
                with urllib.request.urlopen(req, timeout=20) as resp:
                    payload = json.loads(resp.read().decode("utf-8"))
                live_empty = isinstance(payload, list) and len(payload) == 0
            except Exception as exc:  # noqa: BLE001 — report soft failure to scout
                live_error = str(exc)[:200]
                live_empty = None
    blocked = exact or (live_empty is False)
    return {
        "slug": cand,
        "denylist_path": str(DENYLIST_PATH).replace("\\", "/"),
        "denylist_count": len(slugs),
        "exact_in_denylist": exact,
        "fuzzy_hits": fuzzy,
        "live_rest_empty": live_empty,
        "live_rest_error": live_error,
        "ok": (not blocked) and not exact,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--check-slug",
        type=str,
        default="",
        help="Check candidate WP slug against shared/wp-slug-denylist.json (+ optional live REST)",
    )
    ap.add_argument(
        "--rebuild-denylist",
        action="store_true",
        help="Rebuild shared/wp-slug-denylist.json from PUBLIC_SITE_URL wp/v2/posts",
    )
    ap.add_argument(
        "--live-slugs",
        action="store_true",
        help="Alias: rebuild denylist from LIVE WP REST (PUBLIC_SITE_URL); WP MCP is non-authoritative",
    )
    ap.add_argument(
        "--no-live-rest",
        action="store_true",
        help="With --check-slug: skip live ?slug= REST probe",
    )
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    reserved = published | active
    existing = load_existing_topics(root)

    if args.rebuild_denylist or args.live_slugs:
        try:
            result = rebuild_denylist(root)
        except Exception as exc:  # noqa: BLE001
            print(f"❌ DENYLIST REBUILD FAILED: {exc}", file=sys.stderr)
            return 2
        print("=== EXCALIBUR SCOUT HELPER ===")
        mode = "live-slugs" if args.live_slugs else "rebuild-denylist"
        print(f"Denylist rebuilt ({mode}): {result['path']} count={result['count']}")
        print("NOTE: LIVE REST denylist is authoritative; WP MCP post list is non-authoritative.")
        return 0

    if args.check_slug:
        report = check_slug(root, args.check_slug, live_rest=not args.no_live_rest)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report.get("exact_in_denylist") or report.get("live_rest_empty") is False:
            print("❌ SLUG BLOCKED: exact denylist hit or live WP slug already exists.", file=sys.stderr)
            return 1
        if report.get("fuzzy_hits"):
            print("⚠️ FUZZY SLUG HITS (review manually):", file=sys.stderr)
            for hit in report["fuzzy_hits"]:
                print(f"  - {hit}", file=sys.stderr)
        print("✅ SLUG OK: not in denylist exact match.")
        return 0

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        max_num = 0
        for t in existing:
            m = re.match(r"B(\d+)", t["topic_id"])
            if m:
                max_num = max(max_num, int(m.group(1)))

        next_id = f"B{max_num + 1:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        denylist = load_denylist(root)
        print(f"WP slug denylist: {denylist.get('count', 0)} slugs ({DENYLIST_PATH})")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | Topic: {w['topic_id']} ({w['status']})")
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
