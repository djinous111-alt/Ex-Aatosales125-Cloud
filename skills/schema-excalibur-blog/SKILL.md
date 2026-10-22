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


## Commit-safe URL pattern (обязательно)

Cloud secret-scan блокирует commit, если в `schema.jsonld` есть host из `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL`.

- В git коммить **root-relative** `@id` / `url` / `mainEntityOfPage` / `image`: `/<slug>/#blogposting`, `/cover/...`.
- `sameAs` автора — только публичные профили (Instagram, 2GIS, Wikidata и т.п.), не secret-scanned site URLs.
- Publish (`excalibur_blog_wp_publish.py`) **absolutize** root-relative IRIs в runtime payload перед записью WP meta; файл в git остаётся relative.
