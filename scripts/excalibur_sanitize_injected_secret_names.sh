#!/usr/bin/env bash
# Sanitize CLOUD_AGENT_INJECTED_SECRET_NAMES before git commit / Cursor pre-commit.cursor.
# Invalid shell identifiers break bash ${!SECRET_NAME} in the secrets scanner.
set -euo pipefail

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [ -z "$raw" ]; then
  echo "OK CLOUD_AGENT_INJECTED_SECRET_NAMES empty"
  exit 0
fi

filtered=""
IFS=',' read -ra names <<< "$raw"
for name in "${names[@]}"; do
  name="${name#"${name%%[![:space:]]*}"}"
  name="${name%"${name##*[![:space:]]}"}"
  if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    if [ -z "$filtered" ]; then
      filtered="$name"
    else
      filtered+=",$name"
    fi
  else
    echo "WARN skip non-identifier secret name: ${name:0:48}" >&2
  fi
done

export CLOUD_AGENT_INJECTED_SECRET_NAMES="$filtered"
echo "OK CLOUD_AGENT_INJECTED_SECRET_NAMES sanitized count=$(awk -F',' '{print NF}' <<<"${filtered:-}")"
# Print an export line agents can eval:
echo "export CLOUD_AGENT_INJECTED_SECRET_NAMES=$(printf '%q' "$filtered")"
