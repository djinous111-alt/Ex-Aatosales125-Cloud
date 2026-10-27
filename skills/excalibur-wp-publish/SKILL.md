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
| Credentials | Cloud Secrets → `memory/site.env.local` (SSH_*, `PUBLIC_SITE_URL`); auto-bootstrap если файла нет |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |
| Python deps | `paramiko` (SSH). Install: `.cursor/cloud-agent-install.sh` / `requirements.txt` / Dockerfile |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

## Env bootstrap

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check
```

Если `memory/site.env.local` отсутствует — скрипт создаёт его из process env (`SSH_PASSWORD`→`SSH_PASS`, default `SSH_ROOT=.`). Не коммить файл. CTA `${CATALOG_URL}` / legacy `href="[REDACTED]"` expand'ятся в WP payload из env (committed HTML может оставаться с плейсхолдерами).

## Алгоритм

### 1. Preflight publish

```bash
# optional local expand for link-verify; redact before git commit
python3 scripts/excalibur_blog_cta_hrefs.py \
  --article-html memory/blog/articles/<topic_id>-<slug>/article.html \
  --expand --write

python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/link-verify.json \
  --site-base "${PUBLIC_SITE_URL}"
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
- bootstrap'ит `site.env.local` при необходимости;
- expand'ит CTA плейсхолдеры в payload;
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

### 6. Post-publish (рекомендуется)

```bash
python3 scripts/excalibur_blog_interlinker.py --apply \
  --blog-dir memory/blog/articles \
  --site-base "${PUBLIC_SITE_URL}"
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

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет cover/schema, credentials, allow flag, missing paramiko
- `❌ PUBLISH FAIL` — скрипт вернул fail (смотри `raw_output` в wp-publish-result.json)

## Запрещено

- Писать или переписывать longread
- Генерировать cover/schema с нуля
- Пропускать dry-run
- Завершать пайплайн без записи в `published-articles.md` при успешном publish
