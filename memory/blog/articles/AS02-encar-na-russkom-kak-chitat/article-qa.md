# Article QA — AS02

**topic_id:** AS02  
**slug:** encar-na-russkom-kak-chitat  
**article_dir:** memory/blog/articles/AS02-encar-na-russkom-kak-chitat  
**date:** 2026-10-16  
**verdict:** PASS  
**score:** 90

## Beginner-fit / pain → solution → result

| Проверка | Результат |
|----------|-----------|
| Боль новичка | Сайт на корейском, кривой перевод, непонятно что смотреть первым, страх купить «кота в мешке» (lead) |
| Где решение | H2: перевод браузера → манвоны → чеклист 8 полей → схема X/W → мост на Trust/Carhistory → подборщик |
| Первый результат | Заполненный мини-чек по одному лоту + правило стоп/дальше до депозита (секция «Что дальше») |
| Термины «на пальцах» | Манвоны (×10 000), VIN/차대번호, лист 성능점검, коды X/W/C/A/U/T, Encar Diagnosis vs лист |
| Beginner-fit | **PASS** — без API/RAG/MCP-жаргана; первый безопасный шаг на ПК без депозита |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-16; errors=[] |
| fact-check | PASS | 8 stats; 1 verified (2026); 7 unverified (манвоны-примеры 1890/10 000/…) — в research-notes / AutoKoreaGroup |
| link-verify | PASS | 3/3 OK (internal AS09 + catalog + Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long (склейка таблиц/workflow парсером); Flesch RU 71.1 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action_markers 27; pain 17; outcome 20; FAQ×6; tables×2 |
| human-voice gate | PASS | `human-voice-report.json`; pain/outcome/reader_story overlap OK; author registry match |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary «encar на русском» в title/H1/description; H2 how-to; CTA; 1 internal blog (AS09) |
| GEO / citability | 23/25 | Insight «Коротко по делу», таблицы, FAQ×6, чеклисты, workflow blockquote |
| CORE-EEAT lite | 15/15 | 20/20 (см. ниже) |
| Human voice | 15/15 | 0 AI-slop; human-voice PASS; без TL;DR/generic Fact Check |
| Fact safety | 12/15 | Цифры манвонов и ~45k/80%/3,3% в research-notes; soft unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9097 chars, FAQ, CTA×3, без форм |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 20/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «encar на русском» в meta title / H1 |
| C02 | ✓ | Lead — боль + прямой ответ без «в этой статье» |
| C03 | ✓ | Читатель: новичок на Encar, риск депозита / «кота в мешке» |
| C04 | ✓ | Манвоны, VIN, 성능점검, X/W объяснены при первом появлении |
| O01 | ✓ | H2 = action outline research (перевод → цена → 8 полей → схема → история → подборщик) |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблицы + чеклисты, mode B |
| R01 | ✓ | Insight-блок, таблицы, FAQ |
| R02 | ✓ | AuctionsAPI / AutoKoreaGroup / Encar в Fact Check Box + research-notes |
| R03 | ✓ | Нет цен лотов/% пошлин; манвоны как формула с пометкой «не под ключ» |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «читать карточку до депозита»; Trust/Carhistory только мост на AS09 |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс; author_id avtosales-editorial |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | X/W на силовых, нет листа, частник, давление на депозит |
| Ept02 | ✓ | Internal link на AS09 Trust/Carhistory |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблиц/workflow)
- Flesch RU: 71.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/ol) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **fact-check soft:** примеры манвонов (1890 → 18 900 000) и статистика ~45k/80%/3,3% — уже в research-notes; при желании дописать в fact-bank.
2. **slop over-long:** артефакт таблиц; правки не критичны.

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **20/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
