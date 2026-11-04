#!/usr/bin/env python3
"""CLI wrapper: upload a local image via Kie file-base64-upload → tempfile HTTPS URL.

Used when WordPress media / catbox are unreachable from Cloud egress and Cover needs
a reachable reference_url_hosted for gpt-image-2 i2i (quad prompt accepts
tempfile.redpandaai.co / redpandaai.co hosts).

Requires KIE_API_KEY. Does not invent hosts or print the API key.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Reuse the implementation already wired into hero_reference_url.
from excalibur_blog_hero_reference_url import upload_kie_base64  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Upload image via Kie file-base64-upload")
    ap.add_argument("image", type=Path, help="Local PNG/JPEG path")
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Optional JSON report path (downloadUrl only; no secrets)",
    )
    args = ap.parse_args()

    if not args.image.is_file():
        print(f"Not found: {args.image}", file=sys.stderr)
        return 2
    try:
        url = upload_kie_base64(args.image)
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL kie upload: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    report = {
        "ok": True,
        "provider": "kie-file-base64-upload",
        "downloadUrl": url,
        "source": str(args.image).replace("\\", "/"),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
