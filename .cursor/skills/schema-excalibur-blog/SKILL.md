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

## Commit / Cloud secrets

- JSON-LD **обязан** содержать абсолютные public site/author URLs (`PUBLIC_SITE_URL`, catalog/Telegram/MAX из `sameAs` автора).
- Перед commit schema/llms:
  ```bash
  EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 source scripts/sanitize_cloud_secret_names.sh
  ```
- Dashboard: secret **names** только valid bash identifiers (`[A-Za-z_][A-Za-z0-9_]*`). Не инжектить raw URL как имя секрета.
- Предпочтительно не хранить уже публичные marketing URL как commit-blocking secrets.
