# Promotion checklist — AS10 kak-vybrat-toyota-sienta-iz-yaponii-2026

Дата публикации: 2026-11-02 (план; publish ещё не выполнен)  
Live URL: /blog/kak-vybrat-toyota-sienta-iz-yaponii-2026/

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
Hybrid на табличке Sienta — ещё не выгода

• Сначала сценарий семьи и код кузова, потом мотор
• Бензин 1.5 обычно прямее во Владивосток; гибрид чаще через третью страну
• До депозита: аукционный лист + смета под ключ по этапам

Читать: /blog/kak-vybrat-toyota-sienta-iz-yaponii-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: opportunities_found=0 (корпус 3 статьи AS08/AS09/AS10; suggestions=[])

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать toyota sienta из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply --article-dir …/AS10-… --site-base $PUBLIC_SITE_URL` → 0 links.
- llms: `excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (без `--blog-path` — флага нет в CLI).
- Cover+Schema merged; GEO QA PASS 88; publish не стартован indexer'ом.
- LIVE caution: не перезаписывать исторический WP AS10/Haval M6 (4711) — только новый slug.
