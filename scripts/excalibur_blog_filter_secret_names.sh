#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.
# Usage (before git commit if hooks abort with "invalid variable name"):
#   eval "$(python3 - <<'PY'
# import os,re
# names=os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES","")
# keep=[n.strip() for n in names.split(",") if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", n.strip())]
# print("export CLOUD_AGENT_INJECTED_SECRET_NAMES=%r" % (",".join(keep),))
# PY
# )"
#
# Prefer fixing Cloud Dashboard so URL values are never listed as secret *names*.
set -euo pipefail

RAW="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$RAW" ]]; then
  echo "CLOUD_AGENT_INJECTED_SECRET_NAMES="
  exit 0
fi

KEEP=()
IFS=',' read -ra PARTS <<< "$RAW"
for name in "${PARTS[@]}"; do
  name="${name#"${name%%[![:space:]]*}"}"
  name="${name%"${name##*[![:space:]]}"}"
  if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    KEEP+=("$name")
  else
    echo "WARN skip non-identifier secret name: ${name:0:48}" >&2
  fi
done

JOINED=$(IFS=,; echo "${KEEP[*]}")
echo "CLOUD_AGENT_INJECTED_SECRET_NAMES=${JOINED}"
