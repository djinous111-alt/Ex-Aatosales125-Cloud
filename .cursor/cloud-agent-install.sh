#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# paramiko is required by excalibur_blog_wp_publish.py (SSH transport).
# Keep in sync with requirements.txt.
python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko numpy 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko numpy

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
