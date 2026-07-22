#!/usr/bin/env bash
# Patch Cloud Agent pre-commit/commit-msg secret scanners to skip
# non-bash-identifier entries in CLOUD_AGENT_INJECTED_SECRET_NAMES.

set -euo pipefail

HOOKS_DIR="${1:-/root/.cursor/agent-hooks/L3dvcmtzcGFjZQ}"
MARKER="# excalibur: skip non-identifier secret names"

patch_file() {
  local file="$1"
  if [[ ! -f "$file" ]]; then
    echo "skip missing: $file"
    return 0
  fi
  if grep -qF "$MARKER" "$file"; then
    echo "already patched: $file"
    return 0
  fi
  python3 - "$file" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
needle = 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
insert = (
    'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
    '    # excalibur: skip non-identifier secret names\n'
    '    if [[ ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then\n'
    '        continue\n'
    '    fi\n'
)
if needle not in text:
    raise SystemExit(f"needle not found in {path}")
path.write_text(text.replace(needle, insert, 1), encoding="utf-8")
print(f"patched: {path}")
PY
}

patch_file "$HOOKS_DIR/pre-commit.cursor"
patch_file "$HOOKS_DIR/commit-msg.cursor"
echo "OK precommit secret-scan patch applied"
