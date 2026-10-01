# Enterprise Setup Guide

**How to complete `D4_Enterprise_Harness_Form.md` and create the enterprise harness.**

---

## Before You Start

✅ Claude Code installed locally  
✅ Access to marketplace for publishing  
✅ Authority to define organizational policy  
✅ 1-2 weeks available (including stakeholder alignment)

---

## Section 0: Gating Decisions (START HERE)

**These 7 decisions determine everything downstream. Answer them FIRST.**

### 0.1: Gateway Routing

**Question:** Is Claude Code routed through a client-controlled gateway?

**What it means:**
- **YES** → All requests pass through your gateway; you control policy delivery
- **NO** → Users connect directly to Claude; policy via managed files or admin console

**Impact:** Determines how managed settings reach machines (Route A vs. B)

**Fill in:** YES or NO + reasoning

---

### 0.2: Device Management (MDM)

**Question:** Is device management (MDM) reliable across your fleet?

**What it means:**
- **YES** → You trust MDM to reliably push files to all machines
- **NO** → You prefer server-managed policy delivery via admin console

**Impact:** Determines MCP deployment route
- Route A (MDM reliable): Push `managed-mcp.json` to system path
- Route B (MDM unreliable): Deliver MCP config via admin console

**Fill in:** YES or NO + your MDM solution (Jamf, Intune, etc.)

---

### 0.3: Transcript Retention

**Question:** How many days should transcripts be retained?

**What it means:**
- Cleanup period for Claude Code session logs
- 0 = never cleanup, 30 = delete after 30 days, etc.

**Fill in:** Number of days (or 0 for never delete)

---

### 0.4: Application Hooks

**Question:** May applications add their own hooks?

**What it means:**
- **YES** → Apps can add `session-start.sh`, `pre-tool-use.sh` in `.claude/hooks/`
- **NO** → Only enterprise hooks; apps cannot customize

**Impact:** Application flexibility vs. governance

**Fill in:** YES or NO + rationale

---

### 0.5: Marketplace Sources

**Question:** Which marketplace sources are permitted?

**What it means:**
- Internal marketplace? Public? Vetted vendors only?
- Trust model for plugins

**Impact:** Which plugins apps can use

**Fill in:** List of permitted sources (e.g., "Internal only", "Anthropic + vetted partners")

---

### 0.6: KPIs Frozen (CRITICAL)

**Question:** Are KPI definitions frozen in D3?

**What it means:**
- D3 = Deployment Design Document
- KPIs = Key Performance Indicators (success metrics)
- If "no", harness can't be deployed until metrics are defined

**Impact:** If "no", ESCALATE and don't proceed until answered

**Fill in:** YES + reference to D3, or NO + escalate immediately

---

### 0.7: Memory Tiers (CRITICAL)

**Question:** Are memory tier definitions agreed?

**What it means:**
- How Claude Code structures memory (session, project, org)
- If "no", harness can't be deployed until tiers are defined

**Impact:** If "no", ESCALATE and don't proceed until answered

**Fill in:** YES + memory tier structure, or NO + escalate immediately

---

## If Section 0.6 or 0.7 is "NO"

**STOP HERE. Do not proceed.**

- Escalate to leadership / governance committee
- Get KPIs and memory tiers defined
- Then resume with section 0

---

## Sections 1-10: Configuration

For each section:

1. **Read** the section heading and explanation
2. **Answer** the questions in the table
3. **Look for GENERATE instruction** — Create the file mentioned
4. **Look for VERIFY instruction** — Run the command to test

---

## Section 1: Plugin Identity

**What to fill:**

| Field | Example | Notes |
|---|---|---|
| Plugin name | `ai-ready-ssdlc-harness` | Short, descriptive |
| Version | `0.1.0` | Semver (major.minor.patch) |
| Marketplace URL | `https://marketplace.example.com/plugins` | Where it will be published |
| Technical lead | Jane Smith | Contact for support |
| Description | "Org-wide SSDLC governance" | One-line summary |

**GENERATE:** `.claude-plugin/plugin.json`

**VERIFY:** `claude plugin validate enterprise`

---

## Section 2: MCP Server Policy

**What to fill:**

| Field | Answer |
|---|---|
| Route A or B? | A = MDM, B = Admin console (from section 0.2) |
| Approved servers | List: GitHub, Jira, Datadog, etc. |
| Denied servers | List: Nothing? Or specific external vendors? |
| Updates allowed? | Manual only, or auto-update? |

**GENERATE:** `managed/managed-mcp.json` (Route A) or `managed-mcp-via-settings.json` (Route B)

**VERIFY:** `ls -la managed/managed-mcp*.json` (file exists)

---

## Section 3: Execution Boundary (Permission Denies)

**What to fill:**

This section defines what Claude Code **cannot** do:

| Policy | Value | Example |
|---|---|---|
| Permission mode | `read` or `write` | `read` = read-only |
| Denied tools | List | Bash (all), WebFetch (all), Artifact (all) |
| Allowed tools | List | Read, Edit, Agent |
| Max tokens per session | Number | 50000 |
| Max context age | Days | 7 |

**GENERATE:** `managed/managed-settings.json` (permissions block)

**VERIFY:** `grep -A 10 '"permissionMode"' managed/managed-settings.json`

---

## Section 4: Enterprise Instructions

**What to fill:**

| Field | Answer |
|---|---|
| One-liner purpose | "Org-wide SSDLC governance for secure development" |
| For whom | "All applications across RRD" |
| Key constraints | "Read-only + hook gates on tool use" |
| Reference docs | Links to architecture, rules, etc. |

**GENERATE:** `enterprise/CLAUDE.md`

