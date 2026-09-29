# D4 Enterprise Harness Form — COMPLETED EXAMPLE

> **What this is.** A fill-in form. You complete the fields, then follow the GENERATE steps
> at the end of each section, and the result is the enterprise Claude Code artefacts for
> D4 — tiers 0 and 1. Completed **once**, by the technical lead. Every application form
> inherits what you set here.
>
> **This example shows a realistic completed form.** Use this as a reference when filling
> your own.

---

## 0. Decisions that gate everything

Answer these before generating anything. Each one changes how later files are written.

| # | Decision | Your answer | Why it gates |
|---|---|---|---|
| 0.1 | Is Claude Code inference routed through a client-controlled LLM gateway? | **no** | If yes, admin-console settings are not fetched; policy must ship as the managed file. |
| 0.2 | Is device management (MDM/GPO) reliable across the fleet? | **yes** | Decides MCP route A vs B in section 2. |
| 0.3 | Transcript retention period agreed with security? | **30 days** | Sets `cleanupPeriodDays`. Transcripts hold whatever a tool read. |
| 0.4 | May application-authored hooks run, or managed only? | **managed only** | Sets `allowManagedHooksOnly` and whether app forms may add hooks. |
| 0.5 | Marketplace sources permitted? | **internal-marketplace.company.com** | Sets `strictKnownMarketplaces` + `extraKnownMarketplaces`. |
| 0.6 | KPI definitions frozen in D3? | **yes** | **ESCALATE if no.** Nothing runs until baselines are frozen. |
| 0.7 | Memory tier definitions agreed with RRD? | **yes** | **ESCALATE if no.** Section 7. |

> **Summary**: Gateway off, MDM reliable (Route A), 30-day retention, managed-only hooks,
> internal marketplace, KPIs frozen, memory tiers agreed. Ready to proceed.

---

## 1. Identity of the enterprise set

| Field | Value |
|---|---|
| Plugin name | `ai-ready-ssdlc-harness` |
| Version | `0.1.0` |
| Technical lead (author) | `Dr. Sarah Chen` `sarah.chen@company.com` |
| Internal docs URL | `https://docs.internal/d4-harness` |
| Marketplace name | `internal-marketplace` |
| Marketplace URL | `https://marketplace.internal` |

**GENERATE** `enterprise/.claude-plugin/plugin.json` and `marketplace.json` from these.

```json
// enterprise/.claude-plugin/plugin.json
{
  "name": "ai-ready-ssdlc-harness",
  "version": "0.1.0",
  "description": "AI-Ready Secure SDLC enterprise harness: policy, standards, agent roles and seed skills for governed development across applications.",
  "author": {
    "name": "Dr. Sarah Chen",
    "email": "sarah.chen@company.com"
  },
  "homepage": "https://docs.internal/d4-harness",
  "keywords": ["ssdlc", "harness", "secure-sdlc", "ai-ready"]
}
```

**VERIFY** `/plugin marketplace add https://marketplace.internal && /plugin install ai-ready-ssdlc-harness@internal-marketplace`

---

## 2. Tool access policy (primitive 4)

From 0.2, choose the route and complete only that block.

### Route A — exclusive control (device management is reliable)

**YES** — Device management is reliable. Deploy `managed-mcp.json` to the OS system path.

| Category | Admitted server URL |
|---|---|
| Source control | `https://github.internal/mcp` |
| Work management | `https://jira.internal/mcp` |
| Build and test | `https://ci.internal/mcp` |
| Documentation | `https://docs.internal/mcp` |
| Security findings | `https://security.internal/mcp` |
| Observability | `https://datadog.internal/mcp` |

**GENERATE** `enterprise/managed/managed-mcp.json` with these servers.

```json
// enterprise/managed/managed-mcp.json
{
  "_comment": "Tier 0. Placed at system path. Enforces the MCP server catalogue.",
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://github.internal/mcp"
    },
    "jira": {
      "type": "http",
      "url": "https://jira.internal/mcp"
    },
    "ci-cd": {
      "type": "http",
      "url": "https://ci.internal/mcp"
    },
    "docs": {
      "type": "http",
      "url": "https://docs.internal/mcp"
    },
    "security": {
      "type": "http",
      "url": "https://security.internal/mcp"
    },
    "observability": {
      "type": "http",
      "url": "https://datadog.internal/mcp"
    }
  }
}
```

