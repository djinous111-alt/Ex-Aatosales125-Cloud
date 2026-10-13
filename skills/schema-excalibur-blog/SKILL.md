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

## Commit hygiene (обязательно)

- В committed `schema.jsonld` **не** оставляй live `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` (в т.ч. из `authors-registry.json` avatar/sameAs). Замени на `[REDACTED]`.
- Commits: `bash scripts/excalibur_git.sh add|commit|…` — wrapper фильтрует invalid tokens в `CLOUD_AGENT_*_SECRET_NAMES`, чтобы pre-commit `${!name}` не падал.
