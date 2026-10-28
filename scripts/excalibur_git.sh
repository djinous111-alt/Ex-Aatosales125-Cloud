#!/usr/bin/env bash
# Safe git wrapper for Cloud Agent: filter non-identifier names from
# CLOUD_AGENT_INJECTED_SECRET_NAMES so pre-commit.cursor does not die on
# `${!SECRET_NAME}` (e.g. a URL mistakenly listed as a secret name).
set -euo pipefail

filter_secret_names() {
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES-}"
  local -a keep=()
  local part
  if [[ -z "$raw" ]]; then
    return 0
  fi
  IFS=',' read -ra parts <<< "$raw"
  for part in "${parts[@]}"; do
    if [[ "$part" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      keep+=("$part")
    fi
  done
  if ((${#keep[@]})); then
    local IFS=,
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${keep[*]}"
  else
    unset CLOUD_AGENT_INJECTED_SECRET_NAMES || true
  fi
}

filter_secret_names

cmd="${1:-}"
shift || true

case "$cmd" in
  commit)
    exec git commit "$@"
    ;;
  *)
    exec git "$cmd" "$@"
    ;;
esac
