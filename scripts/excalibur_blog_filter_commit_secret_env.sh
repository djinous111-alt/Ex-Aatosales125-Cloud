#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES for git commit subprocesses.
# Use: eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
# Then run git commit with hooks enabled.
set -euo pipefail

_filter_names() {
  local raw="${1:-}"
  local out=()
  local name
  local IFS=','
  # shellcheck disable=SC2206
  local names=($raw)
  for name in "${names[@]}"; do
    name="${name//[[:space:]]/}"
    [[ -z "$name" ]] && continue
    # Valid shell identifier only (avoids "invalid variable name" in pre-commit).
    [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || continue
    # Public marketing URLs belong in article.html / schema.jsonld.
    case "$name" in
      PUBLIC_SITE_URL|WP_HOME|WP_SITE_URL|CATALOG_URL|TELEGRAM_URL|MAX_URL) continue ;;
    esac
    out+=("$name")
  done
  local IFS=','
  printf '%s' "${out[*]}"
}

filtered_all="$(_filter_names "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"
filtered_injected="$(_filter_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"

printf 'export CLOUD_AGENT_ALL_SECRET_NAMES=%q\n' "$filtered_all"
printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$filtered_injected"
