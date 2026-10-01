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

## Pre-commit / publish placeholders

- Если Cloud secret-scanner блокирует `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` в `schema.jsonld`, на таких строках допустим trailing `// pragma: allowlist secret`.
- Альтернатива для commit-safe файла: host `[REDACTED]` или `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` placeholders.
- `excalibur_blog_wp_publish.py` `load_article()` снимает pragma-комментарии и раскрывает `${…}` / `[REDACTED]` из env **только в publish payload** — committed schema может оставаться redacted.
