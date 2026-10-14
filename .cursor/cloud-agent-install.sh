#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko numpy 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko numpy

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

if ! python3 -c "import paramiko" 2>/dev/null; then
  echo "[excalibur-cloud] WARN: paramiko import failed after install" >&2
else
  echo "[excalibur-cloud] paramiko ok"
fi

echo "[excalibur-cloud] install ok"
