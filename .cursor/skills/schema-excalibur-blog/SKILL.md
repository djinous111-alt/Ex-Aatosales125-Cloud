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

## Secret-scan (обязательно)

- В `schema.jsonld` клади реальные публичные site/CTA URL (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) — они нужны для BlogPosting `@id`, `sameAs`, publisher.
- Secret-scan ≠ «не класть site URL». Если commit блокируется, на каждой строке с URL добавь `// pragma: allowlist secret` (JSONC).
- Publish стрипает pragma-trailer перед post meta; не убирай URL и не заменяй их на `[REDACTED]` в runtime schema до publish.
