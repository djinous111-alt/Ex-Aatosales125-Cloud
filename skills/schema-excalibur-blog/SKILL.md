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

## Secret scan / URL fields

Если `@id`, `url`, `sameAs` (или другие URL) равны значениям Cloud Secrets
(`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`, `WP_SITE_URL`):

1. На **той же строке** JSON добавь соседний ключ-маркер:
   `"_a": "pragma: allowlist secret"` (имя ключа может быть `_a` / `_b` … — consumers игнорируют unknown keys).
2. Коммить через `bash scripts/excalibur_git.sh` (фильтрует public CTA names из secret-scan list).
3. Не вставляй raw secret **names that are URL values** в `CLOUD_AGENT_INJECTED_SECRET_NAMES` — только валидные bash identifiers env-имён.
