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

## Commit / secret-scan

Live `schema.jsonld` must contain real site/catalog/telegram/max URLs in BlogPosting `@id`, author `sameAs`, publisher.

Before `git commit`:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
```

On every physical line that contains those URL values, include `pragma: allowlist secret` (compact JSON lines and/or unknown keys like `x-excalibur-scan*` are OK; Google ignores unknown properties). Without the pragma, Cursor secret-scan blocks the commit.

Контракт: `shared/excalibur-article-writing-contract.md` (секция schema.jsonld).

