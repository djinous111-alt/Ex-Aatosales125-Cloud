# Promotion checklist — AS10 sbkts-i-epts-vladivostok-2026

Дата публикации: 2026-07-20  
Live URL: [REDACTED]/2026/07/20/sbkts-i-epts-vladivostok-2026/

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
После таможни — каша СБКТС/ЭПТС? Не платите «кнопку» вслепую

• Порядок: лаборатория → СБКТС → действующий ЭПТС → ОСАГО → ГИБДД
• Для физлица отсрочка УВЭОС (ЭРА) часто до 31.12.2027
• Без СБКТС на единичный ввоз ЭПТС не оформить

Читать: [REDACTED]/2026/07/20/sbkts-i-epts-vladivostok-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 не содержат якоря AS10; наоборот — тоже)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «сбктс эптс» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS10-sbkts-i-epts-vladivostok-2026 --site-base $PUBLIC_SITE_URL` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (CLI без `--blog-path`; см. incident INC-20260720-1329).
- Publish: pending после Indexer.
