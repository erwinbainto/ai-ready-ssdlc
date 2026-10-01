# D4 Forms and Automation

This guide explains how to use the D4 questionnaire forms to drive the harness deployment, and how to automate PowerPoint deck generation with `genbrief.py`.

## Overview

The D4 harness deployment is guided by two questionnaire forms:

1. **D4_Enterprise_Harness_Form.md** — Enterprise policy, configuration, and standards (completed once)
2. **D4_Application_Harness_Form.md** — Application identity, context, and narrowed configuration (completed per application)

Each form has embedded **GENERATE** steps that tell you which files to create and what values to put in them. The forms also include **VERIFY** steps that use Claude Code slash commands to confirm configuration.

## The forms as control

The forms serve multiple purposes:

- **Checklists**: every decision and required step
- **Evidence**: completed forms are your D4 deployment records
- **Data sources**: values flow from the form into the generated artefacts
- **Governance**: the structure ensures nothing is missed

A form is "complete" when:
- Every placeholder `<LIKE_THIS>` has a real value (or is explicitly marked "not applicable")
- Every GENERATE and VERIFY step is done
- The closeout checklist is signed and dated

Incomplete forms are still valid input to `genbrief.py`; they just show **NOT PROVIDED** so gaps are visible.

---

## Enterprise harness workflow

### Step 1: Answer gating decisions

Section 0 contains seven decisions that **gate everything else**. Answer these first:

| Decision | Impact |
|---|---|
| **0.1** Gateway routing (LLM gateway?) | Determines whether policy arrives via managed file or admin console |
| **0.2** Device management reliable? | Determines MCP deployment: Route A (exclusive) vs Route B (server-managed) |
| **0.3** Transcript retention days | Sets cleanup period in managed settings |
| **0.4** Pod hooks permitted? | Determines whether applications can add their own hooks |
| **0.5** Marketplace sources | Determines which plugin marketplaces are trusted |
| **0.6** KPIs frozen in D3? | **ESCALATE if no.** Baseline is required before deployment. |
| **0.7** Memory tiers agreed? | **ESCALATE if no.** Shared tier structure must be agreed before deployment. |

**If 0.6 or 0.7 is "no", stop here.** These block enterprise deployment and require stakeholder resolution.

### Step 2: Fill sections 1–10

Working with the technical lead, fill each section. The form tells you what to fill and what the values mean:

| Section | What to fill |
|---|---|
| 1 | Plugin identity: name, version, marketplace |
| 2 | Tool access policy: MCP server catalogue (Route A or B) |
| 3 | Execution boundary: permission deny list, allowed commands, credential reads to block |
| 4 | Enterprise instructions (CLAUDE.md) |
| 5 | Rules library: secure coding, testing, interfaces, containers (fill `<STACK>` globs) |
| 6 | Agent roles: confirm enablement and tool isolation |
| 7 | Memory tiers: confirm layout and retention |
| 8 | Hooks: SessionStart and PreToolUse (must run at managed tier) |
| 9 | Skills + evals: confirm skill shipment and eval gate settings |
| 10 | Observability: OTLP endpoint, telemetry, KPI alignment |

### Step 3: GENERATE and VERIFY

For each section, the form tells you what to generate:

```
**GENERATE** enterprise/.claude-plugin/plugin.json from section 1 values
**VERIFY** `claude plugin validate enterprise` in section 11
```

Follow these steps in order. When you see **VERIFY**, stop and run the command. Confirm the output before proceeding.

### Step 4: Publish

Section 11 is the publish checklist:

1. `claude plugin validate enterprise` — must pass
2. Deploy `enterprise/managed/` to one test machine
3. `/status` should show enterprise source
4. Publish to marketplace
5. **Record the published version** — every app form cites it

---

## Application harness workflow

### Step 1: Prerequisite

The enterprise plugin must be published and the version must be recorded. Do not start an application form without it.

### Step 2: Fill sections 0–10

Working with the dev lead, fill the application form:

