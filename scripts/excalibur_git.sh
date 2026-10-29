#!/usr/bin/env bash
# Wrapper around git that filters non-identifier entries from
# CLOUD_AGENT_INJECTED_SECRET_NAMES before running hooks.
# Cursor sometimes injects URL-like "secret names" that break
# bash ${!SECRET_NAME} in pre-commit.cursor.
set -euo pipefail

filter_secret_names() {
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
  [[ -z "$raw" ]] && return 0
  local -a keep=()
  local IFS=','
  local part
  for part in $raw; do
    if [[ "$part" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      keep+=("$part")
    fi
  done
  if ((${#keep[@]})); then
    local IFS=','
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${keep[*]}"
  else
    unset CLOUD_AGENT_INJECTED_SECRET_NAMES || true
  fi
}

filter_secret_names

if [[ "${1:-}" == "commit" ]]; then
  shift
  exec git commit "$@"
fi

exec git "$@"