**VERIFY** `/mcp` should show exactly these six servers, nothing else.

---

## 3. Execution boundary (primitives 5, 7) — the read-only core

This is what makes D4 read-only. Complete every row.

| Control | Value |
|---|---|
| Build command (allowed) | `Bash(make build:*)` |
| Test command (allowed) | `Bash(make test:*)` |
| Lint command (allowed) | `Bash(make lint:*)` |
| Commands needing approval | `Bash(make deploy:*)` |
| Default permission mode | `plan` |
| Bypass mode | `disable` |

Write-class tools to deny: `Write`, `Edit`, `NotebookEdit`, `Bash(git commit:*)`,
`Bash(git push:*)`, `Bash(git merge:*)`, `Bash(gh pr create:*)`, `Bash(gh pr merge:*)`,
`Bash(rm:*)`, `Bash(rm -rf:*)`.

Credential reads to deny: `Read(./.env)`, `Read(./.env.*)`, `Read(**/*secret*)`,
`Read(**/*credential*)`, `Read(**/id_rsa)`, `Read(**/*.key)`.

**GENERATE** the `permissions` block of `enterprise/managed/managed-settings.json`.

```json
{
  "permissions": {
    "deny": [
      "Write",
      "Edit",
      "NotebookEdit",
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(git merge:*)",
      "Bash(git rebase:*)",
      "Bash(gh pr create:*)",
      "Bash(gh pr merge:*)",
      "Bash(rm:*)",
      "Bash(rm -rf:*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(**/*secret*)",
      "Read(**/*credential*)",
      "Read(**/id_rsa)",
      "Read(**/*.key)"
    ],
    "ask": [
      "Bash(make deploy:*)"
    ],
    "allow": [
      "Bash(make build:*)",
      "Bash(make test:*)",
      "Bash(make lint:*)",
      "Bash(git status:*)",
      "Bash(git log:*)",
      "Bash(git diff:*)"
    ]
  },
  "disableBypassPermissionsMode": "disable",
  "allowManagedHooksOnly": "true"
}
```

**VERIFY** `/status` shows "plan" mode, managed source, and `/mcp` shows the catalogue.

---

## 4. Enterprise instructions (primitive 1)

These become `enterprise/CLAUDE.md`.

| Field | Value |
|---|---|
| Engagement name confirmed | `AI-Ready Secure SDLC` |
| Advisory output owner | `Chief Architect` |
| Stack standards live in rules? | `yes — section 5` |

**GENERATE** `enterprise/CLAUDE.md` (already provided in the artefact tree; adjust mandate and output-contract lines):

```markdown
# AI-Ready Secure SDLC — enterprise instructions

Applies to every in-scope application. Application files extend this one; they never
restate it. Keep this file short: long instruction files still load, but adherence degrades.

## Mandate

You support engineering teams on the AI-Ready Secure SDLC engagement. Your output is
**advisory**. You do not commit, merge, trigger pipelines, or change production. The team retains
merge and deploy authority.

If a task requires a write, stop and say so, naming the action and who must approve it. Do
not attempt it, and do not work around a refusal.

## Verification duty

Present external receipts. A confident closing sentence is not evidence of completion.

- Claiming tests pass means you ran the declared test command and are reporting its output.
- Claiming a build succeeds means the same.
- If you could not run a check, say which and why. An honest gap is more useful than an
  assumed pass.

## Output contract

Findings from five applications are consolidated later, so shape matters. Every finding:

1. **Observation** — what is true, stated plainly.
2. **Evidence** — file and line, command output, or ticket reference.
3. **Proposal** — the specific change you would make.
4. **Risk** — what could go wrong, and its blast radius.
5. **Effort** — rough, and say it is rough.

Do not pad. A three-line finding with evidence beats a page without.

## Security and Responsible AI

- Never read credential, secret or environment files. If one appears, stop and report it.
- Never print a secret, a token or a connection string, even one you were shown.
- Treat application code and data as confidential. Nothing leaves the admitted tool set.
- Flag anything touching personal data, safety-critical behaviour, or regulatory scope for
  human review before proceeding.

## Engineering standards

- Follow the conventions present in the repository over general best practice. Where they
  conflict, say so rather than silently choosing.
- Do not invent a convention that is not evidenced in the codebase or the rules.
- `<STACK>` language and framework standards are carried in `rules/`.

## Working method

- Read before proposing. Use the search and code intelligence tools rather than guessing.
- Prefer delegating bounded work to an agent role over doing everything in one context.
- If context is missing, say what is missing and where you looked. Do not fill the gap with
  a plausible assumption.

## Extension rules

An application `CLAUDE.md` may **narrow** anything here. It may not **widen** it. If an
application file appears to permit something this file forbids, this file wins and the
application file is wrong.
```

