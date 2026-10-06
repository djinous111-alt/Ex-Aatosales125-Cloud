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

## Commit / secret-scan (Cloud)

- В JSON-LD нужны **абсолютные публичные** URL (`PUBLIC_SITE_URL`, catalog/Telegram/MAX, author `sameAs`). Не заменяй их плейсхолдерами — publish читает файл как есть.
- Публичные site/catalog/social URL **не должны** лежать в Cursor Cloud Secrets под именами, которые ломают `pre-commit.cursor` (`CLOUD_AGENT_INJECTED_SECRET_NAMES` обязан содержать только валидные bash-идентификаторы, не сырые URL).
- Если `git commit` режется secret-scan на публичных URL из `schema.jsonld` / `authors-registry.json`: оставь валидный файл на диске для publish; commit артефакта — после Dashboard allowlist/env fix **или** осознанный `git commit --no-verify` только когда staged-файлы без реальных секретов (см. pitfalls).
- Не коммить private SSH/API ключи; public site URL ≠ secret.
