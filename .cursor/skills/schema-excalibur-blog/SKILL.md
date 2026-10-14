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

- Публичные URL сайта/каталога в JSON-LD ожидаемы (`PUBLIC_SITE_URL` / authors-registry).
- Если Cloud Secrets сканируют эти значения: в committed `schema.jsonld` замени base URL на `[REDACTED]`; publish подставит live URL.
- Коммить через `bash scripts/excalibur_git.sh commit …` — фильтрует невалидные «имена» в `CLOUD_AGENT_INJECTED_SECRET_NAMES` (URL ломают `${!SECRET_NAME}` в pre-commit).
