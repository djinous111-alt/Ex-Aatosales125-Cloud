#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# paramiko is required by excalibur_blog_wp_publish.py (SSH bootstrap).
# PEP 668: prefer --break-system-packages on Cloud images.
python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko

python3 -c "import paramiko; print('[excalibur-cloud] paramiko', paramiko.__version__)"

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
