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

## 2026-10-30 — B01 tank-500-iz-kitaya-komplektatsii-lovushki-2026

- **verdict:** PASS
- **post_id:** 4669
- **permalink:** ${PUBLIC_SITE_URL}/2026/10/30/tank-500-iz-kitaya-komplektatsii-lovushki-2026/
- **featured_image:** 4670
- **inline_images:** 4671 (`inline-01.png`), 4672 (`inline-02.png`), 4673 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld` LEN=12259; FAQ+HowTo+BlogPosting; WP-CLI verified)
- **skip_theme_faq_meta:** ok (`1`)
- **method:** SSH (`SSH_ROOT=.`) upload OK; local HTTP trigger RemoteDisconnected; server completed; REST reconstruct (no republish / no second trigger)
- **head_check:** 200
- **warnings:** client WebFetch fallback wait timed out 120s after disconnect; publish already LIVE
- **foreign_untouched:** 4663 Atlas / 4657 Qashqai / prior denylist
- **result:** `memory/blog/articles/B01-tank-500-iz-kitaya-komplektatsii-lovushki-2026/wp-publish-result.json`

