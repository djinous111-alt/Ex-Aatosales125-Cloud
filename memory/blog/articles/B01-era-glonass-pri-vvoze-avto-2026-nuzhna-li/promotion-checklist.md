# Promotion checklist — B01 era-glonass-pri-vvoze-avto-2026-nuzhna-li

Дата публикации: 2026-10-03 (ожидается)  
Live URL: [REDACTED]/2026/10/03/era-glonass-pri-vvoze-avto-2026-nuzhna-li/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)
- [x] Подставить `[CATALOG_URL]` / `[TELEGRAM_URL]` из Cloud Secrets перед upload (см. GEO QA blocker)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Кнопку SOS ставить или нет?

• Физлицо «для себя»: мораторий до 31.12.2027 (пока нет нового ПП)
• ЮЛ/ИП: ЭРА обязательна с 01.10.2022
• Смотрите дату оформления, не дату аукциона

Читать: [URL после publish]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (AS08/AS09 keywords не пересекаются с B01 HTML)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «нужна ли эра глонасс» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base $PUBLIC_SITE_URL` — 0 links.
- llms.txt / llms-full.txt обновлены: `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (3 articles).
- Cover + schema DONE; ready_for_publish: yes (CTA placeholders — зона Publish).