**VERIFY:** `head -20 enterprise/CLAUDE.md` (readable content)

---

## Section 5: Rules Library

**What to fill:**

For each stack (Java, Node.js, Python, Go, etc.):

| Rule File | Language Globs | Specifics |
|---|---|---|
| `secure-coding.md` | `**/*.java, **/*.js, **/*.py` | Parameterized queries, no hardcoded secrets |
| `database-policy.md` | `backend/**/*.java` | JPA only, no native SQL |
| `api-security.md` | `backend/**/*.java` | HTTPS, rate limiting, input validation |
| `testing-standards.md` | All | Minimum 80% coverage |
| `container-security.md` | `Dockerfile, *.yaml` | Minimal base images, scan CVEs |
| `dependency-management.md` | `pom.xml, package.json, requirements.txt` | CVE scanning, EOL versions blocked |

**GENERATE:** `enterprise/rules/` (5 files)

**VERIFY:** `ls -la enterprise/rules/` (all files present)

---

## Section 6: Agent Roles

**What to fill:**

| Role | Enabled? | Tools | Purpose |
|---|---|---|---|
| Explorer | YES | Read, Bash (grep/find) | Fast codebase search |
| Reviewer | YES | Read, Bash | Code quality checks |
| Verifier | YES | Read | Adversarial verification |
| Vuln-Analyst | YES | Read, WebFetch | Security vulnerability analysis |
| Container-Assessor | YES | Read, Bash | Container hardening |

**GENERATE:** `enterprise/agents/` (5 files)

**VERIFY:** `ls -la enterprise/agents/` (all roles present)

---

## Section 7: Memory Tiers

**What to fill:**

| Tier | Description | Lifetime | Scope |
|---|---|---|---|
| Session | Session-local memory | One Claude Code session | Current session only |
| Project | Project-level memory | Across sessions in one repo | One repository |
| Org | Organization-wide memory | Across all projects | All repositories |

**Notes:** (from section 0.7, you already have tier definitions)

**GENERATE:** Notes in `enterprise/CLAUDE.md`

**VERIFY:** Review memory tier structure for completeness

---

## Section 8: Hooks

**What to fill:**

| Hook | Script | Purpose | Required? |
|---|---|---|---|
| session-start | `session-start.sh` | Check Java, Node, git config | YES |
| pre-tool-use | `pre-tool-use.sh` | Validate permissions, block .env edits | YES |

**Script content:**
- `session-start.sh` — Exit 0 if OK, exit 1 if missing prerequisites
- `pre-tool-use.sh` — Check tool/file, block if dangerous

**GENERATE:** `enterprise/hooks/` (2 scripts)

**VERIFY:**
```bash
bash enterprise/hooks/session-start.sh
# Expected: ✅ Setup complete, exit 0
```

---

## Section 9: Skills + Evals

**What to fill:**

| Skill | Description | Included? |
|---|---|---|
| advisory-writeup | Format security advisories | YES |
| vuln-patch-triage | Prioritize patches | YES |
| containerization-assessment | Hardening guidance | YES |
| receipt-check | Verify compliance | YES |
| repo-onboarding-brief | New repo orientation | YES |

**Evals:**
- Security eval (CVE scanning tests)
- Code quality eval (SAST, linting)
- Compliance eval (regulatory checks)

**GENERATE:** `enterprise/skills/*/SKILL.md` + `enterprise/evals/`

**VERIFY:** `ls -la enterprise/skills/` (all present)

---

## Section 10: Observability

**What to fill:**

| Field | Value |
|---|---|
| OTLP endpoint | `https://otel.example.com:4317` |
| Trace sampling | 100% or percentage |
| Logs retention | Days |
| Metrics endpoint | URL or "none" |

**GENERATE:** Environment block in `managed/managed-settings.json`

**VERIFY:** `grep OTEL managed/managed-settings.json`

---

## Section 11: Sign-Off

**Fill in and archive:**

```markdown
**Completed by:** [Technical Lead Name]
**Date:** [YYYY-MM-DD]
**Enterprise plugin version published:** 0.1.0
**Open items still outstanding:** [List or "none"]

Signatures:
Technical Lead: ________________  Date: ______
Security Team: ________________  Date: ______
Infrastructure: ________________  Date: ______
Enterprise Governance: ________________  Date: ______
```

---

## After All Sections

1. **Validate:**
   ```bash
   cd enterprise
   claude plugin validate .
   # Expected: No errors
   ```

2. **Deploy managed settings** (see `deployment.md`)

3. **Publish to marketplace** (see `publishing.md`)

4. **Record version number** (e.g., 0.1.0) for applications

---

## Quick Checklist

- [ ] Section 0 answered (gating decisions)
- [ ] If 0.6 or 0.7 is "no", escalated ⚠️
- [ ] Sections 1-10 filled
- [ ] All GENERATE steps completed
- [ ] All VERIFY steps passed
- [ ] Plugin validated: `claude plugin validate enterprise`
- [ ] Version recorded
- [ ] Section 11 signed and archived

---

## Common Issues

| Issue | Fix |
|---|---|
| "0.6 or 0.7 is no" | Escalate to leadership; don't proceed until answered |
| Validation error in plugin.json | Check JSON syntax (use `jq enterprise/.claude-plugin/plugin.json`) |
| Don't know what to put in section X | Read `deployment.md` for full procedures, or escalate to enterprise team |

---

## Next Steps

1. **Complete section 0** (gating decisions)
2. **Fill sections 1-10**
3. **Deploy** (see `deployment.md`)
4. **Publish** (see `publishing.md`)
5. **Verify** (see `../../VERIFY.md`)

---

**See also:** `deployment.md`, `publishing.md`, `troubleshooting.md`
