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

- Публичные brand URL (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, `CATALOG_URL`, `MAX_URL`) для BlogPosting/`sameAs` **не redact'ить** в `[REDACTED]` без publish hydrate: schema.org должен оставаться валидным на LIVE.
- Предпочтительный commit wrapper: `bash scripts/excalibur_git.sh commit -m "..."` (фильтрует non-identifier secret names + исключает public URL env из scan).
- Альтернатива: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` затем `git commit`.
- Если Cloud pre-commit падает на `invalid variable name`: `source scripts/excalibur_blog_filter_secret_names.sh` перед `git commit`.
- Не оставляй сломанный JSON-LD с литералом `[REDACTED]` на live сайте: publish обязан hydrate `env:VAR` / placeholders.
