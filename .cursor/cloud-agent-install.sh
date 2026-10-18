#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Prefer requirements.txt so publish deps (paramiko) stay in sync.
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt 2>/dev/null \
    || python3 -m pip install --quiet -r requirements.txt
else
  python3 -m pip install --break-system-packages --quiet \
    requests pillow python-dotenv numpy paramiko 2>/dev/null \
    || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko
fi

# Explicit paramiko check — publish SSH fails late if missing.
python3 - <<'PY'
import importlib.util
import sys
missing = [name for name in ("PIL", "numpy", "paramiko") if importlib.util.find_spec(name) is None]
if missing:
    print("[excalibur-cloud] WARN missing modules:", ", ".join(missing), file=sys.stderr)
    sys.exit(1)
print("[excalibur-cloud] python deps ok: Pillow numpy paramiko")
PY

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
