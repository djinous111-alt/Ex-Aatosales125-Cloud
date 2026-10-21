# Article QA — B01

**topic_id:** B01  
**slug:** kak-chitat-aukcionnyj-list-yaponiya-2026  
**article_dir:** memory/blog/articles/B01-kak-chitat-aukcionnyj-list-yaponiya-2026  
**date:** 2026-10-22  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical topic без official docs URL |
| fact-check | PASS | 3 facts; verified 1 (2026); unverified Reiwa 2018 / Heisei 1988 (нет в fact-bank) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long (flatten таблицы/blockquote); Flesch RU 65.2 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate (article) | PASS | action 17; pain 9; outcome 8; FAQ×6; table×1 |
| human-voice gate | PASS | warning: multiple exactly-5-step lists (regex ≥5); beginner-fit OK |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Смотрит только крупный балл (4.5), пропускает схему/комментарий, рискует депозитом вслепую |
| Где решение | H2: идентификация → шкала → R/RA → схема кодов → перевод комментария → чеклист до депозита |
| Первый результат | За 10–15 мин вердикт «ставить / не ставить / сначала перевести» до депозита |
| Термины «на пальцах» | R/RA (修復歴), A/U/W/X/XX/S/C, салон A–E, Reiwa/Heisei, пометки одометра |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; CTA×3; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт «Коротко», таблица оценок, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 14/15 | PASS; soft warning по спискам ≥5 |
| Fact safety | 13/15 | Годы эпох не в fact-bank; цены/пошлины не обещаны |
| Contract HTML | 10/10 | Whitelist PASS, ~9189 chars, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в meta/H1 |
| C02 | ✓ | Lead: боль новичка + исход «ставить / не ставить» |
| C03 | ✓ | Читатель: заказ из Японии, депозит до ставки |
| C04 | ✓ | Оценки, R/RA, коды схемы объяснены |
| O01 | ✓ | H2 = зоны листа из research outline |
| O02 | ✓ | Логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote, mode B |
| R01 | ✓ | Инсайт, таблица, чеклист, FAQ |
| R02 | ✓ | Факты опираются на research-notes / открытые гайды |
| R03 | ✓ | Нет цен лотов и калькулятора пошлин |
| R04 | ✓ | Ответ FAQ с первого предложения |
| E01 | ✓ | Угол «маркер по листу до ставки» |
| E02 | ✓ | Сделайте / Не делайте / Проверьте |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты листа: не диагностика мотора |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схемы)
- Flesch RU: 65.2

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Убран шаблонный ярлык `TL;DR / Быстрый инсайт` → `Коротко:` (контракт skill/html insight).
2. Заменён англицизм `Workflow` → `Порядок` (beginner-fit).
3. Повторный прогон всех гейтов → PASS (slop WARNING non-blocking).

## FIX (non-blocking / optional)

1. **Ept02:** после URL соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** Reiwa 2018 / Heisei 1988 — дописать в fact-bank.
3. **human-voice warning:** regex «exactly 5» считает любой ol ≥5 — уже в очереди fixer (INC writer).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  
- cannibalization PASS ✓  

**Итог:** PASS — можно cover || schema.
