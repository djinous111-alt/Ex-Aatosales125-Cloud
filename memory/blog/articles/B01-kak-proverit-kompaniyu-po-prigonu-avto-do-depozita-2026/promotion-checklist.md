# Promotion checklist — B01 kak-proverit-kompaniyu-po-prigonu-avto-do-depozita-2026

Дата публикации: 2026-10-14 (ожидается после WP publish)  
Live URL: [REDACTED]/blog/kak-proverit-kompaniyu-po-prigonu-avto-do-depozita-2026/

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
Депозит «сегодня» — или 15 минут проверки?

• ИНН на egrul.nalog.ru + сверка названия с договором
• Платите только на р/с юрлица — не на карту менеджера
• Нет договора со сметой и возвратом аванса — нет перевода

Читать: [REDACTED]/blog/kak-proverit-kompaniyu-po-prigonu-avto-do-depozita-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (корпус AS08/AS09 без совпадений якорей B01)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «компании по пригону авто» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base $PUBLIC_SITE_URL` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir memory/blog/articles` (без `--blog-path`; CLI/doctor stale → INC-20261014-001).
- Commit hygiene: URL bases in llms*.txt / interlink-report → `[REDACTED]` (secret-scan); publish expands before deploy (INC-20261014-1349).
- Publish: pending (publish: yes после Indexer).
