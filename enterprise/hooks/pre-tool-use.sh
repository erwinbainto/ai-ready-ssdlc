#!/usr/bin/env bash
# Logs every tool call and records write-class attempts for the audit trail.
# Enforcement is the permission deny list, not this script. This is the audit trail.
set -euo pipefail

LOG_DIR="${SSDLC_EVIDENCE_DIR:-${HOME}/.ssdlc-harness-evidence}"
mkdir -p "${LOG_DIR}"

PAYLOAD="$(cat || true)"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

printf '%s %s\n' "${TS}" "${PAYLOAD}" >> "${LOG_DIR}/tool-calls.log"

if printf '%s' "${PAYLOAD}" | grep -Eqi '"(Write|Edit|NotebookEdit)"|git (commit|push|merge)'; then
  printf '%s WRITE_ATTEMPT %s\n' "${TS}" "${PAYLOAD}" >> "${LOG_DIR}/write-attempts.log"
fi

exit 0
