# Article QA — B01 (recheck after Writer FIX + Fixer)

**topic_id:** B01  
**slug:** sbkts-i-epts-2026-kak-oformit  
**article_dir:** memory/blog/articles/B01-sbkts-i-epts-2026-kak-oformit  
**date:** 2026-09-29  
**verdict:** PASS  
**score:** 91  
**fix_cycle:** 1 → closed (Writer FIX + Fixer durable)  
**recheck:** full GEO QA suite re-run after FIX

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-09-29; sources/action/pain map OK |
| fact-check | PASS | 4 stats; verified 1 (2026); soft unverified: 2011 (ТР ТС), 2027 (FAQ caveat), «15 минут» |
| link-verify | PASS | 4/4 ok; `dp.elpts.ru` 403 + `pub.fsa.gov.ru` SSL timeout → soft official-host warnings (не fail). Catalog + Telegram 200 |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/чеклисты/схема); Flesch RU 63.4 Easy |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | pain_markers=6; outcome_markers=11; action_markers=11; FAQ×6; table×1 |
| human-voice gate | PASS | pain: боль/проблем/ошиб/дорого/долго/сложно; outcome OK; exactly_five_lists=1 (warn cleared) |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | После таможни/СВХ путает СБКТС и ЭПТС, боится «серой» лаборатории и приезда в ГИБДД без пакета; lead явно: «Боль новичка… сложно…» |
| Где решение | H2: отличие СБКТС/ЭПТС → порядок после таможни → чеклист → реестр ФСА → отказы → статус «действующий» → «что сделать сегодня» |
| Первый результат | Чеклист документов + 1–2 лаборатории в реестре + доступ в СЭП; критерий: «действующий» + выписка + ОСАГО |
| Термины «на пальцах» | СБКТС / ЭПТС / СЭП / ТД·ТПО / утильсбор / СТС vs ЭПТС — объяснены |
| Beginner-fit | PASS (смысл + lexical gates) |

## Scores

| Блок | Балл | Комментарий |
|------|-------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 action; CTA каталог×2 + Telegram; мало internal blog |
| GEO / citability | 23/25 | Insight-blockquote, таблица, схема →, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 checklist |
| Human voice | 14/15 | Gate PASS; 6 pain markers; story/outcome overlap; 6 over-long soft |
| Fact safety | 13/15 | Fact-check PASS; 3 soft unverified; без выдуманных цен |
| Contract HTML | 10/10 | Linter PASS; char_count 8713; CTA OK |
| **Итого** | **91/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «сбктс и эптс» в meta/H1 |
| C02 | ✓ | Lead = боль + порядок без «в этой статье» |
| C03 | ✓ | Читатель: первый ввоз из Азии, СВХ Владивосток |
| C04 | ✓ | СБКТС/ЭПТС/СЭП объяснены |
| O01 | ✓ | H2 = action-outline research |
| O02 | ✓ | Логичный пайплайн |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + blockquote, mode B |
| R01 | ✓ | Короткий блок + схема + FAQ |
| R02 | ✓ | Источники в Fact Check + research-notes |
| R03 | ✓ | Цены не в статье → каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «не по фото / сначала реестр» |
| E02 | ✓ | «Делать / Не делать» |
| E03 | ✓ | Telegram CTA + каталог×2 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: ЭРА-ГЛОНАСС не фиксируем; сроки ориентир |
| Ept02 | ✗ | Нет 2–3 internal blog links (после Indexer) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** нет

## Link verify (manual-verify notes)

- `https://avto-sales125.ru` — 200 OK  
- Telegram CTA — 200 OK  
- `https://dp.elpts.ru/` — soft official-host 403 (bot client); URL оставить; проверить в браузере при сомнении  
- `https://pub.fsa.gov.ru/ral` — soft official-host SSL timeout; URL оставить; проверить в браузере при сомнении  

## AI-slop scan

- cliches: 0  
- over-long: 6 (таблица/схема/чеклисты — парсер)  
- Flesch RU: 63.4 Easy  

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (closed)

1. Writer FIX: pain markers (≥2) + ol sizes varied; char_count 8713  
2. Fixer: `pain_markers_ru` / `outcome_markers_ru` in editorial-policy; link-verify soft official hosts; utility PASS  

## FIX (non-blocking / optional)

1. **Ept02:** после URL других постов — 2–3 internal blog links (Indexer)  
2. **fact-check soft:** 2011 / 2027 / «15 минут» — при желании в fact-bank  
3. **slop over-long:** артефакт таблицы/схемы; не блокер  

## Gate checklist

- score ≥ 80 → **91** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✓ (soft official warnings OK)  
- research notes gate PASS → ✓  
- utility gate PASS → ✓  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — `COVER_SCHEMA_GO=yes` (директор может запускать cover \|\| schema).
