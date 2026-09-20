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


## Commit / secret-scrub

В `schema.jsonld` коммить site/CTA как `[REDACTED]/…` и bare `[REDACTED]` (sameAs).
Publish (`excalibur_blog_wp_publish.py`) раскрывает плейсхолдеры из env и снимает `__excalibur_pragma_*` keys перед WP meta.
Опционально: `__excalibur_pragma_N` allowlist-ключи, если нужны live URL в git.

If Cursor pre-commit dies with `invalid variable name` after secret-name scrub (URL-shaped entries in `CLOUD_AGENT_INJECTED_SECRET_NAMES`), use `git commit --no-verify` and log an incident. Prefer running `bash scripts/excalibur_blog_patch_cursor_secret_scrub.sh` (also via cloud-agent-install).
