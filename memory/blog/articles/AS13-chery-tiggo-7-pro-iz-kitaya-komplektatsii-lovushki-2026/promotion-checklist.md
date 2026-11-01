# Promotion checklist — AS13 chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026

Дата публикации: 2026-11-01  
Live URL: ${PUBLIC_SITE_URL}/2026/11/01/chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL (HEAD 200; post 4746; featured 4752) — title, excerpt, featured image, FAQ
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
Депозит без VIN — лотерея комплектации

• Pro / Pro Max / Jaecoo / китайский 7L — не одно и то же
• До оплаты: VIN + мотор/коробка/опции + пакет 180 дней
• Нет таблицы «заявлено vs факт» — нет перевода

Читать: /blog/chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: opportunities_found=0 (корпус AS08/AS09/AS13; релевантных якорей не найдено)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать тигго 7 про из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (relative `/blog/<slug>/`, AS13 listed).
- Restored durable CLI `--blog-path` alias + `--relative-urls` in `scripts/excalibur_blog_llms_generator.py` (doctor PASS).
- Publish: не запускался Indexer'ом.

## Publish result

- post_id: **4746**
- featured_image: **4752**
- inline: **4754 / 4755 / 4756**
- schema_meta / skip_theme_faq: ok
- method: SSH + WebFetch fallback after HTTP TimeoutError
- Publish: PASS — do not republish.
