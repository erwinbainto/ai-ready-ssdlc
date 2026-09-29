# Quick Reference: Using the AI-Ready SSDLC Harness

## TL;DR — The fastest path

```bash
# 1. Complete the enterprise form
open D4_Enterprise_Harness_Form.md
# Fill sections 0–10 with policy decisions

# 2. Generate enterprise artefacts (form's GENERATE steps tell you which files)
# Example from section 1:
# → Create enterprise/.claude-plugin/plugin.json with form values

# 3. Validate and publish
cd enterprise
claude plugin validate .
# → Publish to marketplace, record version

# 4. Complete app form(s) per application
open D4_Application_Harness_Form.md
# Fill sections 0–10 with app identity and configuration

# 5. Generate app artefacts (form's GENERATE steps)
# Example from section 2:
# → Create .claude/context/commands.md with form values

# 6. Copy template to app repo
cp -r application-template/* /path/to/app-repo/.claude/

# 7. Verify
claude /status
claude /context
claude /mcp
# Run write-attempt test from form section 5

# 8. (Optional) Generate PowerPoint deck brief
python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form.md \
  --out D4_Harness_Deck_Brief.md
# → Hand D4_Harness_Deck_Brief.md to Claude for PowerPoint generation
```

---

## The forms: what they do

### D4_Enterprise_Harness_Form.md

**One per organization.** Captures policy decisions and configuration for the enterprise harness (tier 0–1).

**Critical sections:**
- **0**: Answer gating decisions *first*. They decide routing and deployment method.
- **2**: Choose MCP deployment route (A = exclusive, B = server-managed)
- **3**: Define the read-only boundary (what's denied, what's allowed)
- **11**: Publish and hand off

**Outputs files to:**
- `enterprise/.claude-plugin/` (plugin manifest)
- `enterprise/managed/` (tier 0 policy)
- `enterprise/CLAUDE.md` (enterprise instructions)
- `enterprise/rules/*.md` (standards)
- `enterprise/agents/*.md` (agent roles)
- `enterprise/hooks/*.sh` (lifecycle scripts)
- `enterprise/skills/*/SKILL.md` (reusable capabilities)

**Completed by:** Technical lead (once)

### D4_Application_Harness_Form.md

**One per application.** Captures application identity, context, and narrowed configuration for tier 3 artefacts.

**Critical sections:**
- **0**: Application identity. *Prerequisite*: enterprise plugin version must be cited.
- **2**: Knowledge connection (architecture, commands, glossary, hazards). Draft with explorer, correct with dev lead.
- **5**: Execution environment + write-attempt test (this proves read-only boundary).
- **11**: Close-out and sign-off

**Outputs files to:**
- `<app>/CLAUDE.md` (application instructions)
- `<app>/.claude/settings.json` (narrowed permissions)
- `<app>/.claude/context/*.md` (knowledge connection)
- `<app>/.mcp.json` (server bindings)

**Completed by:** Dev lead with FDE (once per app)

---

## The forms: how they work

### GENERATE and VERIFY

Each section tells you:

```
**GENERATE** enterprise/hooks/session-start.sh from these values
**VERIFY** /hooks in Claude Code; should show SessionStart registered
```

**GENERATE** means: create the file using the form values.
**VERIFY** means: run the command and confirm the output looks right.

### Placeholders

Form fields are written `<LIKE_THIS>`. Replace them with real values.

Examples:
```
| Field | Value |
| Plugin name | <rrd-harness> |  → replace with your org's plugin name
| Version | <0.1.0> |  → replace with your version
```

### Escalation

Some fields say **ESCALATE** if the answer is "no":

```
| Decision | 0.6: KPI definitions frozen in D3? | <yes / no> |
| Escalate if | no |
| Why | Nothing runs until baselines are frozen. |
```

Stop and resolve the issue before proceeding.

---

## The automation: genbrief.py

**Generates a PowerPoint deck brief from completed forms.**

### Usage

```bash
# Single application
python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form.md

# Multiple applications (up to 5)
python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form.md \
         D4_Application_Harness_Form2.md \
         D4_Application_Harness_Form3.md \
  --out D4_Harness_Deck_Brief.md
```

### What it does

1. Reads both form files
2. Parses markdown tables and values
3. Extracts key information (plugin name, version, app identity, etc.)
4. Generates a structured brief with slide plan and resolved values
5. Writes `D4_Harness_Deck_Brief.md`

### What to do with the output

```bash
# Hand to Claude Code
# "Build a PowerPoint deck from this brief in the Claude Code Reference Architecture style"
cat D4_Harness_Deck_Brief.md
```

Claude will generate a PPTX (or PDF) with the visual presentation ready to share.

---

## Common workflows

### "I'm starting the enterprise harness"

1. Open `D4_Enterprise_Harness_Form.md`
2. Answer section 0 (gating decisions) → determines everything else
3. If 0.6 or 0.7 is "no", ESCALATE and stop
4. Fill sections 1–10 with your organization's policy
5. Follow each section's **GENERATE** steps
6. After each GENERATE, follow the **VERIFY** step
7. When done, section 11 publishes the plugin
8. Record the published version for app forms

### "I'm configuring an application"

1. Wait for enterprise plugin to be published (need version number)
2. Open `D4_Application_Harness_Form.md`
3. Fill section 0 with app identity; cite enterprise version
4. **Section 2 cannot be templated**: 
   - Run `explorer` on the codebase to generate initial architecture
   - Dev lead corrects and validates it
   - Use the corrected version as section 2 input
