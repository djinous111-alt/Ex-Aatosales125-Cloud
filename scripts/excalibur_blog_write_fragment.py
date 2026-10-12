#!/usr/bin/env python3
"""Write runtime handoff fragments under .cursor/excalibur-blog-fragments/.

Cursor Write tool may no-op on gitignored paths; this helper always writes via
filesystem and asserts the file exists afterwards.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


ALLOWED = frozenset({"cover.md", "schema.md"})


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser(description="Write Excalibur BLOG runtime fragment and verify it exists")
    ap.add_argument(
        "--name",
        required=True,
        choices=sorted(ALLOWED),
        help="Fragment filename: cover.md or schema.md",
    )
    ap.add_argument(
        "--file",
        type=Path,
        default=None,
        help="Read fragment body from this file (UTF-8). Default: stdin.",
    )
    ap.add_argument(
        "--text",
        type=str,
        default="",
        help="Fragment body as a string (alternative to --file / stdin).",
    )
    args = ap.parse_args()

    if args.text:
        body = args.text
    elif args.file is not None:
        body = args.file.read_text(encoding="utf-8")
    else:
        body = sys.stdin.read()

    if not body.strip():
        print("ERROR: empty fragment body", file=sys.stderr)
        return 2

    if not body.endswith("\n"):
        body += "\n"

    root = project_root()
    out_dir = root / ".cursor" / "excalibur-blog-fragments"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / args.name
    out_path.write_text(body, encoding="utf-8")

    if not out_path.is_file():
        print(f"ERROR: fragment missing after write: {out_path}", file=sys.stderr)
        return 1

    size = out_path.stat().st_size
    print(f"OK wrote {out_path.relative_to(root)} bytes={size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
