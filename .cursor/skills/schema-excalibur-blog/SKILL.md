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

## Pre-commit (Cloud)

Перед `git commit`:

```bash
source scripts/sanitize_cloud_secret_names.sh
```

Фильтрует `CLOUD_AGENT_*_SECRET_NAMES` до bash-identifier (`^[A-Za-z_][A-Za-z0-9_]*$`), иначе pre-commit падает на URL/`[REDACTED]`.
