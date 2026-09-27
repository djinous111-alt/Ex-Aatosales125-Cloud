#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko

# Prefer apt package when available (idempotent; ignore failure if pip already satisfied).
if command -v apt-get >/dev/null 2>&1; then
  apt-get update -qq >/dev/null 2>&1 || true
  apt-get install -y -qq python3-paramiko >/dev/null 2>&1 || true
fi

python3 -c "import paramiko" >/dev/null

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
