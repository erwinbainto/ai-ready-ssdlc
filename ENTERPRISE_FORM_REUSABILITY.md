# Enterprise Form Reusability: One Form, All Applications

This document clarifies that the completed `D4_Enterprise_Harness_Form.md` is **reusable for all applications** in your organization.

**TL;DR:** Fill the enterprise form ONCE. Use that same completed form as the source for ALL applications and projects in RRD.

---

## The Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│        D4_ENTERPRISE_HARNESS_FORM.md (Filled Once)         │
│                                                             │
│  Section 0: Gating decisions                               │
│  Section 1: Plugin identity (name: ai-ready-ssdlc-harness) │
│  Section 2: MCP catalogue (GitHub, Jira, CI/CD, etc.)      │
│  Section 3: Permission deny list                           │
│  Section 4: Enterprise instructions                        │
│  Section 5: Rules library                                  │
│  Section 6: Agent roles                                    │
│  Section 7: Memory tiers                                   │
│  Section 8: Hooks                                          │
│  Section 9: Skills                                         │
│  Section 10: Observability                                 │
│                                                             │
│  VERSION: 0.1.0                                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                    ↓ creates ↓
┌─────────────────────────────────────────────────────────────┐
│  enterprise/                                                │
│  ├─ .claude-plugin/plugin.json (name, version: 0.1.0)      │
│  ├─ managed/managed-settings.json (denies, hooks)          │
│  ├─ managed/managed-mcp.json (catalogue)                   │
│  ├─ CLAUDE.md (enterprise instructions)                    │
│  ├─ rules/ (5 standard rules)                              │
│  ├─ agents/ (5 roles)                                      │
│  ├─ skills/ (5 capabilities)                               │
│  ├─ hooks/ (SessionStart, PreToolUse)                      │
│  └─ evals/ (eval templates)                                │
│                                                             │
│  Published as plugin version: 0.1.0                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                    ↓ inherited by all ↓
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  All applications inherit from the SAME enterprise form:    │
│                                                              │
│  ✓ App 1 (my-api)                                           │
│    D4_Application_Harness_Form.md section 0 cites:          │
│    "Enterprise plugin version inherited: 0.1.0"             │
│                                                              │
│  ✓ App 2 (my-web)                                           │
│    D4_Application_Harness_Form.md section 0 cites:          │
│    "Enterprise plugin version inherited: 0.1.0"             │
│                                                              │
│  ✓ App 3 (my-batch)                                         │
│    D4_Application_Harness_Form.md section 0 cites:          │
│    "Enterprise plugin version inherited: 0.1.0"             │
│                                                              │
│  ✓ App N (any new app)                                      │
│    D4_Application_Harness_Form.md section 0 cites:          │
│    "Enterprise plugin version inherited: 0.1.0"             │
│                                                              │
│  All apps get the SAME:                                     │
│  • Plugin (ai-ready-ssdlc-harness v0.1.0)                   │
│  • MCP catalogue (GitHub, Jira, CI/CD, etc.)                │
│  • Permission deny list (Write, Edit, Read(.env), etc.)     │
│  • Standards and rules                                      │
│  • Agents and skills                                        │
│  • Hooks and observability                                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Timeline: How It Works

### Week 1: Fill Enterprise Form (Once)

```
Technical Lead fills D4_Enterprise_Harness_Form.md
├─ Answers sections 0-10
├─ Section 0 gating decisions: routing, MDM, retention, hooks, etc.
├─ Section 1: Plugin name (ai-ready-ssdlc-harness), version (0.1.0)
├─ Section 2: MCP catalogue (GitHub, Jira, CI/CD, Docs, Datadog)
├─ Section 3: Permission deny list (Write, Edit, git commit, etc.)
├─ Sections 4-10: Standards, rules, agents, skills, hooks, evals
└─ RESULT: Completed enterprise form is the SOURCE OF TRUTH

Technical Lead generates enterprise/ artefacts
├─ Uses form values to create files
├─ Validates plugin: claude plugin validate enterprise
├─ Deploys managed/ to system path
├─ Publishes plugin to marketplace
├─ Records version: 0.1.0
└─ RESULT: Enterprise harness deployed, version 0.1.0 published
```

### Week 2: App 1 Form (Uses Same Enterprise Form)

