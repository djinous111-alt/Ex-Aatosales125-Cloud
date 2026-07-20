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

## Commit hygiene (secret-scan)

Live `schema.jsonld` **должен** содержать реальные `PUBLIC_SITE_URL` / catalog / Telegram / MAX в `url`, `publisher`, `sameAs` для Publish.

Cursor secret-scan часто блокирует commit этих значений (они в Cloud Secrets). Рабочий порядок:

1. Собери **live** schema из env + `authors-registry.json`.
2. Для git: либо commit redacted копию (`[REDACTED]` placeholders, AS04 pattern), либо строки с `pragma: allowlist secret` если scanner это поддерживает.
3. Перед Publish держи **live** файл в working tree (не оставляй литералы `[REDACTED]` в том JSON-LD, который уходит в WP meta).
4. Не коммить permalink/host из publish-result без redaction.
