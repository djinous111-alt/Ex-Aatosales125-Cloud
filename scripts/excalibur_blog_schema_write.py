#!/usr/bin/env python3
"""Write schema.jsonld for one Excalibur BLOG article (durable Schema helper).

Decodes Cloud Secret site URLs that may arrive as unicode-escaped JSON strings,
loads author from shared/authors-registry.json, FAQ from article.html, and
optionally HowTo for article_mode B.
"""
from __future__ import annotations

import argparse
import codecs
import json
import os
import re
import sys
from html import unescape
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

from excalibur_repo_paths import repo_relative


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def decode_site_url(raw: str) -> str:
    """Normalize PUBLIC_SITE_URL from env / Cloud Secrets (unicode_escape safe)."""
    value = (raw or "").strip().strip('"').strip("'")
    if not value:
        return ""
    if "\\u" in value:
        try:
            value = codecs.decode(value, "unicode_escape")
        except Exception:  # noqa: BLE001
            pass
    value = value.strip()
    if value and not value.startswith(("http://", "https://")):
        value = "https://" + value.lstrip("/")
    return value.rstrip("/") + "/" if value else ""


def resolve_site_base(root: Path, override: str = "") -> str:
    if override.strip():
        return decode_site_url(override)
    for key in ("PUBLIC_SITE_URL", "WP_SITE_URL", "WP_HOME"):
        env_val = os.environ.get(key, "")
        decoded = decode_site_url(env_val)
        if decoded:
            return decoded
    brief = root / "memory/brief/site-brief.md"
    if brief.is_file():
        text = brief.read_text(encoding="utf-8")
        m = re.search(r"\*\*site_url:\*\*\s*(\S+)", text)
        if m:
            return decode_site_url(m.group(1))
    return ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def strip_tags(html: str) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def extract_faq(html: str) -> list[dict[str, str]]:
    """Parse FAQ h3 + following paragraph(s) until next h2/h3."""
    # Find FAQ section heading
    faq_match = re.search(
        r"<h2[^>]*>\s*(?:Частые вопросы|FAQ|Часто задаваемые вопросы)[^<]*</h2>([\s\S]*)",
        html,
        flags=re.I,
    )
    section = faq_match.group(1) if faq_match else html
    # Stop at next h2 if present after FAQ
    stop = re.search(r"<h2\b", section, flags=re.I)
    if stop and faq_match:
        section = section[: stop.start()]

    items: list[dict[str, str]] = []
    for m in re.finditer(
        r"<h3[^>]*>([\s\S]*?)</h3>([\s\S]*?)(?=<h3\b|<h2\b|\Z)",
        section,
        flags=re.I,
    ):
        question = strip_tags(m.group(1))
        answer = strip_tags(m.group(2))
        if question and answer:
            items.append({"question": question, "answer": answer})
    return items


def extract_howto_steps(html: str) -> list[dict[str, str]]:
    """H2 sections before FAQ become HowTo steps for mode B."""
    steps: list[dict[str, str]] = []
    parts = re.split(r"(?=<h2\b)", html, flags=re.I)
    for part in parts:
        hm = re.match(r"<h2[^>]*>([\s\S]*?)</h2>([\s\S]*)", part, flags=re.I)
        if not hm:
            continue
        name = strip_tags(hm.group(1))
        if re.search(r"частые вопросы|faq|что дальше", name, flags=re.I):
            continue
        body = strip_tags(hm.group(2))
        if not name or not body:
            continue
        steps.append({"name": name, "text": body[:500]})
    return steps


def find_author(registry: dict[str, Any], author_id: str) -> dict[str, Any]:
    for author in registry.get("authors") or []:
        if str(author.get("id") or "") == author_id:
            return author
    authors = registry.get("authors") or []
    if authors:
        return authors[0]
    return {}


def research_date(article_dir: Path) -> str:
    ctx_path = article_dir / "research-context.json"
    if ctx_path.is_file():
        ctx = load_json(ctx_path)
        date_ctx = ctx.get("date_context") or {}
        for key in ("today_iso", "research_date"):
            value = str(date_ctx.get(key) or ctx.get(key) or "").strip()
            if re.match(r"\d{4}-\d{2}-\d{2}$", value):
                return value
    return ""


