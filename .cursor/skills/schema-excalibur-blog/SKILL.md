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

## Secret scanner (git commit)

Строки с `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` из env и `sameAs` реестра блокируют commit.
На **той же строке**, что и URL, добавь хвост:

```text
 // pragma: allowlist secret
```

Файл станет JSONC: publish (`excalibur_blog_wp_publish.py`) снимает эти маркеры перед записью WP meta.
Instagram/2GIS без env-секретов pragma не требуют.
