#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to bash identifiers only.
# Cursor pre-commit secret-scan uses ${!SECRET_NAME}; non-identifier tokens
# (URLs, [REDACTED], placeholders) cause "invalid variable name".
#
# Usage (before git commit/push in Cloud Agent shells):
#   source scripts/excalibur_blog_filter_injected_secret_names.sh
# Or one-shot:
#   . scripts/excalibur_blog_filter_injected_secret_names.sh && git commit ...
set -euo pipefail

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  _filtered=""
  _IFS_SAVE=$IFS
  IFS=','
  # shellcheck disable=SC2206
  _names=(${CLOUD_AGENT_INJECTED_SECRET_NAMES})
  IFS=$_IFS_SAVE
  for _name in "${_names[@]}"; do
    _name="${_name#"${_name%%[![:space:]]*}"}"
    _name="${_name%"${_name##*[![:space:]]}"}"
    if [[ "$_name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      if [[ -n "$_filtered" ]]; then
        _filtered+=",${_name}"
      else
        _filtered="${_name}"
      fi
    fi
  done
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$_filtered"
  unset _filtered _name _names _IFS_SAVE
fi
