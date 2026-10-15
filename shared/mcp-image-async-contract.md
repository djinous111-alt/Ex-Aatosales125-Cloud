# MCP Image Async Contract

Для image generation в Cursor Cloud нельзя полагаться на один долгий sync MCP call: Cursor MCP client может оборвать соединение раньше, чем backend дождётся Kie.ai.

## Required tools

Рекомендуемый контракт для `user-mcp-kv`:

1. `gpt-image-2-create` / `gpt-image-2-start`
   - input: тот же JSON, что у sync `gpt-image-2` (`prompt`, `input_urls`, `aspect_ratio`, `resolution`)
   - output за короткое время: `{ "task_id": "...", "status": "queued|running" }`
   - должен быть idempotent по `request_id`/hash prompt+input_urls, чтобы агент не создавал дубли

2. `gpt-image-2-status` / `gpt-image-2-result`
   - input: `{ "task_id": "..." }`
   - output: `{ "status": "queued|running|succeeded|failed", "url": "...", "error": "..." }`
   - агент вызывает каждые 10–15 секунд до `status=succeeded` и `url`

## Agent rule

Cover agent (Cloud order of preference):

1. Async MCP tools (`gpt-image-2-create` / `status`), если они есть в Cursor `Available Tools`.
2. **Preferred Cloud path when async MCP отсутствует:** сразу Kie HTTP async script (не legacy sync MCP):
   ```bash
   python3 scripts/excalibur_blog_kie_gpt_image2_api.py --article-dir memory/blog/articles/<topic_id>-<slug>
   ```
   Требует `KIE_API_KEY`. Пишет `cover/quad-mcp-result.json` → далее `excalibur_blog_quad_apply.py --inject-html`.
3. Sync MCP `gpt-image-2` — только один раз, если async MCP и Kie недоступны.
4. После `MCP error -32001 Request timed out` / HTTP `-32001`:
   - **не** blind retry sync create;
   - если в ответе/логе нет URL и Cursor events недоступны → Kie recovery (п.2), если `KIE_API_KEY` есть;
   - `COVER MCP ASYNC BLOCKER` только если нет async MCP tools **и** нет `KIE_API_KEY` **и** нет recoverable URL.

## Why

`KIE_IMAGE_MAX_WAIT_SECONDS` и nginx `proxy_read_timeout` не гарантируют, что Cursor MCP client будет держать один tool call так же долго. Async start/status/result (MCP или Kie HTTP) убирает зависимость от длинного sync соединения и позволяет агенту получить URL через время без дублей.
