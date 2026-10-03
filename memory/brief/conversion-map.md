# Conversion map — Excalibur BLOG (Авто-Сейлс)


| CTA | URL / action | Max mentions per article | Notes |
| --- | --- | --- | --- |
| Каталог авто | https://avto-sales125.ru/ | 3 | главный оффер; расчёты и подбор только здесь |
| Telegram Авто-Сейлс | https://t.me/avtosales125 | 2 | детали заказа, ответы менеджера |
| MAX | https://max.ru/id2508140890_biz | 1 | альтернативный мессенджер |
| Отзывы 2GIS | https://2gis.ru/vladivostok/search/авто%20сейлс%20владивосток/firm/70000001090415417/131.924668%2C43.140033/tab/reviews | 1 | доверие / E-E-A-T |
| Instagram | https://www.instagram.com/avtosales_rf | 1 | опционально, если релевантно |
| Адрес офиса | Владивосток, Днепровская 40а стр. 4 | 1 | в футере/блоке компании, не как CTA-кнопка |

## Git / publish convention

В `article.html` используй плейсхолдеры `[CATALOG_URL]` и `[TELEGRAM_URL]`. Живые URL из этого файла — только для agent-side проверки; в git article не коммить значения Cloud Secrets. Publish expand'ит токены из env.
