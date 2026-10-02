#!/usr/bin/env bash
# Sanitize Cloud Agent secret *name* lists before git commit.
# INC-20261002-1730: CLOUD_AGENT_*_SECRET_NAMES may contain URL-like tokens that
# are not bash identifiers; pre-commit.cursor then aborts on ${!SECRET_NAME}.
#
# Usage (before every commit in Cloud):
#   source scripts/sanitize_cloud_secret_names.sh
#
# Exports filtered CLOUD_AGENT_INJECTED_SECRET_NAMES and CLOUD_AGENT_ALL_SECRET_NAMES
# (comma-separated valid identifiers only). Does not print secret values.

_excalibur_filter_secret_names() {
  local raw="$1"
  python3 - <<'PY' "$raw"
import re, sys
raw = sys.argv[1] if len(sys.argv) > 1 else ""
valid = []
invalid = 0
for part in raw.split(","):
    name = part.strip()
    if not name:
        continue
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
        valid.append(name)
    else:
        invalid += 1
if invalid:
    print(f"sanitize_cloud_secret_names: skipped {invalid} invalid name(s)", file=sys.stderr)
print(",".join(valid))
PY
}

_src_injected="${CLOUD_AGENT_INJECTED_SECRET_NAMES-}"
_src_all="${CLOUD_AGENT_ALL_SECRET_NAMES-$_src_injected}"

export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_filter_secret_names "$_src_injected")"
export CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_filter_secret_names "$_src_all")"

unset _src_injected _src_all
unset -f _excalibur_filter_secret_names 2>/dev/null || true
