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

## Git commit в Cloud (secret redact)

Если `pre-commit.cursor` падает только с `[REDACTED]: invalid variable name`:

1. `git diff --cached` — только нужные артефакты, без handoff/fragments и raw secrets.
2. Допустим `git commit --no-verify` для article/schema файлов, затем push.

Install патчит hook (`scripts/excalibur_blog_patch_precommit_secret_scan.sh`) на Cloud boot; после патча обычный commit должен работать.

## URL placeholders

В `schema.jsonld` используй placeholders `[from env PUBLIC_SITE_URL]` / CATALOG/TELEGRAM/MAX — не сырые site URLs (secret scan).

