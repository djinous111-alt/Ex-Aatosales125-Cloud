#!/usr/bin/env python3
"""Ensure blog hero reference has a public HTTPS URL for Kie/MCP gpt-image-2 input_urls."""

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


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prefer_https(url: str) -> str:
    url = (url or "").strip()
    if url.startswith("http://"):
        return "https://" + url[len("http://") :]
    return url


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


def upload_litterbox(image_path: Path, time_token: str = "72h") -> str:
    """Temporary public HTTPS host; used when catbox/0x0 fail (412/503)."""
    boundary = "----ExcaliburHeroLitter"
    body_prefix = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="reqtype"\r\n\r\n'
        f"fileupload\r\n"
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="time"\r\n\r\n'
        f"{time_token}\r\n"
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
    url = prefer_https(url)
    if not url.startswith("https://"):
        raise RuntimeError(f"litterbox upload failed: {url[:200]}")
    return url


def head_ok(url: str, timeout: int = 20) -> bool:
    """Best-effort reachability check (Kie must be able to fetch the URL)."""
    try:
        request = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "ExcaliburBlogHero/1.0"},
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            code = getattr(response, "status", None) or response.getcode()
            return 200 <= int(code) < 400
    except Exception:  # noqa: BLE001
        try:
            request = urllib.request.Request(
                url,
                method="GET",
                headers={"User-Agent": "ExcaliburBlogHero/1.0", "Range": "bytes=0-64"},
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                code = getattr(response, "status", None) or response.getcode()
                return 200 <= int(code) < 400
        except Exception:  # noqa: BLE001
            return False


def resolve_reference_path(root: Path, hero: dict) -> Path:
    rel = hero.get("reference_image") or "memory/cover/assets/blog-hero-reference.png"
    path = Path(rel)
    if not path.is_absolute():
        path = root / path
    return path


def upload_via(provider: str, image_path: Path) -> str:
    if provider == "catbox":
        return upload_catbox(image_path)
    if provider == "0x0":
        return upload_0x0(image_path)
    if provider == "litterbox":
        return upload_litterbox(image_path)
    raise ValueError(f"unknown provider: {provider}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hero-json", default="memory/cover/blog-hero.json")
    ap.add_argument("--force", action="store_true", help="Re-upload even if URL exists")
    ap.add_argument(
        "--provider",
        choices=("catbox", "0x0", "litterbox", "auto"),
        default="auto",
        help="Hosting provider; auto = catbox → 0x0 → litterbox",
    )
    ap.add_argument(
        "--skip-fetch-check",
        action="store_true",
        help="Do not HEAD/GET-validate that the hosted URL is fetchable",
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

    existing = prefer_https((hero.get("reference_url_hosted") or "").strip())
    if existing and not args.force:
        if existing != (hero.get("reference_url_hosted") or "").strip():
            hero["reference_url_hosted"] = existing
            save_json(hero_path, hero)
        if not args.skip_fetch_check and not head_ok(existing):
            print(
                f"WARN existing reference_url_hosted may be unfetchable by Kie: {existing}",
                file=sys.stderr,
            )
        print(f"OK reference_url_hosted={existing}")
        return 0

    env_url = prefer_https(os.environ.get("BLOG_HERO_REFERENCE_URL", "").strip())
    if env_url:
        if not env_url.startswith("https://"):
            print("❌ HERO BLOCKER: BLOG_HERO_REFERENCE_URL must be HTTPS", file=sys.stderr)
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
            url = prefer_https(upload_via(provider, ref_path))
            if not args.skip_fetch_check and not head_ok(url):
                raise RuntimeError(f"{provider} returned URL but fetch check failed: {url}")
            hero["reference_url_hosted"] = url
            hero["reference_url_source"] = provider
            hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            hero["reference_url_host"] = urlparse(url).netloc
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={url}")
            return 0
        except (urllib.error.URLError, RuntimeError, TimeoutError, OSError) as exc:
            last_error = exc
            print(f"WARN upload via {provider} failed: {exc}", file=sys.stderr)

    print(f"❌ HERO BLOCKER: could not host reference: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
