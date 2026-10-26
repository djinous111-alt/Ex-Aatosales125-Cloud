#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to valid bash identifiers before git commit.
#
# Cursor agent-hooks pre-commit expands ${!SECRET_NAME}. If the injected CSV
# includes a bare URL or "[REDACTED]" as a "name", bash errors with
# "invalid variable name" and blocks the commit.
#
# Usage (before git commit):
#   source scripts/excalibur_blog_sanitize_secret_names.sh
#
# Prefer this over `git commit --no-verify`.

# Do not `set -e` here: this file is meant to be sourced into an interactive shell.

_excalibur_sanitize_secret_csv() {
  local raw="${1:-}"
  local out=()
  local part
  local IFS=','
  # shellcheck disable=SC2086
  for part in $raw; do
    # trim whitespace
    part="${part#"${part%%[![:space:]]*}"}"
    part="${part%"${part##*[![:space:]]}"}"
    [[ -z "$part" ]] && continue
    [[ "$part" == "[REDACTED]" ]] && continue
    # valid bash identifier only
    if [[ "$part" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$part")
    fi
  done
  (IFS=','; echo "${out[*]}")
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_sanitize_secret_csv "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
fi
if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_sanitize_secret_csv "$CLOUD_AGENT_ALL_SECRET_NAMES")"
fi

unset -f _excalibur_sanitize_secret_csv 2>/dev/null || true
