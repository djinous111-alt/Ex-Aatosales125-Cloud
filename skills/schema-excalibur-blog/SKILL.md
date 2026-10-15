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

## Commit (secret-scan)

`schema.jsonld` обязан содержать публичный site URL в `@id`/`mainEntityOfPage` и registry `sameAs` (каталог/Telegram/MAX). Это намеренные публичные NAP/CTA URL, часто совпадающие с Cloud Secrets.

Перед commit:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
git commit ...
```

Не заменяй `sameAs` на `[REDACTED]`. Не полагайся на HTML pragma (JSON-LD не HTML).

