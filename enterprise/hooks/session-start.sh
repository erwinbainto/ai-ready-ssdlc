#!/usr/bin/env bash
# Stamps session identity into the trace so a later finding can be attributed.
# Referenced from settings as "$CLAUDE_PROJECT_DIR"/hooks/session-start.sh
set -euo pipefail

APP="${RRD_APP_NAME:-<UNSET_APP_NAME>}"
HARNESS_VERSION="${RRD_HARNESS_VERSION:-<UNSET_VERSION>}"

cat <<EOF
Session context for this engagement:
- application: ${APP}
- harness version: ${HARNESS_VERSION}
- posture: read-only. Write, commit, merge and deploy are denied by policy.
- receipts: claims about tests or builds must come from the declared command contract.
EOF
