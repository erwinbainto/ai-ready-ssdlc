# Enterprise Architecture Overview

**What each folder in `enterprise/` contains and why.**

---

## Quick View

```
enterprise/
│
├── managed/                          # SYSTEM-LEVEL POLICY (Tier 0)
│   ├── managed-settings.json        # Permission mode, tool access, hooks, env vars
│   └── managed-mcp.json             # MCP server catalogue
│
├── agents/                           # PREDEFINED ROLES (Tier 1)
│   ├── explorer.md                  # Fast search & codebase exploration
│   ├── reviewer.md                  # Code quality & consistency checks
│   ├── verifier.md                  # Adversarial verification
│   ├── vuln-analyst.md              # Security vulnerability analysis
│   └── container-assessor.md        # Container hardening & scanning
│
├── skills/                           # REUSABLE WORKFLOWS (Tier 1)
│   ├── advisory-writeup/            # Format security advisories
│   ├── vuln-patch-triage/           # Prioritize & plan patches
│   ├── containerization-assessment/ # Container hardening guidance
│   ├── receipt-check/               # Verify compliance evidence
│   └── repo-onboarding-brief/       # New repo orientation
│
├── rules/                            # ORG STANDARDS (Tier 1)
│   ├── secure-coding.md             # Language-agnostic security
│   ├── database-policy.md           # Query patterns, parameterization
│   ├── api-security.md              # REST/gRPC security
│   ├── testing-standards.md         # Minimum test coverage
│   ├── container-security.md        # Image hardening & scanning
│   └── dependency-management.md     # CVE scanning, EOL versions
│
├── evals/                            # GATE TESTS (Pre-publication)
│   ├── security-eval.json           # CVE scanning tests
│   ├── code-quality-eval.json       # SAST, linting tests
│   └── compliance-eval.json         # Regulatory compliance tests
│
└── CLAUDE.md                         # MASTER INSTRUCTIONS (Tier 0)
```

---

## Tier 0: System Policy (managed/)

### Purpose
Privileged policy deployed to system path or admin console. Reaches every machine and cannot be overridden.

### Files

#### `managed-settings.json`

**What it contains:**

```json
{
  "permissionMode": "read",          // read-only or write (with limits)
  
  "toolAllowlist": [                 // What Claude can use
    "Read", "Edit", "Bash", "Artifact"
  ],
  
  "denialReasons": [                 // Why writes are denied
    "write_denied_by_policy"
  ],
  
  "hooks": {                         // Lifecycle gates
    "session-start": "path/to/session-start.sh",
    "pre-tool-use": "path/to/pre-tool-use.sh"
  },
  
  "env": {                           // Environment variables
    "OTEL_EXPORTER_OTLP_ENDPOINT": "https://otel.example.com:4317",
    "LOG_LEVEL": "info"
  }
}
```

**When it's loaded:**
- Every Claude Code session starts
- Cannot be overridden by user settings
- Applications can only narrow (never widen) permissions

**Who deploys it:**
- IT/DevOps (Route A: system path)
- Admin console (Route B: server-managed)

---

#### `managed-mcp.json`

