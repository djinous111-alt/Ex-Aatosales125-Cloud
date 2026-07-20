---
name: excalibur-wp-publish
description: Alias для publish-excalibur-blog — публикация статьи в WordPress.
---

# Excalibur BLOG — WP Publish (alias)

Канонический skill субагента Publish: **`skills/publish-excalibur-blog/SKILL.md`**

Используй его для всех шагов publish (preflight, dry-run, publish, fallback, ledger, handoff).

Контракт: `shared/excalibur-wp-publish-contract.md`

## CTA / schema / llms reinject (обязательно)

Перед dry-run/publish артефакты могут содержать `[REDACTED]` (secret-scan hygiene).
`excalibur_blog_wp_publish.py` reinject `PUBLIC_SITE_URL` / CTA env в HTML и `schema.jsonld` при загрузке payload.
Для llms.txt перед деплоем на сайт:
```bash
python3 scripts/excalibur_blog_cta_urls.py --reinject --write memory/blog/llms.txt memory/blog/llms-full.txt
```
Зависимость SSH: `paramiko` (в `requirements.txt` + cloud-agent-install). Проверка: `python3 scripts/excalibur_blog_doctor.py --publish`.
