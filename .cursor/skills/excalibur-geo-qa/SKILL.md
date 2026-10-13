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
  --site-base "${PUBLIC_SITE_URL}"
# Catalog CTA HTTP 5xx при href==CATALOG_URL → soft-pass (warning), не fail.
# В JSON отчёте live URL редактируются в ${CATALOG_URL}/${PUBLIC_SITE_URL}.

python scripts/excalibur_blog_html_linter.py \
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

python scripts/excalibur_blog_utility_gate.py \
  --article-dir memory/blog/articles/<dir> \
  --output utility-gate-report.json

python scripts/excalibur_blog_human_voice_gate.py \
  --article-dir memory/blog/articles/<dir> \
  -o human-voice-report.json
```

**Pass:** score ≥ 80, CORE-EEAT ≥ 16/20, link-verify pass, **research notes gate PASS**, **utility gate PASS**, **human voice gate PASS**, **beginner-fit PASS**. В `article-qa.md` отдельно зафиксируй: какая боль новичка решена, где показано решение, какой первый результат получит читатель, какие сложные термины объяснены «на пальцах».

**Utility markers:** если `pain_markers_ru`/`outcome_markers_ru` в `editorial-policy.json` пусты — это policy regression (doctor FAIL); utility_gate даёт WARN/skip, не ложный BLOCK статьи. Не опустошай эти списки при rebrand/template sync.

**Cloud Task:** typed `excalibur-blog-geo-qa` часто отсутствует в enum → Director запускает эту роль как `Task(generalPurpose)` + `.cursor/agents/excalibur-blog-geo-qa.md`.

**Beginner-fit blocker:** статья звучит как для профи/разработчиков/архитекторов, не объясняет термины без расшифровки «на пальцах», не даёт первого безопасного шага.

Schema и cover — **не** твоя зона (отдельные субагенты после PASS).
