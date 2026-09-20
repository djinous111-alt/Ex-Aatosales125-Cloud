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

- Крупный bootstrap (cover+inline): nginx **504** на HTTP → `excalibur_blog_wp_publish.py` fallback **SSH PHP CLI** (`/usr/local/bin/php8.2`). Нужен paramiko (`requirements.txt` / cloud-agent-install).
- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- **CTA href:** никогда не вставляй литерал `[REDACTED]` в `article.html`. Placeholder допустим в SERP/ledger/notes (secret-scan), но не в живых ссылках. Telegram CTA = env `TELEGRAM_URL` или канон `t.me` + handle из site-brief (`@avtosales125`, как AS08/AS09). При commit secret-scan: `<!-- pragma: allowlist secret -->` на строке CTA. Перед handoff: `'[REDACTED]' not in html` и `'t.me/' in html`.

## QA

- `schema.jsonld` secret-scan: same-line `"_excalibur_scan": "pragma: allowlist secret"` (не JSONC `//`). Publish strips `_excalibur_scan` before WP meta.
- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json`. Пустые списки → check **skipped** (не BLOCK). Writer обязан использовать точные `recommendation_markers_ru` (`не делайте`, `шаг `, `проверьте`, `избегайте`), а не только «Делать/Не делать».

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie `402 Credits insufficient` → human top-up `KIE_API_KEY`. Emergency: **один** Cursor GenerateImage (quad canvas), затем `quad_apply --canvas …` (auto-normalize 2048×1152). Никогда 4 GenerateImage.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `scout_helper --suggest-next` считает **AS* и B*** карточки; next ID = следующий свободный **Bxx** с учётом ledger + article dirs. Всегда сверяй с `EXCALIBUR_RECENT_WP_POSTS` из `today.py`: если на WP уже был B01/тот же slug — начинай с B02+, не слепо с B01.
- `--check-query` сравнивает и с AS*-пулом, и со slug/query из `shared/published-articles.md`.

## Research

- `research_start` при записи `research-serp.json` редактирует host из `PUBLIC_SITE_URL`/`WP_SITE_URL` в `[REDACTED]` (иначе secret-scan блокирует commit).
- `research_notes_gate` определяет `technical_topic` по **token-boundary** маркерам; поле `reader_pain` само по себе не делает тему technical и не требует github_urls≥3.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: только `--blog-dir` + `--out-dir`; устаревший `--blog-path` **не существует** (argparse error).
- URL в `llms.txt` / checklist: same-line `// pragma: allowlist secret` при secret-scan.
