# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat `totalCount`-only (без top list) = PARTIAL: запиши totalCount, не выдумывай топ; LSI с широкого cluster.
- `research_notes_gate` short TECH markers (`ai`/`ии`/`api`/`mcp`/`rag`) — только whole-word/bounded; иначе «регистрации» ложно включает technical_topic + GitHub требования.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Нет `cover/cover.png` (Cover BLOCKER / Kie 402) → publish blocker; не invent PNG, ledger остаётся `in_progress`.

## Secret-scan / commit hygiene

- Публичные brand URL (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`), совпадающие с Cloud Secrets, в git требуют allowlist pragma:
  - HTML (`article.html`, promotion-checklist): `<!-- // pragma: allowlist secret -->` на строке с URL;
  - JSONC (`schema.jsonld`): trailing `// pragma: allowlist secret`;
  - llms.txt/llms-full.txt: generator сам добавляет `// pragma: allowlist secret` на http(s) строки.
- Publish снимает JSONC pragmas через `excalibur_jsonc.strip_allowlist_pragmas` перед WP schema meta.
- Ledger `shared/published-articles.md`: коммить только с `[REDACTED]` вместо live site origin.
- Перед bash `${!SECRET_NAME}` фильтруй имена секретов regex `[A-Za-z_][A-Za-z0-9_]*`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` должны жить в `memory/brief/editorial-policy.json`. Пустой список = check skip; отсутствие ключей раньше давало ложный BLOCK (pain=0/outcome=0) на любой статье.
- Recommendation markers: учитывай оба написания `чеклист` и `чек-лист`.
- Инсайт-блок: не начинай с ярлыка `TL;DR` / `Быстрый инсайт` (GEO skill); допустимо `Коротко:` и т.п.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie/MCP `402 Credits insufficient` → needs-human billing; COVER BLOCKER без фейковых картинок.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
