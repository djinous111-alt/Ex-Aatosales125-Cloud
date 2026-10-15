# Article QA — B01

**topic_id:** B01  
**slug:** avto-iz-korei-pod-klyuch-chto-vhodit-2026  
**article_dir:** memory/blog/articles/B01-avto-iz-korei-pod-klyuch-chto-vhodit-2026  
**date:** 2026-10-15  
**verdict:** FAIL  
**score:** 78 (content-only; gates BLOCK → overall FAIL)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-15; technical_topic=false; github_urls=0 OK |
| fact-check | PASS | 1/1 verified (2026 date in fact-bank) |
| link-verify | PASS | 1/1 OK (`t.me/Djinous`); failed=0 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/цепочка); Flesch RU 65.7 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | **BLOCK** | action_markers 2&lt;8; pain_markers 0&lt;2; outcome_markers 0&lt;3 |
| human-voice gate | **BLOCK** | Fact Check Box: нет фразы «Материал проверен» |

## Scores (content self-check; gates override)

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA Telegram×2; нет 2–3 blog internal |
| GEO / citability | 22/25 | инсайт, таблица финишей, цепочка →, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 10/15 | story/pain OK; Fact Check wording FAIL gate |
| Fact safety | 13/15 | без статичных пошлин; факт-check script PASS |
| Contract HTML | 10/10 | whitelist PASS, ~9473, FAQ, CTA |
| Utility markers | 0/10 | gate BLOCK (маркеры policy) |
| **Итого** | **78/100** | ниже порога 80 + mandatory gates FAIL |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из кореи под ключ» в meta/H1 |
| C02 | ✓ | Lead: депозит vs сюрприз в порту |
| C03 | ✓ | Читатель: заказ из Кореи, страх доплат |
| C04 | ✓ | Encar / СВХ / СБКТС / ЭПТС / ЭРА-ГЛОНАСС объяснены |
| O01 | ✓ | H2 = action outline до депозита |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + цепочка, mode B |
| R01 | ✓ | инсайт + чеклисты + FAQ |
| R02 | ✓ | grounded в research-notes (без фейковых сумм) |
| R03 | ✓ | нет статичного калькулятора пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «докажи строками до депозита» |
| E02 | ✓ | «Делать / Не делать» в секциях (но policy ждёт «сделайте/не делайте») |
| E03 | ✓ | CTA Telegram @Djinous ×2 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | slop hits = 0 |
| Ept01 | ✓ | лимиты: нет единой «под ключ», дыры СВХ/лаборатории |
| Ept02 | ✗ | нет 2–3 внутренних ссылок на другие посты блога |
| Ept02b | ✗ | Fact Check: «Проверено редакцией» ≠ «Материал проверен» |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · **mandatory gates:** FAIL

## Pain / solution / beginner-fit

| Критерий | Статус | Где |
|----------|--------|-----|
| Боль новичка | ✓ (редакционно) | Lead: депозит по рекламе «под ключ» → доплаты СВХ/лаборатория/автовоз |
| Решение в H2 | ✓ | финиш услуги → строки сметы → дыры → документы → график денег → чек-лист |
| Первый результат до FAQ | ✓ | заполненный лист зелёных/красных строк + шаблон в @Djinous |
| Термины «на пальцах» | ✓ | Encar, СВХ, СБКТС, ЭПТС, ЭРА-ГЛОНАСС |
| Beginner-fit | PASS | не профи-жаргон без объяснений; первый шаг безопасный (смета до депозита) |

## Link verify

- total: 1, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/цепочки)
- Flesch RU: 65.7

## Schema ready

BlogPosting: pending (после PASS) | FAQPage: yes (7) | HowTo: yes | Review: no | cover/schema: **не стартовать** до QA PASS

## Blockers (обязательные)

1. **human-voice-report.json = BLOCK** — в blockquote перед FAQ заменить ярлык на «Материал проверен» и имя registry-автора «Редакция Авто-Сейлс».
2. **utility-gate-report.json = BLOCK** — action_markers 2&lt;8 (см. FIX).
3. **utility pain/outcome markers = 0** — в `memory/brief/editorial-policy.json` нет ключей `pain_markers_ru` / `outcome_markers_ru`, при этом gate default min=2/3 → **любая** статья получает BLOCK по этим двум ERROR независимо от текста. Нужен fixer (INC ниже); writer не может закрыть пустой список маркеров.

## FIX cycle → writer (цикл 1)

Не править GEO QA. Вернуть writer с точечным патчем `article.html`:

1. **Fact Check (blocker human-voice):**  
   Сейчас: `<b>Проверено редакцией Авто-Сейлс:</b>…`  
   Нужно: `<b>Материал проверен:</b> Редакция Авто-Сейлс (эксперты по авто под заказ из Японии, Кореи и Китая, Владивосток).<br>` + сохранить блок «Достоверность:…» с конкретными источниками (не Wordstat-шаблон).

2. **Action markers ≥8 (blocker utility):** в `editorial-policy.json` считаются только: `сделайте`, `не делайте`, `шаг `, `проверьте`, `используйте`, `добавьте`, `уберите`, `избегайте`, `ориентир`, `чеклист`, `workflow`.  
   Сейчас в тексте доминирует «Делать:/Не делать:» и «чек-лист» (с дефисом) — **не матчятся**.  
   Заменить/добавить ≥6 новых вхождений, напр.: «Сделайте письменную смету…», «Не делайте депозит…», «Проверьте лимит дней СВХ…», «Избегайте фразы „потом в порту“…», «Шаг 1/2…», «чеклист» без дефиса в 1–2 местах.

3. **Инсайт-блок (soft / contract):** убрать ярлык `TL;DR / Быстрый инсайт:` — оставить смысл инсайта без шаблонного префикса (skill GEO QA).

4. **Списки (soft):** 4× ровно 5 `<li>` в `<ol>` — варьировать длину (human-voice WARN).

5. **Не трогать:** CTA @Djinous, отсутствие калькулятора пошлин, структуру H2/FAQ, cover/schema.

После патча writer: повторный GEO QA (utility + human-voice минимум).  
**Пока policy без pain/outcome lists — utility gate останется BLOCK** даже после пунктов 1–2; директор/fixer должен закрыть INC utility-policy до/параллельно с циклом writer.

## Gate checklist

- score ≥ 80 → **78** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✓  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✗  
- human voice gate PASS → ✗  
- beginner-fit PASS → ✓  

**Итог:** FAIL — cover \|\| schema **не** запускать. Вернуть writer + fixer (policy markers).
