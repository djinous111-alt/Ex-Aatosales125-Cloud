#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Publish SSH transport needs paramiko; cover/QA need pillow+numpy.
python3 -m pip install --break-system-packages --quiet \
  requests pillow numpy python-dotenv paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow numpy python-dotenv paramiko

# Skip URL-shaped / non-identifier Cloud Secret names in pre-commit scanners.
if [[ -f scripts/excalibur_blog_patch_precommit_secret_scan.sh ]]; then
  bash scripts/excalibur_blog_patch_precommit_secret_scan.sh || true
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
