#!/usr/bin/env bash
# Safe git wrapper for Excalibur BLOG Cloud Agents.
# Filters CLOUD_AGENT_*_SECRET_NAMES to valid bash identifiers so pre-commit
# `${!SECRET_NAME}` does not abort on redacted/placeholder tokens.
set -euo pipefail

_filter_secret_names() {
  local raw="${1:-}"
  # Normalize separators to commas (hook expects IFS=',').
  raw="${raw//[[:space:]]/,}"
  local -a out=()
  local IFS=','
  local name
  for name in $raw; do
    [[ -z "$name" ]] && continue
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$name")
    fi
  done
  (IFS=','; echo "${out[*]}")
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES+x}" ]]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_filter_secret_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
fi
if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES+x}" ]]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES="$(_filter_secret_names "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"
fi

exec git "$@"
