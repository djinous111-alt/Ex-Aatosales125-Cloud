#!/usr/bin/env bash
# Filter Cloud secret-name env lists to valid bash identifiers.
# Use before git commit when Cloud pre-commit fails with "invalid variable name"
# (pre-commit.cursor expands ${!SECRET_NAME} and aborts on non-identifiers).
#
# Usage:
#   source scripts/excalibur_blog_filter_secret_names.sh
#   eval "$(scripts/excalibur_blog_filter_secret_names.sh --export)"
#   source scripts/excalibur_git.sh   # wraps filter + git

set -euo pipefail

EXPORT=0
if [[ "${1:-}" == "--export" ]]; then
  EXPORT=1
fi

_filter_and_export() {
  local varname="$1"
  local raw="${!varname-}"
  local filtered=()
  local skipped=0
  local name joined

  if [[ -z "$raw" ]]; then
    export "$varname="
    if [[ "$EXPORT" -eq 1 ]]; then
      printf 'export %s=%q\n' "$varname" ""
    else
      echo "[excalibur] $varname empty" >&2
    fi
    return 0
  fi

  IFS=',' read -ra NAMES <<< "$raw"
  for name in "${NAMES[@]}"; do
    name="${name#"${name%%[![:space:]]*}"}"
    name="${name%"${name##*[![:space:]]}"}"
    [[ -z "$name" ]] && continue
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      filtered+=("$name")
    else
      skipped=$((skipped + 1))
    fi
  done

  joined=$(IFS=','; echo "${filtered[*]}")
  export "$varname=$joined"

  if [[ "$EXPORT" -eq 1 ]]; then
    printf 'export %s=%q\n' "$varname" "$joined"
  else
    echo "[excalibur] $varname kept=${#filtered[@]} skipped_invalid=$skipped" >&2
  fi
}

_filter_and_export CLOUD_AGENT_INJECTED_SECRET_NAMES
# Some Cloud images also expand CLOUD_AGENT_ALL_SECRET_NAMES in pre-commit.
if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES+x}" ]]; then
  _filter_and_export CLOUD_AGENT_ALL_SECRET_NAMES
fi
