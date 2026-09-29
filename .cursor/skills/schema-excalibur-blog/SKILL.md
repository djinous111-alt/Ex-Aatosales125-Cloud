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

## Secret-scan note

BlogPosting / FAQPage / HowTo **намеренно** содержат публичные URL (`PUBLIC_SITE_URL`, Telegram/MAX/catalog sameAs). Это не утечка секретов.
Перед commit, если Cloud pre-commit падает на injected secret names:

1. Оставь в `CLOUD_AGENT_INJECTED_SECRET_NAMES` только валидные bash-идентификаторы (`^[A-Za-z_][A-Za-z0-9_]*$`).
2. Исключи public URL keys (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, `MAX_URL`, `CATALOG_URL`) при коммите schema-артефакта.
3. Не используй `--no-verify`.
