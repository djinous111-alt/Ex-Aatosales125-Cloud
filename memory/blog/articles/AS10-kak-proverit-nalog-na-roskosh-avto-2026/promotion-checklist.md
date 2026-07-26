# Promotion checklist — AS10 kak-proverit-nalog-na-roskosh-avto-2026

Дата публикации: 2026-07-26 (planned; WP publish pending)  
Live URL: [REDACTED]blog/kak-proverit-nalog-na-roskosh-avto-2026/

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
Посредник говорит «дешевле 10 млн — роскоши нет»? ФНС смотрит перечень, не договор

• Налог на роскошь = транспортный налог ×3 по перечню Минпромторга
• До депозита: марка + версия + год → файл 2026 → скрин «в списке / нет»
• Цена в договоре налоговую не интересует

Читать: [REDACTED]blog/kak-proverit-nalog-na-roskosh-avto-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (AS08/AS09 не содержат якорей AS10)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «налог на роскошь автомобили 2026» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir memory/blog/articles/AS10-kak-proverit-nalog-na-roskosh-avto-2026` — 0 links applied (нет keyword overlap с AS08/AS09).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir memory/blog/articles`, без `--blog-path /`).
- Cover ❌ Kie 402 — featured/inline PNG отсутствуют; publish может идти без cover по решению Director.
- Schema PASS: BlogPosting + FAQPage + HowTo.
