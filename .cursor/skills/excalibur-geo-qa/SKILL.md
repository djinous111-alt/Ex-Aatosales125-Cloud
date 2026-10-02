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

# CTA placeholders are intentional in git. Expand before link-verify, then re-redact.
python3 scripts/excalibur_blog_cta_expand.py \
  --article-dir memory/blog/articles/<dir> \
  --mode expand

python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/link-verify.json \
  --site-base "$PUBLIC_SITE_URL"

python3 scripts/excalibur_blog_cta_expand.py \
  --article-dir memory/blog/articles/<dir> \
  --mode redact

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

python scripts/excalibur_blog_utility_gate.py \
  --article-dir memory/blog/articles/<dir> \
  --output utility-gate-report.json

python scripts/excalibur_blog_human_voice_gate.py \
  --article-dir memory/blog/articles/<dir> \
  -o human-voice-report.json
```

**Pass:** score ≥ 80, CORE-EEAT ≥ 16/20, link-verify pass, **research notes gate PASS**, **utility gate PASS**, **human voice gate PASS**, **beginner-fit PASS**. В `article-qa.md` отдельно зафиксируй: какая боль новичка решена, где показано решение, какой первый результат получит читатель, какие сложные термины объяснены «на пальцах».

**CTA policy:** `href="[REDACTED]"` в article.html — не corruption Writer. Обязательный цикл: expand (`CATALOG_URL`/`TELEGRAM_URL`) → link-verify → re-redact (+ redact `link-verify.json` URLs) перед git. Не коммить live secret URLs.

**Utility policy:** `memory/brief/editorial-policy.json` должен иметь non-empty `pain_markers_ru` / `outcome_markers_ru`. Utility gate skip-when-empty; regression: `python3 scripts/excalibur_blog_utility_gate.py --self-test`.

**Beginner-fit blocker:** статья звучит как для профи/разработчиков/архитекторов, не объясняет термины (API, RAG, MCP, workflow, agent), не даёт первого безопасного шага или требует команды разработчиков без альтернативы для новичка.

Schema и cover — **не** твоя зона (отдельные субагенты после PASS).

Перед commit: `source scripts/sanitize_cloud_secret_names.sh`.
