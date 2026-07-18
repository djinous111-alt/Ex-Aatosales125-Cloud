# Pipeline incident queue — Excalibur BLOG

Open incidents first; fixed incidents retained for fixer audit.

## INC-20260718-1250-publish-paramiko-missing
status: open
run_date: 2026-07-18
role: excalibur-blog-publish
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: env

### What went wrong
- `scripts/excalibur_blog_wp_publish.py` requires `import paramiko` for SSH transport.
- Cloud/runtime image had no `paramiko`; `apt python3-paramiko` unavailable; first publish crashed with `ModuleNotFoundError`.

### How the agent recovered this run
- Installed with `pip3 install --break-system-packages paramiko` (PEP 668 externally-managed env).
- Re-ran publish successfully after install.

### Durable fix needed before next run
- Add `paramiko` to Cloud environment deps (`.cursor/environment.json` / snapshot install / requirements).
- Document in pitfalls + publish skill: preflight `python3 -c "import paramiko"` before SSH publish.
- Prefer apt/venv pin over ad-hoc `--break-system-packages` when possible.

### Suggested files to inspect/change
- `.cursor/environment.json`
- `shared/agent-pipeline-pitfalls.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_doctor.py` (optional env dep check)

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1255-publish-http-gateway-504-ssh-php-exec
status: open
run_date: 2026-07-18
role: excalibur-blog-publish
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: high
category: publish

### What went wrong
- SSH upload of `excalibur-blog-publish-once.php` (~5.6MB with cover+inline base64) succeeded.
- Local HTTP trigger timed out at 120s; Cloud WebFetch/urllib fallback got Gateway 504 (~120s).
- Script deletes bootstrap in `finally` after fallback timeout → second HTTP attempt lost the file.
- Same class of failure as AS08/AS09 (then cured with curl `--max-time 300` over FTP); now transport is SSH-only and HTTP path still too short for heavy media payloads.

### How the agent recovered this run
- Workaround: SSH upload + SSH exec `/usr/local/bin/php8.2 -d memory_limit=512M -d max_execution_time=600 excalibur-blog-publish-once.php` (~143s) → PASS.
- Wrote `wp-publish-result.json`, updated ledger/log/promotion/handoff; cleaned bootstrap.

