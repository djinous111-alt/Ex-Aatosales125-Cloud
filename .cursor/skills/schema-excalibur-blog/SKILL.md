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

## Secret scanner / public brand URLs

Публичные site/catalog/Telegram/MAX URL в BlogPosting и `author.sameAs` совпадают с Cloud Secrets → pre-commit secret scanner блокирует commit.

На **каждой строке** с таким URL добавь валидный JSON-ключ:

```json
"_comment": "pragma: allowlist secret"
```

`excalibur_blog_wp_publish.py` удаляет ключи `"_comment"` перед записью post meta, чтобы pragma не попал в live `<script type="application/ld+json">`.

Перед `git commit`:

```bash
export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(bash scripts/excalibur_blog_filter_secret_names.sh)"
```
