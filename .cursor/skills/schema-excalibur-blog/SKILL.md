---
name: schema-excalibur-blog
description: Excalibur BLOG Schema — BlogPosting + FAQPage JSON-LD, автор из registry.
---

# Excalibur BLOG — Schema

## Вход

- `article.html`, `article.meta.json`, `research-notes.md`
- `shared/authors-registry.json`
- `memory/brief/site-brief.md` (site_url)

## Задача

1. BlogPosting: headline, datePublished (today из research-context), author Person + sameAs.
2. FAQPage из FAQ секции статьи.
3. HowTo / Review — только если архетип требует.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).

## Commit hygiene — `[REDACTED]` URL bases

Secret-scanned envs (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) must not appear as live hosts in committed `schema.jsonld`.

1. Build schema with real env URLs for validation.
2. Before `git commit`, replace those bases with `[REDACTED]` (keep public Instagram/2GIS etc. if not secret-scanned).
3. Publish expands via `expand_schema_redacted` in `excalibur_blog_wp_publish.py` before WP schema meta.

Commits: `bash scripts/excalibur_git.sh commit …`.
