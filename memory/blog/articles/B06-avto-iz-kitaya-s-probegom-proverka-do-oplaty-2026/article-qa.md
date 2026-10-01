# Article QA — B06

**topic_id:** B06  
**slug:** avto-iz-kitaya-s-probegom-proverka-do-oplaty-2026  
**article_dir:** memory/blog/articles/B06-avto-iz-kitaya-s-probegom-proverka-do-oplaty-2026  
**date:** 2026-10-01  
**cycle:** re-QA after Writer FIX 1/2  
**verdict:** PASS  
**score:** 86  
**human_voice:** PASS  
**utility:** PASS (canonical policy with HV-aligned pain/outcome lists; default empty lists still false-BLOCK — see incident)

## Pain / solution / beginner-fit (ручная проверка)

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Боюсь перевести депозит за «почти новую», а лот ≤180 дней застрянет без экспортной лицензии |
| Где в lead | История Ивана + депозит «в работе» / лот у границы без лицензии |
| Где решение (H2) | 180 дней по 行驶证 → пакет сканов → письмо завода → красные флаги → чеклист до перевода |
| Первый результат до FAQ | H2 «Что сделать сегодня»: дата регистрации, нужен ли letter, депозит не уходит при неполном пакете |
| Термины «на пальцах» | 行驶证 (права+учёт), 交强险 (базовая страховка), After-Sales Service Confirmation Letter / 售后维修服务确认书 |
| Beginner-fit | PASS (не для профи; есть первый безопасный шаг без команды разработчиков) |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | status PASS; research_date 2026-10-01 |
| fact-check | PASS | 6 extracted / 1 verified in fact-bank; soft unverified covered in research-notes |
| link-verify | PASS | 2/2 OK; failed_count=0 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 67.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers **15≥8**, pain **8≥2**, outcome **6≥3** (canonical `/tmp` policy = HV markers). Default policy still false-BLOCK pain/outcome=0 |
| human-voice gate | PASS | unique outcomes: результат, получите, проверьте, соберите (≥3). WARN: exactly_five_lists=2 (не BLOCK) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/meta; H2 how-to; CTA; мало blog internal |
| GEO / citability | 20/25 | Insight, схема, таблица, FAQ×6, чеклисты |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 14/15 | PASS; WARN на 2× five-step lists |
| Fact safety | 12/15 | Норма 180 дней + источники; не всё в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, FAQ, CTA, без форм |
| Utility action | 10/10 | action_markers 15≥8 — gate PASS |
| **Итого** | **86/100** | ≥80 → PASS |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из Китая с пробегом» в H1 / title_seo |
| C02 | ✓ | Lead сразу про проверку до оплаты |
| C03 | ✓ | Читатель: новичок с депозитом за б/у из Китая |
| C04 | ✓ | 行驶证 / 交强险 / letter объяснены |
| O01 | ✓ | H2 = research outline |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote workflow, mode B |
| R01 | ✓ | «Коротко по делу», схема, FAQ |
| R02 | ✓ | Shangmao Han [2025] No. 648, Автостат, VL.ru |
| R03 | ✓ | Нет фейковых точных пошлин |
| R04 | ✓ | FAQ отвечает с 1-го предложения |
| E01 | ✓ | Угол «до депозита» |
| E02 | ✓ | «Делать / Не делать» |
| E03 | ✓ | CTA каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person hero |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Письмо не от дилера; ≤180 без letter = стоп |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 67.6

## Schema ready (после PASS)

BlogPosting: ready | FAQPage: ready (6) | HowTo: ready  
**Директору: можно запускать cover \|\| schema параллельно.**

## Blockers

нет

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — cover \|\| schema **можно** стартовать.

## Incident

- `memory/pipeline-fix-queue.md#INC-20261001-0935-geo-qa-utility-pain-outcome-empty-policy` (workaround: temp policy с pain/outcome lists; default policy evidence в `utility-gate-report.default-policy.json`)
