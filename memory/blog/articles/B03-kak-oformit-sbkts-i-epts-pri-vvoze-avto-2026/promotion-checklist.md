# Promotion checklist — B03 kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026

Дата публикации: 2026-10-06 (planned; pre-publish)  
Live URL: [PUBLIC_SITE_URL]/blog/kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026/

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
Растаможен — а в ГИБДД развернули?

• После таможни цепочка жёсткая: лаборатория → СБКТС → ЭПТС «Действующий» → ОСАГО → ГИБДД
• СБКТС на единичный ввоз — с очным осмотром, не «по фото»
• Лабораторию сверяйте в реестре РАЛ

Читать: [PUBLIC_SITE_URL]/blog/kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026/
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
- Publish ещё не запускался (Indexer only).
