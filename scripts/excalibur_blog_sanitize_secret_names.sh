#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.
#
# Cloud sometimes injects raw URL values into this list. The Cursor pre-commit
# secret scanner then expands ${!SECRET_NAME} and dies with:
#   bash: ...: invalid variable name
#
# Usage (before every git commit in Cloud):
#   source scripts/excalibur_blog_sanitize_secret_names.sh
#   git commit -m "..."
#
# Do NOT use --no-verify to bypass the scanner.

set -euo pipefail

if [[ -z "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  echo "[excalibur] CLOUD_AGENT_INJECTED_SECRET_NAMES empty — nothing to sanitize"
  return 0 2>/dev/null || exit 0
fi

_filtered=""
_dropped=0
# shellcheck disable=SC2086
for _name in ${CLOUD_AGENT_INJECTED_SECRET_NAMES}; do
  if [[ "${_name}" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    _filtered+="${_name} "
  else
    _dropped=$((_dropped + 1))
  fi
done

export CLOUD_AGENT_INJECTED_SECRET_NAMES="${_filtered%% }"
echo "[excalibur] sanitized CLOUD_AGENT_INJECTED_SECRET_NAMES (dropped non-identifiers=${_dropped})"
unset _filtered _dropped _name
