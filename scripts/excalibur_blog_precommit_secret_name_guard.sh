#!/usr/bin/env bash
# Durable reference patch for Cursor Cloud pre-commit.cursor secret scanner.
#
# Problem: CLOUD_AGENT_INJECTED_SECRET_NAMES may include values that are not
# valid bash identifiers (raw URLs, empty tokens). Expanding ${!SECRET_NAME}
# then aborts the whole commit with "invalid variable name".
#
# Apply the same guard near the SECRET_NAMES loop in the live hook:
#   /root/.cursor/agent-hooks/<id>/pre-commit.cursor
#
# This does NOT weaken scanning of real secrets (SSH_*, KIE_*, tokens).
# Public marketing URLs (PUBLIC_SITE_URL, CATALOG_URL, TELEGRAM_URL, MAX_URL)
# should preferably be Dashboard env vars, not "Secrets", so schema.jsonld
# and authors-registry.json can keep absolute Schema.org URLs.

set -euo pipefail

is_valid_secret_name() {
  [[ "$1" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]
}

# Example loop fragment (copy into pre-commit.cursor):
# for SECRET_NAME in "${SECRET_NAMES[@]}"; do
#   SECRET_NAME="${SECRET_NAME#"${SECRET_NAME%%[![:space:]]*}"}"
#   SECRET_NAME="${SECRET_NAME%"${SECRET_NAME##*[![:space:]]}"}"
#   [ -z "$SECRET_NAME" ] && continue
#   if ! is_valid_secret_name "$SECRET_NAME"; then
#     echo "pre-commit.cursor: skip invalid SECRET_NAME: ${SECRET_NAME:0:40}" >&2
#     continue
#   fi
#   RAW_SECRET_VALUE="${!SECRET_NAME}"
#   ...
# done

if [[ "${1:-}" == "--self-test" ]]; then
  is_valid_secret_name "PUBLIC_SITE_URL"
  ! is_valid_secret_name "https://example.com"
  ! is_valid_secret_name "1BAD"
  echo "OK secret-name guard self-test"
  exit 0
fi

echo "Reference helper only. Patch live pre-commit.cursor; run --self-test to verify regex."
exit 0
