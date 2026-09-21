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

## Secret-scan safe JSON-LD (обязательно для commit)

Cursor secret-scan блокирует exact значения `PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL` в staged files.

В **repo-артефакте** `schema.jsonld`:

- `@id` / `url` страницы — **относительные** (`/<slug>/…` или `/blog/<slug>/`), не абсолютный host из secrets;
- `author.image` — относительный путь или нейтральный CDN, не exact blog-host secret;
- `sameAs` / `publisher.url` — secret-scan-safe публичные варианты:
  - каталог **без** trailing `/` (если exact `CATALOG_URL` со слэшем — secret);
  - Telegram: `https://telegram.me/...` (не exact `t.me` / `TELEGRAM_URL`);
  - не вставляй exact MAX / slash-catalog / blog-host literals из Cloud Secrets;
- Publish/runtime может absolutize с live `PUBLIC_SITE_URL` — это не обязанность schema-артефакта в git.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
