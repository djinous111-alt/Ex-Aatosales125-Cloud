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

## Commit (Cloud)

Pre-commit may abort with `invalid variable name` when `CLOUD_AGENT_*_SECRET_NAMES` contains a non-identifier token. Before commit:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
# or:
bash scripts/excalibur_git.sh commit -m "schema(Bxx): ..."
```

Do not use `--no-verify`.
