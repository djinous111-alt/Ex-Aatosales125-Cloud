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


## Commit vs runtime (secret-scan)

Cloud secret-scan часто блокирует commit `schema.jsonld`, если URL равны Dashboard secrets (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`).

1. **Для git commit:** замени абсолютные URL на `[REDACTED]` или `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` / …
2. **Для publish:** рабочее дерево должно содержать гидратированные URL; `excalibur_blog_wp_publish.py` также вызывает `hydrate_schema_redactions()` из env/`site.env.local`.
3. Не коммить secrets; runtime handoff может держать полный schema локально.
