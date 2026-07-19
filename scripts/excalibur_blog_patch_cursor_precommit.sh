#!/usr/bin/env bash
# Harden Cloud Agent secrets scanner hooks (pre-commit.cursor + commit-msg.cursor).
#
# Problem: CLOUD_AGENT_INJECTED_SECRET_NAMES may include values that are not
# valid bash identifiers (hyphens, spaces, scrubbed placeholders like
# "[REDACTED]"). Stock hooks do RAW_SECRET_VALUE="${!SECRET_NAME}" and abort
# with "invalid variable name" on BOTH pre-commit and commit-msg.
#
# Fix: skip non-identifier SECRET_NAME entries instead of aborting.
# Idempotent: safe to run multiple times.
set -euo pipefail

MARKER="EXCALIBUR_SKIP_NON_IDENTIFIER_SECRET_NAME"

resolve_hooks_dir() {
  local hooks_path=""
  hooks_path="$(git config --get core.hooksPath 2>/dev/null || true)"
  if [[ -n "$hooks_path" && -d "$hooks_path" ]]; then
    printf '%s\n' "$hooks_path"
    return 0
  fi
  local candidate
  shopt -s nullglob
  for candidate in "${HOME}/.cursor/agent-hooks/"*; do
    if [[ -d "$candidate" && -f "$candidate/pre-commit.cursor" ]]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done
  local git_hooks
  git_hooks="$(git rev-parse --git-path hooks 2>/dev/null || true)"
  if [[ -n "$git_hooks" && -d "$git_hooks" ]]; then
    printf '%s\n' "$git_hooks"
    return 0
  fi
  return 1
}

patch_hook_file() {
  local hook="$1"
  if [[ ! -f "$hook" ]]; then
    echo "[excalibur-precommit-patch] missing: $hook (skip)"
    return 0
  fi
  if grep -q "$MARKER" "$hook"; then
    echo "[excalibur-precommit-patch] already applied: $hook"
    return 0
  fi
  python3 - "$hook" "$MARKER" <<'PY'
from pathlib import Path
import sys

hook_path = Path(sys.argv[1])
marker = sys.argv[2]
text = hook_path.read_text(encoding="utf-8")
needle = 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
if needle not in text:
    print(f"[excalibur-precommit-patch] unexpected hook shape: {hook_path}", file=sys.stderr)
    sys.exit(1)

guard = (
    'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
    f"    # {marker}: skip env keys that cannot be used with bash indirect expansion\n"
    '    SECRET_NAME="${SECRET_NAME#"${SECRET_NAME%%[![:space:]]*}"}"\n'
    '    SECRET_NAME="${SECRET_NAME%"${SECRET_NAME##*[![:space:]]}"}"\n'
    '    if [[ -z "$SECRET_NAME" || ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then\n'
    '        echo "[excalibur-precommit-patch] skip non-identifier SECRET_NAME" >&2\n'
    '        continue\n'
    '    fi\n'
)
hook_path.write_text(text.replace(needle, guard, 1), encoding="utf-8")
print(f"[excalibur-precommit-patch] patched: {hook_path}")
PY
}

HOOKS_DIR="$(resolve_hooks_dir || true)"
if [[ -z "${HOOKS_DIR}" ]]; then
  echo "[excalibur-precommit-patch] hooks dir not found; skip"
  exit 0
fi

patch_hook_file "$HOOKS_DIR/pre-commit.cursor"
patch_hook_file "$HOOKS_DIR/commit-msg.cursor"
