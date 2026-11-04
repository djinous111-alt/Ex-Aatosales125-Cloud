# Article QA — AS22

**topic_id:** AS22  
**slug:** changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS22-changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-05  
**verdict:** FAIL  
**score:** 72  
**FIX cycle:** 1 → return to Writer (GEO QA longread not edited)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | recheck; warning technical/no official docs URL |
| fact-check | PASS | 12 extracted; 2 verified / 10 soft unverified (в research-notes / официальные анонсы) |
| link-verify | FAIL | Telegram 200; catalog host SSL handshake timeout (3 retries + 60s); classified `external` |
| html-linter | FAIL | false duplicate FAQ: H2 «…результат до FAQ» + «Частые вопросы» |
| slop-detector | WARNING | 0 клише; 6 over-long (lead/table glue); Flesch RU 68.7 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |
| utility gate | BLOCK | action_markers 3&lt;8; pain_markers 0&lt;2; outcome_markers 0&lt;3 |
| human-voice gate | PASS | pain/outcome/concrete OK; insight «Инсайт до депозита»; warning 2× exactly-5 lists |

## Pain / solution / beginner-fit (editorial)

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит на ярлык Tech/Flagship без мотора/привода/VIN-опций → риск урезанного ПИ |
| Где решение | H2: сценарий → 2.0T/iDD → VIN-опции/AWD → смета Владивосток → красные флаги |
| Первый результат | Блок «Результат: четыре решения до депозита» + ol из 5 шагов до FAQ |
| Термины «на пальцах» | iDD, 2.0T/8AT, AWD BorgWarner, СБКТС, ЭПТС, СВХ объяснены |
| beginner-fit | **PASS** (не профильский жаргон; безопасный шаг без команды разработчиков) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; CTA catalog×2 + Telegram×1; нет blog internal |
| GEO / citability | 20/25 | Insight + схема + таблица + FAQ×6; outcome до FAQ |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop |
| Fact safety | 12/15 | mode B; soft unverified vs fact-bank |
| Contract HTML / gates | 0/10 | utility BLOCK + html-linter FAIL + link-verify FAIL |
| **Итого** | **72/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать changan uni-k из китая» в title/H1 |
| C02 | ✓ | Lead — депозит без мотора/привода |
| C03 | ✓ | Читатель: заказ UNI-K из Китая до предоплаты |
| C04 | ✓ | 2.0T / iDD / AWD / СБКТС / ЭПТС объяснены |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный outline до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + table + blockquote schema; mode B |
| R01 | ✓ | Insight + схема + чеклисты |
| R02 | ✓ | Цифры силовых/логистики с пометкой ориентир |
| R03 | ✓ | Нет цен лотов / static duty calculator |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + ПИ ≠ ОД |
| E02 | ✓ | «Делать / Не делать» в секциях (но **не** совпадают с utility tokens) |
| E03 | ✓ | CTA catalog×2 + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: ориентиры сроков, смета только в каталоге |
| Ept02 | ✗ | Нет 2–3 internal blog links |
| — | ✗ | Utility action/pain/outcome token mismatch (gate BLOCK) |
| — | ✗ | html-linter FAQ false-positive в H2 |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Но gates PASS не достигнуты → overall FAIL**

## FIX для Writer (цикл 1) — не править cover/schema

1. **html-linter:** переименовать H2 `Что сделать сегодня: ваш результат до FAQ` → убрать подстроку `FAQ` (например `Что сделать сегодня: ваш результат`). Оставить ровно один H2 `Частые вопросы`.
2. **utility action_markers (≥8):** сейчас только 3×`ориентир`. Ярлыки `Делать` / `Не делать` и `чек-лист` **не** считаются. Добавить точные токены из `memory/brief/editorial-policy.json` → `recommendation_markers_ru`: `проверьте`, `избегайте`, `сделайте` / `не делайте`, `шаг 1`…, `чеклист` (без дефиса), `используйте` — суммарно ≥8 вхождений по plain text.
3. **utility pain/outcome:** human-voice уже PASS (`боль`/`ошиб`, `результат`/`получите`/`сможете`). Для utility-скрипта списки `pain_markers_ru` / `outcome_markers_ru` в policy **пустые**, поэтому счётчики всегда 0 — см. incident Fixer. Writer: сохранить human-voice маркеры; не раздувать текст ради пустого policy.
4. **link-verify / catalog:** хост в статье `avto-sales125.ru`, а `PUBLIC_SITE_URL` → `avtosales125.ru` (без дефиса). Сверить канонический catalog URL с Publish/site; SSL handshake к `avto-sales125.ru:443` из Cloud timeout (TCP ок). После выравнивания URL — перепросить GEO QA link-verify.
5. **optional:** разнести длину двух ol (human-voice warning: 2× exactly-5); укоротить over-long lead при удобном случае.

## Gate checklist

- score ≥ 80 → **72** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✗  
- human-voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FAIL — **cover \|\| schema не стартовать**. Вернуть Writer (FIX выше) + Fixer по open incidents utility/link soft-pass.
