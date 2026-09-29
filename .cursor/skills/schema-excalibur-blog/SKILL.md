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

## Git commit (Cloud)

`schema.jsonld` намеренно содержит абсолютные public site/catalog/social URLs. Перед commit:

```bash
EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 source scripts/sanitize_cloud_secret_names.sh
```

Это (1) чистит non-identifier names в `CLOUD_AGENT_INJECTED_SECRET_NAMES` и (2) временно убирает `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` из scanner list, чтобы hook не считал публичные href утечкой. Не используй `--no-verify`.
