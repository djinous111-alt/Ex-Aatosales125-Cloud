#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to bash-safe identifiers only.
# Cloud pre-commit uses: IFS=',' read ...; RAW="${!SECRET_NAME}"
# A URL or other non-identifier in the list aborts the hook with
# "invalid variable name". Source this before git commit in Cloud runs.
#
# Usage:
#   source scripts/sanitize_cloud_secret_names.sh
#
# When committing artifacts that intentionally embed public marketing URLs
# (schema.jsonld, llms.txt, promotion-checklist), also exclude those secret
# *names* from the scanner list so the hook does not treat public hrefs as leaks:
#   EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 source scripts/sanitize_cloud_secret_names.sh
#
# Names excluded in that mode (not secret values — only scanner name list):
#   PUBLIC_SITE_URL, WP_HOME, WP_SITE_URL, CATALOG_URL, TELEGRAM_URL, MAX_URL

if [ -z "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]; then
  return 0 2>/dev/null || exit 0
fi

_sanitized="$(
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$CLOUD_AGENT_INJECTED_SECRET_NAMES" \
  EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS="${EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS:-}" \
  python3 - <<'PY'
import os, re
raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
parts = [p.strip() for p in raw.split(",")]
valid = [p for p in parts if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", p or "")]
if os.environ.get("EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS", "").strip().lower() in {"1", "yes", "true"}:
    drop = {
        "PUBLIC_SITE_URL",
        "WP_HOME",
        "WP_SITE_URL",
        "CATALOG_URL",
        "TELEGRAM_URL",
        "MAX_URL",
    }
    valid = [p for p in valid if p not in drop]
print(",".join(valid))
PY
)"
export CLOUD_AGENT_INJECTED_SECRET_NAMES="$_sanitized"
unset _sanitized
