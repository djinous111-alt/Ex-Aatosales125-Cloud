# Excalibur BLOG — Quad Canvas (1 MCP → 4 панели)

Cover-агент работает **после** `article.html` + GEO QA PASS.

## Главное правило

**Один** image job → один холст `2048×1152` (2×2, каждая панель 16:9) → split в `cover.png` + `inline-01..03.png`.

| Панель | Роль | Герой |
|--------|------|-------|
| **top-left cover** | Крючок + RU-мем | **да**, лицо с reference (`input_urls`); **одежда — на усмотрение агента** |
| **3 inline** | Полезность по H2: таблица, workflow, чеклист, UI | **нет** |

## Image provider order

1. **Preferred:** если есть `KIE_API_KEY` → `scripts/excalibur_blog_kie_gpt_image2_api.py` (async createTask → poll → URL).
2. **Fallback:** sync MCP `gpt-image-2` — один attempt. `-32001 Request timed out` ≠ final blocker: ищи URL/task_id в MCP logs; иначе Kie; не делай второй sync create вслепую.
3. Без URL — не запускай `quad_apply`.

См. `timeout_policy` / `preferred_image_flow` в `cover/quad-mcp-batch.json` (пишет `excalibur_blog_cover_quad_prompt.py`).

## Workflow

```bash
# 1. Публичный URL эталона (обязательно для i2i)
python3 scripts/excalibur_blog_hero_reference_url.py

# 2. Manifest: cover_hook + visual_type для inline
python3 scripts/excalibur_blog_quad_manifest.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> --merge

# 3. Промпт + batch (1 job)
python3 scripts/excalibur_blog_cover_quad_prompt.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> --write-batch

# 4. Preferred: Kie async (если KIE_API_KEY)
python3 scripts/excalibur_blog_kie_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
# Fallback only: ONE CallMcpTool gpt-image-2 по cover/quad-mcp-batch.json

# 5. Скачать canvas + split
python3 scripts/excalibur_blog_quad_apply.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --url "<result_url>" --inject-html
```

## Раскладка 2×2

```text
+------------------+------------------+
|  cover (hero)    |  inline_1 (UI)   |
|  top_left        |  top_right       |
+------------------+------------------+
|  inline_2        |  inline_3        |
|  bottom_left     |  bottom_right    |
+------------------+------------------+
```

Split-скрипт **не режет механически 50/50**: ищет белые gutters у центра холста и режет по ним; затем center-crop до 16:9. Промпт: gutters только на линиях x=1024 / y=576, контент строго внутри квадранта.

## Файлы

| Файл | Кто |
|------|-----|
| `memory/cover/blog-hero.json` | `reference_url_hosted` |
| `memory/cover/inline-visual-types.json` | типы inline-панелей |
| `cover/quad-manifest.json` | cover + inline slots |
| `cover/quad-mcp-batch.json` | **1 job**, `input_urls` |
| `cover/canvas-quad.png` | MCP результат |
| `cover/cover.png`, `inline-01..03.png` | split script |
| `cover/cover-registry.json` | split script |

## Design code (открываемость)

`memory/cover/cover-design-code.json` — human hook collage для cover panel:

- fake скрины (Telegram @avtosales125, отзывы 2GIS, Encar/аукцион, чеклист) — **без Wordstat и без Метрики**
- рваная бумага, скотч, розовые стикеры, маркер
- разные мем-реакции (не один Drake на весь холст)
- 16:9 widescreen, **не** vertical carousel

Inline panels: полезный UI + лёгкий human layer (стикер, tape, mini screenshot).

См. `memory/cover/inline-visual-types.json`. Выбор по keywords H2 в `excalibur_blog_quad_manifest.py`.

## Blockers

- `❌ COVER HERO BLOCKER` — нет `reference_url_hosted` или image job без `input_urls`
- **4 отдельных image jobs** на cover+inline — запрещено
- blind second sync MCP create после `-32001` без URL/task_id
- apply без реального image URL
- inline-панель с meme/host вместо UI/схемы
- обложка без крючка / без `meme_caption_ru`
