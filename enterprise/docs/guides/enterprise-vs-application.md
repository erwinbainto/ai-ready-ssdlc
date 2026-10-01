# Enterprise vs. Application: What's Shared, What's Unique

This document clarifies which values in the D4 forms are **enterprise-level** (same for all applications) and which are **application-level** (unique per application).

**TL;DR:** Enterprise form answered ONCE. Application form answered ONCE PER APP. Enterprise values cascade to all apps; application values customize each app locally.

---

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [The Hierarchy](#the-hierarchy)
3. [Enterprise-Level Values](#enterprise-level-values)
4. [Application-Level Values](#application-level-values)
5. [Shared but Narrowable Values](#shared-but-narrowable-values)
6. [Three-App Example](#three-app-example)
7. [Why This Structure](#why-this-structure)

---

## Quick Reference

### Enterprise Form (D4_Enterprise_Harness_Form.md)

| Section | Scope | Same for all apps? | Answer |
|---|---|---|---|
| **0** | Gating decisions (infrastructure) | ✅ YES | Once |
| **1** | Plugin identity | ✅ YES | Once |
| **2** | MCP catalogue (admitted servers) | ✅ YES | Once |
| **3** | Permission deny list | ✅ YES | Once |
| **4** | Enterprise instructions | ✅ YES | Once |
| **5** | Rules library (standards) | ✅ YES | Once |
| **6** | Agent roles | ✅ YES | Once |
| **7** | Memory tiers | ✅ YES | Once |
| **8** | Hooks (audit/logging) | ✅ YES | Once |
| **9** | Skills | ✅ YES | Once |
| **10** | Observability | ✅ YES | Once |

**Total: 11 sections, answered ONCE, inherited by all applications**

### Application Form (D4_Application_Harness_Form.md)

| Section | Scope | Same for all apps? | Answer |
|---|---|---|---|
| **0** | Application identity | ❌ NO | Once per app |
| **1** | Application instructions | ❌ NO | Once per app |
| **2** | Knowledge connection | ❌ NO | Once per app |
| **3** | Sources indexed | ❌ NO | Once per app |
| **4** | Server bindings | ⚠️ SUBSET | Once per app |
| **5** | Narrowed permissions | ❌ NO | Once per app |
| **6** | Enabled roles | ⚠️ SUBSET | Once per app |
| **7** | Capability candidates | ❌ NO | Once per app |
| **8** | Verification receipts | ❌ NO | Once per app |
| **9** | Extension register | ❌ NO | Once per app |
| **10** | D7 enablement | ⚠️ OPTIONAL | Once per app |

**Total: 11 sections, answered ONCE PER APP, customizes each app**

---

## The Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│           ENTERPRISE LAYER (Tier 0–1)                      │
│           Answered ONCE by technical lead                  │
│           Deployed to all machines                         │
│           Inherited by all applications                    │
│                                                             │
│  • Infrastructure policy (gating decisions)                │
│  • Organization identity (plugin, version)                 │
│  • Tool access policy (MCP catalogue)                      │
│  • Security boundary (permission deny list)                │
│  • Organization standards (rules, agents, skills)          │
│  • Audit framework (hooks)                                 │
│  • Observability setup (telemetry)                         │
│                                                             │
│  VALUE: Same for all applications                          │
│  APPLICATION CAN: Only narrow, never widen                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                            ↓ inherited by
┌──────────────────────────────────┬──────────────────────────────────┬──────────────────────────────────┐
│                                  │                                  │                                  │
│   APPLICATION 1 LAYER (Tier 3)   │   APPLICATION 2 LAYER (Tier 3)   │   APPLICATION 3 LAYER (Tier 3)   │
│   Answered ONCE by dev lead      │   Answered ONCE by dev lead      │   Answered ONCE by dev lead      │
│                                  │                                  │                                  │
│   • App identity                 │   • App identity                 │   • App identity                 │
│   • App instructions             │   • App instructions             │   • App instructions             │
│   • Knowledge connection         │   • Knowledge connection         │   • Knowledge connection         │
│   • Narrowed permissions         │   • Narrowed permissions         │   • Narrowed permissions         │
│   • Server bindings (subset)     │   • Server bindings (subset)     │   • Server bindings (subset)     │
│   • Enabled roles (subset)       │   • Enabled roles (subset)       │   • Enabled roles (subset)       │
│                                  │                                  │                                  │
│   UNIQUE TO THIS APP             │   UNIQUE TO THIS APP             │   UNIQUE TO THIS APP             │
│                                  │                                  │                                  │
└──────────────────────────────────┴──────────────────────────────────┴──────────────────────────────────┘
```

---

## Enterprise-Level Values

These are answered **ONCE** in the enterprise form and apply to **ALL applications**.

### Section 0: Gating Decisions

**What:** Infrastructure-level decisions that determine how the entire system is deployed.

| Decision | Example | Same for all apps? |
|---|---|---|
| 0.1 Gateway routing | "Yes, routed through client gateway" | ✅ YES |
| 0.2 Device management | "Yes, MDM is reliable" | ✅ YES |
| 0.3 Transcript retention | "30 days" | ✅ YES |
| 0.4 Pod hooks permitted | "Managed only" | ✅ YES |
| 0.5 Marketplace sources | "https://marketplace.internal" | ✅ YES |
| 0.6 KPIs frozen | "Yes" | ✅ YES |
| 0.7 Memory tiers | "Enterprise, Application, Session" | ✅ YES |

**Why same:** These are infrastructure decisions that affect how the platform is deployed. All applications run on the same infrastructure.

**Application sees:** Applications inherit these decisions. They can't change them.

---

### Section 1: Plugin Identity

**What:** Identifies the enterprise harness plugin.

| Field | Example | Same for all apps? |
|---|---|---|
| Plugin name | "ai-ready-ssdlc-harness" | ✅ YES |
| Version | "0.1.0" | ✅ YES |
| Technical lead | "technical-lead@company.com" | ✅ YES |
| Marketplace | "internal-marketplace" | ✅ YES |

**Why same:** There's only one enterprise plugin. All applications depend on it.

**Application sees:** Application form section 0 cites this version: "Enterprise plugin version inherited: 0.1.0"

---

### Section 2: Tool Access Policy (MCP Catalogue)

**What:** The list of approved MCP servers that applications can bind to.

| Category | Admitted Server | Same for all apps? |
|---|---|---|
| Source control | "https://github.internal/mcp" | ✅ YES |
| Work management | "https://jira.internal/mcp" | ✅ YES |
| Build and test | "https://ci.internal/mcp" | ✅ YES |
| Documentation | "https://docs.internal/mcp" | ✅ YES |
| Observability | "https://datadog.internal/mcp" | ✅ YES |

**Why same:** The catalogue is the control. No unapproved servers can be used.

**Application sees:** Application form section 4 binds from THIS catalogue only. Cannot add servers outside this list.

---

### Section 3: Execution Boundary (Permission Deny List)

**What:** The core security boundary. What tools and paths are globally blocked.

| Control | Example | Same for all apps? |
|---|---|---|
| Denied tools | "Write, Edit, git commit, git push" | ✅ YES |
| Denied paths | "Read(.env), Read(.env.*), Read(\*\*/\*secret\*)" | ✅ YES |
| Allowed commands | "Bash(make build), Bash(make test)" | ✅ YES |

**Why same:** This is the read-only boundary. All applications enforce it.

**Application sees:** Application form section 5 can ADD narrower restrictions, but cannot remove these.

---

### Section 4: Enterprise Instructions (CLAUDE.md)

**What:** The mandate, verification duty, security rules, and standards for all sessions.

| Topic | Same for all apps? |
|---|---|
| Mandate (advisory output) | ✅ YES |
| Verification duty (present receipts) | ✅ YES |
| Output contract (5-part findings) | ✅ YES |
| Security rules | ✅ YES |
| Engineering standards | ✅ YES |

**Why same:** These are organizational standards. They apply everywhere.

**Application sees:** Application form section 1 creates app CLAUDE.md that REFERENCES (never copies) this.

---

### Section 5: Rules Library

**What:** Organizational standards for secure coding, testing, interfaces, and containers.

| Rule | Example | Same for all apps? |
|---|---|---|
| Advisory format | "5-part shape (observation, evidence, proposal, risk, effort)" | ✅ YES |
| Secure coding | "Injection classes, crypto library, auth patterns" | ✅ YES |
| Testing | "Coverage %, mocking policy, baseline" | ✅ YES |
| Interfaces | "API versioning, breaking changes" | ✅ YES |
| Containers | "Base image policy, non-root user" | ✅ YES |

**Why same:** These are organizational standards applied to all code.

**Application sees:** Applications inherit and follow these rules. Can add app-specific rules.

---

### Section 6: Agent Roles

**What:** The five agent roles available to all applications.

| Role | Tools | Same for all apps? |
|---|---|---|
| explorer | Read, Grep, Glob | ✅ YES |
| reviewer | Read, Grep, Glob | ✅ YES |
| verifier | Read, Grep, Glob, Bash | ✅ YES |
| vuln-analyst | Read, Grep, Glob | ✅ YES |
| container-assessor | Read, Grep, Glob | ✅ YES |

**Why same:** These are the standard agent capabilities. All applications have access.

**Application sees:** Application form section 6 chooses which roles to ENABLE (can enable subset). Cannot define new roles.

---

### Section 7: Memory Tiers

**What:** The organization's memory structure (enterprise tier, application tier, session tier).

| Tier | Purpose | Same for all apps? |
|---|---|---|
| Enterprise tier | Shared standards | ✅ YES |
| Application tier | App-specific knowledge | ✅ YES |
| Session tier | Per-session context | ✅ YES |

**Why same:** This is the organization's memory architecture. All applications use it.

**Application sees:** Application form section 6 records where app memory lives within this structure.

---

### Section 8: Hooks

**What:** The lifecycle scripts that run on every session (audit trail).

| Hook | Purpose | Same for all apps? |
|---|---|---|
| SessionStart | Stamp app + version into trace | ✅ YES |
| PreToolUse | Log tool calls, block writes and credential reads | ✅ YES |

**Why same:** These are organizational audit requirements. All sessions run these.

**Application sees:** Applications inherit these hooks. Can add optional app-specific hooks if policy permits (section 0.4).

---

### Section 9: Skills

**What:** The five reusable capabilities available to all applications.

| Skill | Purpose | Same for all apps? |
|---|---|---|
| repo-onboarding-brief | Onboarding new developers | ✅ YES |
| vuln-patch-triage | Patch advisory workflow | ✅ YES |
| containerization-assessment | Containerization readiness | ✅ YES |
| receipt-check | Verify claimed receipts | ✅ YES |
| advisory-writeup | Format findings | ✅ YES |

**Why same:** These are standard capabilities. All applications can use them.

**Application sees:** Application form section 7 logs which skills are actually used.

---

### Section 10: Observability

**What:** Telemetry and logging configuration for the organization.

| Field | Example | Same for all apps? |
|---|---|---|
| OTLP endpoint | "https://telemetry.internal/v1/traces" | ✅ YES |
| Telemetry enabled | "true" | ✅ YES |
| Analytics dashboard | "https://analytics.internal/d/ssdlc" | ✅ YES |

**Why same:** All applications send telemetry to the same endpoint.

**Application sees:** Applications inherit these settings and send data to the same observability system.

---

## Application-Level Values

These are answered **ONCE PER APP** in the application form and are **UNIQUE to each application**.

### Section 0: Application Identity

**What:** Identifies the application.

| Field | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| App name | "my-api" | "my-web" | "my-batch" |
| Dev lead | "Alice" | "Bob" | "Carol" |
| Stack | "Python 3.11" | "TypeScript, React" | "Go 1.21" |
| KPIs | "99.99% uptime, p99 < 200ms" | "99.9% uptime, p99 < 500ms" | "Complete hourly, no data loss" |
| Enterprise version inherited | "0.1.0" | "0.1.0" | "0.1.0" |

**Why different:** Each application is different. Different stacks, different KPIs, different teams.

**Why version is same:** All apps inherit the same enterprise layer version.

---

### Section 1: Application Instructions (CLAUDE.md)

**What:** Business context and guidance specific to this application.

| Field | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| Business purpose | "Payment processing service" | "Customer dashboard" | "Daily batch processor" |
| Entry points | "main.py, FastAPI server" | "src/index.js, React app" | "main.go, batch entry" |
| Approver | "payments-lead@company.com" | "frontend-lead@company.com" | "data-lead@company.com" |

**Why different:** Each application has different purpose, structure, and approval chain.

---

### Section 2: Knowledge Connection

**What:** Business and technical context (architecture, commands, glossary, hazards).

#### 2a. Architecture

| Field | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| Business purpose | "Processes and settles payments securely" | "Shows customer data and analytics" | "Aggregates and backfills metrics" |
| Key components | "PaymentGateway, Settlement, Audit" | "Auth, Dashboard, API client" | "Fetcher, Aggregator, Writer" |
| Interfaces | "REST /payment, Queue payment-events" | "GraphQL /query, WebSocket /updates" | "S3 input, DataStore output" |

**Why different:** Each application has its own architecture and interfaces.

#### 2b. Commands

| Command | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| Build | "make build" | "npm run build" | "go build ./cmd" |
| Test | "make test" | "npm run test" | "go test ./..." |
| Lint | "make lint" | "npm run lint" | "golangci-lint run" |
| Type check | "mypy ." | "tsc --noEmit" | "go build ./..." |

**Why different:** Different stacks have different build systems and commands.

#### 2c. Glossary

| Term | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| Example term | "Settlement = confirmed payment" | "Widget = UI component" | "Shard = data partition" |

**Why different:** Each domain has its own terminology.

#### 2d. Hazards

| Hazard | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| Fragile area | "Settlement system (financial impact)" | "Auth flow (security critical)" | "Data backfill (history correctness)" |

**Why different:** Each application has different risky areas.

---

### Section 3: Sources Indexed

**What:** Where code, tests, docs, and other artifacts live.

| Source | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| Code repo | "github.com/company/payment-api" | "github.com/company/dashboard" | "github.com/company/batch-processor" |
| Tests | "src/tests/", pytest | "src/__tests__/", Jest | "tests/", Go testing |
| Docs | "docs/", markdown | "docs/", markdown + Confluence" | "docs/", markdown + wiki |
| Jira project | "PAY" | "WEB" | "DATA" |

**Why different:** Each application has its own repository and project structure.

---

### Section 4: Server Bindings (From Enterprise Catalogue)

**What:** Which servers from the enterprise catalogue this app binds to.

| Category | Enterprise Catalogue | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|---|
| Source control | GitHub, GitLab | GitHub ✅ | GitHub ✅ | GitHub ✅ |
| Work management | Jira, Azure Boards | Jira ✅ | Jira ✅ | Jira ✅ |
| Build and test | CI/CD system | CI/CD ✅ | CI/CD ✅ | CI/CD ✅ |
| Documentation | Internal wiki | Wiki ✅ | Wiki ✅ | (none) ❌ |
| Observability | Datadog | Datadog ✅ | Datadog ✅ | Datadog ✅ |

**Why can differ:** Each app binds to the servers it needs. All from the same catalogue.

**Constraint:** Cannot bind to servers outside the enterprise catalogue.

---

### Section 5: Narrowed Permissions

**What:** This app's additional restrictions beyond enterprise deny list.

| Restriction | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|
| Enterprise denies | Write, Edit, Read(.env), ... | Write, Edit, Read(.env), ... | Write, Edit, Read(.env), ... |
| App additionally denies | Read(src/secrets/payment-keys) | Read(src/auth-tokens/) | Read(db-credentials/) |
| | Read(config/merchant-ids) | Read(config/api-keys) | Read(encryption-keys/) |

**Why different:** Each app has additional sensitive paths it wants to protect.

**Constraint:** Can only ADD denies, never REMOVE enterprise denies.

---

### Section 6: Enabled Roles

**What:** Which of the five enterprise roles this app enables.

| Role | Enterprise provides | Example App 1 | Example App 2 | Example App 3 |
|---|---|---|---|---|
| explorer | ✅ yes | ✅ enable | ✅ enable | ✅ enable |
| reviewer | ✅ yes | ✅ enable | ✅ enable | ✅ enable |
| verifier | ✅ yes | ✅ enable | ✅ enable | ✅ enable |
| vuln-analyst | ✅ yes | ✅ enable | ❌ disable | ✅ enable |
| container-assessor | ✅ yes | ❌ disable | ❌ disable | ✅ enable |

**Why can differ:** Each app enables the roles it needs.

**Constraint:** Can only enable/disable provided roles, cannot create new ones.

---

### Sections 7-10: App-Specific Data

**What:** Capability candidates, verification receipts, extension register, D7 labs.

**Why different:** Each application has different capabilities observed, different extensions needed, different verification evidence.

---

## Shared but Narrowable Values

These are provided by enterprise but can be narrowed (customized) by applications.

### MCP Server Bindings

**Enterprise provides:** The catalogue of approved servers.

```
Enterprise Catalogue (Section 2):
  Source control: https://github.internal/mcp
  Work management: https://jira.internal/mcp
  Build and test: https://ci.internal/mcp
  Documentation: https://docs.internal/mcp
  Observability: https://datadog.internal/mcp
```

**Application customizes:** Which servers to bind.

```
Example App 1 (Section 4):
  ✅ Bind: Source control (GitHub)
  ✅ Bind: Work management (Jira)
  ✅ Bind: Build and test (CI/CD)
  ✅ Bind: Observability (Datadog)
  ❌ Don't bind: Documentation (doesn't need it)

Example App 2 (Section 4):
  ✅ Bind: Source control (GitHub)
  ❌ Don't bind: Work management (doesn't track in Jira)
  ✅ Bind: Build and test (CI/CD)
  ✅ Bind: Documentation (uses wiki)
  ✅ Bind: Observability (Datadog)
```

**Constraint:** Can only select from enterprise catalogue. Cannot add unapproved servers.

---

### Agent Roles

**Enterprise provides:** Five standard roles (explorer, reviewer, verifier, vuln-analyst, container-assessor).

**Application customizes:** Which roles to enable.

```
Example App 1:
  Enable: explorer (yes) → map code
  Enable: reviewer (yes) → review changes
  Enable: verifier (yes) → run tests
  Enable: vuln-analyst (yes) → check patches
  Enable: container-assessor (no) → not containerized

Example App 2:
  Enable: explorer (yes)
  Enable: reviewer (yes)
  Enable: verifier (yes)
  Enable: vuln-analyst (no) → doesn't do dependency scanning
  Enable: container-assessor (no)

Example App 3:
  Enable: explorer (yes)
  Enable: reviewer (yes)
  Enable: verifier (yes)
  Enable: vuln-analyst (yes)
  Enable: container-assessor (yes) → will containerize
```

**Constraint:** Can only enable/disable provided roles. Cannot create new roles.

---

### Permission Rules

**Enterprise provides:** The core deny list (Write, Edit, git commit, Read(.env), etc.).

**Application customizes:** Additional denies specific to this app.

```
Enterprise Deny List (Section 3):
  - Write, Edit, NotebookEdit
  - Bash(git commit:*)
  - Bash(git push:*)
  - Read(./.env)
  - Read(./.env.*)
  - Read(**/*secret*)

Example App 1 Additions (Section 5):
  - Read(src/payment/keys/)
  - Read(config/merchant-ids)

Example App 2 Additions (Section 5):
  - Read(src/auth-tokens/)
  - Read(config/oauth-secrets)

Example App 3 Additions (Section 5):
  - Read(db-credentials/)
  - Read(encryption-keys/)
```

**Constraint:** Can only ADD denies. Cannot remove enterprise denies.

---

## Three-App Example

Here's a complete example showing how the same enterprise form applies to three different applications.

### Enterprise Form (Answered ONCE)

```markdown
# D4_Enterprise_Harness_Form.md

## 0. Decisions that gate everything

| Decision | Your answer |
|---|---|
| 0.1 Gateway routing? | no |
| 0.2 Device management reliable? | yes |
| 0.3 Transcript retention | 30 days |
| 0.4 Pod hooks permitted? | managed only |
| 0.5 Marketplaces | https://marketplace.internal |
| 0.6 KPIs frozen? | yes |
| 0.7 Memory tiers agreed? | yes |

## 1. Identity of the enterprise set

| Field | Value |
|---|---|
| Plugin name | ai-ready-ssdlc-harness |
| Version | 0.1.0 |
| Technical lead | technical-lead@company.com |
| Marketplace | internal-marketplace |

## 2. Tool access policy

| Category | Admitted server |
|---|---|
| Source control | https://github.internal/mcp |
| Work management | https://jira.internal/mcp |
| Build and test | https://ci.internal/mcp |
| Documentation | https://docs.internal/mcp |
| Observability | https://datadog.internal/mcp |

## 3. Execution boundary

| Control | Value |
|---|---|
| Denied tools | Write, Edit, git commit, git push |
| Denied paths | Read(.env), Read(.env.*), Read(**/*secret*) |
| Allowed commands | Bash(make build), Bash(make test) |

## 4-10. (Enterprise instructions, rules, agents, skills, hooks, evals, observability)

(All filled ONCE, apply to all applications)
```

### Application Forms (Answered ONCE PER APP)

#### **Application Form 1: my-api**

```markdown
# D4_Application_Harness_Form.md

## 0. Application identity

| Field | Value |
|---|---|
| Application name | my-api |
| Enterprise plugin version | 0.1.0 ← SAME (from enterprise form section 1) |
| Dev Lead | Alice |
| Stack | Python 3.11, FastAPI |
| KPIs | 99.99% uptime, p99 < 200ms |

## 1. Application instructions

One-line purpose: "REST API for payment processing"
Entry points: "main.py, FastAPI server on port 8000"
Approver: "payments-lead@company.com"

## 2. Knowledge connection

Business: "Processes payment requests, validates, routes to settlement"
Architecture: "PaymentGateway, Settlement, AuditLog"
Interfaces: "POST /payment, GET /status, Queue payment-events"

## 3. Sources indexed

| Source | Location |
|---|---|
| Code | github.com/company/payment-api |
| Tests | src/tests/, pytest |
| Jira | project PAY |

## 4. Server bindings

| Category | Bind? |
|---|---|
| Source control (GitHub) | ✅ yes |
| Work management (Jira) | ✅ yes |
| Build and test (CI/CD) | ✅ yes |
| Documentation | ❌ no |
| Observability (Datadog) | ✅ yes |

## 5. Narrowed permissions

Enterprise denies: Write, Edit, git commit, git push, Read(.env), ...
Additionally deny:
  - Read(src/payment/merchant-keys/)
  - Read(config/api-keys/)

## 6. Roles

| Role | Enable? |
|---|---|
| explorer | ✅ yes |
| reviewer | ✅ yes |
| verifier | ✅ yes |
| vuln-analyst | ✅ yes |
| container-assessor | ❌ no (not containerized) |
```

#### **Application Form 2: my-web**

```markdown
# D4_Application_Harness_Form.md

## 0. Application identity

| Field | Value |
|---|---|
| Application name | my-web |
| Enterprise plugin version | 0.1.0 ← SAME |
| Dev Lead | Bob |
| Stack | TypeScript 5.0, React 18 |
| KPIs | 99.9% uptime, p99 < 500ms |

## 1. Application instructions

One-line purpose: "Customer-facing dashboard and analytics"
Entry points: "src/index.js, React SPA on port 3000"
Approver: "frontend-lead@company.com"

## 2. Knowledge connection

Business: "Shows customer account data, payments, analytics"
Architecture: "Auth, Dashboard, APIClient, DataStore"
Interfaces: "GraphQL /query, WebSocket /updates"

## 3. Sources indexed

| Source | Location |
|---|---|
| Code | github.com/company/dashboard |
| Tests | src/__tests__/, Jest |
| Jira | project WEB |

## 4. Server bindings

| Category | Bind? |
|---|---|
| Source control (GitHub) | ✅ yes |
| Work management (Jira) | ✅ yes |
| Build and test (CI/CD) | ✅ yes |
| Documentation | ✅ yes |
| Observability (Datadog) | ✅ yes |

## 5. Narrowed permissions

Enterprise denies: Write, Edit, git commit, git push, Read(.env), ...
Additionally deny:
  - Read(src/auth/oauth-secrets/)
  - Read(config/session-keys/)

## 6. Roles

| Role | Enable? |
|---|---|
| explorer | ✅ yes |
| reviewer | ✅ yes |
| verifier | ✅ yes |
| vuln-analyst | ❌ no (frontend, few dependencies) |
| container-assessor | ❌ no (already containerized, not changing) |
```

#### **Application Form 3: my-batch**

```markdown
# D4_Application_Harness_Form.md

## 0. Application identity

| Field | Value |
|---|---|
| Application name | my-batch |
| Enterprise plugin version | 0.1.0 ← SAME |
| Dev Lead | Carol |
| Stack | Go 1.21 |
| KPIs | Complete daily, zero data loss |

## 1. Application instructions

One-line purpose: "Daily batch processor for metrics aggregation"
Entry points: "main.go, batch entrypoint"
Approver: "data-lead@company.com"

## 2. Knowledge connection

Business: "Fetches raw events, aggregates by time window, writes metrics"
Architecture: "EventFetcher, MetricsAggregator, MetricsWriter"
Interfaces: "S3 input-bucket/, DataStore metrics-table"

## 3. Sources indexed

| Source | Location |
|---|---|
| Code | github.com/company/batch-processor |
| Tests | tests/, Go testing |
| Jira | project DATA |

## 4. Server bindings

| Category | Bind? |
|---|---|
| Source control (GitHub) | ✅ yes |
| Work management (Jira) | ✅ yes |
| Build and test (CI/CD) | ✅ yes |
| Documentation | ❌ no |
| Observability (Datadog) | ✅ yes |

## 5. Narrowed permissions

Enterprise denies: Write, Edit, git commit, git push, Read(.env), ...
Additionally deny:
  - Read(db-credentials/)
  - Read(encryption-keys/)
  - Read(s3-access-keys/)

## 6. Roles

| Role | Enable? |
|---|---|
| explorer | ✅ yes |
| reviewer | ✅ yes |
| verifier | ✅ yes |
| vuln-analyst | ✅ yes |
| container-assessor | ✅ yes (planning containerization) |
```

---

## What's the Same Across All Three Apps?

```
✅ Enterprise plugin version: 0.1.0
✅ MCP catalogue: GitHub, Jira, CI/CD, Docs, Datadog
✅ Permission deny list: Write, Edit, git commit, Read(.env), ...
✅ Enterprise instructions: Mandate, standards, output format
✅ Rules: Advisory format, secure coding, testing, interfaces
✅ Agent roles available: explorer, reviewer, verifier, vuln-analyst, container-assessor
✅ Hooks: SessionStart, PreToolUse
✅ Skills: repo-onboarding-brief, vuln-patch-triage, ...
✅ Observability endpoint: same for all
✅ Transcript retention: 30 days for all
✅ Device management policy: yes for all
```

---

## What's Different for Each App?

```
Application 1 (my-api):
  ❌ App name: my-api
  ❌ Dev lead: Alice
  ❌ Stack: Python 3.11
  ❌ KPIs: 99.99% uptime, p99 < 200ms
  ❌ Repo: payment-api
  ❌ Additional denies: Read(merchant-keys/), Read(api-keys/)
  ❌ Enabled roles: all except container-assessor

Application 2 (my-web):
  ❌ App name: my-web
  ❌ Dev lead: Bob
  ❌ Stack: TypeScript, React
  ❌ KPIs: 99.9% uptime, p99 < 500ms
  ❌ Repo: dashboard
  ❌ Additional denies: Read(oauth-secrets/), Read(session-keys/)
  ❌ Enabled roles: explorer, reviewer, verifier only

Application 3 (my-batch):
  ❌ App name: my-batch
  ❌ Dev lead: Carol
  ❌ Stack: Go 1.21
  ❌ KPIs: Complete daily, zero loss
  ❌ Repo: batch-processor
  ❌ Additional denies: Read(db-credentials/), Read(encryption-keys/)
  ❌ Enabled roles: all 5 roles
```

---

## Why This Structure?

### Consistency

Enterprise values being shared ensures:
- Same security boundary across all apps
- Same standards and practices everywhere
- Same observability and audit trail
- Synchronized policy updates

### Flexibility

Application values being unique enables:
- Each app configured for its own domain and stack
- Custom knowledge specific to each app
- Narrowed permissions for sensitive data paths
- Different role enablement based on needs

### Governance

Narrowing-only constraint ensures:
- No application can weaken enterprise policy
- Security boundary cannot be bypassed locally
- Updates at enterprise layer reach all apps
- Compliance is maintained everywhere

---

## Quick Decision Tree

**When answering a question in a form, ask:**

1. **"Does this apply to all applications?"**
   - YES → Answer in **Enterprise Form** (section 0-10)
   - NO → Answer in **Application Form** (section 0-10)

2. **"Is this provided by enterprise but customizable per app?"**
   - YES → It's a "shared but narrowable" value
   - Enterprise provides the base (catalogue, deny list, roles, etc.)
   - Application selects/narrows (binds servers, enables roles, adds denies)

3. **"Is this the same exact value for all applications?"**
   - YES → Enterprise-level (answered once)
   - NO → Application-level (answered once per app)

---

## Summary Table

| Aspect | Enterprise | Application |
|---|---|---|
| **Answered** | Once | Once per app |
| **Applies to** | All applications | One application |
| **Can be changed** | By technical lead | By dev lead (narrowing only) |
| **Inheritance** | Source of policy | Inherits and customizes |
| **MCP servers** | Defines catalogue | Selects from catalogue |
| **Permission rules** | Core deny list | Can add denies, not remove |
| **Agent roles** | Defines available | Enables/disables subset |
| **Standards** | Defines standards | Follows standards |
| **Example values** | "Deny git commit" | "Also deny Read(secrets/)" |

---

## When to Check This Document

- **During enterprise form:** "Is this enterprise-level or app-level?"
- **During application form:** "What values should be same? What should be unique?"
- **During planning:** "Should this be configured once or per app?"
- **During architecture:** "What's inherited vs. what's customized?"

---

## Related Files

- `deployment-guide.md` — Step-by-step for both phases
- `D4_Enterprise_Harness_Form.md` — The enterprise form
- `D4_Application_Harness_Form.md` — The application form
- `usage.md` — Quick reference
- `index.md` — Project reference
