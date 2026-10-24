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

## Cloud pre-commit / secret scan

Absolute URLs из Cloud Secrets (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) в `BlogPosting` / `sameAs` / HowTo **нужны по контракту**, но Cursor secret-scan блокирует commit.

Перед `git commit` schema:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
# или:
bash scripts/excalibur_git.sh commit -m "schema(...)"
```

Фильтр исключает public marketing URL names из scan list. Не заменяй абсолютные URL на `[REDACTED]` в `schema.jsonld` — Rich Results требуют absolute. `--no-verify` только как last resort после подтверждения, что в diff только публичные marketing URL.
