# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-11-02 (черновик до WP publish)  
Live URL: https://avto-sales125.ru/blog/encar-na-russkom-kak-chitat/ (после publish)

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200), в т.ч. `/blog/trust-encar-carhistory-proverka-do-depozita/`
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Перевели Encar — и уже про депозит? Сначала VIN, манвоны и коды X/W.

• Официальный encar.com + перевод браузера, не клон из выдачи
• 5 полей карточки до любого чата о деньгах
• X на каркасе / flood = стоп до депозита

Читать: https://avto-sales125.ru/blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Indexer: AS02 → AS09 Trust Encar (`/blog/trust-encar-carhistory-proverka-do-depozita/`) — 1 link applied
- [ ] Обновить 1–2 старых поста → link to new (если есть на live WP)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query `encar на русском` (ручная проверка / Wordstat)

## Notes

- Indexer 2026-11-02: interlink_count=1; llms.txt + llms-full.txt regenerated.
- llms generator: used `--blog-dir` (no `--blog-path` in script; known INC-20261102-1708-director-llms-blog-path).
- Publish не запускался Indexer'ом.
