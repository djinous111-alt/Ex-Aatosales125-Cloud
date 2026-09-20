# Kie GPT Image 2 API Contract

Primary Cloud path for Excalibur BLOG cover generation.

## Why

Cursor Cloud can terminate long sync MCP tool calls before GPT Image 2 finishes
2K image-to-image generation. The direct Kie API is asynchronous:

```text
createTask -> taskId -> recordInfo polling -> resultUrls[0]
```

This keeps waiting in the shell process instead of a single MCP request.

## Auth

- Env var: `KIE_API_KEY`
- Store only in Cursor Cloud Secrets / environment.
- Never commit, print, or copy the key into handoff, PR bodies, article files, or logs.

## Cover command

```bash
python3 scripts/excalibur_blog_kie_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --min-credits 2.0
```

Credits preflight only:

```bash
python3 scripts/excalibur_blog_kie_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --credits-only --min-credits 2.0
```

Calls `GET /api/v1/chat/credit` and writes `cover/kie-credits-preflight.json`.  
If balance < min (default 2.0 for 2K i2i) → blocker before createTask. Human must top up `KIE_API_KEY` wallet; cover may use emergency GenerateImage→2048×1152→split fallback.

The script reads:

- `cover/quad-mcp-batch.json` -> `jobs[0].mcp_args`

The script writes:

- `cover/kie-credits-preflight.json` -> balance / min / ok
- `cover/kie-image-task.json` -> `task_id` and non-secret status
- `cover/quad-mcp-result.json` -> generated URL, compatible with `quad_apply`

Then run:

```bash
python3 scripts/excalibur_blog_quad_apply.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --inject-html
```

## API shape

Create:

```json
{
  "model": "gpt-image-2-image-to-image",
  "input": {
    "prompt": "...",
    "input_urls": ["https://.../ava.jpg"],
    "aspect_ratio": "16:9",
    "resolution": "2K"
  }
}
```

Poll:

```text
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>
```

Terminal states:

- `success`: parse `data.resultJson` and use `resultUrls[0]`
- `fail`: stop with `KIE API BLOCKER`
- timeout without URL: stop with `KIE API BLOCKER`

## Guardrails

- One API task per article cover run, not four separate images.
- `input_urls` is required; text-only generation is a cover blocker.
- Do not retry createTask blindly after a network ambiguity if a `taskId` is known; poll the known task.
