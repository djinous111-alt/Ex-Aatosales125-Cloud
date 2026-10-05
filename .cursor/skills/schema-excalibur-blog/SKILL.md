---
name: schema-excalibur-blog
description: Excalibur BLOG Schema — BlogPosting + FAQPage JSON-LD, автор из registry.
---

# Excalibur BLOG — Schema

## Вход

- `article.html`, `article.meta.json`, `research-notes.md`
- `shared/authors-registry.json`
- **URL источников (в этом порядке):**
  1. env: `PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`
  2. `sameAs` / avatar из `shared/authors-registry.json`
  3. `memory/brief/site-brief.md` / `conversion-map.md` — только через Python-чтение файла на диске, **не** через masked tool output

## Задача

1. BlogPosting: headline, datePublished (today из research-context), author Person + sameAs.
2. FAQPage из FAQ секции статьи.
3. HowTo / Review — только если архетип требует.
4. **Запрещено** писать литерал `[REDACTED]` в `schema.jsonld` (`@id`, `url`, `sameAs`, `image`).
5. После сборки: `python3 scripts/excalibur_blog_schema_validate.py --article-dir <dir>` → PASS (реальные https). Для secret-scan копии с `[PUBLIC_SITE_URL]` — `--expand-env`.

## Secret-scan / commit

На строках с site/CTA/avatar/sameAs URL добавь суффикс ` // pragma: allowlist secret` при необходимости. Commit: `bash scripts/excalibur_git.sh commit …`.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
