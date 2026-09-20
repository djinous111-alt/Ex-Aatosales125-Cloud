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
| Links | `link-verify.json` → pass (нет literal `[REDACTED]` в href) |
| Cover | `cover/cover.png` + alt в `cover-registry.json` |
| Schema | `schema.jsonld` |
| Credentials | Cloud Secrets / `memory/site.env.local`: `SSH_*`, `PUBLIC_SITE_URL` |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

## Env / deps preflight

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check
```

- `SSH_ROOT` обязателен (рекомендуется `.`). Legacy Cloud Secret `SSH_PATH` скрипт мапит в `SSH_ROOT`.
- Если `ModuleNotFoundError: paramiko`:

```bash
python3 -m pip install --break-system-packages -r requirements.txt
# или минимум:
python3 -m pip install --break-system-packages paramiko
```

Cloud install (`.cursor/cloud-agent-install.sh`) ставит `requirements.txt`, включая paramiko.

## Алгоритм

### 1. Preflight publish

Перед link-verify: в `article.html` не должно быть `href` с literal `[REDACTED]`. Если есть — восстанови из `CATALOG_URL` / `TELEGRAM_URL` и добавь `<!-- pragma: allowlist secret -->` на CTA-строке.

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/link-verify.json \
  --site-base "$PUBLIC_SITE_URL"
```

Gate: `link-verify.json` → pass. Иначе FIX (writer/QA) или BLOCKER.

### 2. Dry-run

```bash
python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --dry-run
```

Проверь: slug, title, размер PHP payload без ошибок.

### 3. Publish

```bash
python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Скрипт:
- создаёт/обновляет WP post;
- загружает featured image + alt;
- загружает **все локальные inline `<img>`** и подменяет `src` на WP media URL;
- пишет post meta `_excalibur_blog_schema_jsonld`.

### 4. Cloud WebFetch Fallback

Если локальный HTTP-триггер bootstrap упал (timeout / WinError 10060):

1. Скрипт печатает `=== FALLBACK_TRIGGER_URL ===` с URL `excalibur-blog-publish-once.php`.
2. Cloud-агент открывает URL через WebFetch и пишет ответ в `memory/webfetch-response.txt`.
3. Скрипт продолжает и читает ответ из файла.

**Не останавливайся** на первом timeout — используй fallback.

### 5. Post-publish артефакты

| Файл | Действие |
|------|----------|
| `wp-publish-result.json` | создаёт скрипт (verdict pass/fail) |
| `memory/blog/wp-publish-log.md` | допиши секцию с post_id, permalink, inline ids |
| `shared/published-articles.md` | строка: date, topic_id, slug, url, status=published |
| `promotion-checklist.md` | Live URL = permalink |
| handoff | блок `=== EXCALIBUR BLOG PUBLISH ===` + permalink в `PIPELINE DONE` |

Перед commit redact literal `PUBLIC_SITE_URL` → `[REDACTED]` в ledger/log/result при необходимости.

### 6. Post-publish (рекомендуется)

```bash
python3 scripts/excalibur_blog_interlinker.py --apply \
  --blog-dir memory/blog/articles \
  --site-base "$PUBLIC_SITE_URL"
```

Inbound-ссылки из старых статей на новую. Перед commit — redact site URL в артефактах.

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

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail / literal REDACTED href, нет cover/schema, credentials, allow flag, paramiko missing
- `❌ PUBLISH FAIL` — скрипт вернул fail (смотри `raw_output` в wp-publish-result.json)

## Запрещено

- Писать или переписывать longread
- Генерировать cover/schema с нуля
- Пропускать dry-run
- Завершать пайплайн без записи в `published-articles.md` при успешном publish
