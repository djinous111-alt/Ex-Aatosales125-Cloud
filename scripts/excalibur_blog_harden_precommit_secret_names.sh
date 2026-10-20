#!/usr/bin/env bash
# Harden Cloud Agent pre-commit.cursor: skip non-identifier entries in
# CLOUD_AGENT_INJECTED_SECRET_NAMES (URL-like / junk values abort ${!SECRET_NAME}).
# Idempotent. Safe to call from .cursor/cloud-agent-install.sh.
set -euo pipefail

HOOK="${1:-}"
if [[ -z "$HOOK" ]]; then
  # Prefer workspace-local agent hook if present
  if [[ -f /root/.cursor/agent-hooks/L3dvcmtzcGFjZQ/pre-commit.cursor ]]; then
    HOOK=/root/.cursor/agent-hooks/L3dvcmtzcGFjZQ/pre-commit.cursor
  else
    mapfile -t CANDIDATES < <(find /root/.cursor/agent-hooks -name 'pre-commit.cursor' 2>/dev/null | head -5 || true)
    if [[ ${#CANDIDATES[@]} -eq 0 ]]; then
      echo "[excalibur] pre-commit.cursor not found; skip harden"
      exit 0
    fi
    HOOK="${CANDIDATES[0]}"
  fi
fi

if [[ ! -f "$HOOK" ]]; then
  echo "[excalibur] missing hook: $HOOK"
  exit 0
fi

MARKER="# EXCALIBUR: skip non-identifier SECRET_NAME"
if grep -qF "$MARKER" "$HOOK"; then
  echo "[excalibur] pre-commit secret-name harden already present: $HOOK"
  exit 0
fi

# Insert identifier guard immediately inside the SECRET_NAMES loop, before ${!SECRET_NAME}.
python3 - "$HOOK" <<'PY'
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
needle = 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
guard = (
    'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
    '    # EXCALIBUR: skip non-identifier SECRET_NAME\n'
    '    # CLOUD_AGENT_INJECTED_SECRET_NAMES may include URL-like junk that is not a bash identifier.\n'
    '    if [[ ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then\n'
    '        continue\n'
    '    fi\n'
)
if needle not in text:
    print(f"[excalibur] unexpected pre-commit.cursor shape; not patched: {path}", file=sys.stderr)
    sys.exit(0)
if "EXCALIBUR: skip non-identifier SECRET_NAME" in text:
    print(f"[excalibur] already hardened: {path}")
    sys.exit(0)
path.write_text(text.replace(needle, guard, 1), encoding="utf-8")
print(f"[excalibur] hardened pre-commit secret-name filter: {path}")
PY
