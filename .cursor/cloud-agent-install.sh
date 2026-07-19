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

# Harden Cursor secret-scan hooks (pre-commit + commit-msg) against invalid
# SECRET_NAME entries (URL values in CLOUD_AGENT_INJECTED_SECRET_NAMES → crash).
if [[ -x scripts/excalibur_blog_patch_cursor_precommit.sh ]]; then
  bash scripts/excalibur_blog_patch_cursor_precommit.sh || true
elif [[ -f scripts/excalibur_blog_patch_cursor_precommit.sh ]]; then
  bash scripts/excalibur_blog_patch_cursor_precommit.sh || true
fi

echo "[excalibur-cloud] install ok"
