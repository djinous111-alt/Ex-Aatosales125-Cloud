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

## Cloud secret-scan (URL в JSON-LD)

`PUBLIC_SITE_URL` / catalog / Telegram / MAX в `@id`, `url`, `sameAs`, HowTo `url` часто ловят pre-commit scanner.

1. Перед commit: `source scripts/sanitize_cloud_secret_names.sh`.
2. На каждом объекте/строке с такими URL добавь same-line `"_scan": "pragma: allowlist secret"` (паттерн B05/B08), **или** коммить schema с placeholder `[REDACTED]` и расширяй URL на publish.
3. Runtime artifact для publish должен содержать полные URL до загрузки в WP.
