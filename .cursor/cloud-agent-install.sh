#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Prefer repo requirements.txt (includes paramiko for SSH publish).
if [ -f requirements.txt ]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt 2>/dev/null \
    || python3 -m pip install --quiet -r requirements.txt
else
  python3 -m pip install --break-system-packages --quiet \
    requests pillow python-dotenv paramiko numpy 2>/dev/null \
    || python3 -m pip install --quiet requests pillow python-dotenv paramiko numpy
fi

# Hard guarantee for publish SSH transport even if requirements drift.
python3 -m pip install --break-system-packages --quiet paramiko 2>/dev/null \
  || python3 -m pip install --quiet paramiko

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