5. Fill sections 3–10 with app configuration
6. Follow each section's **GENERATE** steps
7. **Section 5 is critical**: run the write-attempt test, capture the refusal
8. When done, section 11 is sign-off

### "I need to make a PowerPoint deck for stakeholders"

1. Complete both forms (enterprise + application)
2. Run `python3 genbrief.py --enterprise D4_Enterprise_Harness_Form.md --apps D4_Application_Harness_Form.md`
3. Hand `D4_Harness_Deck_Brief.md` to Claude Code: "Build a PowerPoint deck from this brief"
4. Claude generates the PPTX
5. Share with stakeholders

---

## Verification checklist

After completing each form, run these Claude Code commands:

### After enterprise form

```
/status               # Enterprise source should appear
/context              # Enterprise CLAUDE.md should load
/mcp                  # Exactly the admitted servers, nothing else
/agents               # Five roles present
/skills               # Seed skills available
/hooks                # Enterprise hooks registered
/doctor               # No unresolved findings
```

### After application form

```
/status               # Permission mode should show narrowed settings
/context              # Both enterprise and app CLAUDE.md
/mcp                  # App-bound servers plus enterprise catalogue
/agents               # Five roles enabled
/hooks                # App and enterprise hooks registered
```

**Write-attempt test** (from form section 5):
```
Edit a file (attempt any edit)
→ Should be refused with a trace reference
→ Capture the refusal + trace for form evidence
```

---

## Troubleshooting

| Problem | Check |
|---|---|
| Plugin won't validate | Run `claude plugin validate enterprise` for detailed error |
| Rules don't load | Check `paths:` glob in rule frontmatter matches your files |
| Agent won't run | `/agents` shows if it's registered; check tool permissions |
| MCP server doesn't work | `/mcp` shows if it's listed; try asking a real question to test |
| Write isn't refused | `/status` shows permission mode; run write-attempt test again |
| Placeholder values in output | Check form was actually filled (not left as `<...>`) |

---

## Updating Enterprise and Applications (Months Later)

### When Enterprise Needs Updating

**Scenario:** You've deployed v1.0.0. Six months later, policy changes (new rule, new server, compliance requirement).

### Quick Workflow: Update Enterprise

```bash
# 1. Open the enterprise form
open D4_Enterprise_Harness_Form.md

# 2. Update the sections that changed
#    Example: Section 2 (add new MCP server)

# 3. Bump the version
#    Section 1: v1.0.0 → v1.0.1 (or v2.0.0 if breaking)

# 4. Run GENERATE steps for changed sections

# 5. Validate and publish
cd enterprise
claude plugin validate .
claude plugin publish enterprise
# → v1.0.1 is now available

# 6. Notify app teams
#    "New enterprise version v1.0.1 available"
```

### Quick Workflow: Update an Application

**Each application decides independently whether to update.**

```bash
# 1. Open the app form
open D4_Application_Harness_Form.md

# 2. Update section 0
#    BEFORE: Enterprise plugin version inherited: v1.0.0
#    AFTER:  Enterprise plugin version inherited: v1.0.1

# 3. Review what changed in enterprise
#    Did deny list change? → Update section 5
#    Did servers change? → Update section 4
#    Did rules change? → Review section 7

# 4. Re-run GENERATE steps for affected sections

# 5. Verify in the app
cd /path/to/app-repo
claude /status          # Shows new version
claude /mcp             # Shows updated servers
claude /doctor          # Confirms no problems

# 6. Test the app
make test               # Baseline should pass
# Attempt edit → should still be denied (read-only works)
```

### Version Strategy

**Minor Update** (v1.0.0 → v1.0.1): Non-breaking
- New skills, bug fixes, clarifications
- Apps can stay on v1.0.0 or update (optional)

**Major Update** (v1.0.0 → v2.0.0): Breaking
- New deny list, changed gating, removed roles
- New apps use v2.0.0
- Existing apps stay on v1.0.0 (or migrate deliberately)

---

## Files in this project

| File | Purpose |
|---|---|
| `README.md` | Overview and deployment order |
| `CLAUDE.md` | Guidance for this project |
| `VERIFY.md` | Post-deployment verification checklist |
| `FORMS_AND_AUTOMATION.md` | Detailed guide (you're reading this) |
| `USAGE.md` | Quick reference (this file) |
| `D4_Enterprise_Harness_Form.md` | Enterprise questionnaire |
| `D4_Application_Harness_Form.md` | Application questionnaire |
| `D4_How_To.html` | Visual guide (open in browser) |
| `genbrief.py` | PowerPoint deck brief generator |
| `enterprise/` | Enterprise harness artefacts (tier 0–1) |
| `application-template/` | Application template (tier 3) |

---

## Next steps

1. **Read `D4_How_To.html`** in your browser — it's a visual walkthrough
2. **Start with the enterprise form** — follow the GENERATE and VERIFY steps
3. **For each app, use the application form** — sections 0–11
4. **Run `VERIFY.md`** after deployment
5. **(Optional) Use `genbrief.py`** to generate a PowerPoint deck brief

---

## Getting help

- **Form field doesn't make sense?** → Read the ` > ` explanation in that section
- **Don't know what value to use?** → The form tells you or points to where it's defined
- **GENERATE step unclear?** → It tells you which file to create and what to fill
- **VERIFY step fails?** → The command output will tell you what's wrong

The forms are designed to be self-guided. If you get stuck, the section containing the issue usually has context.
