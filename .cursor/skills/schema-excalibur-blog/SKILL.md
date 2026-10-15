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

## Commit / secret-scan

`schema.jsonld` легитимно содержит публичные URL (`PUBLIC_SITE_URL`, catalog, Telegram, MAX, Instagram sameAs). Перед `git commit`:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
```

Скрипт убирает non-identifier токены (в т.ч. `[REDACTED]`) из `CLOUD_AGENT_INJECTED_SECRET_NAMES` и исключает public URL secret names из commit-time scan. **Не** подменяй реальные public URL на литерал `[REDACTED]` внутри `schema.jsonld`.
