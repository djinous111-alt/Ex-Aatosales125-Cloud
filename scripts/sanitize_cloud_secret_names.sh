#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to valid bash identifiers.
# Cursor pre-commit iterates names with ${!SECRET_NAME}; a literal
# "[REDACTED]" (or URL) in the comma-separated list crashes the hook.
set -euo pipefail

_sanitize_secret_names() {
  local raw="$1"
  local out=()
  local part
  IFS=',' read -ra _parts <<< "$raw"
  for part in "${_parts[@]}"; do
    part="${part#"${part%%[![:space:]]*}"}"
    part="${part%"${part##*[![:space:]]}"}"
    if [[ "$part" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$part")
    fi
  done
  local IFS=','
  printf '%s' "${out[*]}"
}

if [ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_sanitize_secret_names "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
fi
if [ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES="$(_sanitize_secret_names "$CLOUD_AGENT_ALL_SECRET_NAMES")"
fi
