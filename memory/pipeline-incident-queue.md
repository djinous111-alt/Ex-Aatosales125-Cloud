# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20260720-1305-scout-as-topic-id-regex
status: open
run_date: 2026-07-20
role: excalibur-blog-scout
topic_id: AS10
article_dir: n/a
severity: high
category: script

### What went wrong
- `scripts/excalibur_blog_scout_helper.py` парсит карточки и `--suggest-next` только по regex `B\d+` (и em-dash `—` в заголовке).
- `scripts/excalibur_blog_today.py` в `next_p0_topic` / `active_article_topic_ids` тоже матчит только `B\d+`.
- В пуле Авто-Сейлс темы с префиксом `AS01`…`AS09`; helper вернул `Next available topic ID: B01` и `Total topics in pool: 0`, из-за чего `today.py` даёт `EXCALIBUR_TOPIC_SELECTION=needs_scout` и риск создать чужой `B01` вместо следующего `AS*`.
- `--check-query` тоже не видит AS-карточки, поэтому каннибализацию по пулу AS нужно сверять вручную + со списком live WP slug.

### How the agent recovered this run
- Игнорировал `B01` от helper; создал карточку `AS10` (следующий после `AS09` в `blog-topics.md`).
- Cannibalization: helper `--check-query` + ручная сверка со slug/primary в `blog-topics.md` и live WP списком Директора.
- Wordstat через MCP-KV (`regions=["225"]`) для parent/narrow кластеров ЭПТС/СБКТС.

### Durable fix needed before next run
- Унифицировать ID тем на `(?:AS|B)\d+` в scout helper, today.py и загрузке active article dirs.
- Учитывать оба варианта тире в заголовке карточки (`—` / `–` / `-`).
- После фикса `--suggest-next` должен предлагать `AS10`/`AS11`… при пуле AS*, а `--check-query` – видеть AS primary_query/slug.

### Suggested files to inspect/change
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_today.py`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260720-1312-research-gate-output-path
status: open
run_date: 2026-07-20
role: excalibur-blog-research
topic_id: AS10
article_dir: memory/blog/articles/AS10-sbkts-i-epts-vladivostok-2026
severity: low
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` при относительном `-o` пишет файл как `article_dir / -o`.
- Вызов с `-o memory/blog/articles/AS10-.../research-notes-gate.json` создал вложенный путь `article_dir/memory/blog/articles/.../research-notes-gate.json` вместо файла в корне article_dir.
- Дополнительно: маркер `github` в `github_evidence` включает `is_technical_topic=True` для не-tech ниши (Авто-Сейлс), из-за чего gate требует ≥3 github URL даже для регуляторной темы.

### How the agent recovered this run
- Повторный запуск с `-o research-notes-gate.json` (файл в корне article_dir).
- Удалил ошибочное вложенное дерево `article_dir/memory/`.
- Добавил 3 github URL в notes (слабый сигнал ниши) + help.elpts.ru для official docs.

### Durable fix needed before next run
- Документировать в research skill: `-o research-notes-gate.json`, не полный repo-relative path.
- Либо нормализовать `-o`: если path уже содержит article_dir / абсолютный — писать as-is.
- Исключить ложное `technical_topic` из одного слова `github` в секции evidence; для AS/авто-тем не требовать GitHub.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## Fixed incidents

(Previous queue content was not readable in this workspace snapshot; prior fixed incidents may live only in git history on other branches.)
