#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers before git commit.
# Platform may inject a literal [REDACTED] token that breaks pre-commit `${!SECRET_NAME}`.
# Usage: source scripts/excalibur_blog_filter_secret_names.sh
#    or: eval "$(scripts/excalibur_blog_filter_secret_names.sh --export)"
set -euo pipefail

filter_secret_names() {
  # Accept comma- and/or whitespace-separated injection lists; emit comma-separated
  # bash-safe identifiers only (host pre-commit splits on IFS=',').
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
  local out=()
  local name
  raw="${raw//,/ }"
  # shellcheck disable=SC2206
  local names=($raw)
  for name in "${names[@]}"; do
    name="${name// /}"
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$name")
    fi
  done
  local IFS=','
  printf '%s' "${out[*]}"
}

if [[ "${1:-}" == "--export" ]]; then
  filtered="$(filter_secret_names)"
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$filtered"
  exit 0
fi

# When sourced:
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(filter_secret_names)"
else
  filter_secret_names
  echo
fi
