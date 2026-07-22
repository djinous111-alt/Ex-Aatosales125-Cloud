#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko

# PEP 668 / externally-managed env: ensure SSH publish dep even if pip skipped.
if ! python3 -c "import paramiko" 2>/dev/null; then
  if command -v apt-get >/dev/null 2>&1; then
    echo "[excalibur-cloud] paramiko missing after pip; trying apt python3-paramiko"
    sudo apt-get update -qq && sudo apt-get install -y -qq python3-paramiko || true
  fi
fi
if ! python3 -c "import paramiko" 2>/dev/null; then
  echo "[excalibur-cloud] WARN: paramiko still unavailable — publish SSH will fail" >&2
else
  echo "[excalibur-cloud] paramiko OK"
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Cloud pre-commit/commit-msg *.cursor can die on URL-shaped secret *names* in
# CLOUD_AGENT_INJECTED_SECRET_NAMES → "[REDACTED]: invalid variable name".
if [[ -f scripts/excalibur_blog_patch_precommit_secret_scan.sh ]]; then
  bash scripts/excalibur_blog_patch_precommit_secret_scan.sh || true
fi

echo "[excalibur-cloud] install ok"
