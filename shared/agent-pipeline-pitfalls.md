# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- В частности typed `excalibur-blog-geo-qa` часто отсутствует в Cloud Task enum — запускай `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md`; не пиши QA сам в parent.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Cloud `git commit` может упасть в `pre-commit.cursor` с `invalid variable name`, если в `CLOUD_AGENT_INJECTED_SECRET_NAMES` попал URL/не-идентификатор. Все Cloud commits: `bash scripts/excalibur_git.sh commit …` (не сырой `git commit`).

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
- После rebrand/sync проверяй `memory/brief/editorial-policy.json`: `pain_markers_ru` / `outcome_markers_ru` и алиасы `не делать` / `чек-лист` / `делать:` часто пропадают → utility gate ложно BLOCK. Utility gate при пустых списках обязан warn+skip, не BLOCK.
- Инсайт-блок: не ярлык `TL;DR` / `Быстрый инсайт` (writing-contract example устарел относительно GEO QA skill) — пиши `Инсайт до депозита` / `Инсайт до ставки`.
- CTA в committed HTML: `${CATALOG_URL}` / `${TELEGRAM_URL}` (+ `<!-- pragma: allowlist secret -->` на строке). Не оставляй литерал `[REDACTED]` и не коммить сырые secret URL без pragma.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным.
- Prompt builder **не** вставляет demeaning-slang lemmas даже в negatives (нейтрально: «no insults / no demeaning buyer slang»). `excalibur_blog_kie_gpt_image2_api.py` дополнительно санитизирует prompt перед createTask.
- Outfit: по `blog-hero.json` outfit_rule (погода/тема); **запрещены** white-hoodie lock, hood, cap. Reference URL — только `https://`.

## Research notes gate

- `accessed_at` считается и по `accessed_at: YYYY-MM-DD`, и по ISO-датам в колонке `accessed_at` markdown-таблицы (≥5).
- `pain_solution_map`: достаточно data-rows под `## pain_solution_map` (токены pain/solution в ячейках не обязательны).
- Секция `## github_evidence` не делает тему technical сама по себе.

## Git / Indexer

- Indexer llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir … --blog-path / --out-dir memory/blog` (`--blog-path` из site-brief; для Авто-Сейлс обычно `/`, не `/blog/`).
- Для commit артефактов в Cloud — только через `bash scripts/excalibur_git.sh`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
