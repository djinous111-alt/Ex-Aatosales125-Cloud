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

## Commit

Hydrated `schema.jsonld` с живыми sameAs/CTA URL коммить через:

```bash
bash scripts/excalibur_git.sh commit -m "…"
```

Helper фильтрует невалидные имена из `CLOUD_AGENT_INJECTED_SECRET_NAMES` и публичные CTA (`PUBLIC_SITE_URL`, `CATALOG_URL`, …). Не печатай host/URL в fragment.
