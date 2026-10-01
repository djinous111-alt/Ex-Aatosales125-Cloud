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


## Commit hygiene (schema.jsonld)

`schema.jsonld` must include public brand URLs (`PUBLIC_SITE_URL`, Telegram/Catalog/Max in author `sameAs`).
Before `git commit`:

```bash
EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 \
  eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export --empty-ok --exclude-public-url-secrets)"
# or: source scripts/sanitize_cloud_secret_names.sh with EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1
```

Do **not** use `--no-verify` for schema commits unless sanitize tools are missing and staged files contain no SSH/API secrets.
