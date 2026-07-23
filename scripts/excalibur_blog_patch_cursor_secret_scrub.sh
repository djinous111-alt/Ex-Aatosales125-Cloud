#!/usr/bin/env bash
# Harden Cursor Cloud secret-scrub hooks against URL-shaped /
# non-identifier entries in CLOUD_AGENT_INJECTED_SECRET_NAMES.
#
# Root cause (INC-20260723-1322/1327/1334):
#   SECRET_NAME may be a URL (e.g. https://...). Bash dies with
#   `invalid variable name` on ${!SECRET_NAME} under `set -e`.
#
# Wraps every agent-hooks `*.cursor` scanner (pre-commit, commit-msg, …).
# Idempotent. Important constraints:
# - Do not enable `set -u` in the wrap (Cursor uses unset assoc keys).
# - Pristine backups must NOT match dispatcher globs `$HOOK.cursor*`
#   and should live outside `*.cursor` filenames (use a subdir).

set -euo pipefail

MARKER="# excalibur-secret-name-sanitize"

wrap_hook() {
  local hook="$1"
  local hooks_dir base pristine_dir bak wrapped src
  hooks_dir="$(dirname "$hook")"
  base="$(basename "$hook")"
  pristine_dir="${hooks_dir}/excalibur-pristine"
  bak="${pristine_dir}/${base}"
  wrapped="${pristine_dir}/wrap-tmp-${base}"
  src=""

  mkdir -p "$pristine_dir"

  if [[ ! -f "$hook" ]]; then
    return 0
  fi

  # Skip our own pristine copies if somehow selected.
  case "$hook" in
    */excalibur-pristine/*) return 0 ;;
  esac

  # Migrate legacy backups that matched dispatcher globs or *.cursor names.
  for legacy in \
      "${hook}.excalibur-bak" \
      "${hook}.excalibur-pristine" \
      "${hooks_dir}/excalibur-pristine-${base}"
  do
    if [[ -f "$legacy" ]]; then
      if grep -q 'CLOUD_AGENT_INJECTED_SECRET_NAMES' "$legacy" && ! grep -q "$MARKER" "$legacy"; then
        mv -f "$legacy" "$bak"
        chmod a-x "$bak" 2>/dev/null || true
        echo "[excalibur-secret-scrub] migrated legacy bak → $bak"
      else
        rm -f "$legacy"
      fi
    fi
  done
  # Drop only OUR accidental glob-matching backups (never Cursor's *.cursor.co-author etc.).
  for extra in \
      "${hook}.excalibur-bak" \
      "${hook}.excalibur-pristine" \
      "${hook}.excalibur-wrapped"
  do
    [[ -f "$extra" ]] && rm -f "$extra" && echo "[excalibur-secret-scrub] removed $extra"
  done

  if [[ -f "$bak" ]] && grep -q 'CLOUD_AGENT_INJECTED_SECRET_NAMES' "$bak" \
      && ! grep -q "$MARKER" "$bak"; then
    src="$bak"
  elif grep -q 'CLOUD_AGENT_INJECTED_SECRET_NAMES' "$hook" && ! grep -q "$MARKER" "$hook"; then
    cp -f "$hook" "$bak"
    chmod a-x "$bak" 2>/dev/null || true
    src="$bak"
  elif grep -q "$MARKER" "$hook" && grep -q 'CLOUD_AGENT_INJECTED_SECRET_NAMES' "$hook"; then
    {
      echo '#!/bin/bash'
      # Prefer Cursor banner; else drop our sanitize header.
      if grep -q 'Cloud Agent Secrets Scanner' "$hook"; then
        awk '/^# Cloud Agent Secrets Scanner/{emit=1} emit{print}' "$hook"
      else
        awk -v m="$MARKER" '
          BEGIN{emit=0}
          $0 ~ m {next}
          /^set -e$/ && !emit {next}
          /^if \[\[ -n "\$\{CLOUD_AGENT_INJECTED_SECRET_NAMES/ {skip=1}
          skip && /^fi$/ {skip=0; next}
          skip {next}
          /^#!/ {next}
          {print}
        ' "$hook"
      fi
    } > "$bak"
    chmod a-x "$bak" 2>/dev/null || true
    src="$bak"
    echo "[excalibur-secret-scrub] recovered pristine scanner from wrapped $base"
  else
    echo "[excalibur-secret-scrub] WARN skip (no secret scrub body): $hook" >&2
    return 0
  fi

  cat > "$wrapped" <<'WRAP'
#!/usr/bin/env bash
# excalibur-secret-name-sanitize
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid shell identifiers
# before Cursor secret-scrub expands ${!SECRET_NAME}.
# NOTE: do not enable `set -u` — upstream Cursor hooks use unset assoc keys.
set -e

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
  if head -n 1 "$src" | grep -q '^#!'; then
    tail -n +2 "$src" >> "$wrapped"
  else
    cat "$src" >> "$wrapped"
  fi
  chmod +x "$wrapped"
  mv -f "$wrapped" "$hook"
  chmod a-x "$bak" 2>/dev/null || true
  echo "[excalibur-secret-scrub] wrapped: $hook"
}

hooks_root="${HOME}/.cursor/agent-hooks"
if [[ ! -d "$hooks_root" ]]; then
  echo "[excalibur-secret-scrub] no agent-hooks dir yet; skip"
  exit 0
fi

# Only live hook files named exactly <hook>.cursor (not backups).
find "$hooks_root" -type f -name '*.cursor' ! -path '*/excalibur-pristine/*' -print0 2>/dev/null \
  | while IFS= read -r -d '' hook; do
      base="$(basename "$hook")"
      case "$base" in
        excalibur-pristine-*) rm -f "$hook"; echo "[excalibur-secret-scrub] removed legacy $hook"; continue ;;
      esac
      if grep -q 'CLOUD_AGENT_INJECTED_SECRET_NAMES' "$hook" 2>/dev/null; then
        wrap_hook "$hook"
      fi
    done

echo "[excalibur-secret-scrub] done"
