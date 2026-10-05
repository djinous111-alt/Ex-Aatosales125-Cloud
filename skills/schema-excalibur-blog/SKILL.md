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

## Placeholders (git-safe)

В committed `schema.jsonld` используй плейсхолдеры, не live URL:

- `[PUBLIC_SITE_URL]`
- `[CATALOG_URL]`
- `[TELEGRAM_URL]`
- `[MAX_URL]`
- `[REDACTED]` (legacy alias → treat as public site base)

```bash
# Проверить / привести существующий schema к placeholders
python3 scripts/excalibur_blog_schema_build.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --in-place --placeholders --write

# Перед WP meta (обычно делает publish): expand из env / site.env.local
python3 scripts/excalibur_blog_schema_build.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --in-place --expand-env --write
```

`excalibur_blog_wp_publish.py` сам expand-ит placeholders в schema meta перед upload.

Коммиты: `bash scripts/excalibur_git.sh commit ...` (sanitize non-identifier secret names).

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
