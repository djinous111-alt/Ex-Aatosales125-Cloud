# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Typed Task `excalibur-blog-*` часто **нет** в Cloud enum → канон: отдельный `Task(generalPurpose)` на каждую роль + `.cursor/agents/<role>.md` + `.cursor/skills/<skill>/SKILL.md` (см. `AGENTS.md`, `CLOUD-AUTOMATION.md`). Не ждать регистрации typed enum.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

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
- Publish требует `paramiko` (SSH/SFTP). Cloud install: `requirements.txt` + `.cursor/cloud-agent-install.sh` должны ставить `paramiko`; doctor проверяет модуль.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Гос-порталы: перед цитированием проверяй DNS/HTTP (link-verify). Канон проверки ЭПТС (СЭП): `https://elpts.ru/` — **не** `portal.elpts.ru` (NXDOMAIN). Не копировать hostname из вторичных статей вслепую.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Outfit героя = погода/тема из `scene_hint` + `blog-hero.outfit_rule`; **не** hardcode white hoodie. NO cap / NO hood worn.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `excalibur_blog_scout_helper.py` обязан читать `memory/topics/live-wp-occupied-ids.json` (mapped IDs + `avoid_query_fragments` + occupied slugs). Ledger AS* после rebrand ≠ полный live WP.
- MCP `wordpress_*` может указывать на **другой** сайт; denylist = `today.py` recent posts + occupied-ids, не MCP WP search.
- Держи extras в denylist даже вне recent window: автовоз/доставка/перегон, korea-vs-china comparison.

## Research

- `research_notes_gate` определяет `technical_topic` token-boundary по metadata темы, не substring `ai` внутри `reader_pain`. How-to/checklist авто-темы могут иметь `github_evidence: N/A`.

## Writer / utility gate

- `editorial-policy.json` должен содержать непустые `pain_markers_ru` / `outcome_markers_ru` (в sync с human-voice gate). Utility gate пропускает pain/outcome check только если списки пустые.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` / `--out-dir` / `--commit-safe` (флага `--blog-path` нет). Doctor проверяет `--blog-dir`.
- Schema/llms commits: `source scripts/excalibur_blog_filter_injected_secret_names.sh`; public URLs → `pragma: allowlist secret` или `--commit-safe`.
