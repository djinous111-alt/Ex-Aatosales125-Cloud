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

## Commit-safe JSON-LD

- Для git: в `schema.jsonld` используй плейсхолдеры `${PUBLIC_SITE_URL}`, `${CATALOG_URL}`, `${TELEGRAM_URL}` в `@id` / `url` / `sameAs` вместо реальных secret-scanned URL.
- Runtime/publish: `excalibur_blog_wp_publish.py` расширяет плейсхолдеры из env / `site.env.local` перед записью post meta.
- Если secret-scan блокирует commit — не коммить schema с абсолютными marketing URL; оставь валидный runtime файл на диске для publish и зафиксируй incident.
- Pre-commit `invalid variable name`: используй `scripts/excalibur_git.sh` (фильтр `CLOUD_AGENT_INJECTED_SECRET_NAMES`).
