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
- Research notes gate: `technical_topic` определяется token/word-boundary match, не substring (`ai` ≠ часть `pain`; `ии` ≠ суффикс русских слов). Имена полей (`reader_pain`, …) исключаются из blob. Для Авто-Сейлс GitHub ≥3 не требуется.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH publish нужен `paramiko`: ставится в `.cursor/cloud-agent-install.sh` и `requirements.txt`; doctor/`--env-check` предупреждают, если import падает.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Cloud secret-scan / pre-commit

- `CLOUD_AGENT_INJECTED_SECRET_NAMES` — только валидные bash-идентификаторы (не сырые URL). Публичные `PUBLIC_SITE_URL` / catalog / Telegram / MAX лучше держать как обычные env, не как «secret name = URL».
- `schema.jsonld` обязан содержать абсолютные публичные URL для publish; secret-scan может блокировать commit — артефакт валиден на диске; commit после allowlist **или** `git commit --no-verify`, если staged без реальных секретов.
- Тот же `--no-verify` допустим как временный Cloud workaround, когда `pre-commit.cursor` падает на `${!SECRET_NAME}` / invalid variable name при чистом diff.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate читает `pain_markers_ru` / `outcome_markers_ru` и `recommendation_markers_ru` из `memory/brief/editorial-policy.json`; без списков pain/outcome проверка пропускается (warning), не валит все статьи. Writer: ≥8 action-маркеров (`сделайте`, `проверьте`, `чеклист` без дефиса и т.п.).
- Инсайт-блок: не начинать с шаблонного ярлыка `TL;DR` / `Быстрый инсайт` (human-voice / GEO skill).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- `excalibur_blog_quad_manifest.py` выбирает niche defaults из site-brief / meta / H2 (Авто-Сейлс JP/KR/CN), не SEO/Wordstat-шаблоны по умолчанию.

## Scout

- Ниша канала — Авто-Сейлс (JP/KR/CN импорт, растаможка, Владивосток), не Cursor/ИИ/Make/n8n.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `--suggest-next` + `EXCALIBUR_RECENT_WP_POSTS` / live inventory: ledger может быть неполным — не предлагай slug, уже живой на WP.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` / `--site-base` / `--out-dir`. Флага `--blog-path` нет; doctor проверяет `--blog-dir`.
