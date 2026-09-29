# D4 Application Harness Form — COMPLETED EXAMPLE

> **What this is.** A fill-in form, completed **once per application** by the FDE with the
> Dev Lead. Completing it produces the tier-3 Claude Code artefacts for that application
> and the evidence for its **D4 Application Instance Record**.
>
> **Prerequisite.** The enterprise form is done and the plugin is published. You will cite
> its version. Do not start until you can.
>
> **This example shows a realistic completed form for one application.**
> Use this as a template when filling your own application forms.

---

## 0. Application identity and prerequisites

| Field | Value |
|---|---|
| Application name | `payment-api` |
| Enterprise plugin version inherited | `0.1.0` |
| RRD Dev Lead (co-author) | `Alice Johnson` |
| RRD application owner (signs autonomy) | `David Martinez` |
| Autonomy target from D2 (current → target) | `L0→L1` |
| D1 readiness summary + open blockers | `Codebase well-structured with 85% test coverage. No blockers. Ready for L1.` |
| D3 frozen KPIs for this app | `Reference: https://tracker.internal/projects/PAYMENTS/docs/kpis-v1. Frozen 2026-09-28. (1) Uptime: 99.99%, (2) Latency p99 < 200ms, (3) Error rate < 0.1%` |
| Repository set, primary marked | `Primary: github.com/company/payment-api. Secondary: github.com/company/payment-analytics (read-only)` |
| Languages / frameworks in scope | `Python 3.11, FastAPI 0.104, SQLAlchemy 2.0, PostgreSQL 15` |

**Install the plugin first** (do not copy its files):
```
/plugin marketplace add https://marketplace.internal
/plugin install ai-ready-ssdlc-harness@internal-marketplace
```

✅ **VERIFY** `/plugin list ai-ready-ssdlc-harness` shows version 0.1.0

---

## 1. Application instructions (primitive 1) → `CLAUDE.md`

| Field | Value |
|---|---|
| One-line business purpose | `REST API for processing and settling payments securely` |
| Entry points (area / path / role) | `main.py (FastAPI app entry), src/api/routes/ (endpoint handlers), src/services/ (business logic)` |
| Generated paths — never hand-edit | `src/generated/protos/ (Protocol Buffers), docs/openapi.json (auto-generated from decorators)` |
| Named RRD approver for gated actions | `payments-lead@company.com (David Martinez)` |
| Local conventions (each with reason) | `1. Use FastAPI depends() for DI - reduces coupling. 2. All SQLAlchemy models inherit from Base - consistency. 3. Secrets in .env.local never committed - security.` |
| Rules narrowed from enterprise | `None - inherits all enterprise rules and adds specific denies in section 5.` |

**GENERATE** `payment-api/CLAUDE.md`:

```markdown
# payment-api

Extends the AI-Ready Secure SDLC enterprise harness instructions. Everything in the 
enterprise set applies here and is not restated.

## What this application is

REST API for processing and settling payments securely. Accepts payment requests from
upstream systems, validates, routes to settlement providers, and records outcomes. Critical
for financial workflows. PCI-DSS compliance required.

## Repository map

| Area | Path | Responsibility |
|---|---|---|
| FastAPI app | `src/main.py` | ASGI entry point, middleware setup, exception handlers |
| API routes | `src/api/routes/` | Endpoint definitions (POST /payment, GET /status, etc.) |
| Business logic | `src/services/` | PaymentProcessor, SettlementClient, AuditLog |
| Data models | `src/models/` | SQLAlchemy ORM models, database schema |
| Tests | `tests/` | Pytest suite, fixtures, integration tests |
| Generated | `src/generated/protos/` | **Generated. Never hand-edit.** Protobuf Python bindings |
| API docs | `docs/openapi.json` | **Generated. Never hand-edit.** OpenAPI 3.0 spec |

## Commands

The declared command contract is in `.claude/context/commands.md`. Use those commands and
no others when producing receipts.

## Domain terms

See `.claude/context/glossary.md` for terms an outsider would misread.

## Hazards

See `.claude/context/hazards.md`. Read it before proposing changes in those areas.

## Local conventions

Where this application departs from the enterprise standard, each with a reason:

- **Use FastAPI depends() for DI** — reduces coupling, improves testability
- **All SQLAlchemy models inherit from Base** — ensures consistency, enables reflection
- **Secrets in .env.local never committed** — PCI-DSS compliance, security requirement

## Narrowed rules

Where this application is stricter than the enterprise set:

- **Additional credential denies** — Read(src/payment/merchant-keys/), Read(config/api-keys/), 
  Read(db-credentials/) — financial data protection

## Write boundary

Read-only. Write, commit, merge, pipeline trigger and deployment are denied by policy.
Gated actions escalate to `payments-lead@company.com` (David Martinez).
```

