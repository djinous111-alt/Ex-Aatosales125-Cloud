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

## Commit-safe redaction (обязательно)

Pre-commit secret-scan блокирует live `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` в staged файлах.

- В **закоммиченном** `schema.jsonld` пиши литерал `[REDACTED]` вместо этих base URL (как в PASS-схемах EV B01).
- Instagram / 2GIS и прочие публичные sameAs без secret-scan можно оставлять как есть.
- `excalibur_blog_wp_publish.py` вызывает `expand_schema_redacted()` при загрузке payload и подставляет live URL из env **только в WP meta**; диск остаётся redacted.
- Коммиты через `bash scripts/excalibur_git.sh …` — фильтрует невалидные имена в `CLOUD_AGENT_INJECTED_SECRET_NAMES`.

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
