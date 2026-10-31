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

## URL placeholders (обязательно для commit)

Cloud pre-commit secret-scan блокирует live `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` в `schema.jsonld`.

В коммитимом файле используй **только** env placeholders:

- `${PUBLIC_SITE_URL}` — canonical site base (статья, author `@id`, publisher)
- `${CATALOG_URL}` — catalog / Organization.url / sameAs
- `${TELEGRAM_URL}` / `${MAX_URL}` — sameAs social (если в registry через env)
- Публичные Instagram/2GIS и т.п. можно оставлять как обычные URL

`excalibur_blog_wp_publish.py` гидратит `${…}` при сборке payload (файл на диске не переписывает).

Не коммить гидратированный schema с live secret URLs.
