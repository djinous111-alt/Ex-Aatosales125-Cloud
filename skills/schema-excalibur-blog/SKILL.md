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
4. **Commit / secret-scan:** `sameAs` / `@id` с public site или Telegram из registry+env часто ловят secret-scan.
   - В git можно оставить public non-secret hosts; если commit блокируется — redact site URL to `https://SITE.example` и восстановить на publish.
   - Перед commit: `source scripts/excalibur_blog_filter_injected_secret_names.sh` (не `--no-verify` первым шагом).

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
