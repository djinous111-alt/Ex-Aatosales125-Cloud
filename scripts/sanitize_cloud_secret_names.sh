#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to bash-safe identifiers before git hooks.
# pre-commit.cursor splits names by comma and uses ${!SECRET_NAME}; a URL or
# other non-identifier in the list causes: invalid variable name.

_sanitize_name_list() {
  local raw="$1"
  local tok
  local -a out
  out=()
  local IFS=','
  # shellcheck disable=SC2086
  set -- ${raw}
  for tok in "$@"; do
    # trim whitespace
    tok="${tok#"${tok%%[![:space:]]*}"}"
    tok="${tok%"${tok##*[![:space:]]}"}"
    case "$tok" in
      '' ) continue ;;
      [A-Za-z_][A-Za-z0-9_]* )
        # reject if any remaining char is not identifier-safe
        if [[ "$tok" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
          out+=("$tok")
        fi
        ;;
    esac
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
