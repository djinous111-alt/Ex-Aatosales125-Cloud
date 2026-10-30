#!/usr/bin/env bash
# Filter CLOUD_AGENT_*SECRET_NAMES for git commit subprocesses.
#
# Cloud pre-commit expands ${!SECRET_NAME}. Non-identifiers (raw URLs,
# literal [REDACTED], space-joined blobs) crash the hook with
# "invalid variable name" before the content scan runs.
#
# Public marketing URL secret names are excluded by default so article.html
# / schema.jsonld can embed intentional CTA / site / sameAs URLs.
#
# Usage (before every Cloud git commit with hooks enabled):
#   eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
#   git commit ...
#
# Optional: keep public URL names in the scan list (stricter):
#   EXCALIBUR_KEEP_PUBLIC_URL_SECRETS=1 eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
set -euo pipefail

_filter_names() {
  local raw="${1:-}"
  local out=()
  local name
  # Accept comma- and whitespace-separated lists.
  local normalized="${raw//,/ }"
  # shellcheck disable=SC2206
  local names=($normalized)
  for name in "${names[@]}"; do
    name="${name//[[:space:]]/}"
    [[ -z "$name" ]] && continue
    # Valid shell identifier only.
    [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || continue
    if [[ "${EXCALIBUR_KEEP_PUBLIC_URL_SECRETS:-0}" != "1" ]]; then
      case "$name" in
        PUBLIC_SITE_URL|WP_HOME|WP_SITE_URL|CATALOG_URL|TELEGRAM_URL|MAX_URL) continue ;;
      esac
    fi
    out+=("$name")
  done
  local IFS=','
  printf '%s' "${out[*]}"
}

filtered_all="$(_filter_names "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"
filtered_injected="$(_filter_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
filtered_secret="$(_filter_names "${CLOUD_AGENT_SECRET_NAMES:-}")"

printf 'export CLOUD_AGENT_ALL_SECRET_NAMES=%q\n' "$filtered_all"
printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$filtered_injected"
printf 'export CLOUD_AGENT_SECRET_NAMES=%q\n' "$filtered_secret"
