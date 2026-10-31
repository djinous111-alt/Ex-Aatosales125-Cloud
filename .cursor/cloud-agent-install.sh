#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Keep in sync with requirements.txt (Pillow, numpy, paramiko) + small helpers.
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt \
    || python3 -m pip install --quiet -r requirements.txt
fi
python3 -m pip install --break-system-packages --quiet \
  requests python-dotenv 2>/dev/null \
  || python3 -m pip install --quiet requests python-dotenv

# Ensure paramiko is importable even if requirements install was skipped/partial.
python3 - <<'PY' || python3 -m pip install --break-system-packages --quiet paramiko || python3 -m pip install --quiet paramiko
import importlib.util, sys
sys.exit(0 if importlib.util.find_spec("paramiko") else 1)
PY

mkdir -p .cursor/excalibur-blog-fragments memory
touch .cursor/excalibur-blog-handoff.md

# Bootstrap gitignored site.env.local from Cloud Secrets when missing (no secret echo).
if [[ -f scripts/excalibur_blog_site_env_bootstrap.py ]]; then
  python3 scripts/excalibur_blog_site_env_bootstrap.py || true
fi

echo "[excalibur-cloud] install ok"
