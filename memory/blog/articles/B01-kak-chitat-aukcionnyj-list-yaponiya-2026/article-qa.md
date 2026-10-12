# Article QA — B01

**topic_id:** B01  
**slug:** kak-chitat-aukcionnyj-list-yaponiya-2026  
**article_dir:** memory/blog/articles/B01-kak-chitat-aukcionnyj-list-yaponiya-2026  
**date:** 2026-10-12  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic false-positive (см. research incident) |
| utility gate | PASS | action 43; pain 6; outcome 14 (после восстановления markers в editorial-policy) |
| human-voice | PASS | pain: боль/ошиб; outcome: результат/получите/сможете/проверьте |
| fact-check | PASS | 1/1 verified |
| link-verify | PASS | 4/4 OK (2 internal latin slugs + catalog + Telegram) |
| html-linter | PASS | whitelist OK; TOC нет; TL;DR-ярлык снят |
| slop-detector | PASS | 0 клише; 3 over-long (таблица/чек-лист); Flesch RU 71.0 |
| cannibalization (local) | PASS | 0 issues vs AS08/AS09/B01 |

## Pain / solution / result (beginner-fit)

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Не понимает «4.5» vs R/RA и коды A/U/W/XX; боится пропустить аварию или отсечь нормальный лот |
| Где lead называет боль | Абзац 1: история Андрея + «смотришь 4.5 или букву R и не понимаешь, можно ли ставить» |
| Где решения (H2) | Порядок чтения → шкала vs R/RA → коды схемы → заметки → сверка с фото → чек-лист ставка/пауза/пропуск |
| Первый результат до FAQ | Чек-лист: назвать оценку/салон/R/RA/коды и вердикт ставка/пауза/пропуск; «сможете… получите ясный ответ» |
| Термины «на пальцах» | 修復歴, R/RA, A/U/W/S/C/X/XX, болтовые панели vs скелет, салон A–D |

**beginner-fit:** PASS (нет тона «для профи»; первый безопасный шаг — открыть полный лист до ставки)

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; 2 live internal; live WP уже имеет близкие посты про лист (warning) |
| GEO / citability | 23/25 | Инсайт-бокс, таблицы, FAQ×7, чек-лист, схема чтения |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice-report PASS |
| Fact safety | 13/15 | Факты из research-notes; без выдуманных лотов/пошлин |
| Contract HTML | 10/10 | Whitelist PASS, ~8686 chars, FAQ, CTA≤3 |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в title/H1 |
| C02 | ✓ | Lead: боль + порядок чтения до ставки |
| C03 | ✓ | Новичок, первая ставка по японскому лоту |
| C04 | ✓ | Оценка, R/RA, коды схемы объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный порядок до чек-листа |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + 2 таблицы + blockquote workflow |
| R01 | ✓ | Инсайт, схема, FAQ, чек-лист |
| R02 | ✓ | Факты со сверкой SheetJP/JapanAuc/USS (research) |
| R03 | ✓ | Нет цен лотов/калькулятора пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки, не после выкупа» |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: R≠косметика; калибровка TAA vs USS |
| Ept02 | ✗ | Live WP уже содержит близкие гайды про аукционный лист (director: update vs new) |
| Exp04 soft | ✗ | Три списка ровно по 5 пунктов (human-voice warning) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 4, failed: 0
- internals: `/2026/10/04/prohodnye-avto-iz-yaponii-2026-chek-list-do-stavki/`, `/2026/10/05/kak-sdelat-pervuyu-stavku-na-yaponskom-aukcione-2026/`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблицы + длинный критерий результата)
- Flesch RU: 71.0

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## QA edits this run (whitelist-safe)

1. Инсайт-ярлык `TL;DR / Быстрый инсайт` → `Главное до ставки`.
2. Internal links: кириллические 404-пути → актуальные latin slugs с live WP.
3. В блоке результата добавлены outcome-маркеры («сможете», «получите»).
4. Durable: `pain_markers_ru` / `outcome_markers_ru` + расширенные recommendation markers в `memory/brief/editorial-policy.json`.
5. Durable: `utility_gate` skip empty pain/outcome lists; `link_verify` percent-encode non-ASCII paths.

## Blockers

- нет (automated gates PASS)

## Warnings (director)

1. **Live near-duplicate:** на PUBLIC_SITE уже есть посты про чтение аукционного листа (`…/kak-chitat-auktsionnyy-list-…`). Local cannibalization PASS; при publish предпочтительно update существующего поста или явно принять refresh-угол.
2. Topic card `internal_links` указывал кириллические пути 404 — исправлено только в `article.html`.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-report PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
