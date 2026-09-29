# AI-Ready SSDLC Harness — Complete Project Index

## Project overview

This is a complete Claude Code harness kit for Secure Software Development Lifecycle (SSDLC). It provides:

- **Two-tier deployment**: Enterprise (once, as plugin) + Application (per app)
- **Questionnaire forms**: Guided workflows for configuration
- **Python automation**: PowerPoint deck generation from forms
- **Artefact templates**: Ready-to-use structures for agents, skills, rules, hooks

---

## Read these first

In this order:

1. **`README.md`** (3.8 KB)
   - High-level overview
   - What the harness does
   - Order of work
   - **Start here**

2. **`D4_How_To.html`** (13 KB)
   - Visual guide with diagrams
   - Shows the flow and architecture
   - Open in your browser

3. **`USAGE.md`** (9.1 KB)
   - Quick reference
   - TL;DR: the fastest path
   - Common workflows
   - Troubleshooting

---

## Main documentation

### Strategy and setup

- **`CLAUDE.md`** (7.7 KB)
  - Project guidance
  - How to complete the enterprise form
  - How to complete the application form
  - How to run genbrief.py
  - Key constraints and best practices

- **`FORMS_AND_AUTOMATION.md`** (14 KB)
  - Detailed guide to the forms workflow
  - Section-by-section walkthrough
  - genbrief.py explained
  - Artifacts produced
  - Timeline and handoffs
  - Tips and gotchas

- **`VERIFY.md`** (1.3 KB)
  - Post-deployment verification checklist
  - Claude Code slash commands to run
  - What good looks like for each check

### Forms (questionnaires)

- **`D4_Enterprise_Harness_Form.md`** (10 KB)
  - Fill once, by technical lead
  - 11 sections + gating decisions
  - Produces: enterprise layer artefacts
  - Every GENERATE and VERIFY step included
  - Scope: policy, configuration, standards

- **`D4_Application_Harness_Form.md`** (8.3 KB)
  - Fill once per application, by dev lead + FDE
  - 11 sections with closeout checklist
  - Produces: application tier 3 artefacts
  - Every GENERATE and VERIFY step included
  - Scope: application identity, context, narrowed config

### Automation

- **`genbrief.py`** (12 KB)
  - Python 3 script (no dependencies)
  - Reads: completed D4 forms
  - Generates: PowerPoint deck brief
  - Usage: `python3 genbrief.py --enterprise D4_Enterprise_Harness_Form.md --apps D4_Application_Harness_Form*.md`
  - Output: `D4_Harness_Deck_Brief.md` (instruction for Claude to build PPTX)

---

## Artefact directories

### `enterprise/` — Tier 0–1 (deployed once as plugin)

**Purpose**: Central policy, standards, and shared capabilities inherited by all applications.

**Structure**:
```
enterprise/
├── .claude-plugin/           plugin manifest (name, version, marketplace)
├── managed/                  tier 0 policy (system path, NOT in plugin)
│   ├── README.md            deployment routes (A = exclusive, B = server-managed)
│   ├── managed-settings.json permission deny list, hooks, telemetry
│   ├── managed-mcp.json     MCP server catalogue (Route A only)
│   └── managed-mcp-via-settings.json  (Route B variant)
├── CLAUDE.md                enterprise instructions (inherited by all apps)
├── rules/                   topic standards (5 files)
│   ├── 00-advisory-format.md   finding format (always loads)
│   ├── 10-secure-coding.md     injection, crypto, auth practices
│   ├── 20-testing.md           coverage, mocking, baselines
│   ├── 30-interfaces.md        API design, versioning
│   └── 40-containers.md        image security, manifests
├── agents/                  five agent roles (read-only, tool-scoped)
│   ├── explorer.md          map code, follow call paths
│   ├── reviewer.md          review for correctness & security
│   ├── verifier.md          run declared commands, report actual results
│   ├── vuln-analyst.md      patch advisory, reachability analysis
│   └── container-assessor.md containerization readiness
├── skills/                  reusable capabilities (folder-based)
│   ├── advisory-writeup/    format findings into five-part shape
│   ├── vuln-patch-triage/   vulnerability + patch analysis
│   ├── containerization-assessment/  gaps, effort, sequencing
│   ├── receipt-check/       verify claimed receipts
│   └── repo-onboarding-brief/  structured overview for new folks
├── hooks/                   lifecycle scripts (SessionStart, PreToolUse)
│   ├── session-start.sh     stamp app + version into trace
│   └── pre-tool-use.sh      log calls, block credential reads
├── evals/                   pre-publication test templates
│   └── vuln-patch-triage/   eval suite for patch advisory skill
└── README.md                enterprise layer overview

**Key files to fill from enterprise form**:
- Section 1 → `.claude-plugin/plugin.json` (name, version, author)
- Section 2 → `managed/managed-mcp.json` or managed-mcp-via-settings.json (MCP catalogue)
- Section 3 → `managed/managed-settings.json` (permissions, hooks, telemetry)
- Sections 4–10 → individual rule, agent, skill, hook files
```

