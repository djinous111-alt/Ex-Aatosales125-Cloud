# Promotion checklist — AS01 rastamozhka-avto-iz-korei-2026

Дата публикации: 2026-07-19 (pending WP publish)  
Live URL: [REDACTED]/blog/rastamozhka-avto-iz-korei-2026/ (ожидаемый permalink; уточнить после publish)

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
Растаможка ≠ одна пошлина — иначе СВХ во Владивостоке съест депозит

• Цепочка: Encar → море → СВХ → таможня → СБКТС → ЭПТС → ОСАГО → ГИБДД
• Ориентир полного пути 30–45 дней (при заминках до ~60)
• Документы и проверка лота — до депозита, не после

Читать: [REDACTED]/blog/rastamozhka-avto-iz-korei-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] AS01 уже ссылается на AS09 (Trust Encar / Carhistory) вручную в чеклисте
- [x] Локальный interlinker `--apply`: 0 новых opportunities (3 статьи в memory; AS01↔AS08/AS09 без exact keyword match; AS01→AS09 уже есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «растаможка авто из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026 --site-base $PUBLIC_SITE_URL` — links applied: 0.
- llms.txt / llms-full.txt: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (без `--blog-path`; CLI его не принимает).
- Publish: pending (Indexer не публикует).
