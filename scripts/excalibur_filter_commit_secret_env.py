#!/usr/bin/env python3
"""Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to bash-safe identifiers.

Cloud Agent pre-commit hooks expand `${!SECRET_NAME}`. If the injected list
contains a URL or other non-identifier token, bash aborts with
"invalid variable name" before the scan runs.

Prints a space-joined filtered list (or empty) for shell export:
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(python3 scripts/excalibur_filter_commit_secret_env.py)"
Prefer: bash scripts/excalibur_git.sh commit ...
"""
from __future__ import annotations

import os
import re
import sys

IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def filter_names(raw: str) -> list[str]:
    keep: list[str] = []
    for token in re.split(r"[\s,]+", raw.strip()):
        if not token:
            continue
        if IDENT.match(token):
            keep.append(token)
        else:
            print(f"skip non-identifier secret name (len={len(token)})", file=sys.stderr)
    return keep


def main() -> int:
    raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "") or ""
    keep = filter_names(raw)
    sys.stdout.write(" ".join(keep))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
