#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.
# Host pre-commit uses ${!SECRET_NAME}; redacted/invalid names break the hook
# with "invalid variable name" before any file scan.
#
# Usage (before git commit in Cloud Agent):
#   source scripts/sanitize_cloud_secret_names.sh
# or:
#   eval "$(bash scripts/sanitize_cloud_secret_names.sh --export)"

set -euo pipefail

sanitize_cloud_secret_names() {
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
  local -a out=()
  local name
  # shellcheck disable=SC2086
  for name in ${raw}; do
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$name")
    fi
  done
  if ((${#out[@]})); then
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${out[*]}"
  else
    export CLOUD_AGENT_INJECTED_SECRET_NAMES=""
  fi
}

if [[ "${1:-}" == "--export" ]]; then
  sanitize_cloud_secret_names
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "${CLOUD_AGENT_INJECTED_SECRET_NAMES}"
else
  sanitize_cloud_secret_names
fi
