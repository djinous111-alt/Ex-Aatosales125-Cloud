#!/usr/bin/env bash
# Harden Cursor Cloud pre-commit secret scrub against URL-shaped /
# non-identifier entries in CLOUD_AGENT_INJECTED_SECRET_NAMES.
#
# Root cause (INC-20260723-1322/1327/1334):
#   SECRET_NAME may be a URL (e.g. https://...) when Dashboard secrets
#   are misnamed or values leak into the names list. Bash then dies with
#   `invalid variable name` on ${!SECRET_NAME} under `set -e`.
#
# This script wraps every pre-commit.cursor under ~/.cursor/agent-hooks/
# so only valid shell identifiers are expanded. Safe to re-run (idempotent).

set -euo pipefail

MARKER="# excalibur-secret-name-sanitize"

wrap_hook() {
  local hook="$1"
  local bak="${hook}.excalibur-bak"
  local wrapped="${hook}.excalibur-wrapped"

  if head -n 5 "$hook" 2>/dev/null | grep -q "$MARKER"; then
    echo "[excalibur-secret-scrub] already wrapped: $hook"
    return 0
  fi

  if [[ ! -f "$hook" ]]; then
    return 0
  fi

  cp -f "$hook" "$bak"
  cat > "$wrapped" <<'WRAP'
#!/usr/bin/env bash
# excalibur-secret-name-sanitize
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid shell identifiers
# before the Cursor secret-scrub hook expands ${!SECRET_NAME}.
set -euo pipefail

MARKER_FILTER=1
if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  _filtered=""
  IFS=',' read -ra _names <<< "${CLOUD_AGENT_INJECTED_SECRET_NAMES}"
  for _n in "${_names[@]}"; do
    _n="${_n#"${_n%%[![:space:]]*}"}"
    _n="${_n%"${_n##*[![:space:]]}"}"
    if [[ -z "$_n" ]]; then
      continue
    fi
    if [[ "$_n" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      if [[ -z "$_filtered" ]]; then
        _filtered="$_n"
      else
        _filtered="${_filtered},${_n}"
      fi
    else
      echo "[excalibur-secret-scrub] skip non-identifier secret name (len=${#_n})" >&2
    fi
  done
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$_filtered"
fi

WRAP
  # Append the original hook body (skip shebang of backup).
  if head -n 1 "$bak" | grep -q '^#!'; then
    tail -n +2 "$bak" >> "$wrapped"
  else
    cat "$bak" >> "$wrapped"
  fi
  chmod +x "$wrapped"
  mv -f "$wrapped" "$hook"
  echo "[excalibur-secret-scrub] wrapped: $hook"
}

hooks_root="${HOME}/.cursor/agent-hooks"
if [[ ! -d "$hooks_root" ]]; then
  echo "[excalibur-secret-scrub] no agent-hooks dir yet; skip"
  exit 0
fi

find "$hooks_root" -type f -name 'pre-commit.cursor' -print0 2>/dev/null \
  | while IFS= read -r -d '' hook; do
      wrap_hook "$hook"
    done

echo "[excalibur-secret-scrub] done"