```
Dev Lead fills D4_Application_Harness_Form.md for App 1
├─ Section 0: "Enterprise plugin version inherited: 0.1.0" ← from enterprise form
│  (Same enterprise form is the source)
├─ Section 1: App 1 instructions
├─ Section 2: App 1 knowledge connection
├─ Sections 3-10: App 1 configuration
└─ RESULT: App 1 configured to inherit from enterprise form v0.1.0

App 1 deployed
├─ Inherits: plugin v0.1.0, MCP catalogue, deny list, standards
├─ Customizes: narrowed permissions, enabled roles, knowledge connection
└─ RESULT: App 1 running with enterprise policy
```

### Week 3: App 2 Form (Uses SAME Enterprise Form)

```
Dev Lead fills D4_Application_Harness_Form.md for App 2
├─ Section 0: "Enterprise plugin version inherited: 0.1.0" ← SAME enterprise form
│  (Not a new form, same version 0.1.0)
├─ Section 1: App 2 instructions
├─ Section 2: App 2 knowledge connection
├─ Sections 3-10: App 2 configuration
└─ RESULT: App 2 configured to inherit from enterprise form v0.1.0

App 2 deployed
├─ Inherits: plugin v0.1.0, MCP catalogue, deny list, standards (SAME as App 1)
├─ Customizes: narrowed permissions, enabled roles, knowledge connection (UNIQUE)
└─ RESULT: App 2 running with same enterprise policy as App 1
```

### Week 4+: App N Form (Uses SAME Enterprise Form)

```
For every new application:
├─ Dev Lead fills D4_Application_Harness_Form.md for App N
├─ Section 0: "Enterprise plugin version inherited: 0.1.0" ← SAME enterprise form
├─ Fill app-specific sections
└─ All apps inherit the SAME enterprise form values
```

---

## One Completed Enterprise Form → Multiple Applications

### Example: Completed Enterprise Form (Reusable)

```markdown
# D4_Enterprise_Harness_Form.md (Completed and Reusable)

## 0. Decisions that gate everything

| Decision | Your answer |
|---|---|
| 0.1 Gateway routing | no |
| 0.2 Device management | yes |
| 0.3 Transcript retention | 30 days |
| 0.4 Pod hooks permitted | managed only |
| 0.5 Marketplaces | https://marketplace.internal |
| 0.6 KPIs frozen | yes |
| 0.7 Memory tiers | yes |

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

(Sections 4-10 filled...)

## 11. Publish and hand off

**Completed by** Technical Lead  
**Date** 2026-10-06  
**Plugin version published** 0.1.0
```

### This Same Form Used for All Applications

```markdown
# D4_Application_Harness_Form.md (App 1)

## 0. Application identity and prerequisites

| Field | Value |
|---|---|
| Application name | my-api |
| Enterprise plugin version inherited | 0.1.0 ← FROM ENTERPRISE FORM ABOVE |
| Dev Lead | Alice |
| Stack | Python 3.11 |

---

# D4_Application_Harness_Form.md (App 2)

## 0. Application identity and prerequisites

| Field | Value |
|---|---|
| Application name | my-web |
| Enterprise plugin version inherited | 0.1.0 ← SAME ENTERPRISE FORM |
| Dev Lead | Bob |
| Stack | TypeScript |

---

# D4_Application_Harness_Form.md (App 3)

## 0. Application identity and prerequisites

| Field | Value |
|---|---|
| Application name | my-batch |
| Enterprise plugin version inherited | 0.1.0 ← SAME ENTERPRISE FORM |
| Dev Lead | Carol |
| Stack | Go |

All cite the SAME enterprise form version (0.1.0)
```

---

## When Enterprise Form Changes

### Scenario: You need to update the enterprise form (months later)

**Question:** If I update the enterprise form (e.g., add a new rule), do I need to update all applications?

**Answer:** It depends on the change. Applications can stay on old versions or opt into new versions independently.

### Enterprise Update Timeline

```
Month 0: Deploy enterprise v1.0.0
├─ rrd-project1 → cites v1.0.0
├─ rrd-project2 → cites v1.0.0
└─ rrd-project3 → cites v1.0.0

Month 6: Business needs change, update enterprise form
├─ Edit D4_Enterprise_Harness_Form.md
├─ Bump version to v1.0.1 (or v2.0.0)
├─ Run GENERATE steps → create new enterprise/ files
├─ Validate: claude plugin validate enterprise
├─ Publish: claude plugin publish enterprise
└─ Result: v1.0.0 and v1.0.1 now both available
```

