# Promotion checklist — B02 kak-poschitat-polnuyu-stoimost-avto-iz-yaponii-2026

Дата публикации: 2026-10-06 (ожидается после WP publish)  
Live URL: [PUBLIC_SITE_URL]/2026/10/06/kak-poschitat-polnuyu-stoimost-avto-iz-yaponii-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL (HEAD 200) — title, excerpt, featured image, FAQ
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
Цена лота на японском аукционе — ещё не итог во Владивостоке

• «Калькулятор растаможки» ≠ полная смета под ключ
• До ставки: лот + Япония + фрахт + таможня + утильсбор + СБКТС/ЭПТС + доставка по РФ
• Чек-лист из 10 пунктов и запас на курс / порог ~160 л.с.

Читать: [PUBLIC_SITE_URL]/2026/10/06/kak-poschitat-polnuyu-stoimost-avto-iz-yaponii-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (корпус 3 статьи, пересечений якорей не найдено)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «калькулятор авто из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply --article-dir …/B02-… --site-base $PUBLIC_SITE_URL` — opportunities_found=0; article.html без новых internal links.
- llms: `excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (без `--blog-path`; CLI его не принимает).
- Артефакты: `memory/blog/llms.txt`, `memory/blog/llms-full.txt`, `memory/blog/interlink-suggestions.json`.
- Publish ещё не запускался (следующий шаг Директора).
