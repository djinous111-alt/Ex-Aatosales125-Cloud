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

### 4. HTTP timeout → curl → WebFetch Fallback

Порядок в `excalibur_blog_wp_publish.py`:

1. `urllib` timeout 120s;
2. `curl -fsS -L --max-time 300` на тот же bootstrap URL;
3. если curl тоже упал — печатает `=== FALLBACK_TRIGGER_URL ===`; Cloud-агент делает **один** WebFetch и пишет ответ в `memory/webfetch-response.txt` (wait до 180s).

**Не** запускай второй publish / параллельный WebFetch race. **Не останавливайся** на первом timeout.

### 5. Post-publish артефакты

| Файл | Действие |
|------|----------|
| `wp-publish-result.json` | создаёт скрипт (verdict pass/fail) |
| `memory/blog/wp-publish-log.md` | допиши секцию с post_id, permalink, inline ids |
| `shared/published-articles.md` | upsert строки topic_id → published; **никогда не удаляй** исторические AS*/B* ряды при ребренде |
| `promotion-checklist.md` | Live URL = permalink |
| handoff | блок `=== EXCALIBUR BLOG PUBLISH ===` + permalink в `PIPELINE DONE` |

### 6. Post-publish (рекомендуется)

```bash
python3 scripts/excalibur_blog_interlinker.py --apply \
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


## Schema secret-scan

`schema.jsonld` may contain `__excalibur_pragma_N` keys for Cursor allowlist; publish strips them before WP meta.
