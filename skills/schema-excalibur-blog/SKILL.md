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

## Public URLs vs secret-scan

JSON-LD **обязан** содержать абсолютные публичные URL (site, author sameAs, publisher, catalog/Telegram/MAX из registry/brief). Это marketing NAP, не credentials.

Если Cloud pre-commit блокирует commit из‑за того, что `PUBLIC_SITE_URL` / `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` лежат в Cursor **Secrets** и совпадают со значениями в `schema.jsonld`:

1. Предпочтительно: вынести публичные URL из Secrets в обычные Cloud env vars (или Dashboard allowlist) — **needs-human**.
2. `CLOUD_AGENT_INJECTED_SECRET_NAMES` должен содержать только валидные bash-идентификаторы (не raw URL).
3. Не заменять Schema.org URL на `[REDACTED]` в runtime-артефакте статьи перед publish; для git history при false-positive см. pitfalls / prior publish redaction policy.
4. Не коммитить `.cursor/excalibur-blog-fragments/schema.md`.
