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
| Credentials | Cloud Secrets / `memory/site.env.local`: `SSH_HOST`, `SSH_USER`, `SSH_PASS` (или `SSH_PASSWORD`), `SSH_ROOT` (алиас `SSH_PATH` → `SSH_ROOT`), `PUBLIC_SITE_URL` |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |
| Python dep | `paramiko` (install via `.cursor/cloud-agent-install.sh` / `requirements.txt`) |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

Preflight без секретов в stdout:

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check
```

Если `SSH_ROOT`/mapped `SSH_PATH` даёт ENOENT — скрипт сам пробует `.`; после warning выставь Cloud Secret `SSH_ROOT=.`.

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
- создаёт/обновляет WP post **только** если candidate `post_id` — существующий `post` (publish/draft/…); attachment/stale id игнорируется;
- отказывается публиковать, если slug занят attachment (URL отдал бы image);
- после create/update требует `type=post` + `status=publish` в PHP;
- загружает featured image + alt;
- загружает **все локальные inline `<img>`** и подменяет `src` на WP media URL;
- пишет post meta `_excalibur_blog_schema_jsonld`;
- **до ledger/verdict pass** проверяет public REST `GET /wp-json/wp/v2/posts/<id>` (+ slug search). Media OK при 404 поста = FAIL.

### 3b. Обязательный REST verify (агент)

Даже если читаешь `raw_output` вручную — не ставь handoff PASS и не правь ledger в `published`, пока не подтверждено:

```text
GET {PUBLIC_SITE_URL}/wp-json/wp/v2/posts/{post_id} → 200, status=publish
GET .../wp/v2/posts?slug={slug} → содержит тот же id
```

Симптом attachment-slug collision: permalink HTTP 200 отдаёт PNG/JPEG, REST `/posts/<id>` 404. Rename orphan media → publish с `post_id=0`.

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
- `❌ PUBLISH FAIL` — скрипт вернул fail (смотри `raw_output` / `rest_verify` в wp-publish-result.json)
- False PASS запрещён: `OK post=` без REST 200/`publish` не считается успехом; ledger не писать

## Запрещено

- Писать или переписывать longread
- Генерировать cover/schema с нуля
- Пропускать dry-run
- Завершать пайплайн без записи в `published-articles.md` при успешном publish
