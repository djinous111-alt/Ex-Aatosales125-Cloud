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


## Pre-commit secret names

Если `git commit` падает с `invalid variable name` на `${!SECRET_NAME}`:

- в `CLOUD_AGENT_INJECTED_SECRET_NAMES` бывает мусор (`[REDACTED]`, URL-токены);
- filter: только `^[A-Za-z_][A-Za-z0-9_]*$` — уже в Cloud `pre-commit.cursor` и в `scripts/excalibur_blog_filter_secret_names.sh`;
- schema/cover артефакты могут хранить `[REDACTED]` URL placeholders; publish hydrates.

