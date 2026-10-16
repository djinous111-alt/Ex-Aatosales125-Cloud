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

## Commit / secrets

- `schema.jsonld` **может** содержать абсолютные public brand URLs (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, `CATALOG_URL`, `MAX_URL`, …) для BlogPosting `@id` / author `sameAs`.
- Перед commit: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` — скрипт оставляет только valid bash identifiers и **опускает** public CTA URL secret names из `CLOUD_AGENT_INJECTED_SECRET_NAMES`.
- Не клади URL-значения в список имён секретов Cloud Dashboard.
