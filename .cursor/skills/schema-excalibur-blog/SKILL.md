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

- Для git допустимы `[REDACTED]` placeholders вместо `PUBLIC_SITE_URL` / `sameAs` URL — `excalibur_blog_wp_publish.py` hydrates их из env перед upload.
- Если Cloud pre-commit падает на `invalid variable name` в secret injection: `source scripts/excalibur_blog_filter_secret_names.sh` перед `git commit`.
- Не оставляй сломанный JSON-LD с литералом `[REDACTED]` на live сайте: publish обязан hydrate.
