#!/usr/bin/env bash
# Keep only valid shell identifiers in CLOUD_AGENT_INJECTED_SECRET_NAMES.
# Prevents `invalid variable name` when a URL/value was mistakenly injected
# into the secret-name list (schema/indexer commit hooks).
set -euo pipefail

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$raw" ]]; then
  return 0 2>/dev/null || exit 0
fi

filtered=()
for name in $raw; do
  if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    filtered+=("$name")
  fi
done

export CLOUD_AGENT_INJECTED_SECRET_NAMES="${filtered[*]-}"
