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
| Credentials | `memory/site.env.local` **или** Cloud Secrets в process env: `SSH_*`, `PUBLIC_SITE_URL` |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

## Алгоритм

### 1. Preflight publish

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/link-verify.json \
  --site-base [REDACTED]
```

Gate: `link-verify.json` → pass. Иначе FIX (writer/QA) или BLOCKER.

### 1a. `site.env.local` bootstrap (если файла нет)

Cloud часто инжектит Secrets только в process env, без `memory/site.env.local`.

1. `excalibur_blog_wp_publish.py` при `--env-check` / publish **сам** создаёт gitignored `memory/site.env.local` из process env (если файл отсутствует и есть ключи).
2. Если файла нет и Secrets тоже нет → **BLOCKER** (не угадывать хост/пароль).
3. Рекомендуемый `SSH_ROOT=.` (login cwd). Не коммить `site.env.local`.

### 1b. Env / paramiko preflight

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check
```

`paramiko_available` обязан быть `true`. Если нет:

```bash
python3 -m pip install --break-system-packages -r requirements.txt
# or: python3 -m pip install --break-system-packages paramiko
```

`requirements.txt` / `.cursor/cloud-agent-install.sh` / Dockerfile обязаны ставить `paramiko` на каждый Cloud boot.

### 2. Dry-run

```bash
python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --dry-run
```

Проверь: slug, title, размер PHP payload без ошибок.

### 3. Publish

```bash
# optional: longer HTTP wait (defaults are already 300s)
export HTTP_TRIGGER_TIMEOUT_SEC=300
export FALLBACK_POLL_SEC=300

python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Скрипт:
- создаёт/обновляет WP post;
- загружает featured image + alt;
- загружает **все локальные inline `<img>`** и подменяет `src` на WP media URL;
- пишет post meta `_excalibur_blog_schema_jsonld`.

### 4. Cloud WebFetch Fallback + REST reconstruct

Если локальный HTTP-триггер bootstrap упал (timeout / WinError 10060):

1. Скрипт ждёт до `HTTP_TRIGGER_TIMEOUT_SEC` (default **300**), затем печатает `=== FALLBACK_TRIGGER_URL ===`.
2. Cloud-агент открывает URL через WebFetch и пишет ответ в `memory/webfetch-response.txt` (poll до `FALLBACK_POLL_SEC`, default **300**).
3. Если fallback тоже timed out, скрипт пробует **REST reconstruct** `posts?slug=` — success если LIVE post найден (`OK post=`).
4. **Запрещено** второй HTTP trigger bootstrap, пока slug уже LIVE (риск `*-1.png` дублей media).
5. WebFetch watcher должен идти **параллельно** ожиданию poll (отдельный agent/process пишет `memory/webfetch-response.txt`); один блокирующий процесс без watcher почти всегда упрётся в fallback timeout — тогда REST reconstruct.

**Не останавливайся** на первом timeout — используй fallback / REST reconstruct, не повторный trigger.

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
