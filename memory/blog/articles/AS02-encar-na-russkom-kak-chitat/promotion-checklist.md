# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-11-03 (ожидается publish)  
Live URL: /blog/encar-na-russkom-kak-chitat/

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
Переводчик написал «без аварий» — уже тянет кинуть депозит?

• Encar на русском: перевод браузера + сохранить ID лота
• 만원 × 10000, схема X/W, ловушка 무사고
• CarHistory ≠ идеальный кузов; Trust Encar ≠ диагностика

Читать: /blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: spoke уже в body AS02 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`, якорь «Trust Encar и Carhistory до депозита»); `--apply` 2026-11-03 → 0 новых (already present)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS02-encar-na-russkom-kak-chitat` — opportunities=0, applied=0; existing spoke AS02→AS09.
- llms.txt / llms-full.txt: `memory/blog/` via `--blog-dir` (alias `--blog-path` отсутствует; doctor FAIL известен); relative `/blog/...` для commit hygiene.
- Cover+Schema PASS; publish=yes next (не из indexer).
