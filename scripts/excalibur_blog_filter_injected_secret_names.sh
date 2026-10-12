#!/usr/bin/env bash
# Sanitize CLOUD_AGENT_INJECTED_SECRET_NAMES for Cloud Agent pre-commit scanners.
#
# The scanner iterates names and expands ${!SECRET_NAME}. A non-identifier name
# (e.g. a raw URL mistakenly injected as a "secret name") aborts with
# `invalid variable name` before any file scan runs.
#
# Usage (source, do not execute):
#   source scripts/sanitize_cloud_secret_names.sh
#
# For commits that must embed public marketing URLs (schema.jsonld, llms.txt,
# article CTA hrefs already allowlisted via HTML pragma):
#   EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 source scripts/sanitize_cloud_secret_names.sh
#
# Safe to source multiple times. Does not print secret values.

_excalibur_sanitize_cloud_secret_names() {
  local original="${CLOUD_AGENT_INJECTED_SECRET_NAMES-}"
  local exclude_public="${EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS-}"
  local -a kept=()
  local name normalized

  if [[ -z "${original}" ]]; then
    return 0
  fi

  # Support space- and/or comma-separated lists from Cloud injection.
  normalized="${original//,/ }"

  # shellcheck disable=SC2086
  for name in ${normalized}; do
    # Valid bash identifier only (letters/digits/underscore, not starting with digit).
    if [[ ! "${name}" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      continue
    fi

    # Optional: drop env names whose values are public marketing URLs already
    # present in authors-registry / schema / conversion-map patterns.
    if [[ "${exclude_public}" == "1" || "${exclude_public}" == "yes" || "${exclude_public}" == "true" ]]; then
      case "${name}" in
        PUBLIC_SITE_URL|WP_HOME|WP_SITE_URL|CATALOG_URL|TELEGRAM_URL|MAX_URL|SITE_URL)
          continue
          ;;
      esac
    fi

    kept+=("${name}")
  done

  # Re-join with commas — Cloud pre-commit uses:
  #   IFS=',' read -ra SECRET_NAMES <<< "$CLOUD_AGENT_INJECTED_SECRET_NAMES"
  local IFS=','
  CLOUD_AGENT_INJECTED_SECRET_NAMES="${kept[*]}"
  export CLOUD_AGENT_INJECTED_SECRET_NAMES
}

_excalibur_sanitize_cloud_secret_names
unset -f _excalibur_sanitize_cloud_secret_names
