#!/usr/bin/env python3
"""Ensure blog hero reference has a public URL for MCP gpt-image-2 input_urls.

Prefer a durable WordPress media URL (REQUIRED_REFERENCE_HOST). When catbox/0x0
fail under --force, keep the existing WP-hosted URL instead of blocking cover.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Must match scripts/excalibur_blog_cover_quad_prompt.py
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


def upload_litterbox(image_path: Path, *, hours: int = 72) -> str:
    """Temporary https host (litterbox.catbox.moe) — fallback after catbox/0x0."""
    boundary = "----ExcaliburHeroLitter"
    body_prefix = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="reqtype"\r\n\r\n'
        f"fileupload\r\n"
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="time"\r\n\r\n'
        f"{hours}h\r\n"
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="fileToUpload"; filename="{image_path.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8")
    body_suffix = f"\r\n--{boundary}--\r\n".encode("utf-8")
    body = body_prefix + image_path.read_bytes() + body_suffix
    request = urllib.request.Request(
        "https://litterbox.catbox.moe/resources/internals/api.php",
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
        raise RuntimeError(f"litterbox upload failed: {url[:200]}")
    return url


PROVIDERS = {
    "catbox": upload_catbox,
    "0x0": upload_0x0,
    "litterbox": upload_litterbox,
}


def resolve_reference_path(root: Path, hero: dict) -> Path:
    rel = hero.get("reference_image") or "memory/cover/assets/blog-hero-reference.png"
    path = Path(rel)
    if not path.is_absolute():
        path = root / path
    return path


def try_https_upgrade(url: str) -> str | None:
    """If URL is http:// for a known media host, try https:// HEAD and return it."""
    if not url.startswith("http://"):
        return None
    https_url = "https://" + url[len("http://") :]
    try:
        request = urllib.request.Request(
            https_url, method="HEAD", headers={"User-Agent": "ExcaliburBlogHero/1.0"}
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            if 200 <= getattr(response, "status", 200) < 400:
                return https_url
    except Exception:  # noqa: BLE001
        return None
    return None


def url_is_https(url: str) -> bool:
    return url.startswith("https://")


def is_stable_wp_reference(url: str) -> bool:
    return bool(url) and REQUIRED_REFERENCE_HOST in url


def keep_existing_reference(hero: dict, hero_path: Path, existing: str, reason: str) -> int:
    print(
        f"WARN keep existing reference_url_hosted ({reason}): {existing[:120]}",
        file=sys.stderr,
    )
    hero["reference_url_source"] = hero.get("reference_url_source") or "wordpress-media"
    hero["reference_url_keep_reason"] = reason
    hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    save_json(hero_path, hero)
    print(f"OK reference_url_hosted={existing}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hero-json", default="memory/cover/blog-hero.json")
    ap.add_argument("--force", action="store_true", help="Re-upload even if URL exists")
    ap.add_argument(
        "--provider",
        choices=("catbox", "0x0", "litterbox", "auto"),
        default="auto",
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
        # Stable WP media URL is preferred even over http→https upgrade for cover i2i.
        if is_stable_wp_reference(existing):
            print(f"OK reference_url_hosted={existing}")
            return 0
        if url_is_https(existing):
            print(f"OK reference_url_hosted={existing}")
            return 0
        upgraded = try_https_upgrade(existing)
        if upgraded:
            hero["reference_url_hosted"] = upgraded
            hero["reference_url_source"] = (hero.get("reference_url_source") or "upgrade") + "-https"
            hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={upgraded} (upgraded http→https)")
            return 0
        print(
            f"WARN reference_url_hosted is not https ({existing[:80]}…); re-hosting",
            file=sys.stderr,
        )

    env_url = os.environ.get("BLOG_HERO_REFERENCE_URL", "").strip()
    if env_url:
        if not url_is_https(env_url) and not is_stable_wp_reference(env_url):
            upgraded = try_https_upgrade(env_url)
            if upgraded:
                env_url = upgraded
            else:
                print("❌ HERO BLOCKER: BLOG_HERO_REFERENCE_URL must be https or WP media", file=sys.stderr)
                return 1
        hero["reference_url_hosted"] = env_url
        hero["reference_url_source"] = "env:BLOG_HERO_REFERENCE_URL"
        hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        save_json(hero_path, hero)
        print(f"OK reference_url_hosted={env_url}")
        return 0

    providers = ["catbox", "0x0", "litterbox"] if args.provider == "auto" else [args.provider]
    last_error: Exception | None = None
    for provider in providers:
        try:
            url = PROVIDERS[provider](ref_path)
            # Cover quad prompt requires WP host; catbox/0x0/litterbox are i2i-only fallbacks.
            # Prefer not overwriting a stable WP URL with a temp host.
            if existing and is_stable_wp_reference(existing) and not is_stable_wp_reference(url):
                print(
                    f"WARN {provider} uploaded temp URL but stable WP reference exists; keeping WP URL",
                    file=sys.stderr,
                )
                return keep_existing_reference(
                    hero, hero_path, existing, f"prefer-wp-over-{provider}"
                )
            hero["reference_url_hosted"] = url
            hero["reference_url_source"] = provider
            hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            if provider == "litterbox":
                hero["reference_url_last_i2i_fallback"] = url
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={url}")
            return 0
        except (urllib.error.URLError, RuntimeError, TimeoutError) as exc:
            last_error = exc
            print(f"WARN upload via {provider} failed: {exc}", file=sys.stderr)

    # Durable fallback: keep pinned WordPress media URL (AS08/AS09/B01 path).
    if existing and is_stable_wp_reference(existing):
        return keep_existing_reference(
            hero, hero_path, existing, f"upload-failed:{last_error}"
        )

    print(f"❌ HERO BLOCKER: could not host reference: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
