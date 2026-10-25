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

## Pre-commit secret allowlist (обязательно)

Строки `schema.jsonld` с site/CTA URL (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`, author `sameAs`) часто блокирует Cursor secret-scan.

Для JSON-LD **нельзя** HTML-комментарий. На каждой строке, где есть такой URL, добавь JSON-safe pragma на той же строке:

```json
"@id": "[REDACTED]/slug/#blogposting", "x-excalibur-pragma": "pragma: allowlist secret"
```

или для объектов в массиве:

```json
{"@id": "[REDACTED]", "x-excalibur-pragma": "pragma: allowlist secret"}
```

Правила:
- pragma должен быть **на той же строке**, что и секретный URL;
- JSON обязан оставаться валидным (`python3 -m json.tool schema.jsonld`);
- не коммить живые secrets в git без allowlist; для ledger/llms допускается `[REDACTED]` в committed copies.

