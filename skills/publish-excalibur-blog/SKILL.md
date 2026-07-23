---
name: publish-excalibur-blog
description: Excalibur BLOG Publish — WP post, featured image, inline images, schema meta, ledger и post-publish.
---

# Excalibur BLOG — Publish (субагент ⑥)

**Роль:** `Task(excalibur-blog-publish)`  
**Когда:** сразу после Indexer (шаг ⑤), когда QA PASS, cover, schema и indexer готовы.

## Контракт

`shared/excalibur-wp-publish-contract.md`

## Preconditions (все обязательны)

| Проверка | Файл / env |
|----------|------------|
| QA PASS | `article-qa.md` → verdict PASS |
| Links | `link-verify.json` → pass |
| Cover | `cover/cover.png` + alt в `cover-registry.json` |
| Schema | `schema.jsonld` |
| Credentials | `memory/site.env.local`: `FTP_*`, `FTP_ROOT`, `PUBLIC_SITE_URL` |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

## Алгоритм

### 1. Preflight publish

```bash
python scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/link-verify.json \
  --site-base https://avtosales125.ru
```

Gate: `link-verify.json` → pass. Иначе FIX (writer/QA) или BLOCKER.

### 2. Dry-run

```bash
python scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --dry-run
```

Проверь: slug, title, размер PHP payload без ошибок.

### 3. Publish

```bash
python scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Скрипт:
- создаёт/обновляет WP post;
- загружает featured image + alt;
- загружает **все локальные inline `<img>`** и подменяет `src` на WP media URL;
- пишет post meta `_excalibur_blog_schema_jsonld`.

### 4. Cloud WebFetch Fallback / nginx 504

Если локальный HTTP-триггер bootstrap упал (timeout / WinError 10060 / **nginx 504**):

1. Скрипт печатает `=== FALLBACK_TRIGGER_URL ===` с URL `excalibur-blog-publish-once.php` и ждёт `memory/webfetch-response.txt` до ~**300s**.
2. При **504 Gateway Time-out** на large payload (~cover+3 inlines base64, ~9MB) PHP-FPM часто **уже завершил** post/media/meta. Сразу проверь live WP REST (search by slug) + `HEAD` permalink = 200.
3. Если post жив: реконструируй OK-строки в `memory/webfetch-response.txt` (post_id, permalink, media ids, schema ok), чтобы waiting-скрипт завершил PASS и upsert ledger. Не жди, пока `finally` удалит bootstrap.
4. Иначе: Cloud WebFetch/curl на FALLBACK URL и запиши ответ в тот же файл.
5. `SSH_ROOT=.` (или alias `SSH_PATH`) если upload ловил ENOENT. Host CLI `php` 5.x не запускает WP bootstrap — только web SAPI. Нужен `paramiko` в runtime.

**Не останавливайся** на первом timeout/504 — используй REST confirm + fallback.

### 5. Post-publish артефакты

| Файл | Действие |
|------|----------|
| `wp-publish-result.json` | создаёт скрипт (verdict pass/fail) |
| `memory/blog/wp-publish-log.md` | допиши секцию с post_id, permalink, inline ids |
| `shared/published-articles.md` | строка: date, topic_id, slug, url, status=published |
| `promotion-checklist.md` | Live URL = permalink |
| handoff | блок `=== EXCALIBUR BLOG PUBLISH ===` + permalink в `PIPELINE DONE` |

### 6. Post-publish (рекомендуется)

```bash
python scripts/excalibur_blog_interlinker.py --apply \
  --blog-dir memory/blog/articles \
  --site-base https://avtosales125.ru
```

Inbound-ссылки из старых статей на новую.

## Handoff block (шаблон)

```text
=== EXCALIBUR BLOG PUBLISH ===
topic_id:
slug:
article_dir:
publish_date:
verdict: PASS|FAIL
permalink:
post_id:
featured_image:
inline_images:
schema_meta: ok|fail
blockers:
```

## Blockers

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет cover/schema, credentials, allow flag
- `❌ PUBLISH FAIL` — скрипт вернул fail (смотри `raw_output` в wp-publish-result.json)

## Запрещено

- Писать или переписывать longread
- Генерировать cover/schema с нуля
- Пропускать dry-run
- Завершать пайплайн без записи в `published-articles.md` при успешном publish
