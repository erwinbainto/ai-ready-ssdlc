# AI-Ready Secure SDLC Harness Artefacts

Claude Code artefacts for AI-Ready Secure Software Development Lifecycle (SSDLC). Two sets:

| Directory | What it is | Who deploys it | How often |
|---|---|---|---|
| `enterprise/` | Tier 0 and tier 1. Policy, admitted tool catalogue, shared instructions, agent roles, seed skills, hooks, eval templates | Once, centrally | One instance |
| `application-template/` | Tier 3. Copied into each application repository and completed | Per application | Multiple instances |

The enterprise set ships as a **plugin**. Pods install it rather than copying it, so an
update reaches every machine at once and nothing drifts.

## Forms and automation

Two questionnaire forms guide the harness deployment:

| Form | Purpose | Output | Role | Frequency |
|---|---|---|---|---|
| `D4_Enterprise_Harness_Form.md` | Captures enterprise policy decisions, configuration, and standards | Enterprise plugin artefacts | Technical lead | **Once** |
| `D4_Application_Harness_Form.md` | Captures application identity, context, and narrowed configuration | Application `.claude/` artefacts | Dev lead | **Once per app** |
| `genbrief.py` | Generates PowerPoint deck brief from completed forms | `D4_Harness_Deck_Brief.md` | Automation | After forms complete |

**Key principle:** Enterprise form is answered ONCE and applies to ALL applications. Application form is answered ONCE PER APP and customizes each application locally.

**Example references:**
- See `EXAMPLE_COMPLETED_ENTERPRISE_FORM.md` for a fully filled-out enterprise form with realistic values
- See `EXAMPLE_COMPLETED_APPLICATION_FORM.md` for a fully filled-out application form (references enterprise v0.1.0)
- Use them as templates when filling your own

**See these for guidance:**
- `ENTERPRISE_VS_APPLICATION.md` — what's shared vs. unique
- `ENTERPRISE_FORM_REUSABILITY.md` — how one form serves all apps

**Quick start:**
1. Review `EXAMPLE_COMPLETED_ENTERPRISE_FORM.md` to understand what a completed form looks like
2. Fill `D4_Enterprise_Harness_Form.md` with your organization's policy decisions → generates `enterprise/` files
3. Fill `D4_Application_Harness_Form.md` per app → generates app `.claude/` files
4. Run `python3 genbrief.py --enterprise D4_Enterprise_Harness_Form.md --apps D4_Application_Harness_Form*.md` to create a PowerPoint deck brief

See `D4_How_To.html` for the visual guide.

## Read this first

Placeholders are written `<LIKE_THIS>`. Every one must be replaced before deployment.
Anything left unreplaced is a draft.

Stack-specific content — language globs, build commands, language server selection — is
marked `<STACK>`. It cannot be completed without knowing the languages in scope.

## Order of work

⚠️ **IMPORTANT: Enterprise FIRST (once), then Application (per app)**

1. **Complete the enterprise form** (`D4_Enterprise_Harness_Form.md`) with the technical lead.
   - This form is **reusable for ALL applications** in RRD
   - Answer gating decisions (0.1–0.7) first; they gate everything
   - Fill sections 1–10 with policy, standards, configuration
   - Follow GENERATE and VERIFY steps for each section
   - **Do this ONCE — save the completed form**
   
2. **Validate and deploy** `enterprise/managed/` to the system path or admin console.

3. **Publish the enterprise plugin** from your marketplace; **record the version** (e.g., 0.1.0).

4. **For each application**, complete `D4_Application_Harness_Form.md` with the dev lead.
   - **Cite the enterprise plugin version** from step 3 in section 0
   - **Reference the completed enterprise form** — don't answer enterprise questions again
   - Fill sections 1–10 with **app-specific** configuration
   - Section 2 (knowledge connection) must be authored with the team
   - Follow GENERATE and VERIFY steps
   
5. **Copy `application-template/` to each app repo** and populate with form values.

6. **Verify both layers** with the routine in `VERIFY.md`.

7. **Generate the PowerPoint deck brief** (optional) using `genbrief.py` for stakeholder communication.

**See `DEPLOYMENT_GUIDE.md` for step-by-step instructions.**  
**See `ENTERPRISE_FORM_REUSABILITY.md` to understand: one enterprise form → all applications.**  
**See `DEPLOYMENT_GUIDE.md` Phase 3 for how to update enterprise and applications months later.**

## What this set does not do

It does not write the application context pack for you. `.claude/context/` is the knowledge
connection, and it has to be authored against the real codebase with the team that owns it.
The explorer agent can draft it; a human has to correct it.

## Forms as governance

The forms serve as:
- **Checklists**: every required decision and configuration step
- **Evidence**: completed forms are the D4 deployment records
- **Bridges**: form values flow into the generated artefacts via the GENERATE steps

A form is incomplete when placeholders remain (`<LIKE_THIS>`). `genbrief.py` marks these as "NOT PROVIDED" so gaps are visible.

## Syntax caution

Schema and key names change between Claude Code versions. Before relying on any file here,
run `claude plugin validate` on the enterprise plugin and `/doctor` in a session, and check
`/status`, `/mcp` and `/hooks` show what you expect. Treat a file that loads silently but
does nothing as the default failure mode.
