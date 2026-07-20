#!/usr/bin/env python3
"""Build commit-safe schema.jsonld for Excalibur BLOG articles.

Writes BlogPosting + FAQPage (+ HowTo for article_mode B) using article HTML/meta
and shared/authors-registry.json. Secret site/CTA URL bases are stored as
[REDACTED] placeholders; publish reinjects via excalibur_blog_cta_urls.py.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html import unescape
from pathlib import Path
from typing import Any
from urllib.parse import quote

from excalibur_blog_cta_urls import PLACEHOLDER, load_cta_env, redact_text, reinject_text


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def strip_tags(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def slugify_heading(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-а-яё]", "", text, flags=re.I)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-") or "section"


def extract_faq(html: str) -> list[dict[str, str]]:
    faq: list[dict[str, str]] = []
    # FAQ section: H2 Частые вопросы … until next H2 or end
    m = re.search(
        r"<h2[^>]*>\s*Частые вопросы\s*</h2>(.*?)(?=<h2\b|\Z)",
        html,
        flags=re.I | re.S,
    )
    if not m:
        return faq
    block = m.group(1)
    for qm in re.finditer(
        r"<h3[^>]*>(.*?)</h3>\s*(?:<p[^>]*>(.*?)</p>)",
        block,
        flags=re.I | re.S,
    ):
        question = strip_tags(qm.group(1))
        answer = strip_tags(qm.group(2))
        if question and answer:
            faq.append({"question": question, "answer": answer})
    return faq


def extract_howto_steps(html: str) -> list[dict[str, str]]:
    steps: list[dict[str, str]] = []
    # Prefer ordered list items near workflow; fallback: H2 titles with verbs
    for om in re.finditer(r"<ol[^>]*>(.*?)</ol>", html, flags=re.I | re.S):
        items = re.findall(r"<li[^>]*>(.*?)</li>", om.group(1), flags=re.I | re.S)
        if len(items) >= 5:
            for idx, item in enumerate(items, start=1):
                name = strip_tags(item)
                if name:
                    steps.append({"name": name, "text": name, "position": str(idx)})
            return steps
    for hm in re.finditer(r"<h2[^>]*>(.*?)</h2>", html, flags=re.I | re.S):
        name = strip_tags(hm.group(1))
        if name and name.lower() not in {"частые вопросы", "faq"}:
            steps.append({"name": name, "text": name, "position": str(len(steps) + 1)})
    return steps[:9]


def author_from_registry(root: Path, author_id: str) -> dict[str, Any]:
    registry = load_json(root / "shared/authors-registry.json")
    for author in registry.get("authors") or []:
        if str(author.get("id") or "") == author_id:
            return author
    authors = registry.get("authors") or []
    if not authors:
        raise ValueError("authors-registry.json has no authors")
    return authors[0]


def build_schema(
    article_dir: Path,
    root: Path,
    *,
    live_urls: bool = False,
) -> dict[str, Any]:
    meta = load_json(article_dir / "article.meta.json")
    html = (article_dir / "article.html").read_text(encoding="utf-8")
    context_path = article_dir / "research-context.json"
    today = ""
    if context_path.is_file():
        ctx = load_json(context_path)
        today = str((ctx.get("date_context") or {}).get("today_iso") or "")
    if not today:
        today = str(meta.get("publish_date") or meta.get("date") or "")

    slug = str(meta.get("slug") or article_dir.name)
    headline = str(meta.get("h1") or meta.get("title") or slug)
    description = str(
        meta.get("description")
        or (meta.get("meta_ab") or {}).get("description_aeo")
        or (meta.get("meta_ab") or {}).get("description_seo")
        or ""
    )
    author_id = str(meta.get("author_id") or "avtosales-editorial")
    author = author_from_registry(root, author_id)
    site_base = PLACEHOLDER
    page_id = f"{site_base}/{slug}/"
    keywords = []
    if meta.get("primary_query"):
        keywords.append(str(meta["primary_query"]))
    for q in meta.get("secondary_queries") or []:
        keywords.append(str(q))

    author_node = {
        "@type": "Person",
        "@id": f"{site_base}/#author-{author_id}",
        "name": author.get("name_ru") or author.get("name_en") or author_id,
        "jobTitle": author.get("job_title_ru") or author.get("job_title_en") or "",
        "description": author.get("bio_short_ru") or author.get("bio_long_ru") or "",
        "image": author.get("avatar_url") or f"{site_base}/",
        "worksFor": {
            "@type": "Organization",
            "name": "Авто-Сейлс",
            "alternateName": "AVTO SALES",
            "url": f"{site_base}/",
        },
        "sameAs": list(author.get("sameAs") or []),
    }

    blog_posting: dict[str, Any] = {
        "@type": "BlogPosting",
        "@id": f"{page_id}#blogposting",
        "mainEntityOfPage": {"@type": "WebPage", "@id": page_id},
        "headline": headline,
        "description": description,
        "datePublished": today,
        "dateModified": today,
        "inLanguage": "ru-RU",
        "image": "cover/cover.png",
        "author": author_node,
        "publisher": {
            "@type": "Organization",
            "@id": f"{site_base}/#organization",
            "name": "Авто-Сейлс",
            "alternateName": "AVTO SALES",
            "url": f"{site_base}/",
            "sameAs": [f"{site_base}/", typed_or_plain_catalog()],
        },
        "keywords": keywords,
    }

    graph: list[dict[str, Any]] = [blog_posting]

    faq_items = extract_faq(html)
    if faq_items:
        graph.append(
            {
                "@type": "FAQPage",
                "@id": f"{page_id}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item["question"],
                        "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                    }
                    for item in faq_items
                ],
            }
        )

    mode = str(meta.get("article_mode") or "").upper()
    if mode == "B":
        steps = extract_howto_steps(html)
        howto_steps = []
        for step in steps:
            anchor = slugify_heading(step["name"])
            howto_steps.append(
                {
                    "@type": "HowToStep",
                    "position": int(step["position"]),
                    "name": step["name"],
                    "text": step["text"],
                    "url": f"{page_id}#{quote(anchor)}",
                }
            )
        if howto_steps:
            graph.append(
                {
                    "@type": "HowTo",
                    "@id": f"{page_id}#howto",
                    "name": headline,
                    "description": description,
                    "step": howto_steps,
                }
            )

    payload = {"@context": "https://schema.org", "@graph": graph}
    raw = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    env = load_cta_env(root)
    # Always normalize any accidental live URLs to placeholders for git
    raw = redact_text(raw, env)
    if live_urls:
        raw = reinject_text(raw, env)
        return json.loads(raw)
    return json.loads(raw)


def typed_or_plain_catalog() -> str:
    return PLACEHOLDER


def main() -> int:
    ap = argparse.ArgumentParser(description="Write schema.jsonld for an article")
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=None, help="Defaults to <article-dir>/schema.jsonld")
    ap.add_argument(
        "--live-urls",
        action="store_true",
        help="Reinject env URLs (for publish dry-run only; do not commit)",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    if not (article_dir / "article.html").is_file() or not (article_dir / "article.meta.json").is_file():
        print("article.html and article.meta.json required", file=sys.stderr)
        return 2

    schema = build_schema(article_dir, root, live_urls=args.live_urls)
    out = args.out
    if out is None:
        out = article_dir / "schema.jsonld"
    elif not out.is_absolute():
        out = root / out if len(out.parts) > 1 else article_dir / out

    text = json.dumps(schema, ensure_ascii=False, indent=2) + "\n"
    if args.dry_run:
        print(text)
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    try:
        rel = out.relative_to(root).as_posix()
    except ValueError:
        rel = str(out)
    print(f"Wrote {rel} graph_nodes={len(schema.get('@graph') or [])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
