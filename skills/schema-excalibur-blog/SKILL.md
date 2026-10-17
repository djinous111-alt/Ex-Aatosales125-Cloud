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

## Secret-scan / public URLs

BlogPosting/`sameAs` часто содержит публичные marketing URLs (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) из `shared/authors-registry.json`. Они же бывают в Cloud Secrets → pre-commit scanner ловит false positive.

Перед коммитом `schema.jsonld`:
1. На каждой строке с такими URL добавь `_excalibur_allowlist: "pragma: allowlist secret"` (hook вырезает строку из скана), **или**
2. Коммить через `bash scripts/excalibur_git.sh commit …` (фильтрует non-identifier names + public CTA/site secret names).

Не клади raw URL в `CLOUD_AGENT_INJECTED_SECRET_NAMES` — только валидные bash identifiers.
