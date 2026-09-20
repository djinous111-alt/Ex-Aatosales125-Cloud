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

## Secret-scan (commit)

`schema.jsonld` обязан содержать живые URL (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, `CATALOG_URL`, `sameAs`) — иначе JSON-LD на сайте сломан.

JSON не поддерживает HTML/JSONC comments. Для Cursor secret-scan ставь **same-line** маркер рядом с secret-bearing property:

```json
"url": "https://example.example/post/", "_excalibur_scan": "pragma: allowlist secret"
```

или на свёрнутом `sameAs` array. **Запрещено** добавлять `// pragma` строки (это ломает `application/ld+json`).

Publish (`excalibur_blog_wp_publish.py`) снимает ключи `_excalibur_scan` перед записью WP meta.
