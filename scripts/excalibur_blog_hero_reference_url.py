#!/usr/bin/env python3
"""Ensure blog hero reference has a public URL for MCP gpt-image-2 input_urls."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_REFERENCE_HOST = "avtosales125.ru"


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def upload_catbox(image_path: Path) -> str:
    boundary = "----ExcaliburHeroBoundary"
    body_prefix = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="reqtype"\r\n\r\n'
        f"fileupload\r\n"
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="fileToUpload"; filename="{image_path.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8")
    body_suffix = f"\r\n--{boundary}--\r\n".encode("utf-8")
    file_bytes = image_path.read_bytes()
    body = body_prefix + file_bytes + body_suffix

    request = urllib.request.Request(
        "https://catbox.moe/user/api.php",
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "ExcaliburBlogHero/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        url = response.read().decode("utf-8", errors="replace").strip()
    if not url.startswith("https://"):
        raise RuntimeError(f"catbox upload failed: {url[:200]}")
    return url


def upload_0x0(image_path: Path) -> str:
    boundary = "----ExcaliburHero0x0"
    body_prefix = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{image_path.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8")
    body_suffix = f"\r\n--{boundary}--\r\n".encode("utf-8")
    body = body_prefix + image_path.read_bytes() + body_suffix
    request = urllib.request.Request(
        "https://0x0.st",
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "ExcaliburBlogHero/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        url = response.read().decode("utf-8", errors="replace").strip()
    if not url.startswith("https://"):
        raise RuntimeError(f"0x0 upload failed: {url[:200]}")
    return url


def resolve_reference_path(root: Path, hero: dict) -> Path:
    rel = hero.get("reference_image") or "memory/cover/assets/blog-hero-reference.png"
    path = Path(rel)
    if not path.is_absolute():
        path = root / path
    return path


def is_stable_wp_host(url: str) -> bool:
    try:
        host = urlparse(url).netloc.lower().removeprefix("www.")
    except Exception:
        return False
    return REQUIRED_REFERENCE_HOST in host


def remote_content_length(url: str) -> int | None:
    """Best-effort Content-Length via HEAD, then ranged GET."""
    headers = {"User-Agent": "ExcaliburBlogHero/1.0"}
    for method, extra in (("HEAD", {}), ("GET", {"Range": "bytes=0-0"})):
        request = urllib.request.Request(url, headers={**headers, **extra}, method=method)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.headers.get("Content-Length")
                if raw and raw.isdigit():
                    return int(raw)
                content_range = response.headers.get("Content-Range") or ""
                # bytes 0-0/1443352
                if "/" in content_range:
                    total = content_range.rsplit("/", 1)[-1].strip()
                    if total.isdigit():
                        return int(total)
        except (urllib.error.URLError, TimeoutError, ValueError):
            continue
    return None


def keep_existing_wp_url(hero: dict, ref_path: Path, existing: str) -> bool:
    """Keep avtosales125.ru media URL when it matches local PNG size (primary host fallback)."""
    if not existing or not is_stable_wp_host(existing):
        return False
    local_size = ref_path.stat().st_size
    remote_size = remote_content_length(existing)
    if remote_size is None:
        print(
            f"WARN could not verify Content-Length for existing WP URL; keeping it as primary host fallback",
            file=sys.stderr,
        )
        return True
    if remote_size != local_size:
        print(
            f"WARN existing WP URL size mismatch local={local_size} remote={remote_size}",
            file=sys.stderr,
        )
        return False
    print(f"OK existing WP reference matches local size={local_size}")
    return True


def stamp_hero(hero: dict, url: str, source: str) -> None:
    hero["reference_url_hosted"] = url
    hero["reference_url_source"] = source
    hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Host blog-hero reference PNG. Primary durable host is WordPress media on "
            f"{REQUIRED_REFERENCE_HOST}; catbox/0x0 are temporary mirrors only."
        )
    )
    ap.add_argument("--hero-json", default="memory/cover/blog-hero.json")
    ap.add_argument("--force", action="store_true", help="Re-upload even if URL exists")
    ap.add_argument(
        "--provider",
        choices=("catbox", "0x0", "auto", "keep-wp"),
        default="auto",
        help="auto tries catbox→0x0 then keeps verified WP URL; keep-wp skips temp hosts",
    )
    args = ap.parse_args()

    root = project_root()
    hero_path = Path(args.hero_json)
    if not hero_path.is_absolute():
        hero_path = root / hero_path
    if not hero_path.is_file():
        print(f"❌ HERO BLOCKER: missing {hero_path}", file=sys.stderr)
        return 1

    hero = load_json(hero_path)
    ref_path = resolve_reference_path(root, hero)
    if not ref_path.is_file():
        print(f"❌ HERO BLOCKER: reference image not found: {ref_path}", file=sys.stderr)
        return 1

    existing = (hero.get("reference_url_hosted") or "").strip()
    if existing and not args.force:
        print(f"OK reference_url_hosted={existing}")
        return 0

    env_url = os.environ.get("BLOG_HERO_REFERENCE_URL", "").strip()
    if env_url:
        stamp_hero(hero, env_url, "env:BLOG_HERO_REFERENCE_URL")
        save_json(hero_path, hero)
        print(f"OK reference_url_hosted={env_url}")
        return 0

    if args.provider == "keep-wp":
        if keep_existing_wp_url(hero, ref_path, existing):
            stamp_hero(hero, existing, "wp-media-keep")
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={existing}")
            return 0
        print("❌ HERO BLOCKER: keep-wp requested but existing WP URL missing/mismatched", file=sys.stderr)
        return 1

    providers = ["catbox", "0x0"] if args.provider == "auto" else [args.provider]
    last_error: Exception | None = None
    for provider in providers:
        try:
            url = upload_catbox(ref_path) if provider == "catbox" else upload_0x0(ref_path)
            # Temp hosts may work for MCP, but cover_quad_prompt requires avtosales125.ru.
            # Prefer keeping a verified WP media URL when one already matches local bytes.
            if existing and keep_existing_wp_url(hero, ref_path, existing):
                stamp_hero(hero, existing, f"wp-media-keep-after-{provider}")
                save_json(hero_path, hero)
                print(
                    f"WARN temp host {provider} ok but kept stable WP URL for cover gate: {existing}",
                    file=sys.stderr,
                )
                print(f"OK reference_url_hosted={existing}")
                return 0
            stamp_hero(hero, url, provider)
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={url}")
            if not is_stable_wp_host(url):
                print(
                    f"WARN temp host URL is not {REQUIRED_REFERENCE_HOST}; "
                    "cover_quad_prompt will BLOCK unless WP media URL is restored",
                    file=sys.stderr,
                )
            return 0
        except (urllib.error.URLError, RuntimeError, TimeoutError, urllib.error.HTTPError) as exc:
            last_error = exc
            print(f"WARN upload via {provider} failed: {exc}", file=sys.stderr)

    # Durable fallback: keep existing WordPress media when temp hosts fail.
    if existing and keep_existing_wp_url(hero, ref_path, existing):
        stamp_hero(hero, existing, "wp-media-fallback")
        save_json(hero_path, hero)
        print(
            "WARN catbox/0x0 failed; kept verified WordPress media URL as primary host",
            file=sys.stderr,
        )
        print(f"OK reference_url_hosted={existing}")
        return 0

    print(f"❌ HERO BLOCKER: could not host reference: {last_error}", file=sys.stderr)
    print(
        "Hint: upload blog-hero-reference.png to WordPress media on "
        f"{REQUIRED_REFERENCE_HOST}, set reference_url_hosted, or BLOG_HERO_REFERENCE_URL.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
