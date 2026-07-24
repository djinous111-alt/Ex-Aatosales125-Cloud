# Promotion checklist — B05 rastamozhka-elektromobilya-iz-kitaya-2026

Дата публикации: 2026-07-25 (pending WP publish)  
Live URL: (после publish) /blog/rastamozhka-elektromobilya-iz-kitaya-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
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
Электро из Китая: сначала чек-лист, потом депозит

• Льгота ЕАЭС 2026 на EV в AM/BY/KG — не для резидентов РФ
• Путь: проверка → СВХ → платежи на своё имя → СБКТС → ЭПТС → ГИБДД
• Суммы пошлин не из статьи — расчёт под модель в каталоге / @avtosales125

Читать: (live URL после publish)
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть; на WP: rastamozhka-avto-iz-kitaya-2026 / avto-iz-kitaya-pod-zakaz-2026)
- [x] Локальный interlinker `--apply`: 0 opportunities (корпус memory: AS08, AS09, B05 — нет keyword overlap с EV-растаможкой)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «растаможка электромобиля из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B05-… --site-base $PUBLIC_SITE_URL` — opportunities=0, links_applied=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles; site-name «Авто-Сейлс»). CLI: `--blog-dir` (без `--blog-path`).
- GEO QA Ept02 (нет 2–3 blog internal links) остаётся non-blocking до inbound с WP/топовых статей после publish.
