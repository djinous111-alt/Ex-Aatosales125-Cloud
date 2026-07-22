#!/usr/bin/env python3
"""Warn when Cloud Secret *names* are not valid bash identifiers.

Cursor Cloud pre-commit hooks that expand secrets into the shell fail with
``invalid variable name`` when a secret name contains spaces, slashes, or
URL-shaped tokens. This check only inspects names (never values).

Also parses ``CLOUD_AGENT_INJECTED_SECRET_NAMES`` / ``CLOUD_AGENT_ALL_SECRET_NAMES``
(comma/newline lists of secret names) — platform sometimes lists a URL-shaped
token there even when it is not present as an env key.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

BASH_SAFE_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

LIST_ENV_KEYS = (
    "CLOUD_AGENT_INJECTED_SECRET_NAMES",
    "CLOUD_AGENT_ALL_SECRET_NAMES",
)

# Names commonly injected by the platform / shell; not Cloud Secrets.
IGNORE_PREFIXES = (
    "CURSOR_",
    "npm_",
    "NVM_",
    "VSCODE_",
    "TERM_",
    "XDG_",
    "SSH_CLIENT",
    "SSH_CONNECTION",
    "SSH_TTY",
)


def is_ignored(name: str) -> bool:
    if name in {"_", "OLDPWD", "PWD", "HOME", "USER", "PATH", "SHELL", "SHLVL", "HOSTNAME"}:
        return True
    if name in LIST_ENV_KEYS:
        return True
    return any(name.startswith(prefix) for prefix in IGNORE_PREFIXES)


def parse_name_list(raw: str) -> list[str]:
    parts = re.split(r"[\n,;]+", raw or "")
    return [p.strip() for p in parts if p.strip()]


def find_unsafe_names(env: dict[str, str] | None = None) -> list[str]:
    source = env if env is not None else os.environ
    candidates: set[str] = set()
    for name in source:
        if is_ignored(name):
            continue
        candidates.add(name)
    for key in LIST_ENV_KEYS:
        for token in parse_name_list(source.get(key, "")):
            candidates.add(token)
    unsafe = sorted(n for n in candidates if not BASH_SAFE_NAME.match(n))
    return unsafe


def sanitize_injected_list(env: dict[str, str] | None = None) -> str:
    """Return bash-safe subset of CLOUD_AGENT_INJECTED_SECRET_NAMES for commit hygiene."""
    source = env if env is not None else os.environ
    raw = source.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
    safe = [n for n in parse_name_list(raw) if BASH_SAFE_NAME.match(n)]
    return ",".join(safe)


def main() -> int:
    ap = argparse.ArgumentParser(description="Check env var names are bash-safe identifiers")
    ap.add_argument("--json", action="store_true", help="Print JSON report")
    ap.add_argument(
        "--print-sanitized-injected",
        action="store_true",
        help="Print sanitized CLOUD_AGENT_INJECTED_SECRET_NAMES (bash-safe only)",
    )
    args = ap.parse_args()

    if args.print_sanitized_injected:
        print(sanitize_injected_list())
        return 0

    unsafe = find_unsafe_names()
    report: dict[str, Any] = {
        "gate": "secret-names",
        "status": "PASS" if not unsafe else "WARN",
        "unsafe_name_count": len(unsafe),
        "unsafe_names": unsafe,
        "guidance": (
            "Rename/remove Cursor Dashboard Cloud Secrets whose names are not "
            "[A-Za-z_][A-Za-z0-9_]*. URL-shaped tokens in CLOUD_AGENT_*_SECRET_NAMES "
            "break pre-commit (invalid variable name). Before commit: "
            "export CLOUD_AGENT_INJECTED_SECRET_NAMES=\"$(python3 scripts/excalibur_blog_check_secret_names.py --print-sanitized-injected)\". "
            "Durable fix: Dashboard → Secrets → delete/rename the bad name."
        ),
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Secret name check: {report['status']}")
        for name in unsafe:
            # Never print full URL-shaped tokens if they look like secrets/values;
            # show length + prefix only for non-identifiers that contain ://
            if "://" in name or "/" in name:
                print(
                    f"WARN unsafe secret/env name: <url-shaped len={len(name)} starts={name[:8]!r}…>",
                    file=sys.stderr,
                )
            else:
                print(f"WARN unsafe secret/env name: {name}", file=sys.stderr)
        if unsafe:
            print(report["guidance"], file=sys.stderr)
    # Advisory only: do not block shell install/doctor.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
