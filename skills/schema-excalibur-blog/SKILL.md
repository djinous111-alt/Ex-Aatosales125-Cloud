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

## Git commit (Cloud)

Перед любым `git commit` в **том же shell**:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
git add <paths>
git commit -m "..."
```

Хелпер чистит `CLOUD_AGENT_*_SECRET_NAMES`: только valid bash identifiers, comma-separated; дропает public CTA/site URL names и non-identifier junk. Без этого pre-commit падает с `invalid variable name`.

