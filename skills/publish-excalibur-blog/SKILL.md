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
| Credentials | Cloud Secrets overlay **or** `memory/site.env.local` (`SSH_*`, `PUBLIC_SITE_URL`) — site.env.local optional when Secrets cover all keys |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |
| SSH dep | `paramiko` (installed via `requirements.txt` / `.cursor/cloud-agent-install.sh` / Dockerfile) |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

## Алгоритм

### 0. Env + dependency check

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check
```

JSON must show `paramiko_available: true`. If false:

```bash
python3 -m pip install --break-system-packages paramiko
# or: python3 -m pip install -r requirements.txt
```

### 1. Preflight publish

```bash
python3 scripts/excalibur_blog_link_verify.py \
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

### 4. Cloud WebFetch Fallback + 504 reconstruct

Если локальный HTTP-триггер bootstrap упал (timeout / WinError 10060):

1. Скрипт **сначала** пробует REST reconstruct по slug (post может уже быть LIVE после client timeout).
2. Если LIVE нет — печатает `=== FALLBACK_TRIGGER_URL ===` с URL `excalibur-blog-publish-once.php`.
3. Cloud-агент открывает URL через WebFetch/curl и пишет ответ в `memory/webfetch-response.txt`.
4. **nginx 504/502 HTML ≠ success** — не трактуй gateway HTML как OK; скрипт снова делает REST reconstruct по slug.
5. HTTP wait / FALLBACK poll = **300s** (большие ~6–7MB payload часто режутся на ~120s edge).

**Запрещено:** второй bootstrap trigger, если REST уже видит LIVE post (иначе дубли media `*-1.png`).
**Не останавливайся** на первом timeout — reconstruct или fallback, без republish.

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
