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

## 2026-11-02 — AS02 encar-na-russkom-kak-chitat

- **verdict:** FAIL / ❌ PUBLISH BLOCKER
- **post_id:** none (no WP write)
- **permalink:** none
- **featured_image:** none
- **inline_images:** none
- **schema_meta:** n/a
- **method:** not attempted (SSH unreachable)
- **env:** EXCALIBUR_BLOG_ALLOW_PUBLISH=yes; env-check PASS; dry-run PASS (~6.8MB PHP); SSH_ROOT=.
- **blocker:** SSH_HOST DNS resolves, but TCP/22 Connection timed out (Errno 110); `SSH_HOST_IP` unset — IP not invented. PUBLIC_SITE_URL HTTPS SSL handshake also timed out from Cloud.
- **link-verify:** fail (internal `/blog/trust-encar-carhistory-proverka-do-depozita/` SSL timeout; catalog soft_pass; encar/carhistory/telegram OK)
- **denylist:** untouched — WP IDs 4758/4746/4740/3430/3394/4717/4711; foreign slug `encar-na-russkom-kak-chitat-obyavleniya-i-bezopasno-kupit-avto` not targeted. Target slug only: `encar-na-russkom-kak-chitat`.
- **result:** `memory/blog/articles/AS02-encar-na-russkom-kak-chitat/wp-publish-result.json`
- **incident:** `memory/pipeline-fix-queue.md#INC-20261102-1804-publish-ssh-tcp22-timeout`
