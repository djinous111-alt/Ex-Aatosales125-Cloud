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
| Credentials | `memory/site.env.local` из Cloud Secrets: `SSH_*`, `PUBLIC_SITE_URL` (не FTP) |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |
| Python deps | `paramiko` (SSH); `python3 scripts/excalibur_blog_wp_publish.py --env-check` FAIL если нет |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

### Bootstrap `memory/site.env.local` (gitignored)

Файл часто отсутствует в свежей Cloud VM. Создай из env **без кавычек**, без печати значений в handoff:

- `PUBLIC_SITE_URL`, `SSH_HOST`, `SSH_PORT`, `SSH_USER`, `SSH_ROOT=.`
- `SSH_PASS` ← значение из `SSH_PASSWORD` или `SSH_PASS`
- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только если Secret разрешает publish

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check
```

## Алгоритм

### 1. Preflight publish

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/link-verify.json \
  --site-base ""
```

Gate: `link-verify.json` → pass. Иначе FIX (writer/QA) или BLOCKER.

### 2. Dry-run

```bash
python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --dry-run
```

Проверь: slug, title, размер PHP payload без ошибок. Скрипт расширяет `env:VAR` в schema/HTML из env перед сборкой PHP.

### 3. Publish

```bash
python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Скрипт:
- создаёт/обновляет WP post;
- загружает featured image + alt;
- загружает **все локальные inline `<img>`** и подменяет `src` на WP media URL;
- расширяет `env:` плейсхолдеры в `schema.jsonld` / HTML и пишет post meta `_excalibur_blog_schema_jsonld`.

### 4. Cloud WebFetch Fallback + REST reconstruct

Если локальный HTTP-триггер bootstrap упал (timeout / WinError 10060):

1. Скрипт сначала пробует **REST reconstruct** по `slug` (`/wp-json/wp/v2/posts?slug=…`) — если пост уже LIVE, **не** делай второй HTTP/FALLBACK trigger (иначе дубли media `*-1.png`).
2. Иначе печатает `=== FALLBACK_TRIGGER_URL ===` с URL `excalibur-blog-publish-once.php`.
3. Cloud-агент открывает URL через WebFetch и пишет ответ в `memory/webfetch-response.txt`.
4. Скрипт читает ответ; **nginx 504/502 HTML ≠ success** (не пиши HTML в webfetch-response как OK). Снова REST reconstruct, если slug LIVE.

HTTP timeout в скрипте ≈300s (крупный bootstrap ~6MB). **Не republish** LIVE пост после успешного reconstruct.

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
  --site-base ""
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
