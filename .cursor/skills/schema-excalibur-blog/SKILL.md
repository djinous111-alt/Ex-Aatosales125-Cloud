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

## Secret-scan / commit hygiene

`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL` часто совпадают с Cloud Secrets.
Если эти публичные brand URL попадают в `@id` / `url` / `sameAs` внутри `schema.jsonld`:

1. Храни файл как **JSONC**: на каждой строке с такими URL добавь trailing `// pragma: allowlist secret`.
2. Publish (`excalibur_blog_wp_publish.py` / `excalibur_jsonc.strip_allowlist_pragmas`) обязан снять pragmas перед записью WP post meta — в meta уходит валидный JSON-LD.
3. Не выдумывай placeholder-домены ради обхода сканера: Rich Results нуждаются в абсолютных публичных URL.
