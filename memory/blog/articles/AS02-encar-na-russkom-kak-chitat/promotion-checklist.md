# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-07-26 (pending publish)  
Live URL: /blog/encar-na-russkom-kak-chitat/

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
Скрин «без ДТП» — ещё не проверка Encar

• Шапка лота → схема кузова X/W → страховая история
• X/W на стойках/лонжеронах — стоп до депозита
• «Без ДТП» часто про каркас, а не про страховые выплаты

Читать: /blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: AS02 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`, якорь «Trust Encar»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply` — 1 link applied (AS02→AS09, keyword `trust encar`).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles; site-name «Авто-Сейлс»).
- Live/llms URLs в git — relative `/blog/...` (Cloud secret-scan блокирует абсолютный `PUBLIC_SITE_URL`).
- Cover BLOCKER (Kie 402) — cover.png отсутствует; indexer не блокировался.
- Publish ещё не выполнялся.
