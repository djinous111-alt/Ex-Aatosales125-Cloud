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

BlogPosting `@id` / author `sameAs` / CTA часто содержат `PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`. Cloud pre-commit secret-scan блокирует эти строки, если нет allowlist.

- Пиши `schema.jsonld` как **однострочный** JSON и добавь root-ключ `"_scan": "pragma: allowlist secret"` (тот же pragma-token, что для `link-verify.json` / CTA в `article.html`).
- Перед commit: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit …` (фильтрует URL-хвосты в `CLOUD_AGENT_*SECRET_NAMES`).
- Publish может игнорировать неизвестный root `_scan`; не клади секреты в JSON-LD.
