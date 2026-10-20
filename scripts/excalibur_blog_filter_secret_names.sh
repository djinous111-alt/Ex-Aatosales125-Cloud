#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES / CLOUD_AGENT_SECRET_NAMES to bash-safe
# identifiers before git commit. Prevents pre-commit.cursor
# RAW_SECRET_VALUE="${!SECRET_NAME}" → "invalid variable name" when the list
# contains polluted tokens like [REDACTED] or URL fragments.
#
# Usage:
#   source scripts/excalibur_blog_filter_secret_names.sh
#   scripts/excalibur_blog_filter_secret_names.sh --print
#   scripts/excalibur_blog_filter_secret_names.sh git commit ...

filter_names() {
  local raw="${1:-}"
  local out=()
  local name
  local IFS=','
  local -a names
  read -ra names <<< "$raw"
  for name in "${names[@]}"; do
    name="$(echo "$name" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
    [[ -z "$name" ]] && continue
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$name")
    fi
  done
  (IFS=','; echo "${out[*]}")
}

_apply_filter() {
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$(filter_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
  CLOUD_AGENT_SECRET_NAMES="$(filter_names "${CLOUD_AGENT_SECRET_NAMES:-}")"
  export CLOUD_AGENT_INJECTED_SECRET_NAMES CLOUD_AGENT_SECRET_NAMES
}

# Sourced into current shell?
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
  _apply_filter
  return 0 2>/dev/null || exit 0
fi

set -euo pipefail

if [[ "${1:-}" == "--print" ]]; then
  echo "CLOUD_AGENT_INJECTED_SECRET_NAMES_FILTERED=$(filter_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
  echo "CLOUD_AGENT_SECRET_NAMES_FILTERED=$(filter_names "${CLOUD_AGENT_SECRET_NAMES:-}")"
  exit 0
fi

_apply_filter

if [[ $# -gt 0 ]]; then
  exec "$@"
fi

echo "Filtered secret name lists for current shell."
echo "Usage: source scripts/excalibur_blog_filter_secret_names.sh"
echo "   or: scripts/excalibur_blog_filter_secret_names.sh --print"
echo "   or: scripts/excalibur_blog_filter_secret_names.sh git commit ..."
