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

## Cloud pre-commit / secret scan

Absolute URLs из Cloud Secrets (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) в `BlogPosting` / `sameAs` / HowTo **нужны по контракту**, но Cursor secret-scan блокирует commit без маркера.

На **каждой** JSON-строке, где есть такой URL, добавь same-line marker через служебный ключ, например:

```json
"url": "https://example.example/post/",
"x-excalibur-pragma": "pragma: allowlist secret"
```

Тот же текст маркера, что и HTML `<!-- pragma: allowlist secret -->`.

**Предпочтительно для git-артефактов:** site base / `@id` / author `sameAs` из Cloud Secrets → `[REDACTED]` (AS08/AS09 pattern); публичные Instagram/2GIS и т.п. можно оставить. Publish/runtime раскрывает `PUBLIC_SITE_URL`. Не коммить live secret URL values без pragma.
