# Excalibur BLOG — Cover Agent (полный skill)

## Когда запускаться

После **GEO QA PASS**. Вход: `article.html`, `article.meta.json`, handoff `ready_for: excalibur-blog-cover`.

Параллельно с `excalibur-blog-schema`. **Не** править schema и body longread.

---

## Архитектура (зафиксировано)

```text
reference PNG → HTTPS reference_url_hosted (small compressed JPEG preferred)
       ↓
quad-manifest.json (agent fills hooks + scene_hint)
       ↓
quad-mcp-batch.json (1 job, input_urls)
       ↓
PRIMARY: Kie async API (excalibur_blog_kie_gpt_image2_api.py, needs KIE_API_KEY)
       ↓
FALLBACK ONLY: sync MCP gpt-image-2 i2i (timeout-prone -32001 on Cloud 2K quad)
       ↓
canvas-quad.png 2048×1152
       ↓
split → cover.png + inline-01..03.png (1200×675)
       ↓
inject <figure> after H2 in article.html
```

**Запрещено:** 4 отдельных MCP на cover + inline.

---

## Контракты и конфиги

| Путь | Назначение |
|------|------------|
| `shared/kie-gpt-image-api-contract.md` | Kie async API (primary Cloud path) |
| `shared/blog-cover-quad-canvas-contract.md` | канонический quad-контракт |
| `agents/excalibur-blog-cover.md` | agent-md (этот skill дублирует runbook) |
| `memory/cover/blog-hero.json` | visual_lock, outfit_rule, reference_url_hosted |
| `memory/cover/assets/blog-hero-reference.png` | локальный эталон лица |
| `memory/cover/cover-design-code.json` | human hook collage, fake скрины, мемы |
| `memory/cover/quad-style-digital-meme-collage-ru.json` | style preset + design_code link |
| `memory/cover/inline-visual-types.json` | типы inline-панелей |
| `memory/brief/site-brief.md` | blog_hero_id, обложка = крючок |

---

## Панели quad 2×2

| Квадрант | Слот | Содержание |
|----------|------|------------|
| top-left | cover | hook + meme_caption_ru + **герой (reference face)** + design code |
| top-right | inline_1 | visual_type по H2 #1, **без героя** |
| bottom-left | inline_2 | visual_type по H2 #2 |
| bottom-right | inline_3 | visual_type по H2 #3 |

---

## Герой (blog-host)

**Lock (reference i2i):** только лицо и очки с `blog-hero-reference.png`.  
**Одежда (обязательно менять):** под **погоду** сцены (снег/дождь/жара/туман/ночь) и **тему** статьи (порт, таможня, Encar, салон, ямы/комфорт и т.д.). Майку с reference не копировать.  
**Запрет:** кепка, капюшон.  
**Footer / угол обложки:** сайт каталога `avto-sales125.ru` (не Telegram).  
**Стиль:** hyper-realistic action selfie + плашка (blueprint Avto-Sales).

---

## Design code — открываемость

Из `cover-design-code.json`:

1. Fake UI: карточка каталога, отзывы 2GIS, Encar/аукцион, чеклист документов  
   **Угол обложки:** `avto-sales125.ru` (каталог), не Telegram  
   **Запрещено на картинках:** Wordstat, Вордстат, Metrika, Метрика, SEO analytics
2. DIY: torn paper, scotch tape, sticky notes, marker arrows
3. Highlight: маркер на ключевом слове hook
4. Memes: **разные** реакции (cat, facepalm…) — max 1 Drake на холст
5. Формат **16:9**, не Instagram carousel 9:16
6. Inline: полезный UI авто/логистики + лёгкий human layer (стикер, tape)

---

## Пошаговый runbook

### Шаг 0 — прочитать статью

- H2 (до FAQ): первые 3 → inline anchors
- lead, primary query → cover_hook
- `article.meta.json`: h1, topic_id

### Шаг 1 — reference URL

```bash
python scripts/excalibur_blog_hero_reference_url.py
```

