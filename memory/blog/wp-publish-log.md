# WP publish log — Авто-Сейлс

Сайт: ${PUBLIC_SITE_URL}/
FTP/SFTP: [REDACTED_SSH_HOST] → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** ${PUBLIC_SITE_URL}/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
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
- **permalink:** ${PUBLIC_SITE_URL}/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-11-03 — AS02 encar-na-russkom-kak-chitat

- **verdict:** FAIL / ❌ PUBLISH BLOCKER
- **post_id:** none (no WP write)
- **permalink:** none
- **featured_image:** none
- **inline_images:** none
- **schema_meta:** n/a
- **method:** SSH bootstrap attempted; DNS OK; TCP:22 TimeoutError / Errno 110 (~20s probe, ~134s paramiko)
- **env-check:** PASS (`ALLOW=yes`, `SSH_ROOT=.`)
- **dry-run:** PASS (slug `encar-na-russkom-kak-chitat`, PHP ~7.37MB)
- **link-verify:** PASS (soft_pass catalog_ssl ×2; Telegram 200)
- **denylist untouched:** 4758, 4746, 4740, 3430, 3394, 4717, 4711
- **note:** `SSH_HOST_IP` unset; credentials not invented; intentional same-slug refresh of historical 3394 deferred until SSH restored
- **result:** `memory/blog/articles/AS02-encar-na-russkom-kak-chitat/wp-publish-result.json`
- **incident:** `memory/pipeline-fix-queue.md#INC-20261103-1400-publish-ssh-tcp22-timeout`

