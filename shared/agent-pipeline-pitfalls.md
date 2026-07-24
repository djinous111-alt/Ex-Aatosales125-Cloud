# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (**канон**, включая GEO QA). Не ретрай typed name после отказа enum.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research-notes gate: tech markers — **token/word-boundary** только по полям topic card (`ai` ≠ substring в `pain`). Non-tech (авто-логистика JP/KR/CN) не требует GitHub≥3.
- Для gate: минимум 5× литералов `accessed_at:` и строки pain map с маркерами боль|pain|решение|solution|result|результат.
- `research-serp.json` не должен содержать абсолютный `PUBLIC_SITE_URL` (плейсхолдер `[PUBLIC_SITE_URL]`).

## Scout / topic IDs

- `scout_helper` / `today` учитывают **B\* и AS\***; next B ID = max(B in topics+ledger+dirs)+1.
- После AS→B миграции / ledger reset не начинай с B01, если live WP уже занял B-серию — восстанови строку в `published-articles.md` или форсируй max(B)+1.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- Нужен `paramiko` (`requirements.txt` / `.cursor/cloud-agent-install.sh`); doctor проверяет import.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Большой bootstrap (~8–9MB) → nginx RemoteDisconnected/504 при живом PHP-FPM: wait **~300s** unbuffered + REST recovery by slug; `PYTHONUNBUFFERED=1`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA `href` из `CATALOG_URL`/`TELEGRAM_URL`: на той же строке `<!-- pragma: allowlist secret -->` иначе Cloud secret scan блокирует commit.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate требует непустые `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json`; пустые списки = policy incomplete (не «слабая боль» статьи).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie/MCP 402 Credits insufficient (MCP может маскировать как NoneType `.get`) → skill §4b: один GenerateImage + LANCZOS 2048×1152 + split; top-up credits = needs-human.
- Outfit героя: по погоде/теме сцены, не default white hoodie.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` нет).
