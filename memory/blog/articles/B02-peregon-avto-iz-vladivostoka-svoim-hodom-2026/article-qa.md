# Article QA — B02 (re-QA after Writer FIX)

**topic_id:** B02  
**slug:** peregon-avto-iz-vladivostoka-svoim-hodom-2026  
**article_dir:** memory/blog/articles/B02-peregon-avto-iz-vladivostoka-svoim-hodom-2026  
**date:** 2026-10-17  
**verdict:** PASS  
**score:** 88  
**COVER_SCHEMA_GO:** yes

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | reconfirm; research_date=2026-10-17 |
| fact-check | PASS | 12 stats; verified 4 / unverified 8 (кейсы ₽ / 01.03.2025 — в research-notes) |
| link-verify | PASS | 6/6 OK (unique hrefs); CTA catalog/Telegram/MAX = env; internal blog×2 = 200; elpts.ru = 200. Catalog soft-pass rule n/a (HTTP 200, не 503) |
| html-linter | PASS | 0 errors; TOC нет |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/схемы); Flesch RU 64.8 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action 16; pain 18; outcome 8; FAQ×7; table×1 |
| human-voice-gate | PASS | warnings=[] |

## Beginner-fit / pain → solution → result

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Выдали авто → едут без ОСАГО; ловушка «номера и страховку потом» (lead, Игорь) |
| Где решение | H2: go/no-go → осмотр → ЭПТС/ОСАГО/10 суток → первый день → чек-лист 12 → «сегодня» |
| Первый результат | Критерий в H2 чек-листа + 3–5 шагов «Что сделать сегодня» до FAQ |
| Термины | ЭПТС, ТПО, СВХ, 10 суток, ОСАГО на VIN, транзиты vs учёт — на пальцах |
| beginner-fit | PASS |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в H1/title; H2 actionable; CTA live; internal blog×2 |
| GEO / citability | 23/25 | Insight blockquote (без TL;DR-ярлыка), таблица, схема дня, FAQ×7, чеклисты |
| CORE-EEAT lite | 15/15 | 19/20 |
| Human voice | 15/15 | human-voice PASS, 0 warnings |
| Fact safety | 12/15 | Ориентиры ₽ как кейсы; 8 unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; FAQ RU; CTA env; без `$…` |
| Utility / gates | 10/10 | research + utility + link + human-voice PASS |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в H1 / meta |
| C02 | ✓ | Lead — сценарий + ловушка |
| C03 | ✓ | Покупатель после выдачи во Владивостоке |
| C04 | ✓ | ЭПТС / ТПО / СВХ / 10 суток |
| O01 | ✓ | H2 = чек-лист до выезда |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + blockquote, mode B |
| R01 | ✓ | Insight, go/no-go, схема дня, критерий |
| R02 | ✓ | Факты в research-notes |
| R03 | ✓ | Цены как вилки кейсов |
| R04 | ✓ | FAQ: ответ в 1-м предложении |
| E01 | ✓ | Угол «до выезда своим ходом» |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA каталог×3 / Telegram×2 / MAX×1 |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop = 0 |
| Ept01 | ✓ | Зима / дальняк / нет напарника → доставка |
| Ept02 | ✓ | Internal `/blog/…` ×2 + live CTA |

**Target:** ≥16/20 ✓ · veto: нет

## Link verify

- total unique checked: 6, failed: 0, verdict: pass
- CTA href совпадает с env `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` (catalog×3, telegram×2, max×1)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 64.8

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes | cover/schema: **GO**

## Blockers

- нет

## FIX cycle (closed)

1. Writer FIX: live CTA URL, soft (insight label, FAQ RU, list sizes, internal links).
2. Utility markers/policy уже PASS на re-QA (action 16 / pain 18 / outcome 8).
3. Re-QA 2026-10-17: все скрипты PASS → score 88.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — **COVER_SCHEMA_GO=yes**
