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

## Commit hygiene (Cloud Secrets)

Committed `schema.jsonld` **must** use `${ENV}` placeholders for site/social URLs that are Cloud Secrets:

- `${PUBLIC_SITE_URL}` — BlogPosting `url` / `image` / `mainEntityOfPage`
- `${CATALOG_URL}`, `${TELEGRAM_URL}`, `${MAX_URL}` — Organization/`sameAs` site channels

Do **not** embed live `PUBLIC_SITE_URL` host values (secret scanner + pre-commit). Public Instagram/2GIS author links from registry may stay absolute.

Publish (`excalibur_blog_wp_publish.py`) hydrates `${…}` in-memory into the WP payload and does **not** rewrite the committed schema file.
