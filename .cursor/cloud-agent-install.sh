#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Materialize gitignored publish env from Cloud Secrets when missing (no secrets printed).
if [[ ! -f memory/site.env.local ]]; then
  python3 scripts/excalibur_blog_doctor.py >/tmp/excalibur-cloud-doctor-bootstrap.log 2>&1 || true
fi

echo "[excalibur-cloud] install ok"
