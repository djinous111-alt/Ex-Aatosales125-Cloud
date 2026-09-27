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

## Secret-scan-safe JSON-LD (repo commit)

Cloud pre-commit secret-scan трактует значения `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` как secrets.

В **committed** `schema.jsonld`:
- page `@id` / `url` / `mainEntityOfPage` — relative (`/<slug>/` или `/blog/<slug>/`);
- `author.image` — relative path;
- `sameAs` / `publisher.url` — secret-scan-safe варианты (catalog без trailing slash, `telegram.me`, публичные соцсети), либо relative;
- не вставляй абсолютный host из env, если он совпадает с Cloud Secret.

Publish может абсолютизировать schema при выкладке в WP meta. Перед `git commit` при необходимости:
`export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(bash scripts/excalibur_blog_filter_secret_names.sh)"`

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
