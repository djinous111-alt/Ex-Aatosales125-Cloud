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

## Commit hygiene (Cloud)

- В JSON-LD используй placeholders `${PUBLIC_SITE_URL|CATALOG_URL|TELEGRAM_URL|MAX_URL}`, не live site/catalog URLs.
- Коммит через `bash scripts/excalibur_git.sh commit …` — фильтрует `CLOUD_AGENT_*_SECRET_NAMES` до bash-safe ids (URL-токен в списке → `invalid variable name`).
- Не `python3 -c` filter в subshell: export должен быть в той же shell-сессии, что и `git commit`.
