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

Перед `git commit` всегда:

```bash
source scripts/excalibur_blog_sanitize_secret_names.sh
```

`CLOUD_AGENT_INJECTED_SECRET_NAMES` иногда содержит сырой URL (не identifier) → pre-commit падает с `invalid variable name`. Sanitize оставляет только валидные имена.

В `schema.jsonld` URL сайта/CTA/`sameAs`:

- на **той же строке**, что и URL, добавь `"x-excalibur-pragma": "pragma: allowlist secret"`;
- массивы `sameAs` с секретными URL — **в одну строку** вместе с pragma (hook сканит построчно).
