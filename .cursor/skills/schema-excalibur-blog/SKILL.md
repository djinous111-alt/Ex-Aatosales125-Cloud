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

### Placeholders (обязательно для commit)

Не вшивай live CTA hosts в committed JSON-LD (Cloud secret-scan):

- `${PUBLIC_SITE_URL}` — BlogPosting/FAQPage/HowTo `@id` / `url` / `image`
- `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}` — author/publisher `sameAs` CTA
- Публичные Instagram/2GIS и т.п. можно оставлять как есть

**Никогда** не копируй UI-токен `[REDACTED]` в `schema.jsonld` — это отображение redaction tool, не значение из `authors-registry.json`. Читай registry с диска (или через env→placeholder map), не из redact-preview.

Publish (`excalibur_blog_wp_publish.py`) расширяет placeholders **in-memory** перед WP meta upload и **не** переписывает файл на диске.

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
