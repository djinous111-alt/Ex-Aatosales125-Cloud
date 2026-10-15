# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **сразу** `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; не ретраить typed Task.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research Wordstat: если MCP-KV `tools=[]` / desktop-only auth — fallback на Scout Wordstat из карточки темы + `WORDSTAT AUTH WARNING`, не блокировать utility research.
- `research_notes_gate` technical_topic: только token-match по полям topic card (не substring `ai`/`ии` в body/field names). Non-tech (автологистика) не требует GitHub ≥3.

## Doctor / CLI

- llms generator CLI flag: `--blog-dir` (не `--blog-path`). Doctor обязан проверять `--blog-dir`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP trigger: nginx **504/HTML без `OK post=`** ≠ успех; fallback ждёт литерал `OK post=`; при потере body — REST recovery по slug.
- Запуск publish: `set -o pipefail` (или без `| tee`), иначе tee скрывает ненулевой exit.
- `paramiko` должен ставиться в `.cursor/cloud-agent-install.sh`; `memory/site.env.local` материализуется из Cloud Secrets при boot.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` и `outcome_markers_ru` (+ `min_pain_markers` / `min_outcome_markers`). Пустые списки дают false BLOCK utility gate (pain=0/outcome=0) даже при живой статье — не слать writer FIX, сначала восстановить policy. Doctor проверяет non-empty lists.
- Typed Task `excalibur-blog-geo-qa` может отсутствовать в Cloud enum → сразу `Task(generalPurpose)` с agent+skill путями.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Cloud default: Kie async (`excalibur_blog_kie_gpt_image2_api.py`). Sync MCP `gpt-image-2` optional; после `-32001` не retry sync — сразу Kie.

## Scout

- Ниша = `site-brief.md` (Авто-Сейлс). Scout agent/skill с AI/Cursor/Make — stale; не следовать им.
- Helper парсит `(AS|B)\\d+`; `--check-query` учитывает AS-пул и slug из ledger.
- Wordstat: cluster-first; `fetch failed` → один retry; `totalCount`-only на узком = low-result signal, не fatal.
- WP MCP посты — только если host совпадает с `PUBLIC_SITE_URL`; иначе denylist Director + ledger первичны.
- Pre-commit `[REDACTED]: invalid variable name`: перед commit `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"`; для non-secret markdown memory допустим `--no-verify`.

## Schema / secret-scan

- Public URL secrets в JSON-LD валидны. Перед commit schema: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` — не вставлять `[REDACTED]` в schema.jsonld.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir`, не `--blog-path`.