| Section | What to fill | Notes |
|---|---|---|
| 0 | Application identity, stack, KPIs | Cites enterprise plugin version |
| 1 | Application instructions (CLAUDE.md) | References (never copies) enterprise |
| 2 | Knowledge connection: architecture, commands, glossary, hazards | Cannot be templated; draft with explorer, correct with dev lead |
| 3 | Sources indexed: code, specs, tests, ADRs, docs, etc. | Verification Q+A proves indexing worked |
| 4 | Server bindings from admitted catalogue | One test call per bound server |
| 5 | Execution environment + write-attempt test | Write test is the evidence of read-only |
| 6 | Roles, memory, hooks | Confirm which roles are enabled |
| 7 | Capability candidates | Log patterns as they appear |
| 8 | Verification + receipts | Command contract, traces, cost |
| 9 | Extension register | Everything this app did differently |
| 10 | D7 enablement environment | Lab exercises (if D7 is in scope) |

### Step 3: The knowledge connection (section 2)

This is the part that cannot be templated. It requires authoring with the team:

1. **Draft with the explorer agent**: `explorer` can generate initial architecture and glossary
2. **Correct with the dev lead**: they validate and fix it
3. **Iterate until accurate**: an uncorrected draft is worse than nothing

The explorer output goes into:
- `architecture.md` — business purpose, structure, interfaces, data, decisions
- `glossary.md` — terms with local meaning
- `hazards.md` — fragile areas, incident history, surprising behaviour
- `commands.md` — build, test, lint, type-check contract (with baseline)

### Step 4: GENERATE and VERIFY

For each section, the form tells you what to generate. Follow the steps in order.

**Critical section**: Section 5 (Execution environment) includes the **write-attempt test**:

```
What you attempted: <edit src/…>
How it was refused: <deny rule / hook>
Trace reference: <ref>
```

This is the evidence that the read-only boundary holds. It must be run and captured.

### Step 5: Close out

Complete the closeout checklist (section 11):

- [ ] Enterprise plugin installed and version cited
- [ ] Context pack complete and dev-lead-corrected
- [ ] CLAUDE.md references enterprise, duplicates nothing
- [ ] Servers bound, each with logged call
- [ ] Write-attempt test run, refusal captured
- [ ] Every indexed source has verification answer
- [ ] D3 KPIs instrumented and verified
- [ ] Extension register complete
- [ ] D7 lab prepared (if applicable)

Sign and date the form when complete.

---

## genbrief.py automation

### Purpose

`genbrief.py` reads completed D4 forms and generates a PowerPoint deck brief — an instruction file for Claude to create a visual presentation of the deployment.

The brief includes:
- Slide plan (what to show, in what order)
- Resolved values from both forms
- Per-application status profiles
- Open items and gaps (marked **NOT PROVIDED**)

### Usage

```bash
python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form.md \
  --apps D4_Application_Harness_Form2.md \
  --out D4_Harness_Deck_Brief.md
```

Parameters:
- `--enterprise` (required): path to the completed enterprise form
- `--apps` (required, repeatable): paths to application forms (up to 5)
- `--out` (optional): output file name (default: `D4_Harness_Deck_Brief.md`)

### Output

`D4_Harness_Deck_Brief.md` is structured instructions for Claude:

1. Visual language specification (white background, Accenture purple, Segoe UI)
2. Slide-by-slide plan (what content, where it comes from)
3. Resolved values from the forms (prefilled)
4. Placeholder markers (**NOT PROVIDED**) where forms had unset fields
5. Per-application status table
6. Open items checklist

### Workflow

1. Complete both forms (enterprise + applications)
2. Run `python3 genbrief.py` with the form files
3. Hand the brief to Claude: "Build a PowerPoint deck from this brief."
4. Claude generates the PPTX (or PDF)
5. Share with stakeholders

### Handling incomplete forms

`genbrief.py` is tolerant of incomplete forms. Values still marked `<...>` or other placeholders are carried through as **NOT PROVIDED**:

```
Enterprise layer — resolved values
- **Plugin**: ai-ready-ssdlc-harness version **NOT PROVIDED**
- **Technical lead**: **NOT PROVIDED**
```

This makes gaps visible in the brief so you know what needs to be filled before the deck is complete.

---

## Artifacts produced

### From D4_Enterprise_Harness_Form.md

