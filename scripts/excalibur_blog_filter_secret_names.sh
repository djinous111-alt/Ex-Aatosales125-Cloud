#!/usr/bin/env bash
# Print CLOUD_AGENT_INJECTED_SECRET_NAMES filtered to valid bash identifiers.
# Use before git commit when Cloud injects placeholder tokens like [REDACTED].
# Usage:
#   export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(bash scripts/excalibur_blog_filter_secret_names.sh)"
set -euo pipefail

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$raw" ]]; then
  exit 0
fi

IFS=',' read -r -a parts <<< "$raw"
filtered=()
for part in "${parts[@]}"; do
  name="$(echo "$part" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  [[ -z "$name" ]] && continue
  if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    filtered+=("$name")
  fi
done

(IFS=','; echo "${filtered[*]}")
