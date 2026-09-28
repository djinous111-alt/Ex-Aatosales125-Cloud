#!/usr/bin/env bash
# Keep only valid bash identifiers from CLOUD_AGENT_INJECTED_SECRET_NAMES.
# Cloud sometimes injects raw URLs into that env var → `${!SECRET_NAME}` fails
# with "invalid variable name" and aborts pre-commit secret scan.
#
# Pre-commit hook splits on commas (IFS=','), so output MUST be comma-separated.
#
# Usage (before git commit):
#   export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(bash scripts/excalibur_blog_filter_secret_names.sh)"
set -euo pipefail

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "${raw//[[:space:]]/}" ]]; then
  exit 0
fi

# Normalize separators to commas, then filter tokens.
normalized="${raw//[[:space:]]/,}"
filtered=()
IFS=',' read -ra tokens <<< "$normalized"
for token in "${tokens[@]}"; do
  token="${token#"${token%%[![:space:]]*}"}"
  token="${token%"${token##*[![:space:]]}"}"
  [[ -z "$token" ]] && continue
  if [[ "$token" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    filtered+=("$token")
  fi
done

(IFS=','; printf '%s' "${filtered[*]}")
