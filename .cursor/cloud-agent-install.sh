#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Publish needs paramiko (requirements.txt). Keep requests/dotenv for ad-hoc scripts.
pip_install() {
  if python3 -m pip install --break-system-packages --quiet "$@" 2>/dev/null; then
    return 0
  fi
  python3 -m pip install --quiet "$@"
}

if [[ -f requirements.txt ]]; then
  pip_install -r requirements.txt
fi
pip_install requests python-dotenv

python3 - <<'PY'
import importlib.util
import sys

required = [("paramiko", "paramiko"), ("PIL", "Pillow")]
missing = [pkg for mod, pkg in required if importlib.util.find_spec(mod) is None]
if missing:
    print("[excalibur-cloud] missing after install:", ", ".join(missing), file=sys.stderr)
    sys.exit(1)
print("[excalibur-cloud] python deps ok:", ", ".join(pkg for _, pkg in required))
PY

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
