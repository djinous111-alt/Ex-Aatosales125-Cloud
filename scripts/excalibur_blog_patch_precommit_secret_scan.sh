#!/usr/bin/env bash
# Patch Cursor Cloud pre-commit.cursor so invalid secret *names* do not break bash.
#
# Root cause (AS20): CLOUD_AGENT_INJECTED_SECRET_NAMES may include a URL-like token
# (contains : / . -). The stock hook does RAW="${!SECRET_NAME}" and bash dies with
# "invalid variable name" (agent-visible as "[REDACTED]: invalid variable name").
#
# Idempotent. Safe to run from cloud-agent-install.sh on every Cloud boot.
set -euo pipefail

python3 - <<'PY'
from __future__ import annotations

import os
import subprocess
from pathlib import Path

MARKER = "# excalibur: skip non-identifier secret names"
NEEDLE = 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
GUARD = (
    NEEDLE
    + f"    {MARKER}\n"
    + "    # Trim whitespace\n"
    + '    SECRET_NAME="${SECRET_NAME#"${SECRET_NAME%%[![:space:]]*}"}"\n'
    + '    SECRET_NAME="${SECRET_NAME%"${SECRET_NAME##*[![:space:]]}"}"\n'
    + "    # Skip empty names and non-identifiers (e.g. URL-shaped Cloud injects).\n"
    + '    if [[ -z "$SECRET_NAME" || ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then\n'
    + "        continue\n"
    + "    fi\n"
)


def is_hooks_dir(path: Path) -> bool:
    return path.is_dir() and any(path.glob("*.cursor"))


def candidate_dirs() -> list[Path]:
    found: list[Path] = []
    try:
        cfg = subprocess.check_output(
            ["git", "config", "--get", "core.hooksPath"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        cfg = ""
    if cfg:
        found.append(Path(cfg))

    home = Path(os.environ.get("HOME") or "/root")
    for base in (Path("/root/.cursor/agent-hooks"), home / ".cursor" / "agent-hooks"):
        if not base.is_dir():
            continue
        for child in base.iterdir():
            found.append(child)

    uniq: list[Path] = []
    seen: set[str] = set()
    for path in found:
        key = str(path.resolve()) if path.exists() else str(path)
        if key in seen:
            continue
        seen.add(key)
        if is_hooks_dir(path):
            uniq.append(path)
    return uniq


def patch_file(hook: Path) -> None:
    text = hook.read_text(encoding="utf-8")
    if MARKER in text:
        print(f"[excalibur-precommit] already patched: {hook}")
        return
    if NEEDLE not in text:
        return
    if 'RAW_SECRET_VALUE="${!SECRET_NAME}"' not in text:
        print(f"[excalibur-precommit] WARN: indirect expansion missing in {hook}", flush=True)
        return
    hook.write_text(text.replace(NEEDLE, GUARD, 1), encoding="utf-8")
    print(f"[excalibur-precommit] patched: {hook}")


dirs = candidate_dirs()
if not dirs:
    print("[excalibur-precommit] no *.cursor secret-scan hooks found (ok outside Cloud)")
else:
    patched_any = False
    for hooks_dir in dirs:
        for hook in sorted(hooks_dir.glob("*.cursor")):
            before = hook.read_text(encoding="utf-8")
            if NEEDLE in before and 'RAW_SECRET_VALUE="${!SECRET_NAME}"' in before:
                patch_file(hook)
                patched_any = True
    if not patched_any:
        print("[excalibur-precommit] no matching secret-scan loops found")
PY
