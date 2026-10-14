---
name: excalibur-geo-qa
description: Excalibur BLOG GEO QA — fact-check, link verify, linter, slop, cannibalization, article-qa PASS.
---

# Excalibur BLOG — GEO QA

## Когда

После `article.html` + `article.meta.json` от Writer. **До** cover/schema (их делает директор параллельно после PASS).

## Скрипты (обязательно)

```bash
python scripts/excalibur_blog_research_notes_gate.py \
  --article-dir memory/blog/articles/<dir> \
  -o research-notes-gate.json

python scripts/excalibur_blog_fact_checker.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/fact-check-report.json

python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/link-verify.json \
  --site-base "$PUBLIC_SITE_URL"

# Soft-pass (не blocker): catalog host HTTP 5xx → soft_pass=catalog_5xx;
# egrul.nalog.ru SSL/5xx → egrul_ssl / egrul_5xx. Telegram 200 обязателен.
# Перед verify CTA href должны быть живыми URL из env (не литерал [REDACTED]).

python3 scripts/excalibur_blog_html_linter.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/html-linter-report.json
```

HTML linter **блокирует оглавление в теле** (`<ol>/<ul>` с 3+ ссылками `href="#..."`) и любые теги вне whitelist, включая `<pre>`/`<code>`. При fail — Writer удаляет TOC (после инсайт-блока сразу `<p>`) или заменяет код/шаблон на whitelist-safe HTML (`<blockquote><p>...<br>...</p></blockquote>`, таблицу или список). Инсайт-блок не должен начинаться с шаблонного ярлыка `TL;DR` или фразы `Быстрый инсайт`. `research_notes_gate.py -o research-notes-gate.json` пишет файл внутри `--article-dir`; не передавай туда repo-relative путь с повтором `memory/blog/articles/...`.

```bash
python scripts/excalibur_blog_slop_detector.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/slop-detector-report.json

python scripts/excalibur_blog_cannibalization_guard.py \
  --blog-dir memory/blog/articles \
  -o memory/blog/articles/<dir>/cannibalization-report.json

python3 scripts/excalibur_blog_utility_gate.py \
  --article-dir memory/blog/articles/<dir> \
  --output utility-gate-report.json

# utility_gate читает pain_markers_ru / outcome_markers_ru из
# memory/brief/editorial-policy.json (min_pain_markers / min_outcome_markers).
# Если списки пусты — всегда 0 hits: не «чинить» статью, а восстановить policy.

python3 scripts/excalibur_blog_human_voice_gate.py \
  --article-dir memory/blog/articles/<dir> \
  -o human-voice-report.json
```

**Pass:** score ≥ 80, CORE-EEAT ≥ 16/20, link-verify pass (с учётом catalog_5xx soft-pass), **research notes gate PASS**, **utility gate PASS**, **human voice gate PASS**, **beginner-fit PASS**. В `article-qa.md` отдельно зафиксируй: какая боль новичка решена, где показано решение, какой первый результат получит читатель, какие сложные термины объяснены «на пальцах».

**Beginner-fit blocker (Авто-Сейлс):** статья звучит как для перекупов-профи без простого входа покупателя, не объясняет термины (аукционный лист, СВХ, утильсбор, Encar) или не даёт первого безопасного шага до депозита.

Schema и cover — **не** твоя зона (отдельные субагенты после PASS).
