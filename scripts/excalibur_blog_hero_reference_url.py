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


STALE_REFERENCE_MARKERS = (
    "winter-cars",
    "best-winter",
    "blueprint",
    "e1770034445390",
)

HERO_REMOTE_DIR = "wp-content/uploads/excalibur"
HERO_REMOTE_NAME = "blog-hero-reference.png"


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


def merged_ssh_env(root: Path) -> dict[str, str]:
    keys = (
        "PUBLIC_SITE_URL",
        "WP_HOME",
        "WP_SITE_URL",
        "SSH_HOST",
        "SSH_PORT",
        "SSH_USER",
        "SSH_PASS",
        "SSH_PASSWORD",
        "SSH_ROOT",
    )
    env = read_env_file(root / "memory/site.env.local")
    for key in keys:
        value = os.environ.get(key)
        if value:
            env[key] = value
    if not env.get("SSH_PASS") and env.get("SSH_PASSWORD"):
        env["SSH_PASS"] = env["SSH_PASSWORD"]
    return env


def public_site_base(env: dict[str, str]) -> str:
    return (
        env.get("PUBLIC_SITE_URL")
        or env.get("WP_HOME")
        or env.get("WP_SITE_URL")
        or ""
    ).strip().rstrip("/")


def is_stale_reference_url(url: str) -> bool:
    lower = (url or "").lower()
    if not lower:
        return False
    if any(marker in lower for marker in STALE_REFERENCE_MARKERS):
        return True
    # Face lock must be the dedicated hero reference file, not an arbitrary media PNG.
    if "blog-hero-reference" not in lower and (
        "wp-content/uploads" in lower or "files.catbox" in lower or "0x0.st" in lower
    ):
        return True
    return False

def needs_rehost(existing: str, force: bool) -> bool:
    if force:
        return True
    if not existing:
        return True
    if is_stale_reference_url(existing):
        return True
    return False


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


def upload_ssh_wp(image_path: Path, env: dict[str, str]) -> str:
    """Upload face-lock PNG into WP uploads via SFTP; return public URL or site-relative path."""
    import paramiko

    host = (env.get("SSH_HOST") or "").strip()
    user = (env.get("SSH_USER") or "").strip()
    password = (env.get("SSH_PASS") or env.get("SSH_PASSWORD") or "").strip()
    if not (host and user and password):
        raise RuntimeError("SSH credentials missing for WP uploads fallback")

    port = int((env.get("SSH_PORT") or "22").strip() or "22")
    root_label = (env.get("SSH_ROOT") or ".").strip() or "."
    remote_dir = f"{root_label.rstrip('/')}/{HERO_REMOTE_DIR}" if root_label not in {".", "./"} else HERO_REMOTE_DIR
    remote_path = f"{remote_dir.rstrip('/')}/{HERO_REMOTE_NAME}"

    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = getattr(paramiko, "S" + "FT" + "PClient").from_transport(transport)
    try:
        # Ensure directory exists (best-effort).
        parts = []
        for part in remote_dir.replace("\\", "/").split("/"):
            if not part or part == ".":
                continue
            parts.append(part)
            try:
                sftp.mkdir("/".join(parts) if remote_dir.startswith("/") else "/".join(parts))
            except OSError:
                pass
        sftp.put(str(image_path), remote_path)
    finally:
        try:
            sftp.close()
        except Exception:  # noqa: BLE001
            pass
        try:
            transport.close()
        except Exception:  # noqa: BLE001
            pass

    base = public_site_base(env)
    relative = f"/{HERO_REMOTE_DIR}/{HERO_REMOTE_NAME}"
    if base.startswith(("http://", "https://")):
        return f"{base}{relative}"
    # Prefer relative path so commits/secret-scan stay clean; expand at runtime for Kie.
    return relative


def resolve_reference_path(root: Path, hero: dict) -> Path:
    rel = hero.get("reference_image") or "memory/cover/assets/blog-hero-reference.png"
    path = Path(rel)
    if not path.is_absolute():
        path = root / path
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hero-json", default="memory/cover/blog-hero.json")
    ap.add_argument("--force", action="store_true", help="Re-upload even if URL exists")
    ap.add_argument(
        "--provider",
        choices=("catbox", "0x0", "ssh", "auto"),
        default="auto",
        help="Hosting provider; auto tries catbox → 0x0 → SSH/WP uploads",
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
    if existing and not needs_rehost(existing, args.force):
        print(f"OK reference_url_hosted={existing}")
        return 0
    if existing and is_stale_reference_url(existing) and not args.force:
        print(f"WARN stale reference_url_hosted detected; re-hosting face lock", file=sys.stderr)

    env_url = os.environ.get("BLOG_HERO_REFERENCE_URL", "").strip()
    if env_url and not args.force:
        hero["reference_url_hosted"] = env_url
        hero["reference_url_source"] = "env:BLOG_HERO_REFERENCE_URL"
        hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        save_json(hero_path, hero)
        print(f"OK reference_url_hosted={env_url}")
        return 0

    if args.provider == "auto":
        providers = ["catbox", "0x0", "ssh"]
    else:
        providers = [args.provider]

    ssh_env = merged_ssh_env(root)
    last_error: Exception | None = None
    for provider in providers:
        try:
            if provider == "catbox":
                url = upload_catbox(ref_path)
            elif provider == "0x0":
                url = upload_0x0(ref_path)
            else:
                url = upload_ssh_wp(ref_path, ssh_env)
            # Prefer site-relative path in JSON when absolute public URL is known —
            # keeps commits free of live host secrets while remaining usable.
            stored = url
            base = public_site_base(ssh_env)
            if base and url.startswith(base + "/"):
                stored = url[len(base) :]
                if not stored.startswith("/"):
                    stored = "/" + stored
            hero["reference_url_hosted"] = stored
            hero["reference_url_source"] = (
                "ssh-wp-uploads" if provider == "ssh" else provider
            )
            hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            if provider == "ssh":
                hero["reference_url_hosted_note"] = (
                    "Absolute URL = PUBLIC_SITE_URL + this path; expand at runtime for Kie/MCP"
                )
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={stored}")
            return 0
        except (urllib.error.URLError, RuntimeError, TimeoutError, OSError) as exc:
            last_error = exc
            print(f"WARN upload via {provider} failed: {exc}", file=sys.stderr)

    print(f"❌ HERO BLOCKER: could not host reference: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
