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

## Secret-scan / commit path

- BlogPosting `@id`, `mainEntityOfPage`, author `sameAs` требуют **абсолютные публичные** URL (`PUBLIC_SITE_URL`, catalog/Telegram/MAX), как в Schema.org.
- JSON-LD **нельзя** ломать end-of-line `// pragma` и нельзя заменять URL на литерал `[REDACTED]` (это ломает CTA/schema и publish).
- HTML `<!-- pragma: allowlist secret -->` в `schema.jsonld` тоже нельзя (невалидный JSON).
- Если pre-commit secret-scan блокирует `schema.jsonld` из-за публичных marketing URL, которые совпадают с Cloud Secrets:
  1. подтверди, что URL те же, что уже в `shared/authors-registry.json` / прошлых schema;
  2. коммить через `bash scripts/excalibur_git.sh commit …` (фильтр invalid secret names) и, только если scanner всё ещё блокирует публичные URL, `--no-verify` с явной пометкой в handoff;
  3. **не** подставляй `[REDACTED]` в JSON-LD.
- Предпочтительно: убрать публичные site/catalog/Telegram/MAX URL из Dashboard Secrets (оставить обычные env/config), чтобы scanner не считал их секретами.
