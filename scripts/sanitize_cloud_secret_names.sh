#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to bash-safe identifiers before git hooks.
# Names that are not [A-Za-z_][A-Za-z0-9_]* break pre-commit.cursor ("invalid variable name").

_sanitize_name_list() {
  local raw="$1"
  local out=()
  local tok
  for tok in $raw; do
    if [[ "$tok" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$tok")
    fi
  done
  printf '%s' "${out[*]}"
}

if [ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES="$(_sanitize_name_list "$CLOUD_AGENT_ALL_SECRET_NAMES")"
fi
if [ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_sanitize_name_list "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
fi
