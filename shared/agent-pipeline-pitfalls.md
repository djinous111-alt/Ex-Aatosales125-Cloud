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
- `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` должны совпадать с `PAIN_MARKERS` / `OUTCOME_MARKERS` в `excalibur_blog_human_voice_gate.py`; пустые списки в utility_gate → skip+warn, не BLOCK `0 < min`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Opaque MCP image error (`'NoneType' object has no attribute 'get'`) на `gpt-image-2` / flux: сначала проверь баланс через другой Kie tool (часто 402 Credits insufficient). Blocker = credits/top-up, не «битый prompt»; invent PNG запрещён.

## Schema / secret scanner

- В `schema.jsonld` URL из env/`sameAs` помечай хвостом `// pragma: allowlist secret` (JSONC). Publish (`excalibur_blog_wp_publish.py`) снимает маркеры перед WP meta. Без pragma Cursor secret scanner блокирует commit.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Wordstat DNS/`Temporary failure in name resolution` → 2–3 retry с коротким backoff; первый сбой транспорта ≠ мёртвый API.

## Research

- `research_notes_gate` technical GitHub≥3: только token/word-boundary по карточке темы (h1/slug/query), не substring `ai`/`ии` и не скан тела notes (иначе ложные GitHub-требования на авто/налог how-to).
- Официальные `.gov.ru` (в т.ч. minpromtorg) при HTTP 5xx: retry/backoff, затем зеркала ФНС/Гарант/РИА с той же цифрой; не блокируй research из‑за одного 500 на первичном URL.

## Topic IDs / doctor

- Topic ID pattern: `(?:AS|B)\\d+` (Авто-Сейлс `AS01…` и legacy `B01…`). `today.py` / `scout_helper` без AS → ложный `needs_scout`.
- `llms_generator` обязан принимать `--blog-path` (alias `--blog-dir`); doctor это проверяет.
- Cloud image: `python3-numpy` (или `numpy` в pip) нужен interlinker/doctor.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Никогда не передавай `excalibur_blog_llms_generator.py --blog-path /` (или `.`): скрипт вернёт ERROR. Канон: `--blog-dir memory/blog/articles` (+ `--out-dir memory/blog`).

## Publish / cover gate

- `excalibur_blog_wp_publish.py` (dry-run и live) требует `cover/cover.png` + `cover-registry.json` до load/SSH; без них → явный BLOCKER, не invent PNG.
- В `load_article()` не делай локальный `import re` после `re.sub` (schema pragma strip) — будет `UnboundLocalError`; используй module-level `import re`.
