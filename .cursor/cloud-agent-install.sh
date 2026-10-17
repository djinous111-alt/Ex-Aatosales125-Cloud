#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# paramiko is required by excalibur_blog_wp_publish.py SSH transport (--env-check does not import it).
python3 -m pip install --break-system-packages --quiet \
  -r requirements.txt requests python-dotenv 2>/dev/null \
  || python3 -m pip install --quiet -r requirements.txt requests python-dotenv
python3 -c "import paramiko" || {
  echo "[excalibur-cloud] FATAL: paramiko missing after install" >&2
  exit 1
}

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
