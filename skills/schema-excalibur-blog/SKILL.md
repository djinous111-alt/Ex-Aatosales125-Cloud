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

## Secret-scan / public marketing URLs

`PUBLIC_SITE_URL`, `CATALOG_URL`, Telegram/MAX и `sameAs` из `authors-registry` — **публичные** marketing URLs, но Cloud secret-scan часто считает их секретами.

Перед commit `schema.jsonld`:

1. На каждой строке с абсолютным URL сайта/каталога/Telegram/MAX добавь trailing comment / sibling key с `pragma: allowlist secret` (тот же паттерн, что принимает pre-commit hook).
2. Либо пиши relative/redacted URLs в git и раскрывай absolute base только на publish.
3. Перед git commit: `source scripts/excalibur_blog_filter_injected_secret_names.sh` — в `CLOUD_AGENT_INJECTED_SECRET_NAMES` должны остаться только валидные shell identifiers (не URL).
