# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- То же для **geo-qa**: если typed `excalibur-blog-geo-qa` unavailable — отдельный `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md` (не parent-agent).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Topic IDs: `AS\d+` и `B\d+`. `today.py` / scout helper обязаны матчить `((?:AS|B)\d+)`; doctor проверяет regex + discovery AS*.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat `totalCount`-only ответ (без top phrases) = soft warning / low-result signal, не blocker; cluster-first + LSI из рабочих фраз.
- MCP-KV `namespaceStatus: error` / Wordstat tool unavailable → WebSearch-only + явный `wordstat status: unavailable` / `WORDSTAT AUTH WARNING`; **не выдумывать** месячные показы.
- `pain_solution_map` rows должны содержать слова pain|solution|result|боль|решение|результат; `accessed_at:` — ≥5 явных лейблов (даты в таблице без лейбла не считаются).
- `research_start` автоматически редактирует host из `PUBLIC_SITE_URL`/catalog в `research-serp.json` → `example-site.invalid` перед записью (secret scan).
- `CLOUD_AGENT_INJECTED_SECRET_NAMES` должен содержать только bash-идентификаторы (`[A-Za-z_][A-Za-z0-9_]*`), не URL-значения.
- Git commits в Cloud: `bash scripts/excalibur_git.sh commit …` (фильтр secret-name env). Не голый `git commit`, если hook падает на `invalid variable name`.
- Research `TECH_MARKERS`: короткие `ai`/`ии` — только word-boundary; классификация `technical_topic` только по topic card, не по notes/`reader_pain` (иначе «комплектации» / `pain` → ложный GitHub≥3).
- `link-verify.json` пишет `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` / `${TELEGRAM_URL}` placeholders; live hosts не коммитить.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `SSH_PATH` алиас → `SSH_ROOT`; при отсутствии `memory/site.env.local` publish создаёт его из process env (gitignored).
- HTTP bootstrap timeout: `EXCALIBUR_PUBLISH_HTTP_TIMEOUT` / `PUBLISH_HTTP_TIMEOUT` (default **300s**); `--env-check` обязан import-probe `paramiko`.
- При HTTP timeout/`RemoteDisconnected`: сначала REST reconstruct по slug (LIVE → без второго trigger), иначе один WebFetch fallback в `memory/webfetch-response.txt`. Повторный trigger = дубли media `*-1.png`.
- `schema.jsonld` в git: `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}` placeholders; publish гидратирует in-memory, файл не переписывает. Fallback: `"_excalibur_secret_allowlist": "pragma: allowlist secret"` на URL-строках.
- Ledger date: `upsert_publish_ledger` берёт `EXCALIBUR_RUN_DATE`, не `date.today()` контейнера.
- Cloud image: `paramiko` (+ numpy/Pillow) через `.cursor/Dockerfile`, `.cursor/cloud-agent-install.sh` и `requirements.txt`.
- SSH DNS preflight: `--env-check` → `ssh.dns.resolved`. Если `SSH_HOST_DNS` / `gaierror` / empty A на Beget `*.beget.tech` — **PUBLISH BLOCKER**, не выдумывай IP и не ослабляй denylist; нужен human restore DNS или stable SSH IP secret + TCP/22.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA `href` из env (`CATALOG_URL` / `TELEGRAM_URL` / …) должны остаться живыми `https://…`. Literal `href="[REDACTED]"` в `article.html` = QA FAIL; перед commit проверь `https`-count > 0.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- Catalog/site DNS flake в Cloud egress: link-verify soft-fail для hosts из `CATALOG_URL`/`PUBLIC_SITE_URL`/`TELEGRAM_URL`/`MAX_URL` (warning, не blocker).
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Human-voice / research-notes gate: `-o human-voice-report.json` (bare name) → в `--article-dir`; repo-relative `-o memory/blog/.../report.json` резолвится от корня репо, не nested.
- `exactly_five_lists` считает `<li>` **внутри каждого** `<ol>` (не через границы списков).
- `editorial-policy.json` обязан держать `pain_markers_ru` / `outcome_markers_ru` + `_markers_pinned`; doctor pin. Пустые списки → utility gate пропускает pain/outcome checks.
- Инсайт-блок: запрещены ярлыки `TL;DR` / `Быстрый инсайт` (writing-contract + GEO QA + human-voice). Пример: `Инсайт до депозита:`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Outfit: **не** hardcode white hoodie; брать weather/topic из `blog-hero.json` / `scene_hint`.
- Sync MCP `gpt-image-2` `-32001` timeout **или** MCP-KV `namespaceStatus: error` → **Kie** `scripts/excalibur_blog_kie_gpt_image2_api.py` (один batch), не COVER blocker и не blind retry sync create.
- Hero `input_urls`: если WP media HEAD fail + catbox/0x0 down → `excalibur_blog_hero_reference_url.py --provider kie` (file-base64-upload → tempfile.redpandaai.co). Не подставляй недоступный WP media URL в createTask.
- После split `cover_quad_split` автоматически stamp’ит угол `avto-sales125.ru`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal. Research: то же правило для secondary phrases.
- Если MCP-KV недоступен целиком — тот же fallback, что у research: WebSearch + notes, без выдуманных показов.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Runtime llms index может брать `--site-base $PUBLIC_SITE_URL`; **committed** `memory/blog/llms.txt` / `llms-full.txt` — только relative `/blog/<slug>/` (`--relative-urls` или пустой `--site-base`; default при `--out-dir memory/blog`).
- llms generator: `--blog-path` = alias `--blog-dir` + `--relative-urls` (doctor smoke). Indexer без aliases = doctor FAIL — не «чините» только runtime artifact.
