# Deployment Guide: Enterprise + Application Setup

This guide walks you through the **correct order** for deploying the AI-Ready SSDLC harness. It covers both the enterprise layer (once) and the application layer (per application).

**TL;DR:** Enterprise FIRST (once), then Application (per app). Applications inherit from enterprise and cannot widen its policies.

---

## Table of Contents

1. [Deployment Order (Overview)](#deployment-order-overview)
2. [Phase 1: Enterprise Setup](#phase-1-enterprise-setup)
3. [Phase 2: Application Setup](#phase-2-application-setup)
4. [Phase 3: Post-Deployment Updates](#phase-3-post-deployment-updates-months-later)
5. [Verification](#verification)
6. [Common Mistakes](#common-mistakes)
7. [Timeline and Roles](#timeline-and-roles)

---

## Deployment Order (Overview)

### The Sequence

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  PHASE 1: ENTERPRISE SETUP (Once, by technical lead)   │
│                                                         │
│  1. Answer gating decisions (section 0)                │
│  2. Fill enterprise configuration (sections 1-10)      │
│  3. Generate enterprise/ files (GENERATE steps)        │
│  4. Validate and deploy (VERIFY steps)                 │
│  5. Publish to marketplace                             │
│  6. Record published version ← CRITICAL                │
│                                                         │
│  OUTPUT: Enterprise harness deployed, version recorded │
│                                                         │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  PHASE 2: APPLICATION SETUP (Per app, by dev lead)     │
│                                                         │
│  1. Cite enterprise version (section 0)                │
│  2. Complete app configuration (sections 1-10)         │
│  3. Draft knowledge connection (section 2)             │
│  4. Generate .claude/ files (GENERATE steps)           │
│  5. Copy template to app repo                          │
│  6. Run write-attempt test (section 5)                 │
│  7. Verify deployment (VERIFY steps)                   │
│  8. Sign closeout (section 11)                         │
│                                                         │
│  OUTPUT: App configured, evidence captured             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Why This Order Matters

**Enterprise MUST be first because:**

- Applications inherit enterprise permissions, hooks, agents, and skills
- Every application form must cite the enterprise plugin version
- Policy cannot be enforced if enterprise layer doesn't exist
- The MCP catalogue comes from enterprise
- Application rules can only narrow (never widen) enterprise rules

**If you try to do Application first:**

| What happens | Why it fails |
|---|---|
| Can't fill section 0 of app form | No enterprise version published yet |
| Can't bind MCP servers | Enterprise catalogue doesn't exist |
| Can't enable agent roles | Roles not defined yet |
| Can't use enterprise skills | Skills not published yet |
| Permissions won't load | Enterprise managed settings not deployed |

---

## Phase 1: Enterprise Setup

### Duration
**1-2 weeks** (depending on stakeholder alignment and testing)

### Who
**Technical lead** (author and owner)

### Roles involved
- Technical lead (author)
- Security team (policy review)
- Infrastructure team (deployment)
- Marketplace admin (publishing)

### Prerequisites
✅ Claude Code installed locally  
✅ Access to your marketplace  
✅ Authority to define policy (escalations may be needed)

### Step-by-step

#### **Step 1: Open the enterprise form**

```bash
open D4_Enterprise_Harness_Form.md
```

This is your checklist and questionnaire for the entire enterprise layer.

#### **Step 2: Answer gating decisions (Section 0) - START HERE**

**This section is critical.** The seven decisions here determine how everything else is deployed.

| Decision | Question | Impact |
|---|---|---|
| **0.1** | Is Claude Code routed through a client-controlled gateway? | Determines if policy arrives via managed file or admin console |
| **0.2** | Is device management (MDM) reliable across your fleet? | Determines MCP deployment route (A = exclusive vs B = server-managed) |
| **0.3** | Transcript retention days | Cleanup period for transcript storage |
| **0.4** | May applications add their own hooks? | Affects application flexibility |
| **0.5** | Which marketplace sources are permitted? | Trust model for plugins |
| **0.6** | KPI definitions frozen in D3? | **ESCALATE if "no"** — baseline required |
| **0.7** | Memory tier definitions agreed? | **ESCALATE if "no"** — shared structure required |

**Action:** Fill in each decision. If 0.6 or 0.7 is "no", stop and escalate before proceeding.

#### **Step 3: Fill sections 1-10**

For each section, you will:
1. **Read** the section heading and explanation
2. **Fill** the table rows with your organization's values
3. **Follow GENERATE** step to create the file
4. **Follow VERIFY** step to test it

**Sections overview:**

| Section | What to fill | Creates |
|---|---|---|
| **1** | Plugin identity (name, version, marketplace, tech lead) | `.claude-plugin/plugin.json` |
| **2** | Tool access policy (MCP servers, Route A or B) | `managed/managed-mcp.json` or managed-mcp-via-settings.json |
| **3** | Execution boundary (permission denies and allows) | `managed/managed-settings.json` (permissions block) |
| **4** | Enterprise instructions | `enterprise/CLAUDE.md` |
| **5** | Rules library (fill `<STACK>` globs and specifics) | `rules/*.md` (5 files) |
| **6** | Agent roles (confirm enablement and isolation) | `agents/*.md` (5 files) |
| **7** | Memory tiers (confirm layout) | Notes in `CLAUDE.md` |
| **8** | Hooks (SessionStart, PreToolUse) | `hooks/*.sh` (2 scripts) |
| **9** | Skills + evals (ship confirmation) | `skills/*/SKILL.md` + `evals/` |
| **10** | Observability (OTLP endpoint) | `managed-settings.json` (env block) |

**For each section:**

```
1. Read the section
2. Fill the table
3. Look for **GENERATE** instruction
   Example: "**GENERATE** enterprise/managed/managed-settings.json from these values"
   → Create that file with the values you just entered
4. Look for **VERIFY** instruction
   Example: "**VERIFY** `claude plugin validate enterprise`"
   → Run that command, confirm output
```

#### **Step 4: Validate the enterprise harness**

When all sections are complete:

```bash
cd enterprise
claude plugin validate .
```

**Expected output:** No errors. If there are errors, fix them (the validator will tell you what's wrong).

#### **Step 5: Deploy enterprise/managed/ (policy)**

The `managed/` folder contains tier 0 policy. It must reach the system, not the repository.

**Choose based on section 0.1 and 0.2:**

**Route A — Exclusive control (if MDM is reliable):**
```bash
# macOS:
cp enterprise/managed/managed-settings.json \
   /Library/Application\ Support/ClaudeCode/

cp enterprise/managed/managed-mcp.json \
   /Library/Application\ Support/ClaudeCode/

# Linux/WSL:
sudo cp enterprise/managed/managed-settings.json /etc/claude-code/
sudo cp enterprise/managed/managed-mcp.json /etc/claude-code/

# Windows:
copy enterprise\managed\managed-settings.json "C:\Program Files\ClaudeCode\"
copy enterprise\managed\managed-mcp.json "C:\Program Files\ClaudeCode\"
```

**Route B — Server-managed (if no MDM):**
```
Use admin console to deliver managed-settings.json
Merge managedMcpServers block from managed-mcp-via-settings.json into settings
```

#### **Step 6: Verify on one test machine**

Deploy to ONE machine first. Do not fleet-roll yet.

```bash
# On test machine with managed settings deployed
claude /status

# Expected output:
# Setting source: enterprise
# Permission mode: <your_policy>
```

If you don't see "enterprise" in setting sources, the managed settings didn't load. Debug before proceeding.

#### **Step 7: Publish to marketplace**

```bash
# From enterprise/ directory
claude plugin validate .

# If valid, publish
/plugin marketplace add <YOUR_MARKETPLACE_URL>

# Then install on your account
/plugin install ai-ready-ssdlc-harness@<YOUR_MARKETPLACE_NAME>
```

#### **Step 8: Record the published version**

**This is CRITICAL.** Every application form must cite this version.

```bash
# From enterprise/.claude-plugin/plugin.json, get the version:
{
  "name": "ai-ready-ssdlc-harness",
  "version": "0.1.0"  ← THIS NUMBER
}

# Or check plugin marketplace:
/plugin list ai-ready-ssdlc-harness
```

**Save this version.** You will need it when filling application forms.

Example: `0.1.0`

#### **Step 9: Run full verification (VERIFY.md)**

From the root of this project:

```bash
cat VERIFY.md

# Run each check:
/status                # Enterprise source appears
/context               # Enterprise CLAUDE.md loads
/mcp                   # Exactly admitted servers
/agents                # Five roles present
/skills                # Seed skills available
/hooks                 # Enterprise hooks registered
/doctor                # No setup problems
```

All checks should pass.

#### **Step 10: Complete and archive the enterprise form**

Section 11 is the sign-off:

```
**Completed by** <tech lead name>
**date** <date>
**Plugin version published** <version_number>  ← SAVE THIS
**Open items still outstanding** <list or "none">
```

**This completed form is your D4 Enterprise Layer Record.** Archive it.

### Enterprise Phase Complete ✅

**You now have:**
- ✅ Enterprise harness deployed
- ✅ Plugin published and versioned
- ✅ Policy active on managed machines
- ✅ Version number recorded for applications

**Next:** Applications can now be configured (Phase 2).

---

## Phase 2: Application Setup

### Duration
**3-5 days per application** (depending on complexity and knowledge connection authoring)

### Who
**Dev lead** + **FDE** (Framework Development Engineer)

### Roles involved
- Dev lead (author, repository expert)
- FDE (form and harness expert)
- Tech lead (extensions approval)
- Application owner (autonomy sign-off)

### Prerequisites
✅ Enterprise harness published (version number recorded)  
✅ Application repository exists  
✅ Dev lead familiar with the application  
✅ Team available to author knowledge connection

### Step-by-step

#### **Step 1: Open the application form**

```bash
open D4_Application_Harness_Form.md
```

This is your checklist for configuring one application.

#### **Step 2: Fill section 0 (Application identity)**

```
| Field | Value |
|---|---|
| Application name | <my-app> |
| Enterprise plugin version inherited | 0.1.0  ← FROM ENTERPRISE PHASE |
| RRD Dev Lead | <name> |
| Autonomy target | L0→L1 or L1→L2 |
| D3 KPIs frozen | <yes, reference> |
| Stack | <Python, Go, Node.js, etc.> |
```

**CRITICAL:** The "Enterprise plugin version inherited" must match the version published in Phase 1.

#### **Step 3: Fill sections 1-10**

**Like the enterprise form, for each section:**

1. **Read** the section and explanation
2. **Fill** the table rows
3. **Follow GENERATE** to create files
4. **Follow VERIFY** to test

**Section 1: Application instructions (CLAUDE.md)**

```
| Field | Value |
|---|---|
| One-line business purpose | <What the app does> |
| Entry points | <main(), HTTP handlers, etc.> |
| Named RRD approver | <who approves gated actions> |
| Local conventions | <rules unique to this app + why> |
```

**GENERATE:** `<app>/CLAUDE.md`  
**VERIFY:** `claude /context` shows app CLAUDE.md loaded

**Section 2: Knowledge connection (THE CRITICAL SECTION)**

**This section CANNOT be templated. It must be authored by the team.**

**Sub-section 2a: architecture.md**
- Business purpose (one paragraph)
- How it fits (upstream/downstream systems)
- Key components and responsibilities
- Interfaces (REST APIs, queues, etc.)
- Data and state ownership
- Architecture decisions
- Unowned or unclear components

**Sub-section 2b: commands.md**
```
| Purpose | Command | Passes today? |
|---|---|---|
| Build | make build | yes |
| Test | make test | yes |
| Lint | make lint | yes |
| Type check | make type-check | no |
```

**Baseline** (pre-existing failures):
```
Currently failing: type-check (fixture generator is broken)
```

**Sub-section 2c: glossary.md**
```
| Term | Means here | Does not mean |
|---|---|---|
| Tenant | Workspace | User |
| Shard | Data partition | Database |
```

**Sub-section 2d: hazards.md**
- Fragile areas (do not touch without review)
- Incident history (what happened, what we learned)
- Surprising behaviour (non-obvious aspects)
- Known debt (technical debt the team accepts)

**Workflow for section 2:**

```
1. Run the explorer agent:
   "Map this codebase. Tell me: business purpose, structure, 
    interfaces, data ownership, and unclear areas."

2. Collect explorer output

3. Dev lead corrects and validates:
   "Is this accurate? Add missing pieces. Clarify confused parts."

4. Finalize and incorporate into the form

5. Create the four context files from the corrected output
```

**Sections 3-10: Standard configuration**

| Section | What to fill | Example |
|---|---|---|
| **3** | Sources indexed (code, specs, tests, ADRs, docs, metrics, incidents) | GitHub repo, Jira, PagerDuty |
| **4** | Server bindings from admitted catalogue | GitHub, Jira, CI/CD system |
| **5** | Execution environment + WRITE-ATTEMPT TEST | Build/test commands, permission narrowing |
| **6** | Roles, memory, hooks | Which 5 roles enabled |
| **7** | Capability candidates | Log as patterns appear |
| **8** | Verification + receipts | Command outputs, traces, costs |
| **9** | Extension register | How this app differs from enterprise |
| **10** | D7 enablement (if applicable) | Lab exercises |

#### **Step 4: The write-attempt test (Section 5) - CRITICAL**

This is the **proof** that the read-only boundary actually works.

**What to do:**

```
1. In Claude Code, attempt to edit a file:
   
   Open a source file and try to edit it
   
2. You should get a REFUSAL (permission denied)

3. CAPTURE:
   - What you attempted: "edit src/main.py"
   - How it was refused: "Write denied by policy"
   - Trace reference: <from the error message>
   - Date: <today>

4. Put this in the form:

   | Field | Value |
   |---|---|
   | What you attempted | edit src/main.py |
   | How it was refused | Write denied by managed policy |
   | Trace reference | 2026-09-29T19:45:32Z-write-attempt-001 |
   | Verified with Dev Lead | 2026-09-29 |

5. This is your evidence that read-only boundary works
```

#### **Step 5: Generate application artefacts**

Follow the GENERATE steps for sections 1-10. They will tell you:

```
**GENERATE** <app>/.claude/settings.json from section 5 values
**GENERATE** <app>/.claude/context/commands.md from section 2b values
etc.
```

#### **Step 6: Copy application-template to app repo**

```bash
# From this project
cp -r application-template/* /path/to/app-repo/

# You now have:
/path/to/app-repo/
├── CLAUDE.md              (from GENERATE step section 1)
├── .mcp.json              (from GENERATE step section 4)
├── .worktreeinclude       (from GENERATE step section 5)
└── .claude/
    ├── settings.json      (from GENERATE step section 5)
    ├── context/           (from GENERATE step section 2)
    │   ├── commands.md    (from GENERATE step section 2b)
    │   ├── architecture.md (from GENERATE step section 2a)
    │   ├── glossary.md    (from GENERATE step section 2d)
    │   └── hazards.md     (from GENERATE step section 2c)
    ├── rules/
    │   └── 10-app.md      (from GENERATE step section 1)
    ├── agents/
    │   └── README.md      (uses enterprise roles)
    ├── skills/
    │   └── README.md      (uses enterprise skills)
    └── hooks/
        └── session-start.sh (optional, from GENERATE if needed)
```

#### **Step 7: Verify deployment**

```bash
# Inside the application repository
claude /status
# Should show: enterprise source + narrowed permissions

claude /context
# Should show: both enterprise and app CLAUDE.md loaded

claude /mcp
# Should show: enterprise catalogue + app bindings

claude /agents
# Should show: five roles enabled

claude /skills
# Should show: seed skills available

claude /hooks
# Should show: enterprise hooks + app hooks (if enabled)

# FINAL TEST: Attempt a write
# Should be refused (this is what you captured in section 5)
```

#### **Step 8: Complete closeout checklist (Section 11)**

```
Exit checklist — all must be true:
- [ ] Enterprise plugin installed, version cited
- [ ] Context pack complete and Dev-Lead-corrected
- [ ] CLAUDE.md references enterprise, duplicates nothing
- [ ] Servers bound from catalogue, each with logged call
- [ ] Write-attempt test run, refusal + trace captured
- [ ] Every indexed source has verification answer
- [ ] D3 KPIs instrumented and verified
- [ ] Extension register complete
- [ ] D7 lab prepared (if applicable)

Signatures:
FDE: ________________  Date: ______
Tech Lead (extensions): ________________  Date: ______
Dev Lead: ________________  Date: ______
App Owner: ________________  Date: ______
Enterprise version inherited: 0.1.0
```

### Application Phase Complete ✅

**You now have:**
- ✅ Application configured
- ✅ Knowledge connection authored and verified
- ✅ Servers bound from enterprise catalogue
- ✅ Write-attempt test passed and captured
- ✅ All verification checks passing
- ✅ Evidence documented in completed form

**Next:** Repeat Phase 2 for each additional application.

---

## Phase 3: Post-Deployment Updates (Months Later)

### Duration
**As needed** (when business policy changes)

### Scenario
6 months after deployment:
- Enterprise harness is live (v1.0.0)
- All applications cite v1.0.0
- Business requirement changes (e.g., new compliance rule, new MCP server)
- Need to update the enterprise layer
- Question: **How do applications get updated?**

### The Process

#### **3.1 Update the Enterprise Form**

Edit `D4_Enterprise_Harness_Form.md` with the new policy:

| Change | Sections affected |
|---|---|
| Add new rule | Section 5 |
| Add new MCP server | Section 2 |
| Change deny list | Section 3 |
| Change agent roles | Section 6 |
| Change gating decisions | Section 0 |

#### **3.2 Decide: Minor or Major Update?**

**Minor Update** (v1.0.0 → v1.0.1)
- Non-breaking changes: new skills, bug fixes, documentation
- Example: Add one new MCP server, clarify a rule
- **Applications can stay on v1.0.0 or opt into v1.0.1**
- No immediate action required for existing apps

**Major Update** (v1.0.0 → v2.0.0)
- Breaking changes: new deny list, changed gating decisions, removed roles
- Example: Change routing (gateway yes/no), remove MCP server
- **New applications use v2.0.0**
- **Existing applications stay on v1.0.0 until they migrate**

#### **3.3 Bump Version**

In `D4_Enterprise_Harness_Form.md` section 1:

```markdown
| Field | Value |
|---|---|
| Version | v1.0.1 |  ← Bumped from v1.0.0
```

#### **3.4 Publish New Plugin**

```bash
# Generate files with new version
# (Follow form's GENERATE steps for changed sections)

# Validate
cd enterprise
claude plugin validate .

# Publish
claude plugin publish enterprise
# Result: v1.0.1 now available in marketplace
```

**Both v1.0.0 and v1.0.1 now exist.** Applications choose which to use.

#### **3.5 Applications Update (Independent Decision)**

Each application decides whether to update:

**Option A: Stay on v1.0.0** (if v1.0.1 is minor update)
```
rrd-project1: v1.0.0 ✓ Still works (no changes needed)
```

**Option B: Update to v1.0.1** (optional for minor, required for major)

```bash
# Step 1: Open D4_Application_Harness_Form.md for that app
# Step 2: Update section 0

# BEFORE:
| Field | Value |
|---|---|
| Enterprise plugin version inherited | v1.0.0 |

# AFTER:
| Field | Value |
|---|---|
| Enterprise plugin version inherited | v1.0.1 |  ← Updated
```

**Step 3: Check what changed in enterprise**

Ask: What sections changed?
- Section 2 (MCP servers)? → Review and update app section 4 (Server bindings)
- Section 3 (deny list)? → Review and update app section 5 (Execution environment)
- Section 5 (rules)? → Review app rules for conflicts
- Section 6 (agents)? → Review app section 6 (Roles enabled)

**Step 4: Re-run affected GENERATE steps**

For each changed section:
```
**GENERATE** <app>/.claude/settings.json from updated values
**GENERATE** <app>/.claude/context/ if architecture changed
etc.
```

**Step 5: Verify in the app**

```bash
cd rrd-project1
claude /status          # Shows new plugin version (v1.0.1)
claude /mcp             # Shows updated servers (if changed)
claude /context         # Shows updated CLAUDE.md
claude /doctor          # Confirms no problems
```

**Step 6: Test the app**

- Run baseline commands: `make test`, etc.
- Attempt write (should still be denied)
- Confirm app works with new policy

**Result:** rrd-project1 now inherits v1.0.1

#### **3.6 Multi-Version Coexistence**

Organizations can run multiple versions simultaneously:

```
Enterprise harness versions available:
├─ v1.0.0 (older, legacy)
├─ v1.0.1 (current)
└─ v2.0.0 (new, with breaking changes)

Applications using them:
├─ rrd-project1: v1.0.0 (legacy, not updated)
├─ rrd-project2: v1.0.1 (updated to current)
├─ rrd-project3: v2.0.0 (new app, uses new version)
└─ rrd-project4: v2.0.0 (new app, uses new version)
```

Each application controls which version it cites. No forced upgrades.

### Update Decision Tree

```
Enterprise needs updating
│
├─ Is it breaking? (gating decisions, deny list changes, agents removed)
│  ├─ YES → Major version (v1.0.0 → v2.0.0)
│  │        └─ Existing apps stay on old version
│  │        └─ New apps use new version
│  └─ NO → Minor version (v1.0.0 → v1.0.1)
│         └─ All apps can stay or update (optional)
│
└─ Publish to marketplace
   └─ Apps update their form section 0 when ready
```

### Common Update Scenarios

| Scenario | Version | Apps updated? |
|---|---|---|
| Add new skill | v1.0.1 | Optional (enhancement) |
| Fix bug in rule | v1.0.1 | Optional (fix) |
| Add new MCP server | v1.0.1 | Optional if not binding it |
| Remove MCP server | v2.0.0 | Required (breaking) |
| Change deny list | v2.0.0 | Required (breaking) |
| Add new agent role | v1.0.1 | Optional (enhancement) |
| Remove agent role | v2.0.0 | Required (breaking) |

### Checklist: Update Enterprise

- [ ] Update `D4_Enterprise_Harness_Form.md` with new values
- [ ] Decide: minor (v.patch) or major (v.minor)
- [ ] Bump version number in section 1
- [ ] Run GENERATE steps for changed sections
- [ ] Validate: `claude plugin validate enterprise`
- [ ] Publish: `claude plugin publish enterprise`
- [ ] Document changes (what's new, what broke)
- [ ] Notify app teams of new version

### Checklist: Update Application

- [ ] Review enterprise changes
- [ ] Update `D4_Application_Harness_Form.md` section 0 with new version
- [ ] Review sections 2-10 for conflicts
- [ ] Re-run GENERATE steps for affected sections
- [ ] Test in session: `/status`, `/mcp`, `/doctor`
- [ ] Run write-attempt test (should still fail)
- [ ] Update app form section 11 (new version cite)

---

## Verification

### After Enterprise Setup

Run these in a test session:

```bash
/status              # Shows: enterprise source, permission mode
/context             # Shows: enterprise CLAUDE.md
/mcp                 # Shows: exactly the admitted servers
/agents              # Shows: five roles
/skills              # Shows: five seed skills
/hooks               # Shows: SessionStart, PreToolUse
/doctor              # Shows: no problems
```

### After Application Setup

Run these in the application repository:

```bash
/status              # Shows: narrowed permissions for this app
/context             # Shows: enterprise + app CLAUDE.md
/mcp                 # Shows: enterprise catalogue + app bindings
/agents              # Shows: enabled roles
/skills              # Shows: available skills
/hooks               # Shows: enterprise + app hooks
```

**Write-attempt test** (from app form section 5):
```bash
# Attempt an edit
# Should see refusal
# Capture trace reference
# This is your evidence
```

### Full Verification Routine

See `VERIFY.md` for the complete checklist.

---

## Common Mistakes

### ❌ Mistake 1: Application before Enterprise

**What happens:**
- Can't fill enterprise plugin version (not published yet)
- MCP servers can't be bound (catalogue doesn't exist)
- Permissions won't enforce (policy not deployed)
- Write-attempt test fails without enterprise

**Fix:** Always do enterprise first.

### ❌ Mistake 2: Copying enterprise into application

**What happens:**
- Rules drift independently
- Updates don't propagate
- Contradictions appear later
- Governance breaks

**Fix:** Reference enterprise in application CLAUDE.md, never copy.

### ❌ Mistake 3: Widening application rules

**What happens:**
```
Enterprise CLAUDE.md says:
  "Do not use Docker from Docker Hub"

Application CLAUDE.md says:
  "OK to use Docker from Docker Hub"
```

Enterprise rule wins. But now governance is broken.

**Fix:** Application rules can only narrow (never widen) enterprise rules.

### ❌ Mistake 4: Leaving section 2 (knowledge connection) unreviewed

**What happens:**
- Drafted by explorer but never corrected
- Contains inaccuracies and wrong assumptions
- Reads as authoritative but is unreliable
- Agents make mistakes based on bad context

**Fix:** Draft with explorer, THEN correct with dev lead. Sign off only when accurate.

### ❌ Mistake 5: Not running the write-attempt test

**What happens:**
- No evidence that read-only boundary works
- Permission policy might not be enforcing
- Evidence for D4 deployment missing
- Governance claim is unsupported

**Fix:** Section 5 requires running the test. Capture the refusal + trace.

### ❌ Mistake 6: Not recording enterprise version

**What happens:**
- Application form can't cite version
- Can't prove which policy version each app inherited
- Deployment traceability lost
- Governance audit fails

**Fix:** Save the version from `.claude-plugin/plugin.json` (e.g., 0.1.0).

### ❌ Mistake 7: Not filling gating decisions (section 0 of enterprise)

**What happens:**
- Everything downstream gets wrong (routing, MDM, hooks policy)
- Policy doesn't reach machines
- Escalation issues discovered late
- Deployment blocked

**Fix:** Answer section 0 FIRST. If 0.6 or 0.7 is "no", escalate before proceeding.

---

## Timeline and Roles

### Example Timeline

```
Week 1-2: Enterprise Setup
│
├─ Day 1: Technical lead answers section 0 (gating decisions)
├─ Day 2-3: Fill sections 1-10, create enterprise/ files
├─ Day 4: Validate and deploy to test machine
├─ Day 5: Publish to marketplace, record version (0.1.0)
│
├─ Version recorded: 0.1.0 ✅
│
└─ READY FOR APPLICATIONS

Week 3-5: App 1 Setup
│
├─ Day 1: Dev lead + FDE open app form
├─ Day 1: Cite enterprise version (0.1.0)
├─ Day 2-3: Draft knowledge connection with explorer
├─ Day 3: Dev lead reviews and corrects
├─ Day 4: Complete configuration, run write-attempt test
├─ Day 5: Verify, sign closeout
│
└─ App 1 done ✅

Week 6-7: App 2 Setup
│
├─ (Repeat App 1 timeline)
│
└─ App 2 done ✅

... repeat for each application
```

### Roles and Responsibilities

| Role | Enterprise | Application | Frequency |
|---|---|---|---|
| **Technical Lead** | Author section 0-10, publish | Approve extensions | Once |
| **Dev Lead** | — | Author section 0-10, knowledge connection | Per app |
| **FDE** | Guide through process | Guide through process | Per app |
| **Security** | Review policy (section 3) | Review narrowed rules | Per app |
| **Infrastructure** | Deploy managed settings | — | Once |
| **Marketplace Admin** | Publish plugin | — | Once |
| **App Owner** | — | Sign autonomy | Per app |

---

## Quick Checklist

### Enterprise Phase Checklist

- [ ] Section 0 answered (gating decisions)
- [ ] If 0.6 or 0.7 is "no", escalated
- [ ] Sections 1-10 filled
- [ ] All GENERATE steps completed
- [ ] All VERIFY steps passed
- [ ] Plugin validated: `claude plugin validate .`
- [ ] `enterprise/managed/` deployed to system path
- [ ] Plugin published to marketplace
- [ ] **Version recorded** (e.g., 0.1.0)
- [ ] Full VERIFY.md routine passed on test machine
- [ ] Form completed and archived

### Application Phase Checklist (per app)

- [ ] Enterprise version cited in section 0
- [ ] Section 2 knowledge connection authored and reviewed
- [ ] Sections 1, 3-10 filled
- [ ] All GENERATE steps completed
- [ ] Application artefacts copied to app repo
- [ ] All VERIFY steps passed in app repo
- [ ] Write-attempt test run and captured
- [ ] Form completed and archived

### PowerPoint Deck Checklist (optional)

- [ ] Both forms completed
- [ ] `genbrief.py` run
- [ ] `D4_Harness_Deck_Brief.md` generated
- [ ] Brief handed to Claude for deck generation
- [ ] PPTX generated and shared

---

## Troubleshooting

| Problem | Check | Fix |
|---|---|---|
| Plugin won't validate | Run `claude plugin validate enterprise` | Check syntax in `.claude-plugin/plugin.json` |
| Enterprise source not in `/status` | Are managed settings in the right path? | Check `/Library/Application Support/ClaudeCode/` or `/etc/claude-code/` |
| App form won't accept enterprise version | Did you copy version exactly? | From `.claude-plugin/plugin.json`, e.g., "0.1.0" |
| Knowledge connection is inaccurate | Was it corrected by dev lead? | Have dev lead review and approve before signing off |
| Write-attempt test doesn't refuse | Are permissions loaded? | Run `claude /status`; show permission mode |
| Application rules say "widen" but seem OK | Are they actually narrowing? | Check that deny list is included, not replaced |

---

## Next Steps

1. **For enterprise:** Open `D4_Enterprise_Harness_Form.md`, answer section 0
2. **For application:** Wait for enterprise version, then open `D4_Application_Harness_Form.md`
3. **For PowerPoint deck:** After both forms completed, run `genbrief.py`

---

## Related Documentation

- `README.md` — Project overview
- `USAGE.md` — Quick reference and TL;DR
- `FORMS_AND_AUTOMATION.md` — Detailed forms guide
- `VERIFY.md` — Verification checklist
- `INDEX.md` — Complete project index
- `D4_How_To.html` — Visual guide (open in browser)

---

## Quick Commands Reference

```bash
# Enterprise validation
cd enterprise
claude plugin validate .

# Application verification (from app repo)
claude /status
claude /context
claude /mcp
claude /agents
claude /skills
claude /hooks
claude /doctor

# Generate PowerPoint brief
python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form.md
```

---

**Ready to start?** Begin with Phase 1: `D4_Enterprise_Harness_Form.md` section 0.
