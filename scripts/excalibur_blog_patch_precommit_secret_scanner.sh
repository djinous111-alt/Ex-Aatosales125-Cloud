#!/usr/bin/env bash
# Patch Cursor Cloud secrets scanners (pre-commit.cursor / commit-msg.cursor) so
# CLOUD_AGENT_INJECTED_SECRET_NAMES values that are not valid bash identifiers
# (e.g. raw URLs) are skipped before ${!SECRET_NAME} expansion.
# Idempotent. Safe if hooks are absent.
set -euo pipefail

MARKER="# excalibur: skip non-identifier secret names"

is_patched() {
  local path="$1"
  grep -Fq "$MARKER" "$path" 2>/dev/null
}

patch_hook() {
  local path="$1"
  if [[ ! -f "$path" ]]; then
    return 1
  fi
  if is_patched "$path"; then
    echo "[excalibur-precommit] already patched: $path"
    return 0
  fi

  if ! grep -Fq 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do' "$path"; then
    echo "[excalibur-precommit] WARN: expected SECRET_NAMES loop not found in $path" >&2
    return 1
  fi

  python3 - "$path" <<'PY'
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
marker = "# excalibur: skip non-identifier secret names"
if marker in text:
    print(f"already patched {path}")
    raise SystemExit(0)
needle = 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
guard = (
    'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
    f"    {marker}\n"
    "    # CLOUD_AGENT_INJECTED_SECRET_NAMES may contain raw URLs / junk;\n"
    '    # ${!SECRET_NAME} aborts the whole hook with "invalid variable name".\n'
    '    if [[ ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then\n'
    '        echo "[excalibur-precommit] skip non-identifier secret name" >&2\n'
    "        continue\n"
    "    fi\n"
)
if needle not in text:
    print("loop needle missing", file=sys.stderr)
    raise SystemExit(1)
path.write_text(text.replace(needle, guard, 1), encoding="utf-8")
print(f"patched {path}")
PY
}

patched_any=0

# Known Cloud hook locations + any *.cursor scanners under agent-hooks.
HOOK_GLOBS=(
  "${CURSOR_PRECOMMIT_HOOK:-}"
  "${HOME}/.cursor/agent-hooks/L3dvcmtzcGFjZQ/pre-commit.cursor"
  "${HOME}/.cursor/agent-hooks/L3dvcmtzcGFjZQ/commit-msg.cursor"
  "${HOME}/.cursor/agent-hooks/pre-commit.cursor"
  "${HOME}/.cursor/agent-hooks/commit-msg.cursor"
)

for candidate in "${HOOK_GLOBS[@]}"; do
  [[ -z "$candidate" ]] && continue
  if [[ -f "$candidate" ]]; then
    if patch_hook "$candidate"; then
      patched_any=1
    fi
  fi
done

if [[ -d "${HOME}/.cursor/agent-hooks" ]]; then
  while IFS= read -r -d '' hook; do
    case "$(basename "$hook")" in
      pre-commit.cursor|commit-msg.cursor)
        if patch_hook "$hook"; then
          patched_any=1
        fi
        ;;
    esac
  done < <(find "${HOME}/.cursor/agent-hooks" \( -name 'pre-commit.cursor' -o -name 'commit-msg.cursor' \) -print0 2>/dev/null || true)
fi

if [[ "$patched_any" -eq 0 ]]; then
  echo "[excalibur-precommit] no Cloud secret scanner hooks found (ok on non-Cloud hosts)"
fi
