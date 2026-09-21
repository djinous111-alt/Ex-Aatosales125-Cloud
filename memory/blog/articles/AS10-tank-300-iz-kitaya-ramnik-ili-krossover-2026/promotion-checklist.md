# Promotion checklist — AS10 tank-300-iz-kitaya-ramnik-ili-krossover-2026

Дата публикации: 2026-07-27 (план; publish ещё не выполнен)  
Live URL: (после publish) /blog/tank-300-iz-kitaya-ramnik-ili-krossover-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)
- [ ] Cover: сейчас BLOCKER (Kie 402) — без featured/inline PNG до top-up credits

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Депозит за Tank 300 «как за кроссовер» — лотерея

• Tank 300 — рамник с понижайкой, не высокий SUV
• До оплаты: сценарий езды → 300 vs 500 → привод и сервис
• Чек-лист из 10 пунктов «беру / не беру»

Читать: (URL после publish)
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 — другие кластеры; opportunities_found=0)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «танк 300 из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply --article-dir …` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-name «Авто-Сейлс», AS10 в индексе; site-base `[REDACTED]` из-за secret-scan).
- Cover PNG отсутствует (Kie credits 402) — Indexer выполнен на article+schema без invent cover.
- Publish: pending.
