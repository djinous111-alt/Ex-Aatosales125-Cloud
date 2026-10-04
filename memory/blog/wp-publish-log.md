# WP publish log — Авто-Сейлс

Сайт: https://avtosales125.ru/
FTP/SFTP: djinoum7.beget.tech → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** https://avtosales125.ru/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
- **featured_image:** 3349
- **inline_images:** 3351 (`inline-01.png`), 3355 (`inline-02.png`), 3358 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch timeout; curl `--max-time 300` OK)
- **note:** в `article.meta.json` добавлены `title`/`h1`/`description`/`cover_alt` для payload; `FTP_ROOT` исправлен на `/`
- **result:** `memory/blog/articles/AS08-samye-komfortnye-avto-myagkaya-podveska-2026/wp-publish-result.json`

## 2026-07-17 — AS09 trust-encar-carhistory-proverka-do-depozita

- **verdict:** PASS
- **post_id:** 3364
- **permalink:** https://avtosales125.ru/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-10-04 — B01 prohodnye-avto-iz-yaponii-2026-chek-list-do-stavki

- **verdict:** PASS (soft-success)
- **post_id:** 3991
- **permalink:** [PUBLIC_SITE_URL]/2026/10/04/prohodnye-avto-iz-yaponii-2026-chek-list-do-stavki/
- **featured_image:** 4001
- **inline_images:** 3999 (`inline-01.png`), 4003 (`inline-02.png`), 4005 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`; BlogPosting+FAQPage+HowTo; len=10317)
- **skip_theme_faq_meta:** ok
- **method:** SSH bootstrap upload OK → local HTTP timeout 120s → WebFetch timeout → script fallback wait expired → curl `--max-time 300` OK (HTTP 200, ~84s) + WP REST poll by slug soft-success; schema verified via one-shot SSH PHP check
- **avoid_list:** not 3837 / other known Japan-turnkey IDs; new slug `prohodnye-avto-iz-yaponii-2026-chek-list-do-stavki`
- **orphans:** overlapping triggers left unused cover/inline variants (3992–3997, 4002/4004/4007…); live uses featured 4001, inlines [3999, 4003, 4005]
- **result:** `memory/blog/articles/B01-prohodnye-avto-iz-yaponii-2026-chek-list-do-stavki/wp-publish-result.json`

