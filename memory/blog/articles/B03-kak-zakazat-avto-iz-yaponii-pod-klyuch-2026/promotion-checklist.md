# Promotion checklist — B03 kak-zakazat-avto-iz-yaponii-pod-klyuch-2026

Дата публикации: 2026-09-30 (planned)  
Live URL: [REDACTED]/blog/kak-zakazat-avto-iz-yaponii-pod-klyuch-2026/

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
«Под ключ» без сметы — лотерея

• Цена лота ≠ бюджет под ключ: логистика, таможня, утильсбор, СВХ, СБКТС/ЭПТС
• До ставки — возраст, объём/мощность и полный бюджет до вашего города
• Нет письменной сметы и перевода листа — нет депозита

Читать: [REDACTED]/blog/kak-zakazat-avto-iz-yaponii-pod-klyuch-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 corpus; suggestions=[])

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «заказ авто из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir ... --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles indexed; site-name «Авто-Сейлс»).
- llms CLI: `--blog-dir` + `--out-dir` (без `--blog-path`; doctor/skill устарели).
