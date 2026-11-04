# Promotion checklist — AS22 changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026

Дата публикации: 2026-11-05 (publish_blocked)  
Live URL: none (SSH TCP/22 timeout; NO LIVE write)

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
Депозит за ярлык Tech — лотерея?

• Tech/Flagship в объявлении ≠ оснащение ОД: сначала VIN и фото опций
• До оплаты зафиксируйте 2.0T или iDD, 2WD/AWD и полную смету через Владивосток
• Стоп, если в договоре только «автомобиль Changan UNI-K» без мотора и привода

Читать: /blog/changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [ ] Локальный interlinker: 0 opportunities (corpus AS08/AS09/AS22; suggestions пустые)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать changan uni-k из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply` выполнен; `interlink_count=0`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (AS22 в индексе; relative `/blog/<slug>/`).
- Publish: next (Indexer не публикует).

- Publish: ❌ PUBLISH BLOCKER — SSH TCP/22 timeout; ledger `publish_blocked`; no permalink.
