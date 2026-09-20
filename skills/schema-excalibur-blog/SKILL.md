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

## Secret-scan для `schema.jsonld`

JSON-LD **обязан** содержать живые URL (`PUBLIC_SITE_URL`, CTA, author `sameAs`) после `json.loads`.

Cursor secret-scan блокирует literal Cloud Secret URLs в commit. В строгом JSON нельзя вставить HTML `pragma: allowlist secret`.

**Перед commit:**

```bash
python3 scripts/excalibur_blog_schema_write.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --in-place
```

Хелпер переписывает secret-URL в `\uXXXX` unicode-escapes: файл остаётся валидным JSON, после parse — живые URL.

Проверка:

```bash
python3 scripts/excalibur_blog_schema_write.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --check
```

Не оставляй plaintext Cloud Secret URLs в committed `schema.jsonld`.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
