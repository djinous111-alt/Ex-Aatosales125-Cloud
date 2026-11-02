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
- **post_id:** none (LIVE not touched; denylist 4758/4746/4740/3430/3394/4717/4711 untouched)
- **permalink:** none
- **featured_image:** none
- **inline_images:** none
- **schema_meta:** n/a
- **method:** SSH transport only; stopped at `paramiko.Transport` / `socket.getaddrinfo` on `SSH_HOST`
- **preflight:** `--env-check` OK (allow=yes, SSH creds configured, root non-dot + dot fallback); dry-run OK (slug=`encar-na-russkom-kak-chitat`, PHP ~6.7MB); link-verify FAIL on site/catalog DNS Temporary failure (Telegram HEAD 200; catalog soft_pass)
- **blocker:** Beget `SSH_HOST` DNS empty/SERVFAIL in Cloud resolver; no `SSH_HOST_IP` secret; PUBLIC host IP `:22` TCP timeout (HTTP/443 open — not usable as SSH fallback); UDP DNS to 8.8.8.8/1.1.1.1/9.9.9.9 timed out
- **fallback:** HTTP/WebFetch not reached (bootstrap never uploaded)
- **paramiko:** installed via pip workaround (`ModuleNotFoundError` on image)
- **result:** `memory/blog/articles/AS02-encar-na-russkom-kak-chitat/wp-publish-result.json`
- **incident:** `memory/pipeline-fix-queue.md#INC-20261102-1658-publish-ssh-dns-beget`
