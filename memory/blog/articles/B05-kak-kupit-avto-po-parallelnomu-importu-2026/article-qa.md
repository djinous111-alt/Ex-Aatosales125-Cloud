# Article QA — B05

**topic_id:** B05  
**slug:** kak-kupit-avto-po-parallelnomu-importu-2026  
**article_dir:** memory/blog/articles/B05-kak-kupit-avto-po-parallelnomu-importu-2026  
**date:** 2026-09-30  
**verdict:** PASS  
**score:** 86  
**qa_cycle:** retry after Writer FIX (portal.elpts.ru → elpts.ru)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified: 8 недель, №506, №4769 — есть в research-notes |
| link-verify | PASS | 3/3 OK: `elpts.ru` 200, `avto-sales125.ru` 200, Telegram CTA 200 |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы); Flesch RU 56.8 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 23; pain 4; outcome 4; FAQ×6; table×1 |
| human-voice gate | PASS | warn: multiple exactly-5-step lists |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит за ярлык «параллельный импорт» без VIN/ЭПТС → доначисление пошлин / не «действующий» ЭПТС / гарантия на словах |
| Где решение | H2: развести режим vs ярлык; VIN/ЭПТС до депозита; пакет документов; ловушки 2026; чеклист 12 пунктов; подбор если бумаг нет |
| Первый результат | До оплаты пройти 12 пунктов и сказать «плачу» или «стоп» |
| Термины «на пальцах» | Параллельный импорт, VIN, ЭПТС/СЭП, утильсбор, декларант — объяснены при первом появлении |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в H1/title; H2/FAQ/CTA; нет 2–3 internal blog links |
| GEO / citability | 23/25 | Инсайт-блок, схема, таблица, FAQ×6, чеклист 12 |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop; human-voice PASS |
| Fact safety | 12/15 | №506 / 4769 / 2–8 недель — в research, не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9392 знаков, FAQ, CTA≤3; elpts.ru OK |
| **Итого** | **86/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «параллельный импорт авто» в H1/meta |
| C02 | ✓ | Lead: боль депозита + ответ «чек-лист до перевода» |
| C03 | ✓ | Обычный покупатель без хаоса в бумагах |
| C04 | ✓ | Режим / VIN / ЭПТС / утильсбор объяснены |
| O01 | ✓ | H2 = research action outline |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | Инсайт, схема, чеклист, FAQ |
| R02 | ✓ | №506, приказ 4769/27.05.2026 в research-notes |
| R03 | ✓ | Нет сумм пошлин/цен в тексте |
| R04 | ✓ | FAQ: ответ в 1-м предложении |
| E01 | ✓ | Угол «менеджер сказал всё включено» / до оплаты |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | Каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Доначисления, ЕАЭС-схемы, гарантия, «незавершённый» ЭПТС |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0, verdict: **pass**
- ok: `https://elpts.ru/` (200); каталог avto-sales125.ru (200); Telegram CTA (200)
- Writer FIX cycle 1: `portal.elpts.ru` удалён из article.html
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схем)
- Flesch RU: 56.8

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: **разрешены директору** после этого PASS

## Blockers

Нет.

## FIX cycle (закрыт)

1. Writer FIX cycle 1: `https://portal.elpts.ru/` → `https://elpts.ru/` (2 места) — **done**
2. GEO QA retry: link-verify PASS — **done**
3. Optional non-blocking: Ept02 internal blog links; fact-bank для №506/4769; vary exactly-5-step lists

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → **PASS** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — директор может запускать cover \|\| schema.