| GENERATE step | Output | Used by |
|---|---|---|
| Section 1 | `enterprise/.claude-plugin/plugin.json` | Claude Code plugin system |
| Section 2 | `enterprise/managed/managed-mcp.json` (Route A) or managed-mcp-via-settings block | System policy |
| Section 3 | `enterprise/managed/managed-settings.json` (permissions, hooks) | System policy |
| Section 4 | `enterprise/CLAUDE.md` | All sessions using enterprise plugin |
| Section 5 | `enterprise/rules/*.md` (with filled `paths:` globs) | Path-scoped rule loading |
| Section 6 | `enterprise/agents/*.md` | Agent role definitions |
| Section 8 | `enterprise/hooks/*.sh` (chmod +x) | Session and tool-use lifecycle |
| Section 9 | `enterprise/skills/*/SKILL.md` and `enterprise/evals/` | Skill publication gates |

### From D4_Application_Harness_Form.md

| GENERATE step | Output | Used by |
|---|---|---|
| Section 1 | `<app>/CLAUDE.md` | App repository |
| Section 2a-d | `<app>/.claude/context/{architecture,commands,glossary,hazards}.md` | Knowledge connection |
| Section 4 | `<app>/.mcp.json` | MCP server bindings |
| Section 5 | `<app>/.claude/settings.json` and `.worktreeinclude` | Execution environment |
| Section 9 | `<app>/.claude/rules/10-app.md` | App-specific path-scoped rules |

### From genbrief.py

| Output | Used for |
|---|---|
| `D4_Harness_Deck_Brief.md` | PowerPoint deck generation instruction |

---

## Timeline and handoffs

```
Enterprise Lead          Application Team         Automation
     |                        |                         |
     | Form (D4 Enterprise)   |                         |
     | ────────────────────>  |                         |
     | [Tech lead fills]      |                         |
     |                        |                         |
     | GENERATE & VERIFY      |                         |
     | ────────────────────>  |                         |
     |                        |                         |
     | Publish plugin         |                         |
     | ────────────────────>  |                         |
     |                        |                         |
     |         Form (D4 App)  |                         |
     |         <──────────────  |                        |
     |         [Dev Lead fills]|                        |
     |                        |                         |
     |         GENERATE & VERIFY                        |
     |         ────────────── |                         |
     |                        |                         |
     |                        | Forms completed         |
     |                        | ───────────────────────> |
     |                        |                         |
     |                        | genbrief.py runs        |
     |                        | ───────────────────────>|
     |                        |                         |
     |                        | Deck brief produced     |
     |                        | <──────────────────────  |
     |                        |                         |
     |                        | Hand to Claude for      |
     |                        | PowerPoint generation   |
     |                        |                         |
```

---

## Tips and gotchas

### Forms and files

- **Placeholders left unset** are OK for `genbrief.py` (they show as NOT PROVIDED), but the actual harness files must have real values.
- **The GENERATE steps are not optional** — they tell you which files to create and what to put in them.
- **VERIFY steps should not be skipped** — they confirm the configuration actually loaded.

### The knowledge connection (section 2 of app form)

- **Cannot be templated**. It must be authored with the team.
- **Draft with explorer**: run `explorer` on the codebase to generate an initial brief
- **Correct with dev lead**: they validate and fix the draft
- **An uncorrected draft is worse than nothing** — it reads as authoritative but is wrong

### The write-attempt test (section 5 of app form)

- **This is the evidence** that the read-only boundary actually holds
- **Must be run manually**: attempt an edit, capture the refusal and trace reference
- **Verified with dev lead**: they confirm the boundary is correct before signing off
- **Do not skip this step** — it is the only proof that policy enforcement is real

### Policy and rules

- **Managed settings cannot be updated via plugin**. They must flow through system paths or admin console.
- **Application rules can only narrow, never widen** enterprise rules.
- **Hooks at managed tier only** if 0.4 is "managed only" — pod hooks won't run.

### genbrief.py

- **Tolerates incomplete forms** — shows NOT PROVIDED for unset fields
- **Up to 5 applications** — the script warns if more than 5 are supplied
- **Python 3 only** — uses standard library only (no external dependencies)
- **Output is instructions for Claude, not a final deck** — hand it to Claude to build the PPTX

---

## Related files

- `README.md` — Order of work and deployment overview
- `VERIFY.md` — Verification checklist (run after deployment)
- `CLAUDE.md` — Project guidance and working method
- `D4_How_To.html` — Visual guide to the harness approach
