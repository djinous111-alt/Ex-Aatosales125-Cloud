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

## Secret-scan (schema.jsonld)

JSON-LD обязан содержать абсолютные URL (`PUBLIC_SITE_URL`, sameAs). Cursor secret-scan может блокировать commit.

Допустимый workaround (валидный JSON): на каждой secret-bearing строке добавь неизвестный ключ
`"__excalibur_pragma_N": "pragma: allowlist secret"` (Google игнорирует unknown properties).
**Не** вставляй `// pragma` — сломает JSON.

`excalibur_blog_wp_publish.py` strips `__excalibur_pragma_*` перед записью WP meta.
