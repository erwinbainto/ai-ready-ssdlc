# Enterprise Harness Guides

**Detailed how-to documentation for enterprise setup, deployment, and troubleshooting.**

These guides are **on-demand** (not auto-loaded). Reference them when setting up or updating the enterprise harness.

---

## Guides

### 1. Enterprise Setup Guide
**File:** `setup.md`

How to complete `D4_Enterprise_Harness_Form.md` sections 0-10.

**Topics:**
- Understanding gating decisions (section 0)
- Answering each section with examples
- Creating enterprise/ files
- Validation and verification
- Common errors and fixes

**Use this when:** Filling out the enterprise form for the first time.

### 2. Deployment Procedures
**File:** `deployment.md`

Step-by-step instructions for deploying managed settings to machines.

**Topics:**
- Route A (MDM + system path)
- Route B (Admin console)
- Testing on one machine
- Fleet rollout
- Verification procedures

**Use this when:** Ready to deploy `enterprise/managed/` to your organization.

### 3. Architecture Overview
**File:** `architecture.md`

What each folder in `enterprise/` contains and why.

**Topics:**
- `managed/` — System-level policies
- `agents/` — Five predefined roles
- `skills/` — Reusable workflows
- `rules/` — Organization standards
- `evals/` — Gate tests
- File purposes and when they're used

**Use this when:** Understanding the enterprise structure or planning changes.

### 4. Publishing & Versioning
**File:** `publishing.md`

How to publish the enterprise harness to the marketplace and manage versions.

**Topics:**
- Publishing to marketplace
- Version numbering (semver)
- Managing minor vs. major updates
- Multi-version coexistence
- Communicating changes to applications

**Use this when:** Publishing a new version or updating the existing one.

### 5. Troubleshooting
**File:** `troubleshooting.md`

Common issues, diagnosis, and solutions.

**Topics:**
- Plugin validation errors
- Managed settings not loading
- MCP server binding issues
- Permission policy not enforcing
- Hook execution failures
- Escalation procedures

**Use this when:** Something isn't working as expected.

### 6. Rules Library Reference
**File:** `rules-library.md`

Detailed guidance for each rule file in `enterprise/rules/`.

**Topics:**
- `secure-coding.md` — Language-agnostic security patterns
- `database-policy.md` — Query patterns, parameterization
- `api-security.md` — REST/gRPC security
- `testing-standards.md` — Minimum coverage, patterns
- `container-security.md` — Image hardening
- `dependency-management.md` — CVE scanning, EOL policies
- How to customize rules for your stack

**Use this when:** Creating or updating enterprise rules.

### 7. Agent Roles Reference
**File:** `agents-reference.md`

What each agent role does, when to use it, and how to customize.

**Topics:**
- **Explorer** — Fast search & code analysis (read-only)
- **Reviewer** — Code quality & consistency checks
- **Verifier** — Adversarial verification of findings
- **Vuln-Analyst** — Security vulnerability analysis
- **Container-Assessor** — Image scanning & hardening
- Tool access for each role
- When to invoke each role

**Use this when:** Understanding available roles or customizing access.

### 8. Skills Library Reference
**File:** `skills-reference.md`

What each seed skill does, how to invoke, and customization.

**Topics:**
- **Advisory-Writeup** — Format security advisories
- **Vuln-Patch-Triage** — Prioritize & plan patches
- **Containerization-Assessment** — Container hardening guidance
- **Receipt-Check** — Verify compliance evidence
- **Repo-Onboarding-Brief** — New repo orientation
- Invocation patterns
- Customization for your org

**Use this when:** Understanding or using enterprise skills.

### 9. Hooks Configuration
**File:** `hooks-configuration.md`

How to set up and customize enterprise lifecycle hooks.

**Topics:**
- `session-start.sh` — Prerequisites checking
- `pre-tool-use.sh` — Security gating
- Hook registration in managed settings
- Testing hooks
- Debugging hook failures
- Adding org-specific checks

