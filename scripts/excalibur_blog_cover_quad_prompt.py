#!/usr/bin/env python3
"""Build MCP prompt + batch for ONE quad canvas (4 panels) with hero i2i reference."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


MAX_MCP_PROMPT_CHARS = 3500
PREFERRED_REFERENCE_HOST = "avtosales125.ru"
ALLOWED_REFERENCE_HOST_FRAGMENTS = (
    "avtosales125.ru",
    "litter.catbox.moe",
    "files.catbox.moe",
    "catbox.moe",
    "0x0.st",
)
MCP_RESOLUTION = "2K"
KIE_IMAGE_MODEL = "gpt-image-2-image-to-image"


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def compact(value: object, limit: int) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def inline_panel_prompt(slot: dict, types_catalog: dict) -> str:
    type_id = slot.get("visual_type") or "infographic_card"
    type_def = (types_catalog.get("types") or {}).get(type_id) or {}
    label = type_def.get("label_ru", type_id)
    h2 = compact(slot.get("h2_anchor", ""), 95)
    scene = compact(slot.get("scene_hint", ""), 220)
    return f"{label}; H2: «{h2}»; scene: {scene}; no host face."


def validate_reference_url(ref_url: str) -> bool:
    url = (ref_url or "").strip()
    if not url.startswith("https://"):
        print(
            "❌ COVER HERO BLOCKER: reference_url_hosted must be HTTPS "
            "(Kie cannot reliably fetch http:// hosts with redirects).",
            file=sys.stderr,
        )
        return False
    lower = url.lower()
    if any(host in lower for host in ALLOWED_REFERENCE_HOST_FRAGMENTS):
        return True
    print(
        "❌ COVER HERO BLOCKER: reference_url_hosted host not allowlisted for Kie fetch. "
        f"Prefer HTTPS {PREFERRED_REFERENCE_HOST} media, or litterbox/catbox/0x0 fallback. Got: {url}",
        file=sys.stderr,
    )
    return False


def outfit_prompt_line(hero: dict, cover_slot: dict) -> str:
    """Outfit follows blog-hero outfit_rule + cover scene weather/topic — never a white-hoodie lock."""
    outfit_rule = compact(hero.get("outfit_rule") or "", 260)
    scene = compact(cover_slot.get("scene_hint") or "", 180)
    topic_hint = compact(hero.get("topic_outfit_hint") or "", 160)
    rule = outfit_rule or (
        "Change outfit to match scene WEATHER and ARTICLE TOPIC "
        "(rain jacket in rain/port, winter coat in snow, light shirt in heat, smart casual for docs)."
    )
    extras = []
    if scene:
        extras.append(f"cover scene_hint: {scene}")
    if topic_hint:
        extras.append(f"topic_outfit_hint: {topic_hint}")
    extra = (" " + " ".join(extras)) if extras else ""
    return (
        "REFERENCE FACE only on top-left cover: preserve glasses, quiff, beard and old meme-person vibe. "
        f"OUTFIT from scene weather+topic (blog-hero outfit_rule): {rule}.{extra} "
        "Vary pose, gesture, angle, expression, props and composition every cover. "
        "No headphones/headset/earbuds. Do not copy reference clothing. "
        "NOT a locked white hoodie; never force thick heavyweight white hoodie."
    )


def validate_prompt_budget(prompt: str) -> bool:
    prompt_chars = len(prompt)
    if prompt_chars <= MAX_MCP_PROMPT_CHARS:
        return True
    print(
        f"❌ COVER PROMPT BLOCKER: MCP prompt is {prompt_chars} chars, max {MAX_MCP_PROMPT_CHARS}. "
        "Use the compact prompt builder; do not duplicate style/negative blocks per panel.",
        file=sys.stderr,
    )
    return False


def build_prompt(manifest: dict, style: dict, hero: dict, types_catalog: dict, design_code: dict) -> str:
    slots = manifest.get("slots") or {}

    def slot(key: str) -> dict:
        return slots.get(key) or {}

    cover = slot("cover")
    i1, i2, i3 = slot("inline_1"), slot("inline_2"), slot("inline_3")

    lines = [
        "Russian human-made Excalibur BLOG hook collage on PURE WHITE #FFFFFF. Zine/trash-design: torn paper, scotch tape, pink notes, marker arrows, fake RU UI screenshots, meme cutouts. DESIGN.md-inspired bold readable Cyrillic; rotate hot accents (hot pink/purple/blue/orange); keep stickers/memes/collage; no price badges. Not corporate, not stock.",
        "Single 2048x1152 canvas, exact 2x2 grid, four equal 16:9 panels (1024x576 each). Thin center gutters only; no bleed across quadrants.",
        "",
        "ALL panels keep a clean pure white #FFFFFF base; scraps/cards may cast light shadows but no beige, gray, gradient, grunge, paper-tint, or colored full-panel background.",
        "",
        "Sticker and meme text must be sharp but non-toxic: no insults, no humiliating labels, no Russian words like лох, лохов, для лохов.",
        "",
        outfit_prompt_line(hero, cover),
        "",
        f'Top-left COVER: hook "{compact(manifest.get("cover_hook", ""), 120)}"; caption "{compact(cover.get("meme_caption_ru", ""), 45)}"; scene: {compact(cover.get("scene_hint", ""), 320)}; host with reference face; huge readable Cyrillic hook; 1-2 meme reaction cutouts.',
        "",
        f"Top-right inline: {inline_panel_prompt(i1, types_catalog)} Same Excalibur collage layer, useful UI/diagram, small meme cutout.",
        f"Bottom-left inline: {inline_panel_prompt(i2, types_catalog)} Same Excalibur collage layer, useful UI/diagram, small meme cutout.",
        f"Bottom-right inline: {inline_panel_prompt(i3, types_catalog)} Same Excalibur collage layer, useful UI/diagram, small meme cutout.",
        "",
        "Inline panels must NOT be plain whiteboards or clean SaaS slides. Negative: beige/cream/off-white paper background, gray background, gradients, grunge background, headphones, headset, earbuds, English/Latin UI, watermark, logo, vertical 9:16, corporate stock banner, unreadable text, extra faces on inline panels.",
    ]
    return "\n".join(line for line in lines if line)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--write-batch", action="store_true", help="Write cover/quad-mcp-batch.json")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = article_dir / manifest_path
    if not manifest_path.is_file():
        print(f"❌ PROMPT BLOCKER: {manifest_path} not found", file=sys.stderr)
        return 1

    manifest = load_json(manifest_path)
    hero = load_json(root / manifest.get("blog_hero", "memory/cover/blog-hero.json"))
    style = load_json(root / manifest.get("style_file", "memory/cover/quad-style-digital-meme-collage-ru.json"))
    types_path = root / manifest.get("inline_types_catalog", "memory/cover/inline-visual-types.json")
    types_catalog = load_json(types_path) if types_path.is_file() else {"types": {}}
    design_code_path = root / style.get("design_code", "memory/cover/cover-design-code.json")
    design_code = load_json(design_code_path) if design_code_path.is_file() else {}

    ref_url = (hero.get("reference_url_hosted") or "").strip()
    if not ref_url:
        print(
            "❌ COVER HERO BLOCKER: reference_url_hosted missing. Run excalibur_blog_hero_reference_url.py",
            file=sys.stderr,
        )
        return 1
    if not validate_reference_url(ref_url):
        return 1

    prompt = build_prompt(manifest, style, hero, types_catalog, design_code)
    if not validate_prompt_budget(prompt):
        return 1
    prompt_path = article_dir / "cover" / "quad-mcp-prompt.txt"
    prompt_path.write_text(prompt + "\n", encoding="utf-8")
    print(f"OK prompt={prompt_path} chars={len(prompt)} max={MAX_MCP_PROMPT_CHARS}")

    if args.write_batch:
        api_input = {
            "prompt": prompt,
            "input_urls": [ref_url],
            "aspect_ratio": "16:9",
            "resolution": MCP_RESOLUTION,
        }
        batch = {
            "pipeline": "quad_canvas_1x_image_api",
            "reference_url_hosted": ref_url,
            "output_canvas": "cover/canvas-quad.png",
            "expected_runtime_seconds": 900,
            "preferred_image_flow": {
                "provider": "kie.ai",
                "model": KIE_IMAGE_MODEL,
                "script": "python scripts/excalibur_blog_kie_gpt_image2_api.py --article-dir <article_dir>",
                "api_key_env": "KIE_API_KEY",
                "result_path": "cover/quad-mcp-result.json",
                "apply_script": "python scripts/excalibur_blog_quad_apply.py --article-dir <article_dir> --inject-html",
                "note": "Cursor Cloud should use the direct Kie createTask -> recordInfo API flow. It returns task_id quickly and polls in shell, avoiding MCP client timeout.",
            },
            "timeout_policy": {
                "tool": "gpt-image-2",
                "timeout_error": "HTTP MCP tool execution failed: MCP error -32001: Request timed out",
                "not_final_blocker": True,
                "sync_create_max_attempts": 1,
                "backend_max_wait_seconds": 900,
                "recommended_async_poll_interval_seconds": 10,
                "recommended_async_max_wait_seconds": 900,
                "backend_note": "If Cursor receives -32001 while the Kie backend continues working, the sync MCP call is not client-timeout-safe. The robust fix is an async MCP contract: create/start returns task_id quickly, status/result returns url later.",
                "preferred_async_flow": {
                    "create": "Use an available async image create/start MCP tool if present. Call it once with jobs[0].mcp_args and record task_id.",
                    "status": "Poll an available status/result MCP tool by task_id every 10-15 seconds until url is ready, up to backend_max_wait_seconds.",
                    "idempotency": "Do not create a second image job unless status/result confirms the previous job was not created or failed.",
                },
                "blocker_only_if": "Sync gpt-image-2 times out with -32001 and no generated URL, task_id, or async status/result MCP tool is available.",
                "mcp_invocation": "Legacy fallback only. Cursor Cloud should prefer direct Kie API via scripts/excalibur_blog_kie_gpt_image2_api.py because sync MCP gpt-image-2 is client-timeout-prone for 2K i2i.",
                "log_recovery": "If the MCP/Cloud log or expanded MCP tool response already contains a generated image URL after the HTTP timeout, treat it as success: save that URL to cover/quad-mcp-result.json yourself or pass it directly to quad_apply. Do not search cover/* for the URL; it will not exist there until you save it. Do not start another image job while a generated URL exists.",
                "recovery_needed": "If there is no URL/task_id and no async status/result tool after a sync timeout, stop with COVER MCP ASYNC BLOCKER. Do not blindly retry and create a duplicate generation.",
                "instruction": "Prefer async image tools if Available Tools exposes them. If only sync gpt-image-2 exists, call it once. If the HTTP MCP client times out with -32001, inspect the expanded MCP tool response / Cursor MCP Logs for a generated URL or task_id. If a URL exists, save it as cover/quad-mcp-result.json or pass it directly to quad_apply. If task_id exists, use the status/result MCP tool. If no URL/task_id/status tool exists, stop with COVER MCP ASYNC BLOCKER because the MCP backend must expose async retrieval for late image results. Do not continue to split/apply without a real image URL.",
            },
            "jobs": [
                {
                    "slot": "canvas_quad",
                    "tool": "gpt-image-2",
                    "note": "ONE successful image only — 4 panels inside, then excalibur_blog_cover_quad_split.py. Prefer async start/status tools when available. HTTP -32001 from sync gpt-image-2 means client timeout; do not blindly retry sync create.",
                    "api_args": {
                        "model": KIE_IMAGE_MODEL,
                        "input": api_input,
                    },
                    "mcp_args": {
                        **api_input,
                    },
                }
            ],
            "validation": {
                "prompt_chars": len(prompt),
                "max_prompt_chars": MAX_MCP_PROMPT_CHARS,
                "preferred_reference_host": PREFERRED_REFERENCE_HOST,
                "allowed_reference_hosts": list(ALLOWED_REFERENCE_HOST_FRAGMENTS),
                "resolution": MCP_RESOLUTION,
            },
        }
        batch_path = article_dir / "cover" / "quad-mcp-batch.json"
        save_json(batch_path, batch)
        print(f"OK batch={batch_path} jobs=1 input_urls=1")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
