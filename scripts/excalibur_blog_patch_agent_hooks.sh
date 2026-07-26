#!/usr/bin/env bash
# Patch Cursor Cloud agent git hooks so secret-name loops skip non-identifiers.
# CLOUD_AGENT_INJECTED_SECRET_NAMES sometimes contains a URL-as-name; bash then
# fails with: invalid variable name (on ${!SECRET_NAME}).
set -euo pipefail

HOOKS_DIR="${1:-/root/.cursor/agent-hooks/L3dvcmtzcGFjZQ}"
MARKER='Skip non-identifiers (e.g. a URL mistakenly listed as a secret name)'

patch_file() {
  local file="$1"
  [[ -f "$file" ]] || return 0
  if grep -Fq "$MARKER" "$file"; then
    echo "already patched: $file"
    return 0
  fi
  python3 - "$file" <<'PY'
from pathlib import Path
import sys
path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
needle = 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n    # Apply the length threshold'
insert = '''for SECRET_NAME in "${SECRET_NAMES[@]}"; do
    # Skip non-identifiers (e.g. a URL mistakenly listed as a secret name).
    # Indirect expansion ${!name} fails with "invalid variable name" otherwise.
    if [[ ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
        continue
    fi
    # Apply the length threshold'''
if needle not in text:
    raise SystemExit(f"pattern not found in {path}")
path.write_text(text.replace(needle, insert, 1), encoding="utf-8")
print(f"patched: {path}")
PY
}

patch_file "$HOOKS_DIR/pre-commit.cursor"
patch_file "$HOOKS_DIR/commit-msg.cursor"
echo "OK agent hooks patched"