### Minor Update (v1.0.0 → v1.0.1)

**Changes:** Bug fixes, new skills added, documentation updates, non-breaking rule tweaks

**Impact:** Apps continue working on v1.0.0
- Update enterprise form
- Generate new enterprise/ artefacts
- Publish new version (1.0.1)
- **Applications can optionally update to v1.0.1 (or stay on v1.0.0)**
- **No breaking changes, no immediate action required**

**Rollout example:**
```
rrd-project1: v1.0.0 ✓ Still works fine
rrd-project2: v1.0.1 ✓ Upgraded (optional)
rrd-project3: v1.0.0 ✓ Still works fine
```

### Major Update (v1.0.0 → v2.0.0)

**Changes:** Breaking changes (new deny list, changed gating decisions, removed agent roles)

**Impact:** Apps must explicitly migrate
- Update enterprise form with breaking changes
- Bump version to 2.0.0
- Publish new version (2.0.0)
- **New applications automatically use v2.0.0**
- **Existing applications continue on v1.0.0 until they explicitly migrate**
- Organizations can run multiple major versions during transition

**Rollout example:**
```
rrd-project1: v1.0.0 ✓ Legacy (no changes needed)
rrd-project2: v1.0.0 ✓ Legacy (no changes needed)
rrd-project3: v2.0.0 ✓ New app, uses latest
rrd-project4: v2.0.0 ✓ New app, uses latest
(rrd-project1 can migrate to v2.0.0 when ready)
```

---

## How Applications Update to New Enterprise Version

When an app needs to update (rrd-project1 going from v1.0.0 to v1.0.1):

### Step 1: Update the Application Form

Edit `D4_Application_Harness_Form.md` **Section 0:**

**Before:**
```markdown
| Field | Value |
|---|---|
| Application name | rrd-project1 |
| Enterprise plugin version inherited | v1.0.0 |
```

**After:**
```markdown
| Field | Value |
|---|---|
| Application name | rrd-project1 |
| Enterprise plugin version inherited | v1.0.1 |  ← UPDATED
```

### Step 2: Check What Changed in Enterprise

Review the enterprise form changes:
- **Deny list changed?** → Update section 5 (Execution environment)
- **MCP catalogue changed?** → Update section 4 (Server bindings)
- **Agent roles changed?** → Update section 6 (Roles enabled)
- **New rules added?** → Review section 7 (Capability candidates)

### Step 3: Re-run GENERATE Steps

Follow the form's GENERATE steps for affected sections:
- If servers added/removed: re-run section 4 GENERATE
- If deny list changed: re-run section 5 GENERATE
- If agents changed: re-run section 6 GENERATE
- All other sections: run GENERATE to refresh

### Step 4: Verify

```bash
/status          # Shows new plugin version (v1.0.1)
/mcp             # Shows updated servers (if changed)
/context         # Shows updated CLAUDE.md
/doctor          # Confirms no problems
```

### Step 5: Test

- Run your app's baseline commands (make test, etc.)
- Confirm narrowed permissions still work
- Check that write-attempt test still fails (read-only boundary intact)

**Result:** rrd-project1 now inherits v1.0.1. No code changes needed — only form updates.

---

## Key Principles

### 1. **One Enterprise Form Per Organization**

```
NOT this (wrong):
├─ enterprise-form-for-team-a.md
├─ enterprise-form-for-team-b.md
├─ enterprise-form-for-team-c.md

DO this (correct):
└─ D4_Enterprise_Harness_Form.md (one form, all teams use it)
```

### 2. **Versioning Tracks the Form**

```
Enterprise form version = plugin version

D4_Enterprise_Harness_Form.md section 1:
  "Version: 0.1.0"

Published plugin:
  "name": "ai-ready-ssdlc-harness"
  "version": "0.1.0"

All applications cite this version:
  App 1: "Enterprise plugin version inherited: 0.1.0"
  App 2: "Enterprise plugin version inherited: 0.1.0"
  App 3: "Enterprise plugin version inherited: 0.1.0"
```

### 3. **Applications Inherit, Not Copy**

