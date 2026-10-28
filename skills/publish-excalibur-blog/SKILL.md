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
| Schema | `schema.jsonld` (commit-safe `env:*` placeholders OK) |
| Credentials | Cloud Secrets / process env; optional gitignored `memory/site.env.local` |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |
| Python deps | `paramiko` (install via `.cursor/cloud-agent-install.sh`) |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

### Env bootstrap (Cloud)

1. Prefer **process env / Cloud Secrets** — `excalibur_blog_wp_publish.py` читает их через Python (`load_env`), не bash-source password files.
2. Optional: write gitignored `memory/site.env.local` from Secrets if local override needed (`SSH_ROOT=.` recommended).
3. Preflight: `python3 scripts/excalibur_blog_wp_publish.py --env-check` (no secret values printed).

Скрипт **in-memory** гидратирует перед upload:
- `env:PUBLIC_SITE_URL` / `env:CATALOG_URL` / `env:TELEGRAM_URL` / `env:MAX_URL` в `schema.jsonld`
- `${CATALOG_URL}` / `${TELEGRAM_URL}` / … в `article.html`

Не нужно руками подставлять live URL в git-артефакты перед publish.

## Алгоритм

### 1. Preflight publish

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check

python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/link-verify.json
```

Примечание: link-verify сам IRI-encode non-ASCII URL path; CTA-плейсхолдеры `${…}` в HTML для live-check раскрывай только во временной копии или после hydrate в publish.

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
- гидратирует `env:*` / `${…}` из publish env;
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
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base ""
```

Inbound-ссылки из старых статей на новую.

## Handoff block (шаблон)

```text
=== EXCALIBUR BLOG PUBLISH ===
topic_id:
slug:
article_dir:
post_id:
permalink:
featured_media_id:
inline_media_ids:
ledger: shared/published-articles.md
verdict: PASS | BLOCKER
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```

## Blockers

- нет `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`
- нет SSH / PUBLIC_SITE_URL
- нет `paramiko` в окружении (doctor WARN; install script must include it)
- QA/link-verify не PASS
- cover/schema отсутствуют