**What it contains:**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"]
    },
    "jira": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-jira"]
    },
    // ... more approved servers
  }
}
```

**What it does:**
- Defines approved MCP servers (the catalogue)
- Applications bind servers from this list only
- No unapproved servers can be used

**When it's loaded:**
- When Claude Code starts
- When app tries to bind an MCP server

**Who manages it:**
- Enterprise team (defines catalogue)
- Security team (approves new servers)

---

## Tier 1: Enterprise Configuration

### Purpose
Organization-wide agents, skills, and standards. Inherited by all applications.

---

## Agents (agents/)

**What:** Five predefined roles for specialized tasks.

### explorer.md

**Purpose:** Fast codebase search and exploration

**Tools:** Read, Bash (grep, find only)

**When to use:**
- Map a new codebase
- Find which files contain X
- Search for patterns across repo

**Example:** "Map the data flow from user input to database"

---

### reviewer.md

**Purpose:** Code quality and consistency checks

**Tools:** Read, Bash

**When to use:**
- Review code for anti-patterns
- Check naming conventions
- Audit consistency across codebase

**Example:** "Review backend/ for inconsistent transaction handling"

---

### verifier.md

**Purpose:** Adversarial verification of findings

**Tools:** Read

**When to use:**
- Verify findings from other agents
- Double-check security claims
- Challenge assumptions in designs

**Example:** "Verify that this SQL injection fix actually prevents injection"

---

### vuln-analyst.md

**Purpose:** Security vulnerability analysis

**Tools:** Read, WebFetch

**When to use:**
- CVE analysis
- Dependency vulnerability review
- Security threat assessment

**Example:** "Analyze impact of CVE-2024-XXXXX on our codebase"

---

### container-assessor.md

**Purpose:** Container image hardening and scanning

**Tools:** Read, Bash

**When to use:**
- Review Dockerfile for security issues
- Scan container images
- Recommend hardening

**Example:** "Audit our Dockerfile for security best practices"

---

## Skills (skills/)

**What:** Reusable, on-demand workflows. Not auto-loaded; invoked by name.

### advisory-writeup/

**Purpose:** Format and structure security advisories

**When to use:** After discovering a vulnerability, format it for release

**Produces:** Structured advisory with CVE ID, impact, remediation

---

### vuln-patch-triage/

**Purpose:** Prioritize and plan patches

**When to use:** Got a list of CVEs; need to prioritize which to fix first

**Produces:** Prioritized list with effort estimates and risk

---

### containerization-assessment/

**Purpose:** Assess and harden containers

**When to use:** Need guidance on container security

**Produces:** Assessment with recommendations and examples

---

### receipt-check/

**Purpose:** Verify compliance evidence

**When to use:** Audit time; need to verify evidence locations

**Produces:** Evidence map with file paths and verification

---

### repo-onboarding-brief/

**Purpose:** Orient new team members

**When to use:** New person joining team

**Produces:** One-page repo overview with key concepts

---

## Rules (rules/)

**What:** Organization-wide standards. Auto-loaded in every session.

### secure-coding.md

**Purpose:** Language-agnostic security patterns

**Contains:**
- Never store plaintext secrets
- Use parameterized queries
- Validate all inputs
- Don't log sensitive data
- No eval() or dynamic execution

**Path globs:** All languages

---

### database-policy.md

**Purpose:** Database query patterns

**Contains:**
- All queries must be parameterized
- No string concatenation
- Transactions for multi-statement ops
- Audit logging for sensitive queries

**Path globs:** `backend/**`, `db/**`

---

### api-security.md

**Purpose:** REST and gRPC security

**Contains:**
- HTTPS only for transit
- Rate limiting on endpoints
- Input validation
- CORS policy
- Auth/authz on protected endpoints

**Path globs:** `backend/**/*.java`, `backend/**/*.js`

---

### testing-standards.md

**Purpose:** Minimum test coverage and patterns

**Contains:**
- Minimum 80% code coverage
- Unit tests for business logic
- Integration tests for APIs
- Security tests for auth/authz

**Path globs:** `**/*test*.java`, `**/*.spec.js`

---

### container-security.md

**Purpose:** Container image hardening

**Contains:**
- Use minimal base images (alpine, distroless)
- Scan for CVEs before pushing
- Don't run as root
- Remove build tools from final image

**Path globs:** `Dockerfile`, `*.dockerfile`

---

### dependency-management.md

**Purpose:** Dependency security

**Contains:**
- All dependencies scanned for CVEs
- Critical CVEs patched within 48h
- EOL versions not allowed
- No abandoned libraries

**Path globs:** `pom.xml`, `package.json`, `requirements.txt`

---

## Evals (evals/)

**What:** Gate tests before publishing new enterprise versions.

### security-eval.json

**Purpose:** Verify security controls are in place

**Tests:**
- CVE scanning works
- Secret detection works
- SAST rules enforce

---

### code-quality-eval.json

**Purpose:** Verify code quality gates

**Tests:**
- Linting passes
- Tests pass
- Coverage above threshold

---

### compliance-eval.json

**Purpose:** Verify compliance requirements

**Tests:**
- Required evidence present
- Audit trails configured
- Encryption enabled

---

## Tier 0: Master Instructions (CLAUDE.md)

**Purpose:** The instruction set for the entire enterprise harness.

**Contains:**
- Architecture overview
- How applications inherit policies
- Memory tier structure
- Key principles (reference, narrow, no copy)
- Governance model

**When loaded:** Every session

**What applications do with it:** Reference it, extend it, never replace it

---

## Data Flow

### When Claude Code Starts

```
Session Startup
  │
  ├─ Load managed-settings.json
  │  └─ Sets permission mode, tool access, hooks
  │
  ├─ Load managed-mcp.json
  │  └─ Loads approved MCP server catalogue
  │
  ├─ Load enterprise/CLAUDE.md
  │  └─ Sets enterprise policies
  │
  ├─ Load enterprise/agents/ (available, not active)
  │  └─ Roles available on-demand
  │
  ├─ Load enterprise/rules/ (auto-enforced)
  │  └─ Standards checked on every file edit
  │
  ├─ If in application repo:
  │  ├─ Load app/.claude/settings.json (narrower)
  │  ├─ Load app/.claude/rules/ (narrower)
  │  ├─ Load app/CLAUDE.md (extends enterprise)
  │  └─ App policies override enterprise (only narrower)
  │
  └─ Session ready
     └─ Claude Code can now work
