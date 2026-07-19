#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko

# Harden Cloud pre-commit secrets scanner (skip non-identifier SECRET_NAME).
if [[ -f scripts/excalibur_blog_patch_cursor_precommit.sh ]]; then
  bash scripts/excalibur_blog_patch_cursor_precommit.sh || true
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
