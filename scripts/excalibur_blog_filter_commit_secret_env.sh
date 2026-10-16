#!/usr/bin/env bash
# Sanitize CLOUD_AGENT_INJECTED_SECRET_NAMES before git commit / pre-commit secret scan.
#
# Usage (required before commit in Cloud runs):
#   eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
#
# - Keeps only valid bash identifiers (drops URLs / raw values accidentally injected).
# - Omits public CTA / brand URL env names that legitimately appear in schema.jsonld
#   and other reader-facing artifacts (PUBLIC_SITE_URL, TELEGRAM_URL, …).
# - Prints export lines for eval; does not print secret values.

set -euo pipefail

is_public_cta_name() {
  case "$1" in
    PUBLIC_SITE_URL|WP_HOME|WP_SITE_URL|TELEGRAM_URL|CATALOG_URL|MAX_URL|INSTAGRAM_URL|TWOGIS_URL|TG_URL|VK_URL|OK_URL)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$raw" ]]; then
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' ""
  exit 0
fi

cleaned=()
IFS=',' read -r -a parts <<< "$raw"
for part in "${parts[@]}"; do
  name="$(printf '%s' "$part" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  [[ -z "$name" ]] && continue
  # Valid bash identifier only (no https://…, no spaces).
  if [[ ! "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    continue
  fi
  if is_public_cta_name "$name"; then
    continue
  fi
  cleaned+=("$name")
done

joined=""
if ((${#cleaned[@]} > 0)); then
  joined="$(IFS=','; echo "${cleaned[*]}")"
fi
printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$joined"
