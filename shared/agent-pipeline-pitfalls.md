# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- В том числе typed `excalibur-blog-geo-qa` может отсутствовать в Cloud Task enum: Директор обязан запускать GEO QA как отдельный `Task(generalPurpose)` с контрактами роли, не писать QA самому.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Topic id regex: `((?:AS|B)\d+)` — после rebrand wipe не оставлять только `B\d+` (AS## исчезнут из today/scout).
- `llms_generator` / interlinker обязаны сохранять `--blog-path` (doctor + fixer regression smoke).

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
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT`/`SSH_PATH` в Cloud Secrets на `.`.
- `SSH_PATH` алиасится в `SSH_ROOT` в `load_env`; `paramiko` ставится через `.cursor/cloud-agent-install.sh` / `requirements.txt`.
- Ledger AS01–AS07+ обязан отражать live WP denylist; иначе today/scout снова предложат уже LIVE topic_id.

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
- Outfit: `outfit_lock_from_hero` + scene_hint WEATHER+OUTFIT; **запрещён** hardcoded `white hoodie`.
- Sync MCP `gpt-image-2` часто даёт `-32001` timeout → это не финальный blocker: сразу `scripts/excalibur_blog_kie_gpt_image2_api.py` (createTask → recordInfo), без второго sync MCP create.
- После split `quad_apply` по умолчанию штампует угол `avto-sales125.ru` (`excalibur_blog_cover_corner_stamp.py`); не запускай второй image job из-за отсутствующего corner brand.

## Scout / Research Wordstat

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Пустой Wordstat payload `{}` / truncated без top phrases = soft-fail: `WORDSTAT NOTE` в research-notes + fallback на parent/secondary; не выдумывать primary volumes.
- Research gate: TECH_MARKERS с word-boundary (`ai` ≠ substring в `pain` / `комплектации`).

## Schema / commits

- `schema.jsonld` с PUBLIC_SITE_URL/CTA: однострочный JSON + root `"_scan": "pragma: allowlist secret"` (как link-verify CTA lines).
- Перед `git commit` в Cloud: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit …` — иначе URL-хвост в `CLOUD_AGENT_INJECTED_SECRET_NAMES` ломает hook (`invalid variable name`).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Коммиты indexer/writer/publish — через `scripts/excalibur_git.sh` / filter secret-env (см. выше).
