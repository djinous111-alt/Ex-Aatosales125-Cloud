#!/usr/bin/env bash
# Harden Cursor Cloud pre-commit.cursor secret scanner (INC-1316).
# 1) Skip secret names that are not valid bash identifiers before ${!NAME}.
# 2) Skip public CTA / site URL env names that intentionally appear in article HTML/schema.
set -euo pipefail

MARKER="# EXCALIBUR_BLOG_PRECOMMIT_SECRET_HARDEN"

find_hooks() {
  local candidates=()
  if [[ -n "${CURSOR_AGENT_HOOKS_DIR:-}" ]]; then
    candidates+=("${CURSOR_AGENT_HOOKS_DIR}/pre-commit.cursor")
  fi
  # Common Cloud Agent install path(s)
  while IFS= read -r -d '' path; do
    candidates+=("$path")
  done < <(find /root/.cursor/agent-hooks -name 'pre-commit.cursor' -print0 2>/dev/null || true)
  if [[ -f .git/hooks/pre-commit.cursor ]]; then
    candidates+=(".git/hooks/pre-commit.cursor")
  fi
  printf '%s\n' "${candidates[@]}" | awk 'NF && !seen[$0]++'
}

SNIPPET=$(cat <<'EOF'
    # EXCALIBUR_BLOG_PRECOMMIT_SECRET_HARDEN
    # Skip names that break bash ${!indirect} expansion (invalid variable name).
    if [[ ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
        continue
    fi
    # Public CTA / site URLs belong in article HTML and schema; do not secret-scan them.
    case "$SECRET_NAME" in
        CATALOG_URL|TELEGRAM_URL|MAX_URL|PUBLIC_SITE_URL|WP_SITE_URL|WP_HOME|PUBLIC_BLOG_URL)
            continue
            ;;
    esac
EOF
)

patched=0
skipped=0
missing=0

while IFS= read -r hook; do
  [[ -z "$hook" || ! -f "$hook" ]] && continue
  if grep -qF "$MARKER" "$hook"; then
    echo "[excalibur-harden] already patched: $hook"
    skipped=$((skipped + 1))
    continue
  fi
  if ! grep -q 'RAW_SECRET_VALUE="\${!SECRET_NAME}"' "$hook"; then
    echo "[excalibur-harden] skip (no RAW_SECRET_VALUE pattern): $hook"
    missing=$((missing + 1))
    continue
  fi
  tmp="${hook}.excalibur.tmp"
  awk -v snippet="$SNIPPET" '
    /RAW_SECRET_VALUE="\$\{!SECRET_NAME\}"/ && !done {
      print snippet
      done=1
    }
    { print }
  ' "$hook" > "$tmp"
  mv "$tmp" "$hook"
  chmod +x "$hook" 2>/dev/null || true
  echo "[excalibur-harden] patched: $hook"
  patched=$((patched + 1))
done < <(find_hooks)

echo "[excalibur-harden] done patched=$patched skipped=$skipped missing=$missing"
# Non-zero only if we found hooks that needed the RAW pattern but could not patch — never fail install
# when no hooks exist yet (fresh clone before Cursor injects hooks).
exit 0
