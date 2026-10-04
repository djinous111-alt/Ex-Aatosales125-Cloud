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

## Redact-for-git / restore-for-publish

- В коммите `schema.jsonld` site/brand URL → `[REDACTED]` / `[PUBLIC_SITE_URL]` / `[CATALOG_URL]` (JSON-LD нельзя пометить `pragma: allowlist secret`).
- Перед publish скрипт `excalibur_blog_wp_publish.py` сам expand placeholders из env.
- Перед commit: `source scripts/sanitize_cloud_secret_names.sh` или `bash scripts/excalibur_git.sh commit ...`.