### Durable fix needed before next run
- Add SSH-exec trigger path in `excalibur_blog_wp_publish.py` (prefer over HTTP for large payloads / when HTTP times out).
- Increase HTTP timeout and/or keep bootstrap until a successful trigger response (do not delete on fallback wait timeout before agent can refetch).
- Pre-seed `memory/webfetch-response.txt` watcher or longer fallback wait; document php8.x binary candidates on host.
- Set `SSH_ROOT=.` in Cloud Secrets (cwd is WP root; `SSH_PATH=.../public_html` is not a valid SFTP path from login cwd).

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py` (`publish_via_ssh` / `trigger_bootstrap_http`)
- `skills/publish-excalibur-blog/SKILL.md`
- `shared/excalibur-wp-publish-contract.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20260718-1245-indexer-interlink-suggestions-live-site-base
status: open
run_date: 2026-07-18
role: excalibur-blog-indexer
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_interlinker.py --apply` with live `$PUBLIC_SITE_URL` пишет `site_base` в `memory/blog/interlink-suggestions.json`.
- Первый commit indexer пропустил secret-scan для этого JSON (live base попал в git history); llms генерировали отдельно с `[REDACTED]`.

### How the agent recovered this run
- Fixup commit: заменил `site_base` на литерал `[REDACTED]` в `interlink-suggestions.json` и запушил.
- llms.txt / llms-full.txt изначально с `--site-base '[REDACTED]'`.

### Durable fix needed before next run
- Interlinker: default/`--commit-safe` пишет `[REDACTED]` в JSON report (как ожидалось в fixer notes), live URL только для apply href если нужно.
- Indexer skill/pitfalls: после interlinker проверять `PUBLIC_SITE_URL not in interlink-suggestions.json` перед git add.
- Doctor/docs: не требовать `--blog-path` у llms generator (см. INC-1521).

### Suggested files to inspect/change
- `scripts/excalibur_blog_interlinker.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1520-director-topic-id-prefix-as-vs-b
status: open
run_date: 2026-07-18
role: excalibur-blog-director
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_today.py` вернул `needs_scout` / пустой `SUGGESTED_TOPIC_ID`, потому что regex topic_id только `B\d+`, а пул тем Авто-Сейлс — `AS01`…`AS09`.
- Директор вручную выбрал AS04 (P0, utility PASS).

### How the agent recovered this run
- Игнорировал пустой suggested id; взял AS04 из `blog-topics.md` после utility gate и проверки ledger/WP slug.

### Durable fix needed before next run
- Расширить regex/парсер topic_id в `excalibur_blog_today.py` на префикс `AS\d+` (и другие буквенные префиксы ниши).
- Обновить director skill: если suggested пустой, но в пуле есть free AS* — не уходить в scout без проверки.

### Suggested files to inspect/change
- `scripts/excalibur_blog_today.py`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1521-director-llms-blog-path-cli
status: open
run_date: 2026-07-18
role: excalibur-blog-director
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: low
category: script

### What went wrong
- Doctor: FAIL `llms generator supports --blog-path` — CLI генератора имеет `--blog-dir`, не `--blog-path`.

### How the agent recovered this run
- Зафиксировал в incident queue; пайплайн продолжил (writer/research не зависят от doctor llms check).

### Durable fix needed before next run
- Выровнять doctor check и CLI (`--blog-dir` или alias `--blog-path`).
- Обновить docs/examples.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_llms_generator.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1525-research-wordstat-compound-phrase-totalcount
status: open
run_date: 2026-07-18
role: excalibur-blog-research
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: low
category: api

### What went wrong
- Wordstat MCP для составной фразы «утильсбор корея китай япония» вернул нестандартный ответ (`totalCount` без топа).
- Спрос по странам пришлось собирать отдельными запросами.

### How the agent recovered this run
- Отдельные запросы: «утильсбор корея», «утильсбор япония», «утильсбор китай»; цифры зафиксированы в research-notes без выдумки.

### Durable fix needed before next run
- Research skill: compound multi-country phrase → сразу split на страновые запросы при `totalCount`-only.
- Документировать в pitfalls рядом с scout Wordstat cluster-first.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1526-research-notes-gate-tech-marker-ii-false-positive
status: open
run_date: 2026-07-18
role: excalibur-blog-research
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` `TECH_MARKERS` содержал короткие подстроки `ai` / `ии` без границ слова.
- H1 с «Японии» давал `technical_topic=true` → требование `github_urls>=3` для нетехнической авто-темы → BLOCK.

### How the agent recovered this run
- Добавлен `_marker_matches()` с word-boundary для маркеров длиной ≤3; gate PASS без фейковых GitHub URL.
- Также выровнены форматы `accessed_at:` в source_table и keywords pain/solution/result в pain_solution_map (gate regex).

### Durable fix needed before next run
- Закрепить word-boundary для коротких TECH_MARKERS в gate; добавить unit/smoke-тест на тему с «Японии»/«России».
- Документировать контракт pain_solution_map rows (нужны слова pain|solution|result|боль|…) и `accessed_at:` ≥5.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1530-writer-telegram-href-redacted-on-write
status: open
run_date: 2026-07-18
role: excalibur-blog-writer
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: env

### What went wrong
- Cursor Write tool (или secret-scan на запись) подменил живой Telegram CTA URL в `article.html` на литерал `[REDACTED]` внутри `href="..."`.
- Каталог URL прошёл без подмены; ссылка мессенджера – нет.
- В статье оказался бы мёртвый CTA, запрещённый контрактом Writer.

### How the agent recovered this run
- Перезаписал `article.html` через `python3` + `os.environ["TELEGRAM_URL"]` / `CATALOG_URL`.
- Проверил: литерал `[REDACTED]` отсутствует, env-URL присутствует в файле.
- CTA: 2× каталог + 1× Telegram (в лимитах conversion-map).
- При записи incident queue файл был в «ghost» состоянии (listdir видит, open → ENOENT); восстановлен через os.replace. Предыдущие open-incidents восстановлены из handoff + prior read.

