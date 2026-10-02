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

## Git / secret-scan (обязательно)

Абсолютные URL сайта, каталога, Telegram, MAX в BlogPosting/FAQ/`sameAs` часто совпадают с Cloud Secret *values* (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) → pre-commit блокирует commit.

1. **Commit-safe:** в git-копии `schema.jsonld` замени origin bases на `[REDACTED]` (JSON-LD нельзя «лечить» HTML pragma).
2. **Runtime/publish:** `excalibur_blog_wp_publish.py` раскрывает `[REDACTED]` в payload из env (`PUBLIC_SITE_URL`, опционально `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL`) перед записью WP meta — не публикуй redacted schema as-is.
3. Идеал Dashboard: публичные brand URLs не хранить как secret-scanned values (только private tokens).
