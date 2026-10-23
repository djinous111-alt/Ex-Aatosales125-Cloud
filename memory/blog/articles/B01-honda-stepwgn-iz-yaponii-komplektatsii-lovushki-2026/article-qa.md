# Article QA — B01 (recheck after writer FIX + director policy restore)

**topic_id:** B01  
**slug:** honda-stepwgn-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-honda-stepwgn-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-24  
**verdict:** PASS  
**score:** 88  
**fix_cycle:** 1 / 2 (writer FIX applied; recheck PASS)

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка | Страх ставки/депозита без понимания кодов RP, Spada vs база и красных флагов аукционного листа |
| Где решение | H2: сравнение Spada; карта RP1–RP8; чтение листа; комплектация до депозита; итоговый чеклист до ставки |
| Первый результат | Мини-чек-лист по одному лоту + 3–5 вопросов подборщику до оплаты (явный критерий до FAQ) |
| Термины «на пальцах» | Spada = trim; RP-коды; аукционный лист; ★★ у пробега; Waku Waku только 5G; клиренс 4WD ниже на ~5 мм |
| Beginner-fit | PASS (не профильский тон; первый безопасный шаг без роли перекупа) |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: false-technical (см. INC-2116) |
| utility gate (article) | PASS | action 24≥8; pain 9≥2; outcome 11≥3 (после restore markers в editorial-policy) |
| human-voice | PASS | warn: 2× exactly-5-step lists |
| html-linter | PASS | whitelist OK, TOC нет |
| fact-check | PASS | 9 extracted / 1 verified / 8 soft (годы, мм, дни — в research-notes) |
| link-verify | PASS | 3/3 OK; 2GIS ASCII firm URL 200; Telegram CTA 200 (в JSON = `[CTA_TELEGRAM_OK]`) |
| slop-detector | PASS | 0 клише; over-long 3; Flesch RU 77.1 |
| cannibalization | PASS | 0 issues (3 article metas) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; CTA ok; нет 2–3 internal blog links |
| GEO / citability | 22/25 | TL;DR, таблица Spada, схема листа, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | см. 18/20 ниже |
| Human voice | 14/15 | Gate PASS; warn про одинаковые 5-step списки |
| Fact safety | 12/15 | Числа из Honda PDF/research; fact-bank почти пуст по теме |
| Contract HTML | 10/10 | Whitelist PASS, ~9155 chars, FAQ, CTA, без форм |
| **Gate penalty** | **0** | utility PASS + link-verify pass |
| **Итого** | **88/100** | ≥80 → PASS |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary how-to в title / H1 |
| C02 | ✓ | Lead = страх депозита + обещание чек-листа |
| C03 | ✓ | Читатель: семья / заказ из Японии |
| C04 | ✓ | Spada, RP, лист, Waku Waku объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный порядок до ставки |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + mode B |
| R01 | ✓ | TL;DR + схема + FAQ |
| R02 | ✓ | 4735/4690, 155/150 мм, RP map — research sources |
| R03 | ✓ | Нет сумм пошлин/утиля в тексте |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки», не перекуп |
| E02 | ✓ | Сделайте/Не делайте + action markers 24 |
| E03 | ✓ | CTA каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop = 0 |
| Ept01 | ✓ | Лимиты: ориентир сроков, без гарантий |
| Ept02 | ✗ | Нет internal links на другие посты блога |
| Ept03 | ✗ | (soft) fact-bank не покрывает Honda specs |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0, verdict: pass
- OK: каталог `avto-sales125.ru`, Telegram CTA (200), 2GIS firm ASCII URL (200)
- committed `link-verify.json`: Telegram URL = `[CTA_TELEGRAM_OK]` (secret-scan)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 77.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes | Review: no | cover/schema: **READY** (QA PASS)

## Recheck notes (cycle 1)

1. Writer FIX: action markers 5→24; 2GIS → ASCII firm URL — подтверждено скриптами.
2. Director restore: `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` + fail-fast utility — utility PASS (pain 9, outcome 11).
3. INC-2120 / INC-2121: симптомы для B01 сняты этим run; status open для durable fixer close (policy merge + IRI encode в link-verify).

## FIX (non-blocking / optional)

1. Human-voice warn: разнести размеры списков (не два ol ровно по 5 пунктов).
2. Soft fact-check: годы 2015–2022, 4735/4690, 155/150 — уже в research-notes; опционально в fact-bank.
3. Ept02: после publish соседних постов — 2–3 internal links с `anchor_variants`.

## Gate checklist

| Gate | Status |
|------|--------|
| research-notes-gate PASS | ✓ |
| utility article PASS | ✓ |
| human-voice-report PASS | ✓ |
| link-verify pass | ✓ |
| score ≥ 80 | ✓ 88 |
| CORE-EEAT ≥ 16/20 | ✓ 18/20 |
| beginner-fit | ✓ |

**Итог:** PASS — READY FOR COVER\|\|SCHEMA. Cover/schema не выполнялись в этой роли.
