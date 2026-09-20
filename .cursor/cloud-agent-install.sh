#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Harden Cursor secret-scrub against URL-shaped CLOUD_AGENT_INJECTED_SECRET_NAMES
if [[ -f scripts/excalibur_blog_patch_cursor_secret_scrub.sh ]]; then
  bash scripts/excalibur_blog_patch_cursor_secret_scrub.sh || true
fi

echo "[excalibur-cloud] install ok"
