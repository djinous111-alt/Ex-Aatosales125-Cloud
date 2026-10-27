# Article QA — B01

**topic_id:** B01  
**slug:** toyota-land-cruiser-300-iz-yaponii-komplektatsii-lovushki  
**article_dir:** memory/blog/articles/B01-toyota-land-cruiser-300-iz-yaponii-komplektatsii-lovushki  
**date:** 2026-10-27  
**verdict:** PASS  
**score:** 88

## Beginner pain → solution → first result

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Путает LC300 с Prado/LC250, верит в льготный утильсбор «для физика», ставит по скрину грейда без полного листа |
| Где решение | H2: отделить 300 от Prado/250 → грейды GX/VX/ZX/GR → дизель/бензин/HEV → лист пошагово → ловушка утильсбора → чеклист Владивосток |
| Первый результат | Одностраничный мини-бриф до FAQ (код кузова, грейд/места, мотор, лист без R, возраст vs 3 года, потолок ставки) |
| Термины «на пальцах» | DPF = выжигание сажи на нормальных пробегах; R по раме/стойкам; грейды GX→GR; коды VJA/FJA/VJH300; порог льготы ≤3 л и ≤160 л.с. |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL |
| fact-check | PASS | 12 stats; verified 2; unverified 10 — опираются на research-notes (Toyota JP, утиль с 01.12.2025, hybrid 01.10.2026) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 0 over-long; Flesch RU 79.8 |
| cannibalization | PASS | 0 issues (3 meta definitions) |
| utility gate | PASS | action 18; pain 10; outcome 9; FAQ×7; table×1 |
| human-voice gate | PASS | soft warn: 2 списка ровно по 5 пунктов |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2/H3; CTA×3; нет 2–3 blog internal |
| GEO / citability | 24/25 | Инсайт, схема до ставки, таблица сравнения, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop; human-voice PASS |
| Fact safety | 13/15 | Факты в research-notes; часть чисел не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, FAQ, CTA≤3, без форм/pre/code |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать toyota land cruiser 300 из японии» в title / H1 |
| C02 | ✓ | Lead: история Ивана + прямой фокус «до ставки» без «в этой статье» |
| C03 | ✓ | Новичок на JP-аукционе / Владивосток |
| C04 | ✓ | DPF, грейды, R по раме, коды кузова объяснены |
| O01 | ✓ | H2 = research outline (модель → грейд → мотор → лист → утиль → чеклист → FAQ) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт, вердикт по мотору, схема до ставки, FAQ |
| R02 | ✓ | Hybrid с 01.10.2026; льгота утильсбора с 01.12.2025; коды кузова — в research-notes |
| R03 | ✓ | Нет цен лотов/%; утиль 3400/5200 с пометкой порога; калькулятор лота не публикуется |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до ставки» + LC300≠Prado + нет льготы утильсбора |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | DPF/город, R по раме, полная шкала утильсбора, сроки в договоре |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 0
- Flesch RU: 79.8

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. **link-verify FAIL:** в `article.html` три `href="[REDACTED]"` (литеральный токен вместо CTA URL) → восстановлены URL каталога и Telegram из `memory/brief/conversion-map.md`; повтор link-verify → PASS.
2. **Insight label:** убран шаблонный ярлык `TL;DR / Быстрый инсайт` → `Коротко до ставки` (контракт skill).

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** пороги утильсбора / л.с. дизеля — дописать в fact-bank.
3. **human-voice warn:** два списка ровно по 5 пунктов — при следующем рерайте варьировать длину.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
