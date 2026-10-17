#!/usr/bin/env bash
# Safe git wrapper for Cloud Agent pre-commit secret scan.
# Filters CLOUD_AGENT_INJECTED_SECRET_NAMES to bash-safe identifiers only
# so `${!SECRET_NAME}` in platform hooks does not abort with "invalid variable name".
# Usage: bash scripts/excalibur_git.sh commit -m "..."
#        bash scripts/excalibur_git.sh status
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

filter_secret_names() {
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
  if [[ -z "$raw" ]]; then
    return 0
  fi
  # Split on whitespace / commas / newlines; keep only valid bash identifiers.
  local -a keep=()
  local token
  # shellcheck disable=SC2206
  local -a parts=($raw)
  for token in "${parts[@]}"; do
    token="${token//,/}"
    if [[ "$token" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      keep+=("$token")
    else
      echo "excalibur_git: skip non-identifier secret name (len=${#token})" >&2
    fi
  done
  if ((${#keep[@]} == 0)); then
    unset CLOUD_AGENT_INJECTED_SECRET_NAMES
  else
    # Export as space-separated list; hooks that iterate word-split get valid names.
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${keep[*]}"
  fi
}

filter_secret_names
exec git "$@"
