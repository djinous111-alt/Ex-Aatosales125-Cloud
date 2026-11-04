# Article QA — AS22

**topic_id:** AS22  
**slug:** changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS22-changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-05  
**verdict:** PASS  
**score:** 90  
**FIX cycle:** 1 verified (Writer FIX1); GEO QA re-run — longread not edited

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical topic / no official docs URL |
| fact-check | PASS | 12 extracted; 2 verified / 10 soft unverified (research-notes / официальные анонсы) |
| link-verify | PASS | Telegram 200; catalog `catalog_ssl` soft-pass (SSL handshake timeout, host = PUBLIC_SITE_URL) |
| html-linter | PASS | 0 errors; H2 без substring FAQ; один FAQ H2 «Частые вопросы» |
| slop-detector | WARNING | 0 клише; 6 over-long (lead/table glue); Flesch RU 69.1 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |
| utility gate | PASS | action 34; pain 2; outcome 12; FAQ×6; tables×1 |
| human-voice gate | PASS | pain/outcome/concrete OK; insight «Инсайт до депозита»; exactly_five_lists 0 |

## Pain / solution / beginner-fit (editorial)

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит на ярлык Tech/Flagship без мотора/привода/VIN-опций → риск урезанного ПИ |
| Где решение | H2: сценарий → 2.0T/iDD → VIN-опции/AWD → смета Владивосток → красные флаги |
| Первый результат | H2 «Что сделать сегодня: ваш результат» + ol до FAQ |
| Термины «на пальцах» | iDD, 2.0T/8AT, AWD BorgWarner, СБКТС, ЭПТС, СВХ объяснены |
| beginner-fit | **PASS** (не профильский жаргон; безопасный шаг без команды разработчиков) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; CTA catalog×2 + Telegram×1; host = PUBLIC_SITE_URL; нет blog internal |
| GEO / citability | 20/25 | Insight + схема + таблица + FAQ×6; outcome до FAQ |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop |
| Fact safety | 12/15 | mode B; soft unverified vs fact-bank |
| Contract HTML / gates | 10/10 | research + utility + human-voice + link-verify + html-linter PASS |
| **Итого** | **90/100** | |

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
| E02 | ✓ | «Сделайте / Не делайте» + recommendation tokens |
| E03 | ✓ | CTA catalog×2 + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: ориентиры сроков, смета только в каталоге |
| Ept02 | ✗ | Нет 2–3 internal blog links |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после LIVE URL соседних постов — 2–3 internal blog links.
2. **slop WARNING:** укоротить over-long lead при удобном случае.
3. **catalog_ssl soft-pass:** publish probe вручную подтвердит TLS каталога (Cloud egress flaky).

## Gate checklist

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✓ (`catalog_ssl` soft-pass)  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✓  
- human-voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — **cover \|\| schema may start: YES**. GEO QA longread не правил.
