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

## Commit в redacted Cloud sandbox

site_url в JSON-LD держи как `[REDACTED]` (как AS08/AS09), не пиши live `PUBLIC_SITE_URL`.

Если `git commit` падает с `invalid variable name` из-за `CLOUD_AGENT_INJECTED_SECRET_NAMES` (литерал `[REDACTED]`):

```bash
eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export --empty-ok)"
git commit ...
```

Не отключай secret-scan на prod worker — только фильтр невалидных bash identifiers в sandbox.
