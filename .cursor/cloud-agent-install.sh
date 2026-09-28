#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Keep in sync with requirements.txt + .cursor/Dockerfile
# paramiko is required for SSH publish (do not rely on ad-hoc pip each run).
python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

# Soft-sanitize Cloud secret-name injection for later commits in this shell.
if [[ -f scripts/excalibur_blog_sanitize_secret_names.sh ]]; then
  # shellcheck disable=SC1091
  source scripts/excalibur_blog_sanitize_secret_names.sh || true
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

python3 - <<'PY'
import importlib.util

checks = {
    "requests": "requests",
    "PIL": "PIL",
    "numpy": "numpy",
    "paramiko": "paramiko",
    "dotenv": "dotenv",
}
missing = [label for label, mod in checks.items() if importlib.util.find_spec(mod) is None]
if missing:
    raise SystemExit(f"[excalibur-cloud] missing modules after install: {', '.join(missing)}")
print("[excalibur-cloud] python deps ok: requests pillow numpy paramiko python-dotenv")
PY

echo "[excalibur-cloud] install ok"
