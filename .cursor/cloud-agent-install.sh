#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Harden Cloud pre-commit secrets scanner against non-identifier secret names
if [[ -f scripts/excalibur_blog_harden_precommit_secret_names.sh ]]; then
  bash scripts/excalibur_blog_harden_precommit_secret_names.sh || true
fi

echo "[excalibur-cloud] install ok"
