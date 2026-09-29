#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to bash-safe identifiers only.
# Cloud pre-commit uses: IFS=',' read ...; RAW="${!SECRET_NAME}"
# A URL or other non-identifier in the list aborts the hook with
# "invalid variable name". Source this before git commit in Cloud runs.
#
# Usage: source scripts/sanitize_cloud_secret_names.sh

if [ -z "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]; then
  return 0 2>/dev/null || exit 0
fi

_sanitized="$(
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$CLOUD_AGENT_INJECTED_SECRET_NAMES" python3 - <<'PY'
import os, re
raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
parts = [p.strip() for p in raw.split(",")]
valid = [p for p in parts if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", p or "")]
print(",".join(valid))
PY
)"
export CLOUD_AGENT_INJECTED_SECRET_NAMES="$_sanitized"
unset _sanitized
