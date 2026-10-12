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

Fragment для Директора: `.cursor/excalibur-blog-fragments/schema.md`.
Путь gitignored — Cursor Write может вернуть success без файла на диске.
Пиши через `python3 scripts/excalibur_blog_write_fragment.py --name schema.md ...` (или shell redirect) и сразу `test -f`.

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