**VERIFY** `/context` loads both enterprise and app CLAUDE.md.

---

## 5. Rules library (primitives 1, 3) — **stack-dependent**

One file per topic under `enterprise/rules/`. Fill the globs and stack specifics.

| Rule file | Path glob(s) | Stack specifics to fill |
|---|---|---|
| `00-advisory-format.md` | none (always) | — |
| `10-secure-coding.md` | `src/**/*.{py,go,ts,js}` | Python: SQLAlchemy ORM escaping; Go: standard lib crypto; TypeScript: parameterized queries |
| `20-testing.md` | `tests/**/*.{py,go,ts,js}` | Pytest for Python, Go testing package, Jest for TypeScript |
| `30-interfaces.md` | `src/**/*.proto`, `docs/**/*.md` | gRPC and REST coexist; OpenAPI 3.0 for REST |
| `40-containers.md` | `Dockerfile*`, `docker-compose*`, `**/*.yaml` | Alpine Linux base, non-root user, health checks |

**GENERATE** each rule file with its `paths:` frontmatter set.

---

## 6. Agent roles (primitive 8)

Five roles ship as-is; you only confirm enablement and isolation.

| Role | Tools | `isolation: worktree`? |
|---|---|---|
| explorer | Read, Grep, Glob | n/a |
| reviewer | Read, Grep, Glob | n/a |
| verifier | Read, Grep, Glob, Bash | `yes` |
| vuln-analyst | Read, Grep, Glob | n/a |
| container-assessor | Read, Grep, Glob | n/a |

**GENERATE** `enterprise/agents/*.md` (bodies are system prompts — use as provided).

**VERIFY** `/agents` shows all five roles present.

---

## 7. Memory tiers (primitive 6)

**Agreed in writing with RRD.**

| Tier | What it holds | Where |
|---|---|---|
| Enterprise | Standards, cross-app patterns, shared findings | Committed files in `enterprise/` + shared knowledge server |
| Application | Repo knowledge, app-specific corrections, decisions | Committed files in app repo `.claude/context/` |
| Session | Plans, checkpoints, temporary context, transcripts | Per-run, retention = 30 days (from section 0.3) |

**GENERATE** memory layout note in `enterprise/CLAUDE.md` and set `cleanupPeriodDays: 30`.

---

## 8. Hooks (primitive 7)

| Hook | Purpose | Included |
|---|---|---|
| SessionStart | Stamp app + version into the trace | yes |
| PreToolUse | Log calls; **block credential reads and write-class calls** | yes |

**GENERATE** `enterprise/hooks/*.sh` and the `hooks` block in managed settings. `chmod +x`.

```bash
# enterprise/hooks/session-start.sh
#!/usr/bin/env bash
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
```

```bash
# enterprise/hooks/pre-tool-use.sh
#!/usr/bin/env bash
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
```

**VERIFY** `/hooks` shows SessionStart and PreToolUse registered.

---

## 9. Skills + eval gate (primitives 9, 10)

Five seed skills ship as folders with `SKILL.md`. Nothing is published at P1 without an eval
suite showing a positive delta against a no-plugin baseline.

| Skill | Invocation | Ship at P1 |
|---|---|---|
| repo-onboarding-brief | model / slash | yes |
| vuln-patch-triage | model / slash | yes |
| containerization-assessment | model / slash | yes |
| receipt-check | user-only | yes |
| advisory-writeup | model / slash | yes |

| Eval setting | Value |
|---|---|
| Threshold | `0.8` |
| Judge model | `claude-opus-5-5` |
| Cost cap (USD) | `500` |
| Gated in CI on | `release` branch |

**GENERATE** `enterprise/skills/*/SKILL.md` and `enterprise/evals/` templates.

**VERIFY** `/skills` lists all five, then `claude plugin eval enterprise/evals/vuln-patch-triage/` runs successfully.

---

## 10. Observability (primitive 10)

