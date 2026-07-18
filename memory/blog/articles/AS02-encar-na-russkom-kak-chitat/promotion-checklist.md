# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-07-18  
Live URL: [REDACTED]/2026/07/18/encar-na-russkom-kak-chitat/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
«Encar на русском» чаще ведёт на зеркало — читайте живую карточку

• За 10 минут: цена, пробег, тип продажи, все фото, Performance Check
• X/W на силовых = стоп до депозита
• Carhistory по VIN ≠ замена схеме кузова

Читать: [REDACTED]/blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Writer уже вставил internal link AS02 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`)
- [x] Локальный interlinker `--apply`: 0 новых opportunities (корпус 3 статьи; дубликатов якорей нет)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS02-encar-na-russkom-kak-chitat --site-base [REDACTED]` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (AS02 в индексе).
- Publish: PASS post=3394 permalink=[REDACTED]/2026/07/18/encar-na-russkom-kak-chitat/