```

---

## Policy Inheritance

### Enterprise → Application

**Enterprise sets the baseline:**
```
Permission: Read-only (cannot write)
Tools: Read, Edit, Bash
Deny: WebFetch, Artifact
```

**Application can narrow:**
```
Permission: Read-only (same or stricter)
Tools: Read, Edit (removed Bash because scripts are dangerous here)
Deny: WebFetch, Artifact (same)

Result: Application is stricter than enterprise ✅
```

**Application CANNOT widen:**
```
Permission: Write (wider than read-only) ❌
Tools: Read, Edit, Bash, WebFetch (added WebFetch) ❌
Deny: Artifact (removed, so Artifact is now allowed) ❌

Result: Enterprise rule wins; application policy ignored
```

---

## File Purposes Summary

| Folder | File | Purpose | Auto-Loaded? | Scope |
|---|---|---|---|---|
| **managed/** | managed-settings.json | Permission policy | YES (system) | All machines |
| **managed/** | managed-mcp.json | MCP catalogue | YES (system) | All machines |
| **agents/** | 5 files | Predefined roles | NO (on-demand) | Available to all apps |
| **skills/** | 5 folders | Reusable workflows | NO (on-demand) | Available to all apps |
| **rules/** | 6 files | Org standards | YES (auto-loaded) | Every app inherits |
| **evals/** | 3 files | Gate tests | NO (pre-publication) | Pre-release only |
| **CLAUDE.md** | — | Master instructions | YES (auto-loaded) | Every session |

---

## When to Update Each Section

| Component | When to Update | Impact |
|---|---|---|
| managed-settings.json | Policy changes, new tools added | All machines (immediate) |
| managed-mcp.json | New servers approved/removed | All machines (immediate) |
| agents/ | New role needed | New applications can use it |
| skills/ | New workflow created | Available to all apps |
| rules/ | New pattern discovered, compliance change | All apps (auto-inherit) |
| evals/ | Testing gates need update | New versions (pre-publication) |
| CLAUDE.md | Architecture or principles change | All sessions (auto-inherit) |

---

## Quick Reference: What's Where

**"Where do I define security rules?"** → `rules/secure-coding.md`

**"Where do I add a new MCP server?"** → `managed/managed-mcp.json`

**"Where do I define permission mode?"** → `managed/managed-settings.json`

**"Where do I find pre-built agents?"** → `agents/` (5 files)

**"Where do I find reusable skills?"** → `skills/` (5 folders)

**"Where do I find the master policy?"** → `CLAUDE.md`

---

## Related Documentation

- `setup.md` — How to create these files
- `deployment.md` — How to deploy to machines
- `publishing.md` — How to version and publish
- `rules-library.md` — Details on each rule file
- `agents-reference.md` — Details on each agent role
- `skills-reference.md` — Details on each skill

---

**Maintained by:** Enterprise Team  
**Last Updated:** 2026-10-01