### Durable fix needed before next run
- В Writer skill: писать CTA href только из env через python/shell, не через Write с полным Telegram URL в аргументе.
- Добавить post-write assert: `"[REDACTED]" not in article.html` и env Telegram URL in file.
- Документировать в pitfalls: secret redaction может ломать `href` в HTML; ghost ENOENT на memory/*.md.

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-writer.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1531-writer-incident-queue-ghost-enoent
status: open
run_date: 2026-07-18
role: excalibur-blog-writer
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: high
category: env

### What went wrong
- `memory/pipeline-incident-queue.md` отображался в `listdir`/`os.path.exists`, но `open()`/`Path.read_text()` давали `FileNotFoundError` (ENOENT) несколько попыток подряд.
- Попытка append через recreate уничтожила бы незакоммиченные open-incidents, если бы не восстановление из handoff/prior read.

### How the agent recovered this run
- Перезаписал очередь через `os.replace(tmp, path)`; восстановил INC-1520/1521/1525/1526 из handoff и ранее прочитанного тела; добавил writer INC-1530/1531.

### Durable fix needed before next run
- Исследовать ghost-file на Cloud FS для `memory/*.md`; добавить retry+backup copy перед rewrite.
- Fixer: smoke-тест «listdir видит → open читает» для queue file.
- Не использовать «пустой recreate» при ENOENT без попытки восстановить из handoff/git.

### Suggested files to inspect/change
- `shared/pipeline-incident-fix-contract.md`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/agents/excalibur-blog-fixer.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260616-2015-geo-qa-html-cli-mismatch
status: fixed
run_date: 2026-06-16
role: excalibur-blog-geo-qa
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: qa

### What went wrong
- `article.html` used `<pre><code>` for the llms.txt template, but `excalibur_blog_html_linter.py` forbids those tags and only allows the strict article whitelist.
- `excalibur_blog_research_notes_gate.py` interprets a relative `-o` path inside `article_dir`; passing a repo-relative path as `-o` produced a nested duplicate output before cleanup.
- `.cursor/skills/excalibur-geo-qa/SKILL.md` instructs `excalibur_blog_cannibalization_guard.py --article-dir ...`, while the actual script accepts `--blog-dir`, `--threshold` and `-o/--output`; the documented command exited with argparse error.

### How the agent recovered this run
- Replaced the template block with whitelist-safe `<blockquote><p><br>` markup without changing the article's practical meaning.
- Removed the unintended nested duplicate `research-notes-gate.json` and kept the canonical file in the article directory.
- Re-ran the cannibalization guard with `--blog-dir memory/blog/articles -o memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta/cannibalization-report.json`; verdict PASS.

### Durable fix needed before next run
- Update Writer/QA contracts to avoid `<pre><code>` in `article.html` unless the linter whitelist is intentionally expanded.
- Update `.cursor/skills/excalibur-geo-qa/SKILL.md` to use the actual cannibalization guard CLI or update the script to support `--article-dir`.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_cannibalization_guard.py`
- `scripts/excalibur_blog_html_linter.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Writer/article writing contracts now forbid `<pre>`/`<code>` in `article.html` until the HTML linter whitelist is intentionally expanded, and document whitelist-safe blockquote/table/list alternatives.
- GEO QA skill now documents the actual cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`.
- GEO QA note clarifies that `research_notes_gate.py -o research-notes-gate.json` is relative to `--article-dir`.
files_changed:
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_cannibalization_guard.py --help`
- `rg` check for old Writer `<pre><code>` instruction strings
- `rg` check for old cannibalization `--article-dir` command in source docs
commit: pending-parent-commit


## INC-20260616-2018-cover-toxic-sticker
status: fixed
run_date: 2026-06-16
role: excalibur-blog-cover
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: prompt

### What went wrong
- The one-shot Kie image-to-image quad generation succeeded, but the cover panel included an insulting Russian sticker phrase even though the style preset asks for a non-toxic tone.

### How the agent recovered this run
- Retouched only the offending sticker layer in cover assets with a neutral phrase.

### Durable fix needed before next run
- Explicit negative prompt: no insults / toxic labels in generated sticker text.

### Suggested files to inspect/change
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16

## INC-20260616-1950-scout-wordstat-format
status: fixed
run_date: 2026-06-16
role: excalibur-blog-scout
topic_id: B09
article_dir: n/a
severity: low
category: api

### What went wrong
- `wordstat_get_top_requests` for a narrow phrase returned only `totalCount`.

### How the agent recovered this run
- Used broader Wordstat cluster first.

### Durable fix needed before next run
- Scout: cluster-first Wordstat validation.

### Suggested files to inspect/change
- `.cursor/skills/scout-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16

## INC-20260616-2031-indexer-python-missing
status: fixed
run_date: 2026-06-16
role: excalibur-blog-indexer
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: env

### What went wrong
- Shell examples used `python`, Cloud has only `python3`.

### How the agent recovered this run
- Re-ran with `python3`.

### Durable fix needed before next run
- Standardize on `python3` in Indexer docs.

### Suggested files to inspect/change
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16

## INC-20260616-2042-publish-ssh-root-dot
status: fixed
run_date: 2026-06-16
role: excalibur-blog-publish
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: publish

### What went wrong
- SSH publish root ENOENT; secret-scan blocked commit of public site URL in artifacts.

### How the agent recovered this run
- Retry with `SSH_ROOT=.`; redact site URL in committed artifacts.

### Durable fix needed before next run
- Publish env-check CLI; SSH root fallback to `.`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16

## INC-20260718-1535-geo-qa-task-enum-missing
status: open
run_date: 2026-07-18
role: excalibur-blog-geo-qa
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: env

### What went wrong
- Cloud Task enum не принимает typed `excalibur-blog-geo-qa` (и другие excalibur-blog-* roles).
- Director уже знает fallback; GEO QA выполнен через `Task(generalPurpose)` + `.cursor/agents/excalibur-blog-geo-qa.md` + skill path.

### How the agent recovered this run
- Работал как generalPurpose = одна роль GEO QA; не запускал cover/schema/writer.
- Контракт роли прочитан из `.cursor/agents/` + `.cursor/skills/excalibur-geo-qa/SKILL.md`.

### Durable fix needed before next run
- Зарегистрировать `excalibur-blog-*` в Cloud Task enum ИЛИ зафиксировать в director skill обязательный immediate fallback на generalPurpose без retry typed Task.
- Добавить pitfalls note: typed geo-qa часто отсутствует → сразу generalPurpose.

### Suggested files to inspect/change
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
- `CLOUD-AUTOMATION.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260718-1536-geo-qa-utility-empty-pain-outcome-markers
status: open
run_date: 2026-07-18
role: excalibur-blog-geo-qa
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: script

### What went wrong
- `memory/brief/editorial-policy.json` не содержал `pain_markers_ru` / `outcome_markers_ru`.
- `excalibur_blog_utility_gate.py` всё равно применял `min_pain_markers`/`min_outcome_markers` (default 2/3) при пустых списках → ложный BLOCK (`pain_markers=0 < 2`).
- Pipeline notes уже описывали: enforce only when lists non-empty — код не соответствовал.

### How the agent recovered this run
- Добавил marker lists + min_* в `editorial-policy.json`.
- Исправил gate: проверка pain/outcome только если списки непустые.
- Точечно: CTA live URLs, убран ярлык TL;DR, дописан критерий результата; перегон скриптов → PASS.

### Durable fix needed before next run
- Зафиксировать в pitfalls/skill: utility pain/outcome markers обязательны в policy; empty list = skip.
- Unit/smoke test utility gate на policy без markers (не должен BLOCK).
- Синхронизировать marker lists с `excalibur_blog_human_voice_gate.py` (единый source).

### Suggested files to inspect/change
- `scripts/excalibur_blog_utility_gate.py`
- `memory/brief/editorial-policy.json`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## Fixed incidents

Handled above; commit is pending Director review.

