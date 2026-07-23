#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Prefer requirements.txt (Pillow, numpy, paramiko). PEP 668 Cloud images need --break-system-packages.
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt 2>/dev/null \
    || python3 -m pip install --quiet -r requirements.txt
else
  python3 -m pip install --break-system-packages --quiet \
    requests pillow numpy paramiko python-dotenv 2>/dev/null \
    || python3 -m pip install --quiet requests pillow numpy paramiko python-dotenv
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
