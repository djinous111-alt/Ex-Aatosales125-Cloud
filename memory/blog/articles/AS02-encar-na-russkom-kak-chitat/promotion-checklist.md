# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: YYYY-MM-DD  
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
Переводчик сказал «без аварий» — схема кузова может врать иначе

• Encar на русском читают через перевод браузера на encar.com
• Манвоны ×10 000, схема X/W, прокат и страховая — до депозита
• «Без аварий» ≠ «ничего не чинили»

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

- Indexer: interlinker `--apply` — 1 link applied (AS02→AS09 Trust Encar).
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir` (CLI без `--blog-path`; INC-20261102-1606-director-llms-blog-path open).
- Publish: не выполнен Indexer (следующий шаг — publish).
