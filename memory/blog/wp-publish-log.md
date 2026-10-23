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

## 2026-10-23 — B01 geely-coolray-iz-kitaya-komplektatsii-lovushki-2026

- **verdict:** PASS
- **post_id:** 4465
- **permalink:** [REDACTED]/2026/10/23/geely-coolray-iz-kitaya-komplektatsii-lovushki-2026/
- **featured_image:** 4472
- **inline_images:** 4473 (`inline-01.png`), 4474 (`inline-02.png`), 4475 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`, len≈8326, BlogPosting+FAQPage)
- **skip_theme_faq_meta:** ok (`1`)
- **method:** SSH (`SSH_ROOT=.`) + HTTP RemoteDisconnected → FALLBACK curl `--max-time 300` OK (~111s); script wait 120s timed out before curl finished → REST/wp-cli reconstruct (no third publish)
- **note:** duplicate media from double trigger (orphans 4466–4469; live content/featured point at 4472–4475 `*-1.png`). NEW post — do not republish as 4453/4447/4441/4435/etc. HEAD 200; REST id=4465.
- **result:** `memory/blog/articles/B01-geely-coolray-iz-kitaya-komplektatsii-lovushki-2026/wp-publish-result.json`
- **incidents:** INC-20261023-0942-publish-site-env-paramiko; INC-20261023-0943-publish-http-fallback-wait-120