```
NOT this (wrong):
├─ app1/.claude/CLAUDE.md (copies enterprise form content)
├─ app2/.claude/CLAUDE.md (copies enterprise form content)
├─ app3/.claude/CLAUDE.md (copies enterprise form content)
← Drift! Updates don't reach all apps

DO this (correct):
├─ enterprise/CLAUDE.md (source of truth from enterprise form)
├─ app1/.claude/CLAUDE.md (references enterprise, adds app-specific)
├─ app2/.claude/CLAUDE.md (references enterprise, adds app-specific)
├─ app3/.claude/CLAUDE.md (references enterprise, adds app-specific)
← Synchronized! Updates reach all apps
```

### 4. **Enterprise Form is Organization-Wide Policy**

```
The enterprise form answers:
├─ How is Claude Code routed? (same for all apps)
├─ Is device management reliable? (same for all apps)
├─ What servers are permitted? (same for all apps)
├─ What tools are blocked? (same for all apps)
├─ What are the organization standards? (same for all apps)

Each application then answers:
├─ What's this app's name? (unique per app)
├─ What's this app's stack? (unique per app)
├─ What does this app do? (unique per app)
├─ What are this app's narrowed rules? (unique per app)
```

---

## Reusability at Scale

### Single Enterprise Form Serves Multiple Scenarios

```
One D4_Enterprise_Harness_Form.md (v0.1.0) serves:

├─ Payment Processing Apps
│  ├─ my-api (payment service)
│  ├─ settlement-service
│  └─ reconciliation-batch
│
├─ Customer Experience Apps
│  ├─ my-web (dashboard)
│  ├─ mobile-app
│  └─ admin-portal
│
├─ Data Platform
│  ├─ my-batch (metric aggregation)
│  ├─ data-ingestion
│  └─ analytics-engine
│
└─ Infrastructure Apps
   ├─ logging-service
   ├─ metrics-service
   └─ secrets-manager

All cite: "Enterprise plugin version inherited: 0.1.0"
All inherit: same MCP catalogue, deny list, standards
All customize: unique app configuration
```

---

## When to Update Enterprise Form

Update the enterprise form when:

| Scenario | Action | New Version |
|---|---|---|
| Add new rule (e.g., new secure coding standard) | Update section 5 | v0.1.1 |
| Add new skill or agent | Update section 6 or 9 | v0.1.1 |
| Change gating decision (e.g., different retention) | Update section 0 | v1.0.0 |
| Change MCP catalogue (add/remove server) | Update section 2 | v0.2.0 |
| Change permission deny list | Update section 3 | v1.0.0 |

**New applications automatically use the latest version.**

---

## Checklist: Reusable Enterprise Form

- [ ] **Create** D4_Enterprise_Harness_Form.md ONCE
- [ ] **Fill** sections 0-10 with organization policy
- [ ] **Generate** enterprise/ artefacts from form values
- [ ] **Publish** as plugin, record version (e.g., v0.1.0)
- [ ] **Store** completed form as organizational record
- [ ] **Reuse** this SAME form for all applications
- [ ] **Every app** cites the SAME enterprise version
- [ ] **Update** form only when organization policy changes
- [ ] **Version bump** when you publish updates
- [ ] **New apps** automatically use latest published version

---

## Summary

| Aspect | Detail |
|---|---|
| **How many times fill?** | ONCE (then reuse for all apps) |
| **Used by** | All applications in RRD |
| **Scope** | Organization-wide policy and standards |
| **Versioning** | One version (e.g., 0.1.0) for all apps citing it |
| **Updates** | When organization policy changes, bump version |
| **Per-app customization** | In application form, not enterprise form |
| **Inheritance** | All apps inherit from the SAME completed enterprise form |

---

## Related Documentation

- `DEPLOYMENT_GUIDE.md` — Phase 1: Enterprise setup (do ONCE)
- `ENTERPRISE_VS_APPLICATION.md` — What's shared vs. unique
- `D4_Enterprise_Harness_Form.md` — The form itself
- `D4_Application_Harness_Form.md` — Per-app form (cites enterprise version)

---

**Bottom Line:** Fill the enterprise form ONCE. Every application and project in RRD then uses that SAME completed form as the source of truth. No duplication, no drift, no copies. One form, all apps, perfect sync.