Проверить `memory/cover/blog-hero.json` → `reference_url_hosted` (**HTTPS**, желательно небольшой сжатый JPEG лица).  
Fallback env: `BLOG_HERO_REFERENCE_URL`.  
`MCP_KV_TOKEN` ≠ `KIE_API_KEY` — для cover нужен **`KIE_API_KEY`** в Cloud Secrets (см. `shared/kie-gpt-image-api-contract.md`).

### Шаг 2 — manifest

```bash
python scripts/excalibur_blog_quad_manifest.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --merge
```

**Руками** доработать `cover/quad-manifest.json`:

- `cover_hook` — провокация
- `slots.cover.meme_caption_ru` — 2–6 слов
- `slots.cover.scene_hint` — fake скрины + мемы + outfit агента
- `slots.inline_*.scene_hint` — конкретика H2
- `alt` — осмысленные, не «seo картинка»

### Шаг 3 — prompt + batch

```bash
python scripts/excalibur_blog_cover_quad_prompt.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --write-batch
```

Проверить `cover/quad-mcp-batch.json`: **jobs.length === 1**, `input_urls` не пуст.

### Шаг 4 — ONE image job (Kie async, primary)

**Primary (Cloud):** async Kie API — без sync MCP client timeout:

```bash
python3 scripts/excalibur_blog_kie_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Требует `KIE_API_KEY` в Cloud Secrets. Пишет `cover/quad-mcp-result.json` и `cover/kie-image-task.json`.

**Legacy fallback only:** sync `CallMcpTool` → `user-mcp-kv` / `gpt-image-2`  
Аргументы = `jobs[0].mcp_args` из batch. Sync MCP **часто** даёт `-32001` на 2K quad i2i; не повторять create вслепую.

Ожидание: Image to Image, 1 входное фото, aspect 16:9, 2K.

### Шаг 5 — apply

```bash
python3 scripts/excalibur_blog_quad_apply.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --inject-html
```

(`--url` опционален, если есть `cover/quad-mcp-result.json` от Kie или MCP.)

Требует Pillow. Выход: cover, inline PNG, registry, inject в article.html.

### Шаг 6 — fragment

`.cursor/excalibur-blog-fragments/cover.md` — шаблон в `agents/excalibur-blog-cover.md`.

---

## visual_type (inline)

| type | Когда |
|------|-------|
| `comparison_table_ui` | SEO vs GEO, сравнение |
| `workflow_diagram` | структура, шаги, longread |
| `checklist_board` | чеклист, публикация |
| `schema_faq_ui` | FAQ, schema, JSON-LD |
| `tool_screenshot` | Encar / аукционный лист / карточка авто |
| `infographic_card` | цифры, факты |

Keywords + автовыбор: `inline-visual-types.json` + `quad_manifest.py`.

---

## QA перед ✅

- [ ] `KIE_API_KEY` доступен в Cloud (или задокументирован blocker)
- [ ] `reference_url_hosted` — HTTPS, fetchable для Kie
- [ ] 1 image job (Kie async или legacy sync MCP), не 4
- [ ] input_urls в batch / Kie payload
- [ ] cover.png + 3 inline существуют
- [ ] alt в registry для всех 4
- [ ] inline привязаны к H2 (`h2_anchor`)
- [ ] cover: hook + meme caption видны на PNG
- [ ] inline: без лица героя
- [ ] fragment cover.md записан

---

## Blockers → verdict ❌

- нет `KIE_API_KEY` в Cloud → `KIE API BLOCKER` (добавить secret в Dashboard)
- нет reference_url_hosted или не HTTPS
- sync MCP `-32001` без task_id/URL и без Kie fallback
- MCP text-only (без input_urls)
- 4 отдельные генерации
- QUAD SPLIT fail
- inline = meme с ведущим вместо UI

---

## Deprecated scripts

Не вызывать:

- `excalibur_blog_visual_prompts.py`
- `excalibur_blog_visual_apply.py`
- `excalibur_blog_visual_manifest.py`

См. `shared/blog-visual-pipeline-contract.md`.

---

## Эталон (B01)

`memory/blog/articles/B01-primer-seo-stati/cover/` — reference implementation после design code v1.
