#!/usr/bin/env bash
# Harden Cursor Cloud secret scanners (pre-commit.cursor + commit-msg.cursor).
# CLOUD_AGENT_INJECTED_SECRET_NAMES must stay comma-separated env *names*.
# Non-identifier entries (e.g. a URL value accidentally listed as a name) make
# bash ${!SECRET_NAME} fail with "invalid variable name" and block every commit.
set -euo pipefail

HOOKS_PATH="$(git rev-parse --git-path hooks 2>/dev/null || true)"
CORE_HOOKS="$(git config --get core.hooksPath 2>/dev/null || true)"

CANDIDATES=()
if [[ -n "${HOOKS_PATH}" ]]; then
  CANDIDATES+=("${HOOKS_PATH}/pre-commit.cursor" "${HOOKS_PATH}/commit-msg.cursor")
fi
if [[ -n "${CORE_HOOKS}" ]]; then
  CANDIDATES+=("${CORE_HOOKS}/pre-commit.cursor" "${CORE_HOOKS}/commit-msg.cursor")
fi

# Deduplicate while preserving order
declare -A SEEN=()
UNIQUE=()
for hook in "${CANDIDATES[@]}"; do
  [[ -n "${SEEN[$hook]:-}" ]] && continue
  SEEN[$hook]=1
  UNIQUE+=("$hook")
done

patched=0
for hook in "${UNIQUE[@]}"; do
  [[ -f "${hook}" ]] || continue
  if grep -q 'non-identifier secret name' "${hook}" 2>/dev/null; then
    echo "[excalibur-precommit-patch] already hardened: ${hook}"
    patched=1
    continue
  fi
  if ! grep -q 'RAW_SECRET_VALUE="\${!SECRET_NAME}"' "${hook}" 2>/dev/null; then
    echo "[excalibur-precommit-patch] unexpected hook format, skip: ${hook}"
    continue
  fi
  python3 - "${hook}" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
old = '''for SECRET_NAME in "${SECRET_NAMES[@]}"; do
    # Apply the length threshold to the raw value first so newline-terminated
    # secrets keep the same scan eligibility they had before normalization.
    RAW_SECRET_VALUE="${!SECRET_NAME}"'''
new = '''for SECRET_NAME in "${SECRET_NAMES[@]}"; do
    # Skip empty / non-identifier names. CLOUD_AGENT_INJECTED_SECRET_NAMES must
    # stay comma-separated env *names*; URL values or space-joined blobs break
    # bash indirect expansion ${!SECRET_NAME} with "invalid variable name".
    SECRET_NAME="${SECRET_NAME#"${SECRET_NAME%%[![:space:]]*}"}"
    SECRET_NAME="${SECRET_NAME%"${SECRET_NAME##*[![:space:]]}"}"
    if [ -z "$SECRET_NAME" ]; then
        continue
    fi
    if [[ ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
        echo "$(basename "$0"): skip non-identifier secret name (len=${#SECRET_NAME})" >&2
        continue
    fi
    # Apply the length threshold to the raw value first so newline-terminated
    # secrets keep the same scan eligibility they had before normalization.
    RAW_SECRET_VALUE="${!SECRET_NAME}"'''
if old not in text:
    raise SystemExit(f"anchor not found in {path}")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
print(f"[excalibur-precommit-patch] hardened: {path}")
PY
  patched=1
done

if [[ "${patched}" -eq 0 ]]; then
  echo "[excalibur-precommit-patch] no cursor secret-scan hooks found; nothing to do"
fi
