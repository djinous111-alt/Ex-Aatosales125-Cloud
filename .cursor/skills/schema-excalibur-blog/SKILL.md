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

## Helper script

```bash
python3 scripts/excalibur_blog_schema_write.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Пишет `schema.jsonld` с BlogPosting + FAQPage (+ HowTo для mode B).
Secret URL bases → `[REDACTED]` (typed `[REDACTED:CATALOG_URL]` и т.п. тоже ок).
Publish reinject из env перед записью WP meta (`excalibur_blog_cta_urls.py` / wp_publish load_article).
Не коммить live `PUBLIC_SITE_URL` / CTA URLs.
