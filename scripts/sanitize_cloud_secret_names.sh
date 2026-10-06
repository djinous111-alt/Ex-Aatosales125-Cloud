#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.
# Cursor Cloud sometimes injects secret *values* (e.g. site URLs) into the
# names list; expanding ${!SECRET_NAME} then crashes pre-commit hooks.
#
# Usage:
#   source scripts/sanitize_cloud_secret_names.sh
#   # or
#   eval "$(scripts/sanitize_cloud_secret_names.sh --export)"
set -euo pipefail

sanitize_cloud_secret_names() {
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES-}"
  local -a kept=()
  local name
  for name in $raw; do
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      kept+=("$name")
    fi
  done
  if ((${#kept[@]})); then
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${kept[*]}"
  else
    unset CLOUD_AGENT_INJECTED_SECRET_NAMES 2>/dev/null || true
    export CLOUD_AGENT_INJECTED_SECRET_NAMES=""
  fi
}

if [[ "${1:-}" == "--export" ]]; then
  sanitize_cloud_secret_names
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
elif [[ "${BASH_SOURCE[0]:-}" == "${0}" ]]; then
  sanitize_cloud_secret_names
  echo "CLOUD_AGENT_INJECTED_SECRET_NAMES=${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
fi
