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

## Commit / secret scan

Live `PUBLIC_SITE_URL` / catalog / Telegram / MAX в JSON-LD нужны publish post meta, но Cloud secret-scan блокирует commit. Перед `git commit`:

```bash
source scripts/sanitize_cloud_secret_names.sh
```

На узлах `@graph` с live URL держи `pragma: allowlist secret` (через компактную строку или поле `x-excalibur-scan`; publish-скрипт снимает `x-excalibur-scan` перед записью meta).
