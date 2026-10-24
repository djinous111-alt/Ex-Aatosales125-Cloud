#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to shell-safe ENV identifiers.
# Cursor Cloud may inject raw URL tokens / redacted junk that break `${!name}`.
# Pre-commit hook splits on commas: IFS=',' read -ra SECRET_NAMES <<< "$..."
#
# Usage:
#   source scripts/excalibur_blog_filter_secret_names.sh
#   # or:
#   eval "$(scripts/excalibur_blog_filter_secret_names.sh --export)"
set -eo pipefail

export_mode=0
if [[ "${1:-}" == "--export" ]]; then
  export_mode=1
fi

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$raw" ]]; then
  if [[ "$export_mode" -eq 1 ]]; then
    echo "export CLOUD_AGENT_INJECTED_SECRET_NAMES=''"
  fi
  return 0 2>/dev/null || exit 0
fi

filtered=()
# Split on commas and/or whitespace
# shellcheck disable=SC2206
tokens=(${raw//,/ })
for token in "${tokens[@]}"; do
  token="${token//$'\n'/}"
  token="${token//$'\r'/}"
  token="${token#"${token%%[![:space:]]*}"}"
  token="${token%"${token##*[![:space:]]}"}"
  [[ -z "$token" ]] && continue
  # Valid bash/ENV identifier only
  if [[ "$token" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    filtered+=("$token")
  fi
done

# Comma-separated — required by Cursor pre-commit.cursor secret scanner
safe=""
if ((${#filtered[@]} > 0)); then
  safe=$(IFS=','; echo "${filtered[*]}")
fi

if [[ "$export_mode" -eq 1 ]]; then
  # Single-quote for eval safety; value is only [A-Za-z0-9_,] after filter.
  printf "export CLOUD_AGENT_INJECTED_SECRET_NAMES='%s'\n" "$safe"
else
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$safe"
fi