**VERIFY** `/context` shows both enterprise and app instructions loaded.

---

## 2. The knowledge connection (primitives 2, 3) → `.claude/context/`

**CRITICAL:** Draft with explorer, then dev lead corrects it. A draft nobody corrected is worse than nothing.

### 2a. `architecture.md`

| Field | Value |
|---|---|
| What it is / how it fits | `REST API service. Receives payment requests from web/mobile/batch systems. Routes to Stripe/Square settlement providers. Records all transactions in PostgreSQL for audit and reconciliation.` |
| Key components + responsibilities | `PaymentProcessor (validate + transform requests), SettlementRouter (route to provider), AuditLogger (immutable record), ErrorHandler (transaction rollback on failure), RateLimiter (DDoS protection)` |
| Interfaces (name / type / consumers / contract) | `POST /payment (REST, JSON request/response), Consumer: web frontend, mobile app. Contract: docs/openapi.json. Also: POST /webhook (Stripe webhooks), Consumer: Stripe. Contract: https://stripe.com/docs/webhooks.` |
| Data and state ownership | `Owns: payment transactions, settlement records, audit logs (PostgreSQL). Reads: merchant config (central KV store). Writes: payment_events queue (Kafka) for downstream consumption.` |
| **Unowned or unclear components** | `Settlement provider integration: Stripe client is owned by Stripe, not us (external dependency). Webhook signature validation: delegated to Stripe SDK (Stripe owns verification logic).` |

### 2b. `commands.md` — the command contract

| Purpose | Command | Expected | Typical duration | Passes today? |
|---|---|---|---|---|
| Build | `make build` | exit 0, creates `dist/app.whl` | 30s | yes |
| Test | `make test` | exit 0, pytest runs, coverage > 85% | 2m | yes |
| Lint | `make lint` | exit 0, no style issues | 15s | yes |
| Type check | `make type-check` | exit 0, no type errors (mypy) | 20s | yes |

**Baseline** (pre-existing failures):
```
Currently failing: None. All commands pass.
```

### 2c. `hazards.md` — do-not-touch, incidents, surprising behaviour

| Do not touch without review | Path | Why | Who to ask |
|---|---|---|---|
| Settlement routing logic | `src/services/settlement_router.py` | Incorrect routing loses payments | `Alice Johnson` |
| Transaction rollback on failure | `src/services/payment_processor.py` lines 45-67 | Must be atomic or balances corrupt | `Alice Johnson` |
| Webhook signature validation | `src/api/routes/webhooks.py` lines 12-25 | If skipped, fake settlements are accepted | `David Martinez` |

**Incident history:**

| What happened | Area | Lesson |
|---|---|---|
| 2024-03-15: Settlement routing sent payment to wrong provider for 2 hours | `settlement_router.py` | Test all routing paths in CI/CD |
| 2024-05-22: Webhook signature check disabled for testing, left enabled in prod | `webhooks.py` | Never disable security in non-test code |

**Surprising behaviour:**

- **Idempotency key handling**: Sending the same payment twice with same idempotency key returns cached result, not duplicate charge. This is correct but not obvious.
- **Retry logic**: Failed settlements retry up to 3 times with exponential backoff, but only within 24 hours. After 24h, manual intervention required.
- **Rate limiting**: Per-merchant, not per-API-key. High-volume merchant hitting rate limit affects all their payments, not just one API key.

**Known debt:**

- Settlement provider abstraction is payment-provider-specific, not generic. Would take 2 weeks to genericize. Deferring.
- Webhook retry logic is in Stripe docs but not in our code. Relying on Stripe's retry behavior.
- Audit log currently written synchronously; should be async for performance. Deferring to L2.

### 2d. `glossary.md` — only terms with local meaning

