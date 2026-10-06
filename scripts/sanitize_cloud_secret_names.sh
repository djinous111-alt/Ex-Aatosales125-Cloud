#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to bash-safe identifiers before git hooks.
# pre-commit.cursor splits names by comma and uses ${!SECRET_NAME}; a URL or
# other non-identifier in the list causes: invalid variable name.

_sanitize_name_list() {
  local raw="$1"
  local tok
  local -a out=()
  local -a parts=()
  local OLDIFS="$IFS"
  IFS=','
  read -ra parts <<< "$raw"
  IFS="$OLDIFS"
  for tok in "${parts[@]}"; do
    tok="${tok#"${tok%%[![:space:]]*}"}"
    tok="${tok%"${tok##*[![:space:]]}"}"
    if [[ "$tok" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$tok")
    fi
  done
  local IFS=','
  printf '%s' "${out[*]}"
}

if [ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]; then
  CLOUD_AGENT_ALL_SECRET_NAMES="$(_sanitize_name_list "$CLOUD_AGENT_ALL_SECRET_NAMES")"
  export CLOUD_AGENT_ALL_SECRET_NAMES
fi
if [ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]; then
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_sanitize_name_list "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
  export CLOUD_AGENT_INJECTED_SECRET_NAMES
fi
