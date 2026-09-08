#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Install publish/runtime deps into the same python3 used by pipeline scripts.
# paramiko is required by excalibur_blog_wp_publish.py (SSH transport).
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt \
    || python3 -m pip install --quiet -r requirements.txt
else
  python3 -m pip install --break-system-packages --quiet \
    requests pillow python-dotenv numpy paramiko \
    || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko
fi

# Explicit sanity: fail loud if publish SSH dependency missing after install.
python3 -c "import paramiko" || {
  echo "[excalibur-cloud] WARN: paramiko still missing; retrying direct install"
  python3 -m pip install --break-system-packages --quiet paramiko \
    || python3 -m pip install --quiet paramiko
}

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
