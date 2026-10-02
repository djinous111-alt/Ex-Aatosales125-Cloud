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

## Commit hygiene

- В `schema.jsonld` site-base часто `[REDACTED]` — это нормально.
- Перед commit: `source scripts/sanitize_cloud_secret_names.sh` (иначе pre-commit падает на литерале `[REDACTED]` внутри `CLOUD_AGENT_*_SECRET_NAMES`).
- Push 401 / Bad credentials → needs-human (обновить Cloud GitHub token); артефакты валидируй локально.

