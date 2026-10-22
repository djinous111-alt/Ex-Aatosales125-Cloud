# Promotion checklist — B01 levyj-rul-iz-yaponii-2026-chek-list

Дата публикации: 2026-10-22  
Live URL: (после publish) /levyj-rul-iz-yaponii-2026-chek-list/

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
"Левый руль из Японии" почти никогда не значит массовую Toyota с аукциона.

• До депозита: фото салона (руль), страна вывоза, VIN в договоре
• Нужен обычный LHD — честнее Корея или Китай, не «любой ценой» JP
• Нет трёх строк в договоре — нет перевода

Читать: [URL после publish]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [ ] Soft Ept02: interlinker нашёл 0 auto-opportunities (AS08/AS09 keywords не совпали с текстом B01); при publish/fixer можно вручную связать B01↔AS09 (Корея/Encar до депозита)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat): «левый руль из японии»

## Notes

- Indexer 2026-10-22: interlink opportunities_found=0; llms.txt + llms-full.txt regenerated (root-relative `/blog/<slug>/`).
- Cover+Schema DONE; GEO QA PASS 86.
- Doctor preflight: FAIL `llms generator supports --blog-path` — см. INC-20261022-0935.
