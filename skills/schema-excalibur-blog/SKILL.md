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

- В `schema.jsonld` держи URL-плейсхолдеры `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}` — не живые host из secrets.
- Коммит: `bash scripts/excalibur_git.sh commit -m "…"` (фильтрует `CLOUD_AGENT_*_SECRET_NAMES` → valid bash ids; чинит `invalid variable name` в pre-commit).
- Перед commit: проверь staged diff; ad-hoc `git commit --no-verify` — только fallback после ручной проверки.
