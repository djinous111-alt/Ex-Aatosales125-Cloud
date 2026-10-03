# Promotion checklist — B01 kak-proverit-30-minutnuyu-moshchnost-ev-iz-kitaya-2026

Дата публикации: 2026-10-03 (planned)  
Live URL: [REDACTED]/2026/10/03/kak-proverit-30-minutnuyu-moshchnost-ev-iz-kitaya-2026/

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
Депозит без 30-минутной мощности — лотерея утильсбора

• Для ЭПТС важна не пик из рекламы, а 30-минутная мощность
• С 01.12.2025 льгота физлица по EV завязана на порог ≤80 л.с.
• Сначала прецедент/документы завода, потом деньги

Читать: [REDACTED]/2026/10/03/kak-proverit-30-minutnuyu-moshchnost-ev-iz-kitaya-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (нет пересечений якорей с AS08/AS09)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «30 минутная мощность» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles, B01 включён).
- CLI llms generator: использовать `--blog-dir` (не `--blog-path`); doctor/skill examples пока расходятся.