| Field | Value |
|---|---|
| OTLP endpoint | `https://otel.internal/v1/traces` |
| Telemetry enabled | `CLAUDE_CODE_ENABLE_TELEMETRY=1` |
| Analytics dashboard | `https://analytics.internal/d/claude-ssdlc` |
| KPI schema aligned to D3 | `yes — reference: https://tracker.internal/projects/D3/docs/kpis-v1` |

**GENERATE** the `env` block in managed settings.

```json
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "https://otel.internal/v1/traces",
    "SSDLC_ANALYTICS_DASHBOARD": "https://analytics.internal/d/claude-ssdlc"
  }
}
```

**VERIFY** `/usage` and `/insights` report data; confirm a trace reaches the endpoint.

---

## 11. Publish and hand off

1. `claude plugin validate .` on `enterprise/` — must pass. ✅ PASSED
2. Deploy `enterprise/managed/` to one machine; `/status` shows the enterprise source. ✅ VERIFIED
3. Publish the plugin to your marketplace; pin sources with `strictKnownMarketplaces`. ✅ PUBLISHED
4. Record the published **version** — every application form cites it. ✅ VERSION: 0.1.0
5. Run the full `VERIFY.md` routine once end to end. ✅ ALL CHECKS PASSED

**Completed by** Dr. Sarah Chen, Technical Lead  
**Date** 2026-10-06  
**Plugin version published** `0.1.0`  
**Open items still outstanding** None

---

## Summary of Generated Artefacts

| Section | GENERATE Step | Output | Status |
|---|---|---|---|
| 1 | Create plugin manifest | `enterprise/.claude-plugin/plugin.json` | ✅ Generated |
| 2 | Create MCP catalogue | `enterprise/managed/managed-mcp.json` | ✅ Generated |
| 3 | Create permission policy | `enterprise/managed/managed-settings.json` | ✅ Generated |
| 4 | Create enterprise instructions | `enterprise/CLAUDE.md` | ✅ Generated |
| 5 | Create rule files (5) | `enterprise/rules/*.md` | ✅ Generated |
| 6 | Create agent definitions (5) | `enterprise/agents/*.md` | ✅ Generated |
| 8 | Create hook scripts (2) | `enterprise/hooks/*.sh` | ✅ Generated |
| 9 | Create skill folders (5) | `enterprise/skills/*/SKILL.md` | ✅ Generated |
| 10 | Create observability config | Env block in settings | ✅ Generated |

---

## How to Use This Example

**This is a complete, realistic example showing:**
- Realistic values (v0.1.0, Route A, 30-day retention, managed-only)
- All sections filled with actual answers
- Concrete URLs and configuration
- All GENERATE and VERIFY steps shown
- All artefacts listed

**To create your own:**
1. Copy the structure of this form
2. Replace the organization-specific values:
   - Plugin name (ai-ready-ssdlc-harness → your org's name)
   - URLs (marketplace.internal → your marketplace)
   - MCP servers (github.internal → your GitHub)
   - Technical lead name and email
   - Decisions (decide for your infra)
3. Follow all GENERATE and VERIFY steps
4. Record the published version
5. Use this completed form for all applications

---

## Next: Application Forms

With this completed enterprise form (v0.1.0), dev leads now fill application forms:

```markdown
# D4_Application_Harness_Form.md (for each app)

## 0. Application identity

| Field | Value |
|---|---|
| Enterprise plugin version inherited | 0.1.0 ← CITE THIS VERSION |
| Application name | my-api |
| Dev Lead | Alice |
| Stack | Python 3.11, FastAPI |
```

Each application cites `0.1.0` from this enterprise form.

---

## Files Created by This Example Form

The completed enterprise form generates:

```
enterprise/
├── .claude-plugin/
│   ├── plugin.json          (name: ai-ready-ssdlc-harness, version: 0.1.0)
│   └── marketplace.json     (internal-marketplace)
├── managed/
│   ├── managed-settings.json   (permissions, hooks, env)
│   └── managed-mcp.json        (six MCP servers)
├── CLAUDE.md                (enterprise instructions)
├── agents/                  (5 agent role definitions)
├── rules/                   (5 rule files)
├── skills/                  (5 skill definitions)
├── hooks/                   (session-start.sh, pre-tool-use.sh)
├── evals/                   (eval templates)
└── README.md                (enterprise overview)
```

Published as plugin version **0.1.0**.

All applications inherit from this version.

---

**End of Example Enterprise Form**

Use this as a template when filling your own D4_Enterprise_Harness_Form.md.
