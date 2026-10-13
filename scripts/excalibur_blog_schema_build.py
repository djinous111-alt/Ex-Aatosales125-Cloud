#!/usr/bin/env python3
"""Build or expand Excalibur BLOG schema.jsonld with git-safe placeholders."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from excalibur_repo_paths import repo_relative



def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _read_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def load_env(root: Path) -> dict[str, str]:
    env = _read_env_file(root / "memory/site.env.local")
    for key in (
        "PUBLIC_SITE_URL",
        "WP_SITE_URL",
        "WP_HOME",
        "CATALOG_URL",
        "TELEGRAM_URL",
        "MAX_URL",
    ):
        value = os.environ.get(key)
        if value:
            env[key] = value
    if not env.get("PUBLIC_SITE_URL"):
        env["PUBLIC_SITE_URL"] = env.get("WP_SITE_URL") or env.get("WP_HOME") or ""
    return env


def expand_placeholders(text: str, env: dict[str, str]) -> str:
    mapping = {
        "[PUBLIC_SITE_URL]": (env.get("PUBLIC_SITE_URL") or "").rstrip("/"),
        "[CATALOG_URL]": (env.get("CATALOG_URL") or "").rstrip("/"),
        "[TELEGRAM_URL]": (env.get("TELEGRAM_URL") or "").rstrip("/"),
        "[MAX_URL]": (env.get("MAX_URL") or "").rstrip("/"),
        "[REDACTED]": (env.get("PUBLIC_SITE_URL") or "").rstrip("/"),
    }
    out = text
    for needle, value in mapping.items():
        if value:
            out = out.replace(needle, value)
    return out


def to_placeholders(text: str, env: dict[str, str]) -> str:
    """Replace absolute env URLs with git-safe placeholders (reverse of expand)."""
    pairs = [
        ("PUBLIC_SITE_URL", "[PUBLIC_SITE_URL]"),
        ("WP_SITE_URL", "[PUBLIC_SITE_URL]"),
        ("WP_HOME", "[PUBLIC_SITE_URL]"),
        ("CATALOG_URL", "[CATALOG_URL]"),
        ("TELEGRAM_URL", "[TELEGRAM_URL]"),
        ("MAX_URL", "[MAX_URL]"),
    ]
    out = text
    for key, placeholder in pairs:
        raw = (env.get(key) or "").strip().rstrip("/")
        if raw:
            out = out.replace(raw + "/", placeholder + "/")
            out = out.replace(raw, placeholder)
    return out


def extract_faq(html: str) -> list[dict[str, str]]:
    faqs: list[dict[str, str]] = []
    # Simple FAQ extraction: <h3>Q</h3><p>A</p> inside FAQ section if present.
    section = html
    m = re.search(r"<h2[^>]*>\s*Frequently asked|Частые вопросы|FAQ", html, flags=re.I)
    if m:
        section = html[m.start() :]
    for qm, am in re.findall(
        r"<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>",
        section,
        flags=re.I | re.S,
    ):
        q = re.sub(r"<[^>]+>", "", qm).strip()
        a = re.sub(r"<[^>]+>", "", am).strip()
        if q and a:
            faqs.append({"q": q, "a": a})
    return faqs[:12]


def build_schema(article_dir: Path, root: Path, *, placeholders: bool = True) -> dict[str, Any]:
    meta = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    html = (article_dir / "article.html").read_text(encoding="utf-8")
    registry = json.loads((root / "shared/authors-registry.json").read_text(encoding="utf-8"))
    author_id = meta.get("author_id") or "avtosales-editorial"
    author = next((a for a in registry.get("authors") or [] if a.get("id") == author_id), None)
    if not author:
        raise ValueError(f"author_id={author_id} not found in authors-registry.json")

    site = "[PUBLIC_SITE_URL]" if placeholders else (load_env(root).get("PUBLIC_SITE_URL") or "").rstrip("/")
    slug = meta["slug"]
    date = meta.get("date_published") or meta.get("date") or ""
    ctx_path = article_dir / "research-context.json"
    if not date and ctx_path.is_file():
        ctx = json.loads(ctx_path.read_text(encoding="utf-8"))
        date = ((ctx.get("date_context") or {}).get("today_iso")) or ""
    if not date or len(date) < 10:
        date = "1970-01-01"
    y, mth, day = date[:10].split("-")
    permalink = f"{site}/{y}/{mth}/{day}/{slug}/"

    same_as = [str(x) for x in (author.get("sameAs") or [])]
    if placeholders:
        same_as = [to_placeholders(x, load_env(root)).replace("[REDACTED]", "[PUBLIC_SITE_URL]") for x in same_as]
    avatar = author.get("avatar_url") or ""
    if placeholders:
        avatar = to_placeholders(str(avatar), load_env(root)).replace("[REDACTED]", "[PUBLIC_SITE_URL]")

    faqs = extract_faq(html)
    graph: list[dict[str, Any]] = [
        {
            "@type": "BlogPosting",
            "@id": f"{permalink}#blogposting",
            "mainEntityOfPage": {"@type": "WebPage", "@id": permalink},
            "headline": meta.get("h1") or meta.get("title") or slug,
            "description": meta.get("description") or "",
            "datePublished": date[:10],
            "dateModified": date[:10],
            "inLanguage": "ru-RU",
            "image": "cover/cover.png",
            "author": {
                "@type": "Person",
                "@id": f"{site}/#author-{author_id}",
                "name": author.get("name_ru") or author.get("name_en") or author_id,
                "jobTitle": author.get("job_title_ru") or "",
                "description": author.get("bio_short_ru") or "",
                "image": avatar,
                "worksFor": {
                    "@type": "Organization",
                    "name": "Авто-Сейлс",
                    "alternateName": "AVTO SALES",
                    "url": f"{site}/",
                },
                "sameAs": same_as,
            },
            "publisher": {
                "@type": "Organization",
                "@id": f"{site}/#organization",
                "name": "Авто-Сейлс",
                "alternateName": "AVTO SALES",
                "url": f"{site}/",
            },
            "keywords": [meta.get("primary_query") or ""]
            + list(meta.get("secondary_queries") or [])[:5],
        }
    ]
    if faqs:
        graph.append(
            {
                "@type": "FAQPage",
                "@id": f"{permalink}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item["q"],
                        "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
                    }
                    for item in faqs
                ],
            }
        )
    return {"@context": "https://schema.org", "@graph": graph}


def main() -> int:
    ap = argparse.ArgumentParser(description="Build/expand schema.jsonld with placeholders or env URLs")
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument(
        "--placeholders",
        action="store_true",
        help="Write/keep git-safe placeholders (default when building)",
    )
    ap.add_argument(
        "--expand-env",
        action="store_true",
        help="Expand [PUBLIC_SITE_URL]/[CATALOG_URL]/... from env/site.env.local",
    )
    ap.add_argument(
        "--write",
        action="store_true",
        help="Write schema.jsonld (otherwise print to stdout)",
    )
    ap.add_argument(
        "--in-place",
        action="store_true",
        help="With --expand-env/--placeholders: transform existing schema.jsonld",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    schema_path = article_dir / "schema.jsonld"
    env = load_env(root)

    if args.expand_env and args.placeholders:
        print("Use only one of --expand-env or --placeholders", file=sys.stderr)
        return 2

    if args.in_place or (args.expand_env and schema_path.is_file() and not args.placeholders):
        if not schema_path.is_file():
            print(f"schema.jsonld not found: {schema_path}", file=sys.stderr)
            return 1
        raw = schema_path.read_text(encoding="utf-8")
        if args.expand_env:
            out = expand_placeholders(raw, env)
            if "[PUBLIC_SITE_URL]" in out and not (env.get("PUBLIC_SITE_URL") or "").strip():
                print("WARN: PUBLIC_SITE_URL not set; placeholder left in schema", file=sys.stderr)
        else:
            out = to_placeholders(raw, env)
        if args.write:
            schema_path.write_text(out if out.endswith("\n") else out + "\n", encoding="utf-8")
            print(f"OK schema={repo_relative(schema_path, root)} mode={'expand-env' if args.expand_env else 'placeholders'}")
            return 0
        print(out, end="" if out.endswith("\n") else "\n")
        return 0

    # Build fresh schema with placeholders by default (git-safe).
    use_placeholders = args.placeholders or not args.expand_env
    data = build_schema(article_dir, root, placeholders=use_placeholders)
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if args.expand_env:
        text = expand_placeholders(text, env)
    if args.write:
        schema_path.write_text(text, encoding="utf-8")
        print(f"OK schema={repo_relative(schema_path, root)} mode={'placeholders' if use_placeholders and not args.expand_env else 'expand-env'}")
        return 0
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
