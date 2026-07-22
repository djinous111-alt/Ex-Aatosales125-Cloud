#!/usr/bin/env python3
"""Warn when Cloud Secret *names* are not valid bash identifiers.

Cursor Cloud pre-commit hooks that expand secrets into the shell fail with
``invalid variable name`` when a secret name contains spaces, slashes, or
URL-shaped tokens. This check only inspects names (never values).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

BASH_SAFE_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

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
    return any(name.startswith(prefix) for prefix in IGNORE_PREFIXES)


def find_unsafe_names(env: dict[str, str] | None = None) -> list[str]:
    source = env if env is not None else os.environ
    unsafe: list[str] = []
    for name in sorted(source):
        if is_ignored(name):
            continue
        if not BASH_SAFE_NAME.match(name):
            unsafe.append(name)
    return unsafe


def main() -> int:
    ap = argparse.ArgumentParser(description="Check env var names are bash-safe identifiers")
    ap.add_argument("--json", action="store_true", help="Print JSON report")
    args = ap.parse_args()

    unsafe = find_unsafe_names()
    report: dict[str, Any] = {
        "gate": "secret-names",
        "status": "PASS" if not unsafe else "WARN",
        "unsafe_name_count": len(unsafe),
        "unsafe_names": unsafe,
        "guidance": (
            "Rename Cursor Dashboard Cloud Secrets to [A-Za-z_][A-Za-z0-9_]* only. "
            "If pre-commit fails with 'invalid variable name', verify staged files then "
            "commit with --no-verify until secrets are renamed."
        ),
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Secret name check: {report['status']}")
        for name in unsafe:
            print(f"WARN unsafe secret/env name: {name}", file=sys.stderr)
        if unsafe:
            print(report["guidance"], file=sys.stderr)
    # Advisory only: do not block shell install/doctor.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
