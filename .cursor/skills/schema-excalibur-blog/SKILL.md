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

## Commit-safe URL placeholders (обязательно)

Cloud secret-scan блокирует commit `schema.jsonld` с живыми `PUBLIC_SITE_URL` / CTA host strings.

В коммитимом `schema.jsonld` используй токены:

| Поле | Commit-safe значение |
|------|----------------------|
| `@id` / `url` / `mainEntityOfPage` site base | `env:PUBLIC_SITE_URL` |
| CTA catalog | `env:CATALOG_URL` |
| Telegram | `env:TELEGRAM_URL` |
| Max | `env:MAX_URL` |

Публичные non-secret URL (Instagram, 2GIS и т.п.) можно оставлять абсолютными.

`excalibur_blog_wp_publish.py` **гидратирует** `env:NAME` и `${NAME}` из publish env **в памяти** перед SSH upload — не пиши live URL обратно в git.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