def build_schema(
    *,
    meta: dict[str, Any],
    author: dict[str, Any],
    site_base: str,
    faq: list[dict[str, str]],
    howto_steps: list[dict[str, str]],
    date_published: str,
) -> dict[str, Any]:
    slug = str(meta.get("slug") or "").strip()
    page_url = urljoin(site_base, f"{slug}/") if site_base and slug else ""
    author_id = str(meta.get("author_id") or author.get("id") or "author")
    author_name = str(author.get("name_ru") or author.get("name") or "Author")
    org_name = "Авто-Сейлс"
    org_alt = "AVTO SALES"

    blog_posting: dict[str, Any] = {
        "@type": "BlogPosting",
        "@id": f"{page_url}#blogposting" if page_url else "#blogposting",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": page_url or "#webpage",
        },
        "headline": meta.get("h1") or meta.get("title") or "",
        "description": meta.get("description") or "",
        "datePublished": date_published,
        "dateModified": date_published,
        "inLanguage": "ru-RU",
        "image": "cover/cover.png",
        "author": {
            "@type": "Person",
            "@id": f"{site_base}#author-{author_id}" if site_base else f"#author-{author_id}",
            "name": author_name,
            "jobTitle": author.get("job_title_ru") or author.get("job_title") or "",
            "description": author.get("bio_short_ru") or author.get("bio") or "",
            "image": author.get("avatar_url") or "",
            "worksFor": {
                "@type": "Organization",
                "name": org_name,
                "alternateName": org_alt,
                "url": site_base or "",
            },
            "sameAs": list(author.get("sameAs") or []),
        },
        "publisher": {
            "@type": "Organization",
            "@id": f"{site_base}#organization" if site_base else "#organization",
            "name": org_name,
            "alternateName": org_alt,
            "url": site_base or "",
            "sameAs": [site_base] if site_base else [],
        },
        "keywords": list(meta.get("secondary_queries") or [])[:8]
        or ([meta.get("primary_query")] if meta.get("primary_query") else []),
    }
    if meta.get("primary_query") and meta["primary_query"] not in (blog_posting.get("keywords") or []):
        blog_posting["keywords"] = [meta["primary_query"], *(blog_posting.get("keywords") or [])]

    graph: list[dict[str, Any]] = [blog_posting]

    if faq:
        graph.append(
            {
                "@type": "FAQPage",
                "@id": f"{page_url}#faq" if page_url else "#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item["question"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": item["answer"],
                        },
                    }
                    for item in faq
                ],
            }
        )

    mode = str(meta.get("article_mode") or "").upper()
    if mode == "B" and howto_steps:
        graph.append(
            {
                "@type": "HowTo",
                "@id": f"{page_url}#howto" if page_url else "#howto",
                "name": meta.get("h1") or meta.get("title") or "",
                "description": meta.get("description") or "",
                "step": [
                    {
                        "@type": "HowToStep",
                        "position": idx,
                        "name": step["name"],
                        "text": step["text"],
                        "url": f"{page_url}#step-{idx}" if page_url else f"#step-{idx}",
                    }
                    for idx, step in enumerate(howto_steps, start=1)
                ],
            }
        )

    return {"@context": "https://schema.org", "@graph": graph}


def write_schema(article_dir: Path, site_base: str, root: Path) -> dict[str, Any]:
    meta_path = article_dir / "article.meta.json"
    html_path = article_dir / "article.html"
    registry_path = root / "shared/authors-registry.json"
    if not meta_path.is_file():
        raise FileNotFoundError(f"missing {meta_path}")
    if not html_path.is_file():
        raise FileNotFoundError(f"missing {html_path}")

    meta = load_json(meta_path)
    html = html_path.read_text(encoding="utf-8")
    registry = load_json(registry_path) if registry_path.is_file() else {"authors": []}
    author = find_author(registry, str(meta.get("author_id") or ""))
    faq = extract_faq(html)
    howto = extract_howto_steps(html)
    date_published = research_date(article_dir)
    if not date_published:
        from datetime import date

        date_published = date.today().isoformat()

    schema = build_schema(
        meta=meta,
        author=author,
        site_base=site_base,
        faq=faq,
        howto_steps=howto,
        date_published=date_published,
    )
    out = article_dir / "schema.jsonld"
    out.write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    types = [node.get("@type") for node in schema.get("@graph") or []]
    return {
        "schema_path": repo_relative(out, root),
        "site_base_configured": bool(site_base),
        "faq_count": len(faq),
        "howto_steps": len(howto),
        "types": types,
        "author_id": meta.get("author_id"),
        "datePublished": date_published,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Write schema.jsonld for an Excalibur BLOG article")
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("--site-base", default="", help="Override PUBLIC_SITE_URL (unicode_escape safe)")
    ap.add_argument("--dry-run", action="store_true", help="Print summary JSON without writing")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    site_base = resolve_site_base(root, args.site_base)

    if args.dry_run:
        meta = load_json(article_dir / "article.meta.json")
        html = (article_dir / "article.html").read_text(encoding="utf-8")
        report = {
            "dry_run": True,
            "article_dir": repo_relative(article_dir, root),
            "site_base_configured": bool(site_base),
            "faq_count": len(extract_faq(html)),
            "howto_steps": len(extract_howto_steps(html)),
            "author_id": meta.get("author_id"),
            "datePublished": research_date(article_dir) or "today",
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    report = write_schema(article_dir, site_base, root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"OK schema written: {report['schema_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
