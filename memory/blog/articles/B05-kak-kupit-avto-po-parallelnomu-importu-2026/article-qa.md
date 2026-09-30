# Article QA — B05

**topic_id:** B05  
**slug:** kak-kupit-avto-po-parallelnomu-importu-2026  
**article_dir:** memory/blog/articles/B05-kak-kupit-avto-po-parallelnomu-importu-2026  
**date:** 2026-09-30  
**verdict:** FIX  
**score:** 86

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified: 8 недель, №506, №4769 — есть в research-notes |
| link-verify | FAIL | 1/3 fail: `https://portal.elpts.ru/` → DNS NXDOMAIN (`No address associated with hostname`); `elpts.ru` / `www.elpts.ru` → 200 |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы); Flesch RU 57.2 |
| cannibalization | PASS | 0 issues |
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
| Contract HTML | 10/10 | Whitelist PASS, ~9406 знаков, FAQ, CTA≤3 |
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

- total: 3, failed: 1
- fail: `https://portal.elpts.ru/` — hostname не резолвится
- ok: каталог avto-sales125.ru; Telegram CTA
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схем)
- Flesch RU: 57.2

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: blocked until QA PASS

## Blockers

1. **link-verify FAIL:** заменить `https://portal.elpts.ru/` на рабочий URL официального СЭП (`https://elpts.ru/` резолвится и отдаёт 200 в этом окружении). Обновить анкор/упоминание в тексте и в блоке «Источники сверки». Не править из GEO QA — вернуть Writer (FIX cycle 1).

## FIX cycle (QA)

1. Writer: починить битую ссылку ЭПТС/СЭП (и текст-источник), затем повтор link-verify.
2. Optional non-blocking: Ept02 internal blog links; fact-bank для №506/4769; vary exactly-5-step lists.

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → **FAIL** ✗  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** FIX — cover \|\| schema **не** запускать до повторного GEO QA PASS после правки ссылки Writer.
