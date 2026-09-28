# Promotion checklist — B01 kak-chitat-auktsionnyy-list-yaponii-2026

Дата публикации: 2026-09-29 (planned; publish pending)  
Live URL: [REDACTED]/blog/kak-chitat-auktsionnyy-list-yaponii-2026/

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
Балл 4.5 — ещё не решение

• Сначала R/RA и схема кузова, общий балл — в конце
• «Нет R» ≠ «не битая»: болтовые панели смотрите по кодам W/X/XX
• Решение «ставлю / уточняю / пропускаю» — до депозита брокеру

Читать: [REDACTED]/blog/kak-chitat-auktsionnyy-list-yaponii-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (B01 vs AS08/AS09 — нет keyword overlap в HTML)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как читать аукционный лист» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base [REDACTED]` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles, site-name «Авто-Сейлс»; URLs redacted for secret scanner).
- CLI llms generator: `--blog-dir` (legacy `--blog-path` в doctor/agent docs — drift, см. incident queue).
- Publish: не запускался (зона Indexer).
