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

## URL hygiene (git-safe)

- **Не коммить** абсолютные host URL из Cloud Secrets (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, `MAX_URL`, `CATALOG_URL` и т.п.) — pre-commit secrets scanner блокирует commit.
- В `schema.jsonld` используй плейсхолдеры `env:VAR` / `env:VAR/path` (как в `link-verify.json`).
- `excalibur_blog_wp_publish.py` расширяет `env:` из process env / `memory/site.env.local` **перед** записью `_excalibur_blog_schema_jsonld`.
- Публичные sameAs без секретов (например Instagram/2GIS) можно оставлять абсолютными; private sameAs — только через `env:`.