| Term | Means here | Does not mean |
|---|---|---|
| Settlement | Confirmed transfer of money to merchant account | The payment itself (that's the "transaction") |
| Idempotency key | Client-supplied token to ensure exactly-once delivery | A random request ID |
| Webhook | HTTP callback from Stripe when settlement completes | A payment request |
| Rollback | Transaction abort, all-or-nothing semantics | Payment cancellation (that's a separate flow) |

**Overloaded terms:**

- **"Transaction"**: In this codebase means payment transaction (amount + merchant). In database terms means SQL transaction (ACID unit). Context determines meaning.
- **"Settlement"**: Means confirmed transfer (after our validation). In accounting means final reconciliation (different). Always say "payment settlement" vs. "monthly settlement" to disambiguate.

---

## 3. Sources indexed (primitive 2)

| Source | Location | Index method | Owner | Verification Q + answer |
|---|---|---|---|---|
| Source code | `github.com/company/payment-api` | README.md file listing | Alice Johnson | Q: "Where's the payment router?" A: "src/services/settlement_router.py" ✅ Found |
| Specs / contracts | `docs/openapi.json` (auto-generated) | OpenAPI 3.0 standard | Alice Johnson | Q: "What's the POST /payment request schema?" A: (Shows schema in OpenAPI) ✅ Verified |
| Tests | `tests/` pytest suite | `make test` runs all | Alice Johnson | Q: "What's the settlement routing test?" A: "tests/test_settlement_router.py::test_route_to_correct_provider" ✅ Passes |
| ADRs / decisions | `docs/adr/` directory | Markdown files, numbered | Alice Johnson | Q: "Why use FastAPI?" A: "ADR-001: FastAPI chosen for async support and built-in OpenAPI" ✅ Documented |
| Docs | `README.md`, `docs/` folder | Markdown, human-readable | Alice Johnson | Q: "How to setup locally?" A: README section "Development Setup" ✅ Accurate |
| Manifests | `k8s/` directory (if containerized) | Kubernetes YAML files | DevOps team | Q: "What's the pod memory limit?" A: "k8s/deployment.yaml: resources.limits.memory=1Gi" ✅ Set |
| Incidents | Jira project `PAYMENTS` | Issue tracker, tagged "incident" | David Martinez | Q: "Any recent payment incidents?" A: "PAYMENTS-1234: 2024-03-15 settlement routing bug" ✅ Linked above |
| Metrics / logs | Datadog dashboard `payment-api-production` | URL: https://datadog.internal/d/payment-api-prod | DevOps team | Q: "What's current error rate?" A: Dashboard shows 0.08% (OK) ✅ Visible |
| Tickets | Jira project `PAYMENTS` | Backlog, sprint board | Alice Johnson | Q: "What's in progress?" A: "PAYMENTS-1450: Add webhook retry logic" ✅ Current sprint |
| Vulnerability data | Dependabot alerts, Snyk scans | GitHub security tab | Alice Johnson | Q: "Any known vulns?" A: "No critical/high vulns. One medium in FastAPI (patch available)" ✅ Checked |

> "Indexed" is not "delivered". The verification answer is the evidence indexing worked.

---

## 4. Server bindings (primitive 4) → `.mcp.json`

Bind only from the admitted catalogue. An unadmitted server will not load.

| Category | Bound? | Read scope | First successful call logged |
|---|---|---|---|
| Source control (GitHub) | `yes` | `github.com/company/payment-api` | 2026-09-28T14:32:05Z - Fetched latest commit |
| Work management (Jira) | `yes` | `PAYMENTS` project | 2026-09-28T14:33:12Z - Listed tickets in sprint |
| Build and test (CI/CD) | `yes` | Triggers for payment-api repo | 2026-09-28T14:34:22Z - Fetched last build result |
| Documentation (internal wiki) | `no` | Not needed for this app | — |
| Security findings (Security scanner) | `yes` | Security scan results for this repo | 2026-09-28T14:35:50Z - Fetched vulnerability scan |
| Observability (Datadog) | `yes` | payment-api metrics and logs | 2026-09-28T14:36:33Z - Fetched error rate metric |

**GENERATE** `payment-api/.mcp.json`:

```json
{
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

**VERIFY** `/mcp` shows exactly these five servers (no documentation server).

---

## 5. Execution environment (primitive 5) → `.claude/settings.json` + the write test

| Field | Value |
|---|---|
| Repository mount / mode | `read-only. Mounted at /workspace/payment-api` |
| Worktree isolation | `yes` |
| Service identity + scope (non-human) | `Claude Code session, scoped to payment-api repo only` |
| Network egress permitted | `yes (to GitHub, Jira, CI/CD, Security scanner, Datadog MCP endpoints)` |
| Permissions narrowed for this app | `Read(src/payment/merchant-keys/) denied - PCI compliance, Read(config/api-keys/) denied - credential protection, Read(db-credentials/) denied - database security` |
| Untracked build deps → `.worktreeinclude` | `.env.local (runtime config, never committed), venv/ (Python virtual env), .mypy_cache/ (type checker cache)` |

### The write-attempt test — the one row that proves the deliverable

| Field | Value |
|---|---|
| What you attempted | `Edit src/main.py line 42 to change FastAPI app initialization` |
| How it was refused | `Write denied by managed policy (core deny list prohibits Write tool)` |
| Trace reference + date | `2026-09-28T15:42:33Z-write-attempt-001. Policy source: enterprise managed-settings.json, Write in deny list.` |
| Verified with Dev Lead | `2026-09-28 - Alice Johnson confirmed refusal, boundary holds.` |

**GENERATE** `payment-api/.claude/settings.json` and `.worktreeinclude`:

```json
{
  "_comment_scope": "Tier 3. Narrows the enterprise policy for this application.",
  "permissions": {
    "deny": [
      "Read(src/payment/merchant-keys/)",
      "Read(config/api-keys/)",
      "Read(db-credentials/)"
    ],
    "allow": [
      "Bash(make build:*)",
      "Bash(make test:*)",
      "Bash(make lint:*)",
      "Bash(make type-check:*)"
    ]
  },
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  },
  "env": {
    "RRD_APP_NAME": "payment-api",
    "RRD_HARNESS_VERSION": "0.1.0"
  }
}
```

```
# payment-api/.worktreeinclude
.env.local
venv/
.mypy_cache/
```

**VERIFY** `/status` shows narrowed permissions and app name "payment-api".

---

## 6. Roles, memory, hooks (primitives 8, 6, 7)

| Role | Enabled | Why not, if disabled |
|---|---|---|
| explorer / reviewer | `yes` | — |
| verifier | `yes` | Need to verify test results, build success |
| vuln-analyst | `yes` | Stripe SDK has dependencies; need patch analysis |
| container-assessor | `no` | Not containerized yet. Migration to L2. |

**Memory:** App tier location `.claude/context/`; session retention 30 days (per enterprise); evidence vault `$HOME/.ssdlc-harness-evidence/` (enterprise-managed).

**Hooks:** Pod hooks enabled only if enterprise section 0.4 = "pod allowed". **Current: "managed only".** So no app-specific hooks. Only enterprise hooks run (SessionStart, PreToolUse).

**VERIFY** `/agents` shows explorer, reviewer, verifier, vuln-analyst enabled. `/hooks` shows enterprise hooks only, no app-specific.

---

## 7. Capability candidates (primitive 9)

Log as real patterns appear. Nothing is published here — publication is WP2 / D11.

| Candidate | Observed need | Invocation | Owner | Logged |
|---|---|---|---|---|
| `payment-settlement-edge-case-detection` | Detecting when settlement could fail (invalid merchant, insufficient balance) | Model | Alice Johnson | 2026-09-28 |
| `pci-dss-compliance-checker` | Checking code paths for credential exposure | Model | Alice Johnson | 2026-09-28 |

---

## 8. Verification + evidence (primitive 10)

| Field | Value |
|---|---|
| Declared commands runnable by harness | `yes` |
| Receipt sample reference | `Build receipt: 2026-09-28T15:44:22Z, make build exit 0, created dist/app.whl. Test receipt: 2026-09-28T15:45:30Z, make test exit 0, pytest 127 passed, coverage 87%.` |
| Full trace export reference | `2026-09-28T15:42-15:50_payment-api_session.jsonl available in $HOME/.ssdlc-harness-evidence/` |
| Cost + latency captured | `yes` |
| D3 KPIs instrumented + verified vs definitions | `2026-09-28 - All three KPIs instrumented. Uptime: 99.99% (pass). Latency p99: 145ms (pass, target 200ms). Error rate: 0.08% (pass, target 0.1%).` |

**VERIFY** `/usage` shows token usage for this session. `/insights` shows cost estimate. Export trace with `jq '.[]' $HOME/.ssdlc-harness-evidence/tool-calls.log | head -5`.

---

## 9. Extension register

Every difference from the inherited harness, against the five mechanisms.

| Mechanism | What this app did | Reason | Approved by |
|---|---|---|---|
| Add | `None` | Inherits all enterprise artefacts | FDE |
| Narrow | `Added three credential read denies: src/payment/merchant-keys/, config/api-keys/, db-credentials/` | PCI-DSS compliance requires stricter credential protection | FDE |
| Bind | `Five servers from catalogue: GitHub, Jira, CI/CD, Security, Datadog. Skipped Documentation.` | App doesn't use internal wiki | FDE |
| Implement (a contract) | `Command contract in .claude/context/commands.md` | Declared build/test/lint/type-check commands | FDE |
| Change request (widens/shared) | `None` | No changes needed to enterprise policy | FDE |

> Narrow yes, widen no. A local allowlist cannot defeat a managed deny.

---

## 10. D7 enablement environment (primitives 5, 9)

| Field | Value |
|---|---|
| Read-only sandbox prepared | `Lab-env: https://ci.internal/payment-api-lab. Prepared 2026-09-28.` |
| Practitioners from this pod for D7 | `3 engineers: Alice Johnson, Bob Chen, Carol Lee` |
| Lab exercises drafted + verified end to end | `yes - Exercise 1: Fix broken settlement router (intentional bug), Exercise 2: Add new payment method, Exercise 3: Security audit of credential handling. All verified.` |
| Facilitator (FDE) | `Sarah Chen (sarah.chen@company.com)` |

> Labs run against *this* application, not a demo repo.

---

## 11. Close-out

Exit checklist — all must be true:

- [x] Enterprise plugin installed, version cited (0.1.0)
- [x] Context pack complete and Dev-Lead-corrected (Alice Johnson reviewed and approved 2026-09-28)
- [x] `CLAUDE.md` references enterprise, duplicates nothing
- [x] Servers bound from catalogue, each with a logged call
- [x] Write-attempt test run, refusal + trace captured (2026-09-28T15:42:33Z)
- [x] Every indexed source has a verification answer
- [x] D3 KPIs instrumented and verified before first run
- [x] Extension register complete, change requests approved
- [x] D7 lab prepared

**Signatures:**

**FDE** Sarah Chen                    **Date** 2026-09-28  
**Tech Lead (extensions)** Dr. Sarah Chen   **Date** 2026-09-28  
**Dev Lead** Alice Johnson             **Date** 2026-09-28  
**App Owner** David Martinez           **Date** 2026-09-28  

**Enterprise version inherited** 0.1.0

---

## Summary of Generated Artefacts

| Section | GENERATE Step | Output | Status |
|---|---|---|---|
| 1 | Create app instructions | `payment-api/CLAUDE.md` | ✅ Generated |
| 2a-d | Create knowledge connection (4 files) | `.claude/context/{architecture,commands,glossary,hazards}.md` | ✅ Generated |
| 4 | Create server bindings | `payment-api/.mcp.json` | ✅ Generated |
| 5 | Create app settings + include file | `.claude/settings.json`, `.worktreeinclude` | ✅ Generated |
| 9 | Create app-specific rule | `.claude/rules/10-app.md` (narrowed rules) | ✅ Generated |

---

## How to Use This Example

**This is a complete, realistic example showing:**
- All 11 sections filled with actual answers
- Real application (payment-api)
- Real team members and dates
- All artefacts listed
- Verification evidence provided
- Sign-offs completed

**To create your own application form:**
1. Copy this example's structure
2. Replace with your application's values:
   - Application name (payment-api → your app name)
   - Dev lead name and email
   - App owner name and email
   - Repository URL
   - Technology stack
   - Knowledge connection details
   - Business rules
   - Hazards and incidents
3. Follow all GENERATE and VERIFY steps
4. Get all signatures
5. Archive completed form

---

## What This Completed Form Produces

```
payment-api/
├── CLAUDE.md                 ✅ Generated from section 1
├── .mcp.json                 ✅ Generated from section 4
├── .worktreeinclude          ✅ Generated from section 5
└── .claude/
    ├── settings.json         ✅ Generated from section 5
    ├── context/              ✅ Generated from section 2
    │   ├── architecture.md
    │   ├── commands.md
    │   ├── glossary.md
    │   └── hazards.md
    ├── rules/
    │   └── 10-app.md         ✅ Generated from section 9
    ├── agents/               (empty; uses enterprise roles)
    ├── skills/               (empty; uses enterprise skills)
    └── hooks/                (empty; enterprise manages hooks)
```

All files reference the **enterprise form v0.1.0**.

---

**End of Example Application Form**

Use this as a template when filling your own D4_Application_Harness_Form.md forms.
