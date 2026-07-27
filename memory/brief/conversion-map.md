# Conversion map — Excalibur BLOG (Авто-Сейлс)


| CTA | URL / action | Max mentions per article | Notes |
| --- | --- | --- | --- |
| Каталог авто | https://avto-sales125.ru/ | 3 | главный оффер; расчёты и подбор только здесь |
| Telegram Авто-Сейлс | plaintext `Telegram @avtosales125` (no t.me href in git) | 2 | secret-scan: do not put TELEGRAM_URL/t.me secret value as href in committed HTML |
| MAX | https://max.ru/id2508140890_biz | 1 | альтернативный мессенджер |
| Отзывы 2GIS | https://2gis.ru/vladivostok/search/авто%20сейлс%20владивосток/firm/70000001090415417/131.924668%2C43.140033/tab/reviews | 1 | доверие / E-E-A-T |
| Instagram | https://www.instagram.com/avtosales_rf | 1 | опционально, если релевантно |
| Адрес офиса | Владивосток, Днепровская 40а стр. 4 | 1 | в футере/блоке компании, не как CTA-кнопка |

## Committed HTML CTA canon

- В `article.html` (git): Telegram = plaintext `@handle`, без `href` на secret `TELEGRAM_URL` / `t.me/...`.
- Не используй `href="[REDACTED]"` как заглушку — не кликабельно.
- Live WP может получить кликабельный URL через publish/env; git-артефакт остаётся secret-scan-safe.
