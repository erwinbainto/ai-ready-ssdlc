# AI-Ready SSDLC Harness — Complete Architecture Guide

**Purpose:** Understand the two-tier deployment architecture, folder structures, and how enterprise and application harnesses work together.

---

## Table of Contents

1. [Quick Overview](#quick-overview)

2. [Part 1: Enterprise Harness (Tier 0-1)](#part-1-enterprise-harness-tier-0-1)
   - [What It Is](#what-it-is)
   - [Key Principle](#key-principle)
   - [Enterprise Directory Structure](#enterprise-directory-structure)
   - [Enterprise: Usage at a Glance](#enterprise-usage-at-a-glance)
   - [Enterprise Deployment Flow](#enterprise-deployment-flow)

3. [Part 2: Application Harness (Tier 3)](#part-2-application-harness-tier-3)
   - [What It Is](#what-it-is-1)
   - [Key Principle](#key-principle-1)
   - [Application Template Directory Structure](#application-template-directory-structure)
   - [Application: Usage at a Glance](#application-usage-at-a-glance)

4. [Part 3: The `.claude/` Folder Explained](#part-3-the-claude-folder-explained)
   - [Purpose: Auto-Loaded Configuration](#purpose-auto-loaded-configuration)
   - [Key Subfolders](#key-subfolders)
     - [`.claude/context/` — Knowledge Base](#claude-context--knowledge-base)
     - [`.claude/rules/` — Enforced Standards](#claude-rules--enforced-standards)
     - [`.claude/hooks/` — Lifecycle Automation](#claude-hooks--lifecycle-automation)

5. [Part 4: The `docs/` Folder Explained](#part-4-the-docs-folder-explained)
   - [Purpose: On-Demand Reference](#purpose-on-demand-reference-not-auto-loaded)
   - [Key Subfolders](#key-subfolders-1)
     - [`docs/security/` — Compliance & Threat Documentation](#docssecurity--compliance--threat-documentation)
     - [`docs/guides/` — Detailed How-To](#docsguides--detailed-how-to-created-by-template)
     - [`docs/architecture/` — Design Documentation](#docsarchitecture--design-documentation)

6. [Part 5: Enterprise vs. Application Rules](#part-5-enterprise-vs-application-rules)
   - [Rule Inheritance Hierarchy](#rule-inheritance-hierarchy)
   - [Examples](#examples)

7. [Part 6: Deployment Workflow](#part-6-deployment-workflow)
   - [Step 1: Deploy Enterprise Harness (Once)](#step-1-deploy-enterprise-harness-once)
   - [Step 2: Deploy Application Harness (Per App)](#step-2-deploy-application-harness-per-app)

8. [Part 7: Quick Start Checklist](#part-7-quick-start-checklist)
   - [For Platform/Security Team (Enterprise)](#for-platformsecurity-team-enterprise)
   - [For Dev Lead (Application)](#for-dev-lead-application)

9. [Part 8: File Size & Context Budget](#part-8-file-size--context-budget)
   - [Auto-Loaded Files (Always Count)](#auto-loaded-files-always-count)
   - [On-Demand Files (Don't Count Unless Read)](#on-demand-files-dont-count-unless-read)
   - [Context Efficiency Principle](#context-efficiency-principle)

10. [Part 9: Common Workflows](#part-9-common-workflows)
    - [Workflow 1: Team Member Starts on New App](#workflow-1-team-member-starts-on-new-app)
    - [Workflow 2: Security Review / Audit](#workflow-2-security-review--audit)
    - [Workflow 3: Add New Security Rule](#workflow-3-add-new-security-rule)
    - [Workflow 4: Handle Incident](#workflow-4-handle-incident)

11. [Part 10: Key Principles](#part-10-key-principles)
    - [1. Reference, Never Copy](#1-reference-never-copy)
    - [2. Permissions: Narrow, Never Widen](#2-permissions-narrow-never-widen)
    - [3. Placeholders: Complete All](#3-placeholders-complete-all)
    - [4. Auto-Loaded: Keep Concise](#4-auto-loaded-keep-concise)

12. [Part 11: Troubleshooting](#part-11-troubleshooting)

13. [Part 12: Related Files & Commands](#part-12-related-files--commands)

14. [Part 13: Summary Table](#part-13-summary-table)

15. [Quick Reference: Where to Find What](#quick-reference-where-to-find-what)

---

## Quick Overview

The AI-Ready SSDLC Harness is a **two-tier governance system** for Claude Code:

```
┌─────────────────────────────────────────┐
│   ENTERPRISE HARNESS (Tier 0-1)         │
│   • Organization-wide policies          │
│   • Deployed once                       │
│   • Inherited by all applications       │
│   • Read-only governance                │
└──────────────────┬──────────────────────┘
                   │ inherited by
        ┌──────────▼──────────┐
        │ APPLICATION         │
        │ HARNESS             │
        │ (Tier 3)            │
        │ • App-specific      │
        │ • Per-repository    │
        │ • Narrower rules    │
        └─────────────────────┘
```

---

## Part 1: Enterprise Harness (Tier 0-1)

### What It Is

**Organization-wide policy framework** deployed once and inherited by all applications.

### Key Principle

> Enterprise is the **policy engine**. Write once, inherit everywhere. Never copied into apps; always referenced.

### Enterprise Directory Structure

```
ai-ready-ssdlc/enterprise/
│
├── managed/                          # Privileged policy (system path)
│   ├── settings.json                # Org-wide Claude Code settings
│   ├── hooks/                       # Org-wide lifecycle automation
│   │   ├── session-start.sh         # Setup checks (Java, Node, Python, etc.)
│   │   └── pre-tool-use.sh          # Security gate (blocks secrets, etc.)
│   └── mcp-catalogue.json           # Approved MCP servers
│
├── agents/                           # Five pre-defined agent roles
│   ├── explorer.md                  # Fast search & exploration (read-only)
│   ├── reviewer.md                  # Code quality & consistency review
│   ├── verifier.md                  # Adversarial verification of findings
│   ├── vuln-analyst.md              # Security vulnerability analysis
│   └── container-assessor.md        # Container image scanning & hardening
│
├── skills/                           # Reusable capabilities (on-demand)
│   ├── advisory-writeup/
│   │   ├── SKILL.md                 # Full skill definition
│   │   └── templates/               # Report templates
│   │
│   ├── vuln-patch-triage/           # Prioritize & plan patches
│   ├── containerization-assessment/ # Container hardening
│   ├── receipt-check/               # Verify compliance evidence
│   └── repo-onboarding-brief/       # New repo orientation
│
├── rules/                            # Organization-wide standards
│   ├── secure-coding.md             # Language-agnostic security
│   ├── database-policy.md           # Query patterns, parameterization
│   ├── api-security.md              # REST/gRPC security
│   ├── testing-standards.md         # Minimum test coverage
│   ├── container-security.md        # Image hardening
│   └── dependency-management.md     # CVE scanning, EOL policies
│
├── evals/                            # Test templates for pre-pub gates
│   ├── security-eval.json           # CVE scanning tests
│   ├── code-quality-eval.json       # SAST/linting tests
│   └── compliance-eval.json         # Regulatory compliance tests
│
└── CLAUDE.md                         # Enterprise master instructions
```

### Enterprise: Usage at a Glance

| What | Purpose | Who Uses | Frequency |
|---|---|---|---|
| **managed/** | Policies pushed to all machines | IT/DevOps | On deployment |
| **agents/** | Pre-built roles (explorer, reviewer, etc.) | Any app | As needed |
| **skills/** | Reusable workflows (vulnerability triage, etc.) | Any app | On request |
| **rules/** | Org-wide standards (no SQL injection, etc.) | Any app | Auto-loaded |
| **evals/** | Gate tests before publishing changes | Platform team | Pre-release |

### Enterprise Deployment Flow

```
1. Complete D4_Enterprise_Harness_Form.md
   ↓
2. Run GENERATE steps → Creates enterprise/ files
   ↓
3. Validate: claude plugin validate enterprise
   ↓
4. Publish to marketplace
   ↓
5. Deploy to fleet:
   • Route A (MDM): /Library/Application Support/ClaudeCode/
   • Route B (Admin console): Via managed settings delivery
   ↓
6. Apps inherit automatically
```

---

## Part 2: Application Harness (Tier 3)

### What It Is

**Application-specific configuration** copied per repository. Narrows enterprise policies for this one app.

### Key Principle

> Application extends enterprise, never replaces it. Rules can only narrow, never widen.

### Application Template Directory Structure

```
application-template/                # Copy this to each app repo
│
├── CLAUDE.md                         # App instructions (extends enterprise)
├── .mcp.json                         # MCP bindings (admitted catalogue only)
├── .worktreeinclude                  # Git: ignore build artifacts
│
├── .claude/                          # Auto-loaded config (minimal, efficient)
│   │
│   ├── settings.json                # Permissions (narrowed)
│   ├── settings.local.json          # Dev-only overrides
│   │
│   ├── context/                     # Auto-loaded knowledge base (~290 lines)
│   │   ├── architecture.md          # App structure, components, decisions
│   │   ├── commands.md              # Available commands & contracts
│   │   ├── glossary.md              # Business & technical terms
│   │   ├── hazards.md               # Known risks, incident history
│   │   └── security-posture.md      # Compliance, auth, data classification
│   │
│   ├── rules/                       # Auto-loaded standards (~130 lines)
│   │   ├── 10-app.md                # App conventions (naming, patterns)
│   │   └── security-guardrails.md   # Mandatory security controls
│   │
│   ├── hooks/                       # Lifecycle automation
│   │   ├── session-start.sh         # Setup checks (Java 21?, Node 20?, etc.)
│   │   ├── pre-tool-use.sh          # Permission gates
│   │   └── pre-write-approved.sh    # Post-approval automation
│   │
│   ├── agents/                      # App-specific roles (usually empty)
│   └── skills/                      # App-specific skills (usually empty)
│
├── docs/                            # On-demand documentation
│   │
│   ├── architecture/
│   │   ├── README.md                # Navigation
│   │   └── adr/                     # Architectural Decision Records
│   │
│   ├── security/                    # Compliance & threat docs
│   │   ├── README.md                # Navigation guide
│   │   ├── threat-model.md          # Assets, threats, attack vectors
│   │   ├── compliance-mapping.md    # PCI/NIST/ISO → implementation
│   │   └── incident-response.md     # Procedures, escalation matrix
│   │
│   ├── specs/
│   │   └── README.md                # API specs, schemas
│   │
│   ├── testing/
│   │   └── README.md                # Test strategy
│   │
│   ├── audits/
│   │   └── README.md                # Compliance audit logs
│   │
│   ├── guides/                      # Detailed how-to docs (NOT auto-loaded)
│   │   ├── context/README.md        # How to complete .claude/context/
│   │   ├── rules/README.md          # How to create app-specific rules
│   │   └── hooks/README.md          # How to wire lifecycle hooks
│   │
│   └── agent-workflow/
│       └── README.md                # Custom agent patterns
│
└── src/                             # Application source code
    ├── backend/                     # Server-side code
    ├── frontend/                    # Client-side code
    └── shared/                      # Shared libraries
```

### Application: Usage at a Glance

| Folder | Purpose | Auto-Loaded? | Effort to Complete |
|---|---|---|---|
| **.claude/context/** | App knowledge base | YES (290 lines) | 2-3h to author with tech lead |
| **.claude/rules/** | App-specific guardrails | YES (130 lines) | 1-2h to customize for stack |
| **.claude/hooks/** | Lifecycle automation | YES | 1h setup + per-hook logic |
| **docs/security/** | Compliance documentation | NO (on-demand) | 3-4h to map to implementation |
| **docs/guides/** | How-to instructions | NO (on-demand) | Part of template |
| **src/** | Source code | NO (app-specific) | Your codebase |

---

## Part 3: The `.claude/` Folder Explained

### Purpose: Auto-Loaded Configuration

Every `.md` file in `.claude/` is automatically loaded into Claude Code's context window. **Keep them concise!**

### Key Subfolders

#### `.claude/context/` — Knowledge Base

**What:** App details Claude needs to know (structure, commands, risks, compliance)  
**When loaded:** Every Claude Code session  
**Size target:** ~290 lines total  
**Key files:**

```markdown
📄 architecture.md (64 lines)
   └─ Components, data flow, tech decisions
   └─ Helps Claude understand the system
   
📄 commands.md (33 lines)
   └─ Available commands ("mvn test", "npm start", etc.)
   └─ Contracts: what they do, when they fail
   
📄 glossary.md (42 lines)
   └─ Business terms: invoice, customer, SKU
   └─ Technical terms: JWT, RBAC, microservice
   
📄 hazards.md (63 lines)
   └─ Known fragile areas, incident history
   └─ Security hazards: SQL injection risks, auth gaps
   
📄 security-posture.md (90 lines)
   └─ Compliance: PCI DSS YES/NO, HIPAA, GDPR
   └─ Auth method, data classification, known risks
```

**Usage:** Claude reads these automatically; no manual reference needed.

#### `.claude/rules/` — Enforced Standards

**What:** Mandatory security & coding rules (narrower than enterprise)  
**When loaded:** Every session  
**Size target:** ~130 lines total  
**Key files:**

```markdown
📄 10-app.md (37 lines)
   └─ Naming conventions, patterns
   └─ Anti-patterns specific to this app
   └─ Narrower than enterprise
   
📄 security-guardrails.md (143 lines)
   └─ Secrets management (never hardcode)
   └─ SQL rules (parameterized only)
   └─ Auth, encryption, logging, rate limiting
   └─ Enforcement: SAST, pre-commit, code review
```

**Usage:** Claude enforces these during code work; flags violations.

#### `.claude/hooks/` — Lifecycle Automation

**What:** Shell scripts that run at specific points  
**When triggered:** Session start, before tool execution, after approval  
**Key scripts:**

```bash
session-start.sh
  └─ Run: When Claude Code starts
  └─ Purpose: Check Java 21, Node 20, git config, etc.
  └─ Exit 0 = OK; exit 1 = block
  
pre-tool-use.sh
  └─ Run: Before any tool executes
  └─ Purpose: Validate permissions (block .env edits, etc.)
  
pre-write-approved.sh
  └─ Run: After file edit approved by user
  └─ Purpose: Auto-format Java with google-java-format, etc.
```

**Usage:** Enforce policies without user intervention.

---

## Part 4: The `docs/` Folder Explained

### Purpose: On-Demand Reference (NOT auto-loaded)

Files here are **not** loaded into context automatically. Teams read them when needed.

### Key Subfolders

#### `docs/security/` — Compliance & Threat Documentation

```markdown
📄 threat-model.md
   └─ STRIDE analysis: spoofing, tampering, repudiation, info disclosure
   └─ Assets: databases, APIs, credentials
   └─ Attack vectors: SQL injection, XSS, CSRF
   └─ Residual risks after mitigations
   
📄 compliance-mapping.md
   └─ PCI DSS 6.2.1 → Code: src/auth/LoginValidator.java:42
   └─ NIST CSF ID.AM-1 → Code: scripts/asset-inventory.sh
   └─ ISO 27001 A.6.1.1 → Code: .claude/hooks/pre-tool-use.sh
   └─ GDPR Article 32 → Code: src/crypto/DataEncryption.java
   
📄 incident-response.md
   └─ Classification: CRITICAL (< 30 min), HIGH (< 2h), MEDIUM, LOW
   └─ Escalation matrix: Who to notify (Security, CTO, Legal)
   └─ On-call rotation and runbooks
   └─ Post-incident: Root cause, remediation, metrics
```

**Usage:** Reference for compliance audits, security reviews.

#### `docs/guides/` — Detailed How-To (Created by template)

```markdown
📁 guides/context/README.md
   └─ Full step-by-step guide to complete .claude/context/ files
   └─ Examples: architecture.md with data flow diagrams
   └─ When to use (2-3h with tech lead)
   
📁 guides/rules/README.md
   └─ How to create app-specific rules by stack
   └─ Java: @Transactional, JPA examples
   └─ React: Functional components, hook rules
   └─ Python: Virtual envs, async patterns
   
📁 guides/hooks/README.md
   └─ Lifecycle automation: session-start, pre-tool-use
   └─ Template scripts for each use case
   └─ Testing hooks manually
```

**Usage:** Team reference during harness setup.

#### `docs/architecture/` — Design Documentation

```markdown
📄 README.md
   └─ Navigation to architecture docs
   
📁 adr/
   └─ ADR-001-database-choice.md
   └─ ADR-002-api-gateway.md
   └─ ... (decisions in this app)
```

**Usage:** Design reviews, onboarding new team members.

---

## Part 5: Enterprise vs. Application Rules

### Rule Inheritance Hierarchy

```
┌─────────────────────────────────────────┐
│ ENTERPRISE (Tier 0-1)                   │
│ • All DB queries must be parameterized  │
│ • All auth endpoints need MFA checks    │
│ • No hardcoded secrets                  │
└─────────────────────┬───────────────────┘
                      │ inherited by
        ┌─────────────▼────────────┐
        │ APPLICATION (Tier 3)     │
        │ NARROWER rules:          │
        │ • All queries use JPA    │ ✅ Narrower (OK)
        │ • MFA + rate limiting    │ ✅ Narrower (OK)
        │ • Secrets via AWS SM     │ ✅ Narrower (OK)
        │                          │
        │ WIDER rules (NOT OK):    │
        │ ❌ SQL concat if reviewed │ ❌ Violates enterprise
        │ ❌ Skip MFA for admins    │ ❌ Violates enterprise
        │ ❌ Hardcode in tests      │ ❌ Violates enterprise
        └──────────────────────────┘
```

### Examples

| Enterprise Rule | App Narrowing | Status |
|---|---|---|
| "Parameterized queries only" | "Use JPA @Query; no native SQL" | ✅ OK |
| "No hardcoded credentials" | "Use AWS Secrets Manager; rotate every 30d" | ✅ OK |
| "Rate limit login endpoint" | "Max 5 attempts/minute per IP" | ✅ OK |
| "Encrypt sensitive data" | "AES-256 with FIPS 140-2 keys" | ✅ OK |
| "Hardcode OK if reviewed by lead" | — | ❌ NOT OK (violates) |

---

## Part 6: Deployment Workflow

### Step 1: Deploy Enterprise Harness (Once)

```bash
1. Complete D4_Enterprise_Harness_Form.md
   ↓ Answer sections 0.1–0.7 (gating decisions)
   ↓ Fill sections 1–10 (policy decisions)
   ↓ Run GENERATE steps
   
2. Validate:
   claude plugin validate enterprise
   
3. Publish to marketplace
   
4. Deploy to fleet:
   Route A: /Library/Application Support/ClaudeCode/
   Route B: Admin console → managed settings
   
5. Verify on one machine:
   /status → shows enterprise source
```

### Step 2: Deploy Application Harness (Per App)

```bash
1. Copy application-template/ to app repository
   
2. Complete D4_Application_Harness_Form.md
   ↓ Record enterprise version (0.1.0, etc.)
   ↓ Complete .claude/context/ with tech lead (2-3h)
   ↓ Customize security-guardrails.md for stack
   ↓ Map compliance in docs/security/
   
3. Verify setup:
   /status → enterprise + app sources
   /context → auto-loads .claude/ files
   /mcp → only admitted servers
   /doctor → no setup issues
   
4. Test write boundary:
   Edit a file → should be allowed in src/
   Edit .env → should be blocked
   → Capture refusal message as evidence
   
5. Team sign-off:
   Dev lead + security lead approve
```

---

## Part 7: Quick Start Checklist

### For Platform/Security Team (Enterprise)

- [ ] Read `enterprise/CLAUDE.md`
- [ ] Complete `D4_Enterprise_Harness_Form.md` (sections 0.1–0.7 gating decisions first)
- [ ] Run form GENERATE steps → creates `enterprise/` files
- [ ] Validate: `claude plugin validate enterprise`
- [ ] Publish to marketplace
- [ ] Deploy to fleet (Route A or B)
- [ ] Verify: `/status` shows enterprise policy

### For Dev Lead (Application)

- [ ] Record enterprise plugin version
- [ ] Copy `application-template/` to app repo
- [ ] Rename `<APPLICATION_NAME>` placeholder everywhere
- [ ] Complete `.claude/context/` with tech lead:
  - [ ] `architecture.md` — system structure
  - [ ] `commands.md` — available commands
  - [ ] `glossary.md` — domain terms
  - [ ] `hazards.md` — known risks
  - [ ] `security-posture.md` — compliance baseline
- [ ] Customize `.claude/rules/`:
  - [ ] `10-app.md` — naming conventions
  - [ ] `security-guardrails.md` — for your stack (Java/Node/Python)
- [ ] Wire hooks in `.claude/hooks/` and `settings.json`
- [ ] Map compliance in `docs/security/`:
  - [ ] `threat-model.md`
  - [ ] `compliance-mapping.md`
  - [ ] `incident-response.md`
- [ ] Run verification: `/status`, `/context`, `/mcp`, `/doctor`
- [ ] Test write boundary (edit .env → should fail)
- [ ] Get team sign-off

---

## Part 8: File Size & Context Budget

### Auto-Loaded Files (Always Count)

```
.claude/context/*.md        → ~290 lines (~725 tokens)
.claude/rules/*.md          → ~130 lines (~325 tokens)
.claude/hooks/*.sh          → ~0 lines (scripts, not tokens)
CLAUDE.md                   → ~400 lines (~1,000 tokens)

TOTAL AUTO-LOADED:          ~820 lines (~2,050 tokens)
```

### On-Demand Files (Don't Count Unless Read)

```
docs/guides/context/README.md    → 398 lines (on-demand)
docs/guides/rules/README.md      → 600 lines (on-demand)
docs/guides/hooks/README.md      → 400 lines (on-demand)
docs/security/threat-model.md    → on-demand
docs/security/incident-response  → on-demand

These are read ONLY when team opens them.
```

### Context Efficiency Principle

> Keep `.claude/` concise (~800 lines). Move detailed guides to `docs/guides/` to save ~5,000 tokens for actual code work.

---

## Part 9: Common Workflows

### Workflow 1: Team Member Starts on New App

```
1. Clone app repo
   
2. Claude Code auto-loads:
   • .claude/context/ → App structure
   • .claude/rules/ → App conventions
   • Enterprise policies
   
3. If confused about rules:
   → Read docs/guides/rules/README.md
   
4. If confused about architecture:
   → Read docs/architecture/README.md or adr/
   
5. Start coding with Claude
   → Claude enforces security guardrails
   → Claude flags violations
```

### Workflow 2: Security Review / Audit

```
1. Open .claude/context/security-posture.md
   → See: Compliance status, auth method, data classification
   
2. Open docs/security/threat-model.md
   → See: Assets, threats, attack vectors, mitigations
   
3. Open docs/security/compliance-mapping.md
   → See: PCI DSS 6.2.1 → src/auth/LoginValidator.java:42
   
4. Open docs/security/incident-response.md
   → See: Escalation matrix, on-call contacts
   
5. Audit: Verify all evidence locations still current
```

### Workflow 3: Add New Security Rule

```
1. Team identifies pattern in code reviews (3+ PRs)
   
2. Document in .claude/rules/security-guardrails.md:
   • Rule statement
   • ✅ Correct example
   • ❌ Wrong example
   • Enforcement method (SAST, pre-commit, test)
   
3. Add enforcement (choose one):
   • SonarQube rule
   • Pre-commit hook in .claude/hooks/pre-tool-use.sh
   • Test in CI/CD
   
4. Announce to team
   
5. Next review quarter: Check compliance
```

### Workflow 4: Handle Incident

```
1. Classify by severity (docs/security/incident-response.md)
   
2. Escalate per matrix:
   CRITICAL → Security + CTO + Legal
   HIGH → Security lead
   MEDIUM → Dev lead
   
3. Document findings in .claude/context/hazards.md:
   • What happened
   • Why it wasn't caught
   • Mitigation
   
4. Update rules if pattern discovered
   
5. Post-incident review (within 48h)
   → Update docs/security/incident-response.md
```

---

## Part 10: Key Principles

### 1. Reference, Never Copy

```markdown
❌ WRONG (copies enterprise):
"This app follows enterprise security standards..."

✅ RIGHT (references):
"See @enterprise/rules/secure-coding.md for org-wide standards"
```

**Why:** Enterprise rules are versioned. Copies drift and become stale.

### 2. Permissions: Narrow, Never Widen

```json
{
  "enterpriseVersion": "0.1.0",
  "permissionMode": "read",
  "toolAllowlist": ["Read", "Bash", "Edit"]
  // Never add tools not in enterprise allowlist
}
```

**Why:** App permissions can't override enterprise governance.

### 3. Placeholders: Complete All

```markdown
❌ DRAFT (has placeholders):
- Owner: <name>
- Compliance: <PCI DSS: YES/NO>

✅ READY (filled):
- Owner: Jane Smith
- Compliance: PCI DSS: YES
```

**Why:** Incomplete templates lead to governance gaps.

### 4. Auto-Loaded: Keep Concise

```markdown
❌ WASTEFUL (1,500 lines in .claude/):
- 400 lines of README in .claude/context/
- 600 lines of README in .claude/rules/

✅ EFFICIENT (420 lines in .claude/):
- 290 lines actual content in .claude/context/
- 130 lines actual content in .claude/rules/
- Move guides to docs/guides/ (on-demand)

SAVINGS: ~5,000 tokens for code!
```

**Why:** Every auto-loaded line counts toward context budget.

---

## Part 11: Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| App rules ignored | Path glob doesn't match files | Test: `find . -path "<glob>"` |
| CLAUDE.md not loading | Malformed YAML frontmatter | Validate syntax, check unclosed blocks |
| Security guardrails not enforcing | Missing pre-tool-use hook | Wire hook in `settings.json` + test |
| Enterprise policy not inherited | Enterprise plugin not installed | Run `claude plugin install enterprise` |
| Context docs not accessible | Not in `.claude/` directory | Move to `.claude/context/filename.md` |
| Too many tokens used | Oversized `.claude/` files | Move guides to `docs/guides/` |

---

## Part 12: Related Files & Commands

### Key Commands

```bash
# Verify setup
/status          # Shows enterprise + app sources
/context         # Lists auto-loaded files
/mcp             # Lists admitted MCP servers
/doctor          # Finds setup issues
/help            # Claude Code help

# Validate
claude plugin validate enterprise

# Test write boundary
Edit .env        # Should be blocked
Edit src/app.py  # Should be allowed
```

### Related Documentation

| File | Purpose |
|---|---|
| `README.md` | Enterprise & app intro |
| `deployment-guide.md` | Step-by-step deployment |
| `VERIFY.md` | Post-deployment checklist |
| `D4_Enterprise_Harness_Form.md` | Enterprise configuration form |
| `D4_Application_Harness_Form.md` | App configuration form |

---

## Part 13: Summary Table

| Layer | Folder | Audience | Purpose | Auto-Loaded | Effort |
|---|---|---|---|---|---|
| **Enterprise** | `enterprise/managed/` | IT/DevOps | Org policies | System path | Deploy once |
| **Enterprise** | `enterprise/agents/` | All teams | Predefined roles | On-demand | Reference |
| **Enterprise** | `enterprise/rules/` | All teams | Org standards | Inherited | Reference |
| **App** | `.claude/context/` | Dev team | App knowledge | YES | 2-3h |
| **App** | `.claude/rules/` | Dev team | App guardrails | YES | 1-2h |
| **App** | `.claude/hooks/` | Admins | Lifecycle gates | YES | 1h setup |
| **App** | `docs/security/` | Security team | Compliance | NO (on-demand) | 3-4h |
| **App** | `docs/guides/` | Dev team | How-to | NO (on-demand) | Template |

---

## Quick Reference: Where to Find What

**"How do I set up Claude Code for this app?"**
→ `.claude/context/` (auto-loaded on start)

**"What are the security rules?"**
→ `.claude/rules/security-guardrails.md` (auto-loaded) or `docs/guides/rules/README.md` (detailed)

**"What compliance frameworks apply?"**
→ `docs/security/compliance-mapping.md` (see PCI, NIST, ISO, GDPR)

**"How do I handle an incident?"**
→ `docs/security/incident-response.md`

**"What happened last time this broke?"**
→ `.claude/context/hazards.md` (auto-loaded) or `docs/security/incident-response.md`

**"How do I add a new rule?"**
→ `.claude/rules/10-app.md` or contact dev lead

**"I'm new; where do I start?"**
→ Read `.claude/context/` (auto-loaded) + `docs/guides/context/README.md` (full guide)

---

**Version:** 1.0  
**Last Updated:** 2026-10-01  
**Maintained by:** Platform / Security Team  
**Contact:** [Your team email]
