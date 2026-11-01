#!/usr/bin/env bash
# Filter Cloud Agent secret-name lists to valid bash identifiers before git commit.
# Fixes: pre-commit.cursor aborts with `invalid variable name` on ${!SECRET_NAME}
# when CLOUD_AGENT_INJECTED_SECRET_NAMES contains empty tokens or non-identifiers
# (e.g. a URL accidentally appended to the comma-separated list).
#
# Usage:
#   source scripts/excalibur_blog_filter_commit_secret_env.sh
#   eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
#   bash scripts/excalibur_git.sh commit -m "..."
set -euo pipefail

_excalibur_filter_secret_names() {
  local raw="${1:-}"
  local -a parts=()
  local -a keep=()
  local part
  IFS=',' read -ra parts <<< "$raw"
  for part in "${parts[@]}"; do
    part="${part#"${part%%[![:space:]]*}"}"
    part="${part%"${part##*[![:space:]]}"}"
    [[ -z "$part" ]] && continue
    # bash identifier: [A-Za-z_][A-Za-z0-9_]*
    if [[ "$part" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      keep+=("$part")
    fi
  done
  local IFS=','
  echo "${keep[*]}"
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_filter_secret_names "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
  export CLOUD_AGENT_INJECTED_SECRET_NAMES
fi

if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]]; then
  CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_filter_secret_names "$CLOUD_AGENT_ALL_SECRET_NAMES")"
  export CLOUD_AGENT_ALL_SECRET_NAMES
fi

# When executed (not sourced), emit export lines for: eval "$(bash …)"
if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
  printf 'export CLOUD_AGENT_ALL_SECRET_NAMES=%q\n' "${CLOUD_AGENT_ALL_SECRET_NAMES:-}"
fi
