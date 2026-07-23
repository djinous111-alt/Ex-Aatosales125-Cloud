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

## Cloud / git commit

- Pre-commit secrets scanner (`pre-commit.cursor`) может упасть с `invalid variable name` на `${!SECRET_NAME}`, если `CLOUD_AGENT_INJECTED_SECRET_NAMES` содержит имена, невалидные как bash identifiers.
- Workaround (пока hook в Cloud env не санитизирует имена): `CLOUD_AGENT_INJECTED_SECRET_NAMES="" git commit ...` — hook выполняется, но не dereferenc'ит битые имена. Крайний случай: `git commit --no-verify` (только если scanner сам ломает commit без секретов в diff).

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`. Секрет `SSH_PATH` читается как alias `SSH_ROOT`.
- **nginx 504 на large payload:** HTTP trigger с base64 cover+inlines (~9MB) часто получает 504 @~120s, пока PHP-FPM всё ещё пишет post/media/meta. Не считай это мгновенным FAIL: проверь live WP REST (по slug) + HEAD 200, запиши OK-строки в `memory/webfetch-response.txt` пока скрипт ждёт fallback (до ~300s). Host CLI `php` 5.x не запускает WP bootstrap — только web SAPI.
- Нужен `paramiko` в runtime image (`pip install paramiko` / requirements), иначе SSH upload не стартует.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Рекомендации в теле: маркеры из `memory/brief/editorial-policy.json` → `recommendation_markers_ru` (напр. «Сделайте»/«Не делайте», «Шаг N»). **Запрещён** шаблонный ярлык «TL;DR / Быстрый инсайт» в blockquote-выжимке.

## QA / utility policy

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` **обязан** содержать непустые `pain_markers_ru` / `outcome_markers_ru` и `article_required_signals.min_pain_markers` / `min_outcome_markers`. Пустые списки = policy drift; `utility_gate` soft-skip (warning), но это аварийный режим — восстанови маркеры до следующего run. Smoke: `python3 scripts/excalibur_blog_utility_gate.py --article-dir <dir>` после правок policy.

## Research / tech markers

- `research_notes_gate` помечает `technical_topic` только по полям карточки темы (h1/queries/intent/slug) с **token-match**, не substring: `ai`≠`pain`, `ии`≠`Японии`. Автоимпорт JP/KR/CN и бытовые чек-листы — **non-tech**: GitHub ≥3 и official developer docs **не** требуются.
- Официальный портал (напр. ЭПТС) HTTP 5xx → вторичные брокерские/отраслевые источники + явная пометка в notes.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie `gpt-image-2` **402 Credits insufficient** → emergency: Cursor `GenerateImage` + `reference_image_paths=[memory/cover/assets/blog-hero-reference.png]`, aspect 16:9, prompt из `cover/quad-mcp-prompt.txt` → часто 1536×1024 → LANCZOS resize **2048×1152** → `excalibur_blog_cover_quad_split.py --inject-html`. Записать `method: emergency_GenerateImage` в `cover/quad-mcp-result.json`. Канон — снова Kie после top-up кредитов (needs-human).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `excalibur_blog_llms_generator.py` CLI: только `--blog-dir`, `--site-base`, `--out-dir` (и опционально site-name/desc). Флага **`--blog-path` нет** — argparse упадёт.