**Use this when:** Configuring or modifying enterprise hooks.

### 10. MCP Server Management
**File:** `mcp-servers.md`

How to define, approve, and bind MCP servers.

**Topics:**
- What is MCP server catalogue
- Vetting servers for security & reliability
- Adding servers to catalogue
- Deployment via Route A or Route B
- Binding servers in applications
- Removing servers (breaking change)

**Use this when:** Adding/removing servers or managing the catalogue.

---

## Quick Navigation

### By Task

**"I'm setting up enterprise for the first time"**
→ Start with `setup.md`, then `deployment.md`

**"I need to update an enterprise rule"**
→ Read `architecture.md` (structure), then `rules-library.md` (detail)

**"Something's not working"**
→ Check `troubleshooting.md`

**"I need to publish a new version"**
→ Read `publishing.md`

**"I want to understand what agents/skills do"**
→ Read `agents-reference.md` and `skills-reference.md`

### By Role

**Technical Lead (setting up enterprise)**
1. `setup.md` — Complete the form
2. `deployment.md` — Deploy to machines
3. `publishing.md` — Publish to marketplace
4. `troubleshooting.md` — Fix any issues

**Security Team (reviewing policies)**
1. `architecture.md` — Understand structure
2. `rules-library.md` — Review each rule
3. `troubleshooting.md` — Check enforcement

**DevOps (deploying to fleet)**
1. `deployment.md` — Deployment procedures
2. `troubleshooting.md` — Troubleshoot issues

**Infrastructure (managing MCP servers)**
1. `mcp-servers.md` — Server management
2. `troubleshooting.md` — MCP issues

---

## Related Documentation

- **Quick Start:** `../../QUICK_START.md` — One-page command sequence
- **Deployment Guide:** `../../DEPLOYMENT_GUIDE.md` — Full procedures
- **Harness Guide:** `../../HARNESS_GUIDE.md` — Architecture overview
- **Enterprise Form:** `../../D4_Enterprise_Harness_Form.md` — Configuration form
- **Verification:** `../../VERIFY.md` — Post-deployment checks

---

## File Structure

```
enterprise/
├── docs/
│   ├── guides/
│   │   ├── README.md (you are here)
│   │   ├── setup.md
│   │   ├── deployment.md
│   │   ├── architecture.md
│   │   ├── publishing.md
│   │   ├── troubleshooting.md
│   │   ├── rules-library.md
│   │   ├── agents-reference.md
│   │   ├── skills-reference.md
│   │   ├── hooks-configuration.md
│   │   └── mcp-servers.md
│   │
│   └── (other documentation)
│
├── managed/
│   ├── managed-settings.json
│   └── managed-mcp.json
│
├── agents/
├── skills/
├── rules/
├── evals/
└── CLAUDE.md
```

---

## When to Use These Guides

| Scenario | Guide |
|---|---|
| First time setting up | `setup.md` + `deployment.md` |
| Need to add/remove rules | `rules-library.md` + `architecture.md` |
| Publishing new version | `publishing.md` |
| Deployment failed | `troubleshooting.md` + `deployment.md` |
| Want to understand structure | `architecture.md` |
| Need to customize hooks | `hooks-configuration.md` |
| Managing MCP servers | `mcp-servers.md` |
| Understanding agents/skills | `agents-reference.md` + `skills-reference.md` |

---

## Tips

1. **Start with the task, not the alphabet.** Use "When to Use" table above.
2. **Reference, not copy.** These guides reference the enterprise form and files; don't duplicate them.
3. **Keep guides current.** If the form changes, update relevant guides.
4. **Link to DEPLOYMENT_GUIDE.md for full procedures.** These guides are deep dives; the deployment guide has the overview.

---

**Maintained by:** Platform / Enterprise Team  
**Last Updated:** 2026-10-01  
**Questions?** See `troubleshooting.md` or escalate to enterprise team.
