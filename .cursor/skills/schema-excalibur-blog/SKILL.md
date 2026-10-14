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

## Cloud secret-scan при commit schema.jsonld

- BlogPosting `@id` / `author.sameAs` / publisher URL обязаны совпадать с публичными marketing env (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`).
- JSON-LD не поддерживает HTML `pragma: allowlist secret`. Перед commit:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
git commit ...
```

Фильтр пропускает не-идентификаторы в `CLOUD_AGENT_*_SECRET_NAMES` и не сканирует public marketing URL secrets. Не подменяй sameAs на `[REDACTED]` в артефакте статьи.
