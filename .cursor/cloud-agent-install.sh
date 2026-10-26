#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  -r requirements.txt 2>/dev/null \
  || python3 -m pip install --break-system-packages --quiet \
    requests pillow python-dotenv numpy paramiko \
  || python3 -m pip install --quiet \
    requests pillow python-dotenv numpy paramiko

# Ensure SSH publish dependency is importable even if requirements.txt was skipped.
python3 - <<'PY'
import importlib.util
import subprocess
import sys
if importlib.util.find_spec("paramiko") is None:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--break-system-packages", "--quiet", "paramiko"]
    )
print("[excalibur-cloud] paramiko ok")
PY

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Fix Cloud pre-commit secrets scanner when CLOUD_AGENT_INJECTED_SECRET_NAMES
# contains non-identifier junk (raw URLs) that aborts every git commit.
if [[ -f scripts/excalibur_blog_patch_precommit_secret_scanner.sh ]]; then
  bash scripts/excalibur_blog_patch_precommit_secret_scanner.sh || true
fi

echo "[excalibur-cloud] install ok"
