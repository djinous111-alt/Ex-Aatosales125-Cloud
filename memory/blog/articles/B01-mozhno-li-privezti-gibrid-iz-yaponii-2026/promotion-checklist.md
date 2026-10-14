# Promotion checklist — B01 mozhno-li-privezti-gibrid-iz-yaponii-2026

Дата публикации: 2026-10-14 (план; live после publish)  
Live URL: [REDACTED]/blog/mozhno-li-privezti-gibrid-iz-yaponii-2026/

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
Hybrid на шильдике ≠ разрешение на вывоз

• Сначала код кузова в аукционном листе
• Мягкий гибрид до 1,9 л — кандидат; полный / PHEV / EV / e-POWER — стоп
• Чек-лист из 10 пунктов до депозита через Владивосток

Читать: [REDACTED]/blog/mozhno-li-privezti-gibrid-iz-yaponii-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09/B01 — нет безопасных якорей)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «можно ли привезти гибрид из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base [REDACTED]` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles; site-name «Авто-Сейлс»).
- Doctor preflight ложно требует `--blog-path` у llms generator; CLI принимает только `--blog-dir` — см. incident queue.
