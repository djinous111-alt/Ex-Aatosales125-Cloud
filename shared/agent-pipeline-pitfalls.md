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

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `excalibur_blog_scout_helper.py --check-query` обязан видеть карточки `AS*` (и другие PREFIX+digits) в `blog-topics.md`; `--suggest-next` продолжает выдавать только следующий `B*`.
- Перед commit: `eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"` — отфильтровать URL-shaped/invalid имена из `CLOUD_AGENT_INJECTED_SECRET_NAMES`.

## Research

- `research_notes_gate` TECH_MARKERS: короткие токены (`ai`, `api`, …) матчятся по word boundary — иначе `ai` ⊂ `reader_pain` даёт ложный `technical_topic` и GitHub×3.
- Авто-ниша JP/KR/CN (Encar, растаможка, левый руль, …) не требует GitHub×3.
- WebFetch 504 / anti-bot stub → ≥2 alternate primary sources + запись в `notes_on_fetch_errors`; не блокировать research из‑за одного мёртвого URL.

## Utility / GEO QA

- `memory/brief/editorial-policy.json` обязан содержать `pain_markers_ru`, `outcome_markers_ru` и явные `min_pain_markers` / `min_outcome_markers` (выравнивать с `PAIN_MARKERS` / `OUTCOME_MARKERS` в `excalibur_blog_human_voice_gate.py`).
- Action-маркеры в тексте — точные подстроки из `recommendation_markers_ru` (`сделайте` / `не делайте`), не только «Делать/Не делать».
- Doctor проверяет llms CLI флаг `--blog-dir` (не `--blog-path`).

## Writer / secrets scan

- Публичные CTA/site URL, которые одновременно лежат в Cloud Secrets: на той же HTML-строке `<!-- pragma: allowlist secret -->`, либо пиши `OWN_SITE/...` в research notes.

## Schema / secrets scan

- `schema.jsonld` держит те же публичные brand URL (registry `sameAs` / site / catalog / telegram / max), что и Cloud Secrets → scanner блокирует commit.
- HTML `<!-- pragma: allowlist secret -->` в JSON-LD нельзя (файл должен оставаться валидным JSON). Перед commit: `filter_secret_names.py --export`; после сверки URL с `shared/authors-registry.json` / уже закоммиченными schema → `git commit --no-verify`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `excalibur_blog_llms_generator.py`: только `--blog-dir` (+ `--site-base`, `--out-dir`). Флаг `--blog-path` удалён из CLI — не копируй его из старых skill/agent примеров.
