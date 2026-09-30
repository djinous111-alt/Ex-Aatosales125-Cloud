# Article QA — B01 (re-run after Fixer)

**topic_id:** B01  
**slug:** postanovka-na-uchet-vvezennogo-avto-2026  
**article_dir:** memory/blog/articles/B01-postanovka-na-uchet-vvezennogo-avto-2026  
**date:** 2026-09-30  
**verdict:** PASS  
**score:** 86/100  
**re-run:** после Fixer (`pain_markers_ru` / `outcome_markers_ru` в editorial-policy.json); `article.html` без изменений Writer

## Scripts (полный пересчёт)

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | status PASS; research_date / today_iso=2026-09-30; errors=[] |
| fact-check | PASS | 6 stats; verified 2; unverified 4 (2025, 1500/2000/4500 — в research-notes) |
| link-verify | PASS | 2/2 OK; failed_count=0 |
| html-linter | PASS | 0 errors; whitelist OK; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы); Flesch RU 62.8 — soft, не veto |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | **PASS** | pain_markers=3; outcome_markers=10; action_markers=11; water_hits=[] |
| human voice gate | PASS | warnings only: Fact Check template; 3× exactly-5-step lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в H1/title; H2 actionable; CTA catalog×2 + TG×1; нет 2–3 blog internal |
| GEO / citability | 23/25 | Insight + схема + таблица + FAQ×7; ярлык `TL;DR / Быстрый инсайт` шаблонный (soft) |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice-report PASS |
| Fact safety | 12/15 | 4 unverified vs fact-bank (есть в research-notes) |
| Contract HTML | 10/10 | Whitelist PASS, ~8867, FAQ×7, CTA≤3 |
| **Итого** | **86/100** | ≥80 ✓ |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «постановка на учет авто из японии» в title/H1 |
| C02 | ✓ | Lead — боль + ответ без «в этой статье» |
| C03 | ✓ | Читатель: владелец после растаможки, страх ГАИ/10 дней |
| C04 | ✓ | ЭПТС, СБКТС объяснены при первом появлении |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + схемы →, mode B |
| R01 | ✓ | Insight, схема ОСАГО, критерий результата, FAQ |
| R02 | ✓ | 10 дней / ОСАГО с 01.03.2025 / госпошлины — в research-notes |
| R03 | ✓ | Цифры как ориентир + сверка в Госуслугах |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «таможня ≠ финиш» + ОСАГО окно vs дорога |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA ≤3 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Отказ ЭПТС/VIN/свет/просрочка названы |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit (human)

| Check | Status | Evidence |
|-------|--------|----------|
| Боль новичка в lead | PASS | «в ГАИ ехать страшно… слот… 10 дней»; история Андрея |
| Решение в H2 | PASS | проверка ЭПТС → пакет → ОСАГО → Госуслуги → осмотр → день учёта |
| Результат до FAQ | PASS | «Критерий результата: в руках СТС и госномера…» |
| Термины «на пальцах» | PASS | ЭПТС, СБКТС |
| Beginner-fit | PASS | первый шаг без команды профи; безопасный чек до записи |
| Utility pain/outcome markers | **PASS** | pain=3 (≥2), outcome=10 (≥3) после Fixer policy |

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схем) — soft WARN
- Flesch RU: 62.8

## Soft notes (не блокируют PASS)

1. Insight label: `TL;DR / Быстрый инсайт` — шаблонный ярлык (geo-qa skill).
2. Fact Check: варьировать формулировку «Материал проверен» (human-voice WARN).
3. Lists: один из трёх ровно-5-шаговых списков сделать 4 или 6 пунктов.
4. Ept02: 2–3 internal blog links, когда URL соседних постов готовы.

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

нет

## Gate checklist

- score ≥ 80 → **86** ✓  
- utility gate PASS → ✓ (pain=3, outcome=10)  
- human voice PASS → ✓  
- research notes gate PASS → ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✓  
- beginner-fit → ✓  

**Итог:** PASS — директор может запускать cover \|\| schema.
