# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Typed `excalibur-blog-geo-qa` **часто missing** → сразу `Task(generalPurpose)` с полным GEO QA контрактом; не крутить typed-retry.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Pre-commit secrets scanner: `CLOUD_AGENT_INJECTED_SECRET_NAMES` может содержать non-identifier (URL-like). Install/harden через `scripts/excalibur_blog_harden_precommit_secret_names.sh` (вызывается из cloud-agent-install).

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Outfit default: softshell/jacket/crewneck — **никогда** не hard-code `hoodie` / «белое плотное худи» в prompt builder или default `scene_hint`. Hoodie только в FORBIDDEN/negatives.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Research

- `research_notes_gate` TECH_MARKERS — word-boundary (не substring): `pain` ≠ `ai`, `комплектации` ≠ `ии`. Auto/dealer ниши (Encar, Hyundai, растаможка) не требуют `github_urls >= 3`.
- `accessed_at` засчитывается и как `accessed_at:`, и как колонка markdown-таблицы с ISO-датами.

## QA / policy

- `editorial-policy.json` обязан содержать non-empty `pain_markers_ru` / `outcome_markers_ru` (sync с human_voice_gate). Пустые списки → POLICY BLOCK в utility gate.
- Writer action-маркеры: `сделайте` / `не делайте` / `проверьте` / `шаг ` (не только «Делать:/Не делать:»).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` + `--out-dir` (флага `--blog-path` нет). Committed `memory/blog/llms*.txt` → `--site-base ""` (relative `/blog/...`).
