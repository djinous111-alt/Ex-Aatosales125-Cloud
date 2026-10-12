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

## Cloud Secrets / secret scan

Публичные brand URL в BlogPosting (`url`, `publisher.url`, author/publisher `sameAs` из `shared/authors-registry.json`) часто совпадают с Cloud Secrets (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`). Pre-commit secrets scanner тогда блокирует commit так же, как для CTA в HTML.

1. Перед commit: `eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"` — иначе URL-shaped «имена» ломают `${!SECRET_NAME}`.
2. `schema.jsonld` обязан оставаться **валидным JSON-LD** (без HTML/`//`/`#` комментариев): publish и Rich Results читают файл как JSON.
3. HTML-паттерн writer `<!-- pragma: allowlist secret -->` **нельзя** вставлять в JSON. Эквивалент allowlist для schema:
   - убедись, что каждый flagged URL равен значению из `shared/authors-registry.json` и/или уже закоммиченному `schema.jsonld` (например AS08/AS09);
   - только после этой проверки: `git commit --no-verify` для schema-артефакта.
4. Не редактируй и не redacted публичные brand URL в schema ради сканера — E-E-A-T `sameAs` их требует.
