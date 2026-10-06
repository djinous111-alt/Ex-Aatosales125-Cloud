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

## Secret-scan / commit (публичные URL в JSON-LD)

`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL` часто лежат в Cloud Secrets, но **должны** оставаться в BlogPosting/FAQPage `@id` / `sameAs`.

Перед `git commit`:

```bash
source scripts/sanitize_cloud_secret_names.sh
# или
scripts/excalibur_git.sh commit -m "..."
```

В `schema.jsonld` для строк с публичными URL добавляй allowlist-маркер на том же JSON-объекте (компактный one-line node в `@graph`):

```json
{"@type":"BlogPosting","@id":"https://example.example/blog/slug/","x-excalibur-scan":"pragma: allowlist secret"}
```

Не редактируй секреты/пароли — только публичные marketing URL. Не клади credential values в schema.
