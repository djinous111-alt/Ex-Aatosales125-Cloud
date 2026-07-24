#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# PEP 668: prefer --break-system-packages (Cloud Ubuntu). Fallback without flag.
# paramiko is required for SSH publish bootstrap.
python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
