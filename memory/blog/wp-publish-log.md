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

## 2026-07-24 — B02 dostavka-avto-iz-vladivostoka-2026

- **verdict:** PASS (REST recovery after HTTP disconnect)
- **post_id:** 3553 (update existing slug from 2026-07-21)
- **permalink:** [REDACTED]/2026/07/21/dostavka-avto-iz-vladivostoka-2026/
- **featured_image:** 3702 (`cover-3.png`)
- **inline_images:** 3703 (`inline-01-3.png`), 3704 (`inline-02-3.png`), 3705 (`inline-03-3.png`)
- **schema_meta:** ok (PHP writes `_excalibur_blog_schema_jsonld` before inline uploads; live page currently shows theme BlogPosting graph, not Excalibur FAQPage/HowTo echo)
- **skip_theme_faq_meta:** ok (set with schema_meta)
- **method:** SSH upload (`SSH_ROOT=.`) + HTTP trigger RemoteDisconnected; script fallback wait 120s timed out (stdout fully buffered); recovered via WP REST (`modified_gmt=2026-07-24T10:06:22`) + live HEAD 200
- **php_bytes:** 8847692
- **notes:** first attempt failed `ModuleNotFoundError: paramiko` (cloud install omits `requirements.txt`); pip install `--break-system-packages` then republish
- **result:** `memory/blog/articles/B02-dostavka-avto-iz-vladivostoka-2026/wp-publish-result.json`
