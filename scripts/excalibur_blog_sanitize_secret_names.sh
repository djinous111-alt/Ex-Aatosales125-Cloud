#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers before git commit.
# Use when pre-commit fails with "invalid variable name" (INC-20261015-0906).
#
#   eval "$(python3 scripts/excalibur_blog_sanitize_secret_names.sh --export)"
#   # or:
#   source <(python3 - <<'PY'
#   ... see below ...
#   PY
#   )
set -euo pipefail

RAW="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$RAW" ]]; then
  if [[ "${1:-}" == "--export" ]]; then
    echo "# CLOUD_AGENT_INJECTED_SECRET_NAMES empty — nothing to sanitize"
  fi
  exit 0
fi

FILTERED="$(
  python3 - <<'PY'
import os, re
raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
parts = [p.strip() for p in raw.split(",") if p.strip()]
ok = [p for p in parts if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", p)]
print(",".join(ok))
PY
)"

if [[ "${1:-}" == "--export" ]]; then
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$FILTERED"
else
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$FILTERED"
  echo "Sanitized CLOUD_AGENT_INJECTED_SECRET_NAMES ($(echo "$FILTERED" | tr ',' '\n' | grep -c . || true) names)"
fi
