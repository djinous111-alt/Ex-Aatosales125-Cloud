# Article QA — AS10

**topic_id:** AS10  
**slug:** tank-300-iz-kitaya-ramnik-ili-krossover-2026  
**article_dir:** memory/blog/articles/AS10-tank-300-iz-kitaya-ramnik-ili-krossover-2026  
**date:** 2026-07-27  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic false-positive (AS prefix) |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified 300/110/218 — в research-notes |
| link-verify | PASS | 1/1 OK (`avto-sales125.ru`); Telegram plaintext без href |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (lead + table artifact); Flesch RU 70.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 31; pain 5; outcome 7 |
| human-voice gate | PASS | warning: exactly-5 lists regex (≥5 li); story/pain/outcome overlap OK |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «танк 300 из китая» в title/H1; H2 actionable; CTA каталог×2 |
| GEO / citability | 24/25 | Коротко-блок, таблица сравнения, FAQ×6, чеклист, схема → |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice-report PASS; 0 AI-openers |
| Fact safety | 12/15 | Цифры 110/218/Автотор в research; не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9289 знаков, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: боль депозита за «похож на Танк» + ответ |
| C03 | ✓ | Читатель: заказ из Китая / путаница рамник vs кроссовер |
| C04 | ✓ | Рама / unibody / Part-time / муфта / СБКТС / ЭПТС на пальцах |
| O01 | ✓ | H2 = comparison → рама → кроссовер → чеклист → VIN → решение |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + таблица + blockquote workflow, mode B |
| R01 | ✓ | Коротко-блок, схема, FAQ |
| R02 | ✓ | Автотор 2026 / Hi4-T/Z / 218 л.с. из research |
| R03 | ✓ | Нет сумм пошлин; «калькулятор в тексте» запрещён |
| R04 | ✓ | FAQ ответ в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + сценарий недели |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram @avtosales125 plaintext |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Fact Check: Редакция Авто-Сейлс (author_id avtosales-editorial) |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Стоп-правило VIN/осмотр; каналы CN vs Автотор |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Поле | Где в статье |
|------|----------------|
| **reader_pain** | Lead: депозит за «квадратный» по фото → рамник в городе или кроссовер без рамы |
| **решение** | H2 сравнение + таблица Tank 300 / T2 / Dargo / H9; H2 рама; H2 кроссовер |
| **результат до FAQ** | H2 «Зафиксируйте решение…»: чеклист сценарий→кузов→привод→пакет; стоп-правило депозита |
| **термины на пальцах** | рама/body-on-frame, unibody, Part-time, муфта, СБКТС, ЭПТС |
| **beginner-fit** | PASS: первый безопасный шаг без «команды разработчиков»; тон не для профи |

## Link verify

- total: 1, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (lead + table/schema parse artifact)
- Flesch RU: 70.6

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. **Utility BLOCK:** `action_markers=1`, `pain/outcome=0` из-за (a) Writer «Делать/Не делать» + «чек-лист» ≠ `recommendation_markers_ru`; (b) rebrand удалил `pain_markers_ru`/`outcome_markers_ru` из `editorial-policy.json`.
2. **QA FIX:** article — `Сделайте/Не делайте`, `чеклист`, `ориентир/избегайте/шаг`, убран ярлык TL;DR; Fact Check author casing; список «что дальше» → 6 шагов.
3. **Durable restore (этот run):** вернул markers + mins в `editorial-policy.json`; empty-list skip в `utility_gate.py`. Incident → fixer queue.
4. Re-run: all gates PASS, human-voice PASS.

## Next

Cover || Schema (параллельно) после GEO QA PASS.