### `application-template/` — Tier 3 (copied per app, narrowed from enterprise)

**Purpose**: Application-specific configuration, context, and narrowed rules.

**Structure**:
```
application-template/
├── CLAUDE.md                app instructions (references enterprise, never copies)
├── README.md                setup order
├── .mcp.json                server bindings from admitted catalogue (enterprise only)
├── .worktreeinclude         untracked files the build needs
└── .claude/
    ├── settings.json        narrowed permissions (never looser than enterprise)
    ├── context/             the knowledge connection (must be authored)
    │   ├── commands.md      build, test, lint, type-check contract + baseline
    │   ├── architecture.md  business purpose, structure, interfaces, data
    │   ├── glossary.md      domain terms (only local meanings)
    │   └── hazards.md       fragile areas, incidents, surprising behaviour
    ├── rules/
    │   └── 10-app.md        app-specific conventions (path-scoped)
    ├── agents/              (empty; uses enterprise roles)
    │   └── README.md
    ├── skills/              (empty; uses enterprise skills)
    │   └── README.md
    └── hooks/
        └── session-start.sh (optional app-specific hook)

**Key files to fill from app form**:
- Section 1 → `CLAUDE.md` (business purpose, entry points, narrowed rules)
- Section 2 → `.claude/context/*.md` (knowledge connection — cannot be templated)
- Section 4 → `.mcp.json` (servers from enterprise catalogue only)
- Section 5 → `.claude/settings.json` and `.worktreeinclude` (narrowed permissions)
- Section 9 → `.claude/rules/10-app.md` (app conventions)
```

---

## The workflow: from forms to deployment

### Enterprise layer (technical lead)

```
1. Open D4_Enterprise_Harness_Form.md
   ↓
2. Answer section 0 (gating decisions) — these gate everything
   ↓
3. Fill sections 1–10 with policy, standards, configuration
   ↓
4. Follow each section's GENERATE steps
   Each step tells you which file to create and what to put in it
   ↓
5. Follow each section's VERIFY steps
   Run Claude Code slash commands to confirm
   ↓
6. Publish (section 11)
   · Validate: claude plugin validate enterprise
   · Deploy: copy enterprise/managed/ to system path or admin console
   · Publish: to marketplace, record version
   ↓
7. Result: enterprise/ is deployed; version is recorded
```

### Application layer (dev lead + FDE)

```
1. Open D4_Application_Harness_Form.md
   ↓
2. Fill section 0 with app identity
   Must cite enterprise plugin version (from enterprise form)
   ↓
3. Fill section 2 (knowledge connection)
   This cannot be templated:
   · Run explorer agent on codebase (draft)
   · Dev lead corrects and validates (final)
   ↓
4. Fill sections 3–10 with app configuration
   ↓
5. Follow each section's GENERATE steps
   Each step tells you which file to create
   ↓
6. **Section 5 critical**: run write-attempt test
   Attempt an edit, capture the refusal + trace
   This is the evidence of read-only boundary
   ↓
7. Follow each section's VERIFY steps
   Run Claude Code slash commands
   ↓
8. Complete closeout checklist (section 11)
   Sign and date when done
   ↓
9. Result: app/.claude/ is configured; evidence is captured
```

### PowerPoint deck (optional, automation)

```
1. Both forms completed (enterprise + application)
   ↓
2. Run genbrief.py
   python3 genbrief.py --enterprise D4_Enterprise_Harness_Form.md --apps D4_Application_Harness_Form.md
   ↓
3. Generates: D4_Harness_Deck_Brief.md
   A structured instruction file for Claude
   ↓
4. Hand to Claude Code
   "Build a PowerPoint deck from this brief in the Claude Code Reference Architecture style"
   ↓
5. Result: D4_Harness_Deck_Brief.md is ready for Claude to build the PPTX
   Gaps appear as **NOT PROVIDED** so they're visible in review
```

---

## Key concepts

### Two tiers

- **Enterprise (tier 0–1)**: One plugin, deployed once, inherited by all apps
  - Policy, standards, agent roles, seed skills, hooks
  - Shipped as plugin; updates reach all apps at once
  
- **Application (tier 3)**: Per-application configuration
  - Application identity, context, narrowed rules
  - Copied to each app repo; can be customized locally

### Five agent roles

All read-only, tool-scoped:

| Role | Tools | Use for |
|---|---|---|
| `explorer` | Read, Grep, Glob | map code, where things live |
| `reviewer` | Read, Grep, Glob | whether something is sound |
| `verifier` | Read, Grep, Glob, Bash | actual build/test results (receipts) |
| `vuln-analyst` | Read, Grep, Glob | patch advisory, reachability |
| `container-assessor` | Read, Grep, Glob | containerization readiness |

### Five seed skills

Reusable capabilities:

| Skill | What it does |
|---|---|
| `repo-onboarding-brief` | structured overview for someone new to the codebase |
| `vuln-patch-triage` | vulnerability ticket → patch advisory + effort |
| `containerization-assessment` | how ready for containers, what's blocking |
| `receipt-check` | verify claimed test/build receipts are genuine |
| `advisory-writeup` | format raw findings into five-part advisory shape |

### Five rules (enterprise standards)

Template-filled with stack-specific content:

| Rule | Scope | Examples |
|---|---|---|
| `00-advisory-format` | findings format | always loads |
| `10-secure-coding` | language-specific | injection classes, crypto, auth |
| `20-testing` | testing standards | coverage, mocking, baselines |
| `30-interfaces` | API design | versioning, breaking changes |
| `40-containers` | containerization | base images, non-root, state |

### The knowledge connection

Application-specific context that **cannot be templated**. Must be authored with the team:

- `commands.md`: build, test, lint, type-check contract (+ baseline)
- `architecture.md`: business purpose, structure, interfaces, data ownership
- `glossary.md`: domain terms with local meaning
- `hazards.md`: fragile areas, incident history, surprising behaviour

**Workflow**: Draft with `explorer` agent → correct with dev lead → finalize

### The write-attempt test

Evidence that the read-only boundary actually holds. **Must be run and captured**:

```
Attempt: Edit a file
Refused: Policy denial or hook block
Trace: <reference_id>
Verified: <date> by dev lead
```

This is the only proof that enforcement is real.

---

## File manifest

```
/Users/erwin.t.bainto/ai_projects/ai-ready-ssdlc/

📄 Documentation
├── README.md                    Overview, order of work
├── CLAUDE.md                    Project guidance
├── FORMS_AND_AUTOMATION.md      Detailed forms workflow
├── USAGE.md                     Quick reference + TL;DR
├── VERIFY.md                    Post-deployment checklist
└── INDEX.md                     This file

📋 Forms (questionnaires)
├── D4_Enterprise_Harness_Form.md     Fill once (enterprise layer)
├── D4_Application_Harness_Form.md    Fill per application
└── D4_How_To.html                    Visual guide

🐍 Automation
└── genbrief.py                  PowerPoint deck brief generator

📁 Enterprise artefacts (tier 0–1)
└── enterprise/
    ├── .claude-plugin/
    ├── managed/                 (not in plugin; system path)
    ├── CLAUDE.md
    ├── rules/                   (5 standard files)
    ├── agents/                  (5 roles)
    ├── skills/                  (5 seed skills)
    ├── hooks/                   (SessionStart, PreToolUse)
    ├── evals/                   (eval templates)
    └── README.md

📁 Application template (tier 3)
└── application-template/
    ├── CLAUDE.md
    ├── README.md
    ├── .mcp.json
    ├── .worktreeinclude
    └── .claude/
        ├── settings.json
        ├── context/             (4 files)
        ├── rules/               (1 file)
        ├── agents/              (empty; uses enterprise)
        ├── skills/              (empty; uses enterprise)
        └── hooks/               (optional)
```

---

## Getting started

### For the enterprise technical lead

1. Open `D4_How_To.html` in your browser (visual walkthrough)
2. Read `README.md` (overview)
3. Read `USAGE.md` TL;DR section (fastest path)
4. Open `D4_Enterprise_Harness_Form.md`
5. Answer section 0 first (gating decisions)
6. Follow GENERATE and VERIFY steps

### For the application dev lead

1. Wait for enterprise plugin version to be published
2. Read `D4_How_To.html` (visual walkthrough)
3. Read `USAGE.md` "I'm configuring an application" section
4. Open `D4_Application_Harness_Form.md`
5. Fill section 0, cite enterprise version
6. Use `explorer` agent to draft section 2 (knowledge connection)
7. Follow GENERATE and VERIFY steps
8. Run write-attempt test (section 5) and capture evidence

### For anyone generating a PowerPoint deck

1. Complete both forms
2. Run: `python3 genbrief.py --enterprise D4_Enterprise_Harness_Form.md --apps D4_Application_Harness_Form.md`
3. Hand `D4_Harness_Deck_Brief.md` to Claude: "Build a PowerPoint deck from this brief"

---

## The forms as governance

Completed forms are your deployment records:

- **D4 Enterprise Layer Record**: enterprise form + published plugin version
- **D4 Application Instance Record**: application form + evidence (write-attempt test, receipts)

The forms serve as:

- **Checklists**: every required decision and step
- **Evidence**: completed forms are governance records
- **Bridges**: form values flow into generated artefacts via GENERATE steps
- **Audit trail**: who did what, when, why

An incomplete form is OK for `genbrief.py` (shows NOT PROVIDED), but the actual deployment requires all values filled.

---

## Key principles

1. **Never copy from enterprise.** Reference instead. Copied instructions drift within weeks.
2. **Application rules can only narrow enterprise rules, never widen them.**
3. **The knowledge connection cannot be templated.** It must be authored against the real codebase.
4. **The write-attempt test is the only proof.** Attempt an edit, capture the refusal.
5. **GENERATE and VERIFY steps are not optional.** They tell you what files to create and how to verify they work.
6. **Placeholders left unset are OK for genbrief.py.** They show as NOT PROVIDED so gaps are visible.
7. **Gating decisions (section 0) decide everything else.** Answer them first.

---

## Related resources

- `D4_How_To.html` — Open in browser for visual guide
- `VERIFY.md` — Verification checklist with Claude Code commands
- `enterprise/README.md` — Enterprise layer details
- `application-template/README.md` — Application setup order

---

## Quick commands

```bash
# Validate enterprise plugin
cd enterprise && claude plugin validate .

# Verify deployment (run after completing any form)
claude /status
claude /context
claude /mcp
claude /agents
claude /skills
claude /hooks

# Generate PowerPoint deck brief
python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form.md \
  D4_Application_Harness_Form2.md

# List all placeholders still needing values
grep -r '<.*>' D4_*.md | grep -v 'LIKE_THIS' | wc -l
```

---

**Ready to start?** Open `README.md` or `D4_How_To.html` next.
