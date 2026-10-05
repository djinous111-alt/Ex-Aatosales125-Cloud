# Promotion checklist — B03 kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026

Дата публикации: 2026-10-06  
Live URL: [PUBLIC_SITE_URL]/2026/10/06/kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (post_id=4055; live HEAD 200; featured=4062; inlines=4057/4058/4059)
- [x] View source — JSON-LD BlogPosting + FAQPage via post meta `_excalibur_blog_schema_jsonld` (schema_len≈13146; skip_theme_faq=1)
- [x] Проверить internal links из статьи (200) — preflight link-verify PASS 0/8 failed
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Растаможен — а в ГИБДД развернули?

• После таможни цепочка жёсткая: лаборатория → СБКТС → ЭПТС «Действующий» → ОСАГО → ГИБДД
• СБКТС на единичный ввоз — с очным осмотром, не «по фото»
• Лабораторию сверяйте в реестре РАЛ

Читать: [PUBLIC_SITE_URL]/2026/10/06/kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 новых связей (corpus AS08/AS09/B03; пересечений с СБКТС/ЭПТС нет)
- [ ] Writer уже заложил relative anchors на LIVE: ЭРА-ГЛОНАСС, таможня, растаможка Китая — проверить 200 после publish

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как оформить СБКТС и ЭПТС» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B03-… --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-name «Авто-Сейлс»; B03 в индексе).
- Publish PASS: post **4055**; featured **4062**; inline **4057/4058/4059**; orphans from curl race 4056/4063/4064.
- Interlinker post-publish `--apply`: opportunities_found=0 (без изменений корпуса).
