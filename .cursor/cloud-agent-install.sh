#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Auto-sanitize Cloud secret *names* that may contain URLs/non-identifiers.
# pre-commit.cursor uses ${!SECRET_NAME}; bad names → "invalid variable name".
REPO_ROOT="$(pwd)"
SANITIZE_SH="$REPO_ROOT/scripts/sanitize_cloud_secret_names.sh"
if [ -f "$SANITIZE_SH" ]; then
  # shellcheck disable=SC1090
  source "$SANITIZE_SH"
  MARKER="# excalibur sanitize_cloud_secret_names"
  for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
    touch "$rc"
    if ! grep -Fq "$MARKER" "$rc" 2>/dev/null; then
      {
        echo ""
        echo "$MARKER"
        echo "if [ -f \"$SANITIZE_SH\" ]; then source \"$SANITIZE_SH\"; fi"
      } >> "$rc"
    fi
  done
  chmod +x "$REPO_ROOT/scripts/excalibur_git.sh" 2>/dev/null || true
  echo "[excalibur-cloud] secret-name sanitize sourced + shell rc hooked"
fi

echo "[excalibur-cloud] install ok"
