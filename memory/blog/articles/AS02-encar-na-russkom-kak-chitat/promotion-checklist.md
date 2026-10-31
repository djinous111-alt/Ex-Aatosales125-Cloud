# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-11-01 (план; live после publish)  
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
Красивый перевод Encar ≠ проверка лота

• N만원 × 10 000 = воны (не «тысячи рублей»)
• 무사고 часто только про каркас, не «идеал кузова»
• До депозита: схема X/W + страховая + свежий отчёт

Читать: /blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (corpus AS08/AS09/AS02; exact match)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir … --site-base [REDACTED]` → opportunities_found=0; report `memory/blog/interlink-suggestions.json` (site_base redacted).
- llms: `memory/blog/llms.txt`, `memory/blog/llms-full.txt` через `--blog-dir` + `--site-base ""` (relative `/blog/<slug>/`); CLI без `--blog-path` (doctor drift — open INC).
- Publish: not started by indexer.
