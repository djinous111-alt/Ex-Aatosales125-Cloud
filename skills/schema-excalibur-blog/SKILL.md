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

### Secret-scan safe URLs (обязательно)

В **committed** `schema.jsonld` не вшивай абсолютные site/CTA URL из env:

- `${PUBLIC_SITE_URL}` / `env:PUBLIC_SITE_URL` (+ path suffix ok)
- `${CATALOG_URL}`, `${TELEGRAM_URL}`, `${MAX_URL}`

Публичные Instagram/2GIS можно оставлять как есть.  
`excalibur_blog_wp_publish.py` расширяет placeholders **in-memory** перед WP meta; на диск placeholders не перезаписывать.

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
