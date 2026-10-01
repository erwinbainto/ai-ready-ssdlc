# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The AI-Ready SSDLC harness is a deployment kit for Secure Software Development Lifecycle. It configures Claude Code for governed, read-only operation across a fleet of applications. Two tiers:

- **Enterprise set** (`enterprise/`): Ships as a plugin. Deployed once, inherited by all applications. Tier 0–1 policy, agent roles, seed skills, lifecycle hooks.
- **Application template** (`application-template/`): Copied per application. Tier 3 context, narrowed rules, knowledge connection.

## Key files and roles

| File/Directory | Purpose |
|---|---|
| `README.md` | Start here. Deployment order and what each tier does |
| `VERIFY.md` | Verification checklist with Claude Code slash commands to confirm deployment |
| `enterprise/` | Enterprise plugin content: agents, skills, hooks, rules, managed settings |
| `application-template/` | Template for app repositories: CLAUDE.md, .mcp.json, .claude/settings.json, .claude/context/* |

## Common tasks

### Use the enterprise form

1. Open `D4_Enterprise_Harness_Form.md` with the technical lead
2. **Answer the gating decisions first** (section 0.1–0.7). These are critical:
   - 0.1: Gateway routing (determines policy delivery)
   - 0.2: Device management (determines MCP deployment route A vs B)
   - 0.6: KPI definitions frozen (blocks deployment if not)
   - 0.7: Memory tier definitions (blocks deployment if not)
3. Fill sections 1–10 with policy decisions, standards, and configuration values
4. **Follow the GENERATE steps** in each section to create the artefacts
5. Follow the VERIFY steps with Claude Code slash commands
6. Complete section 11 (Publish and hand off) to publish the plugin

**Key sections:**
- Section 0: Gating decisions (answer these first)
- Section 2: Tool access policy (route A or B)
- Section 3: Execution boundary (the read-only core)
- Section 5: Rules library (stack-dependent; fill language globs)
- Section 8: Hooks (PreToolUse is the credential guard; must run)

### Complete the enterprise harness

1. Fill `D4_Enterprise_Harness_Form.md` (form workflow above)
2. The form's GENERATE steps create the files; follow them in order
3. Validate plugin: `claude plugin validate enterprise`
4. Publish to marketplace: follow section 11 of the form

### Deploy the enterprise harness

1. Deploy `enterprise/managed/` to the system path (managed settings and MCP catalogue)
   - Route A (exclusive control, if device management is reliable): `/Library/Application Support/ClaudeCode/` (macOS)
   - Route B (server-managed via admin console, if no MDM): Use managed settings delivery
2. Verify on one machine: `/status` should show enterprise source
3. Confirm to fleet

### Use the application form

1. Open `D4_Application_Harness_Form.md` with the dev lead
2. **Prerequisite**: Enterprise plugin must be published; record its version in section 0
3. Fill sections 0–10:
   - Section 0: Application identity, stack, KPIs
   - Section 2: Knowledge connection (context/); use explorer agent to draft
   - Section 4: MCP server bindings (from admitted catalogue only)
   - Section 5: Execution environment and write-attempt test (this proves read-only boundary)
4. **Follow the GENERATE and VERIFY steps** in each section
5. Complete section 11 (Close-out checklist)

**Key sections:**
- Section 2: Knowledge connection (cannot be templated; must be authored with the team)
- Section 5: Write-attempt test (produces evidence of read-only boundary)

### Add an application

1. Fill `D4_Application_Harness_Form.md` (form workflow above)
2. Copy `application-template/` to the application repository root
3. The form's GENERATE steps populate `.claude/`
4. Complete `.claude/context/` with the team (use explorer to draft, dev lead to correct)
5. Run verification from `VERIFY.md`

### Generate the PowerPoint deck brief

```bash
python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form*.md \
  --out D4_Harness_Deck_Brief.md
```

The output (`D4_Harness_Deck_Brief.md`) is instructions and data for Claude to build a PowerPoint deck in the Claude Code Reference Architecture style. Unset form fields appear as **NOT PROVIDED** so gaps are visible in review.

## Architecture highlights

### Enterprise layer

- **Managed settings** (`enterprise/managed/`): Privileged policy applied via system path or admin console. Enforces permission mode, hook policy, MCP catalogue.
- **Agents** (`enterprise/agents/`): Five roles (explorer, reviewer, verifier, vuln-analyst, container-assessor), each tool-scoped.
- **Skills** (`enterprise/skills/`): Reusable capabilities (advisory-writeup, vuln-patch-triage, containerization-assessment, receipt-check, repo-onboarding-brief).
- **Rules** (`enterprise/rules/`): Topic guidance (advisory format, secure coding, testing, interfaces, containers).
- **Hooks** (`enterprise/hooks/`): Lifecycle scripts (session-start.sh, pre-tool-use.sh).
- **Evals** (`enterprise/evals/`): Test case templates for pre-publication gates.

### Application layer

- **Context** (`.claude/context/`): The knowledge connection. Commands, architecture, glossary, hazards. Must be authored with the team.
- **Rules** (`.claude/rules/`): App-specific guidance, path-scoped.
- **Settings** (`.claude/settings.json`): Permissions narrowed, hooks wired. Never looser than enterprise.
- **Agents** (`.claude/agents/`): Roles enabled for this app (usually empty; uses enterprise set).
- **Skills** (`.claude/skills/`): App-specific capabilities (usually empty; uses enterprise set).
- **Evals** (`evals/`): Reserved for future skill publication gates (WP2/D11). Empty in D4; see `evals/README.md` for the publication pattern.

## Verification workflow

After deployment or changes, run these Claude Code commands:

| Command | What it confirms |
|---|---|
| `/status` | Enterprise policy active; permission mode set |
| `/context` | Enterprise and application CLAUDE.md loaded |
| `/mcp` | Exactly the admitted servers, no unauthorized ones |
| `/agents` | Five roles present, each restricted to declared tools |
| `/skills` | Seed skills available |
| `/hooks` | Enterprise hooks registered |
| `/doctor` | No unresolved setup problems |

Finally, attempt a write (edit a file). The refusal, with trace reference, is the evidence that the boundary holds.

## Placeholder convention

All unresolved values are written `<LIKE_THIS>`. Every one must be replaced before deployment. Anything left unreplaced is a draft.

Stack-specific content (language globs, build commands, language server selection) is marked `<STACK>` and requires knowledge of the languages in scope.

## Key constraints

1. **The application CLAUDE.md must extend the enterprise set, never restate it.** Long instruction files still load, but adherence degrades.
2. **Application rules can only narrow the enterprise set, never widen it.** If an app file permits something the enterprise forbids, the enterprise rule wins.
3. **Do not copy from enterprise.** Duplicated instructions drift within weeks. Reference instead.
4. **Managed settings cannot be updated via plugin.** They must flow through privileged paths or the admin console.
5. **The `.claude/context/` knowledge connection cannot be templated.** It must be authored against the real codebase with the team that owns it.

## Working method

- Start with `README.md` to understand the deployment order
- Use `VERIFY.md` as a checklist after each deployment milestone
- Keep `CLAUDE.md` files short; they load but long files degrade adherence
- Fill placeholders with `<LIKE_THIS>` so gaps are explicit
- Always validate the plugin before distributing: `claude plugin validate enterprise`
- Test on one machine before fleet rollout

## Plugin versioning

Every change to `enterprise/` must bump `version` in `.claude-plugin/plugin.json`. Applications record the version they depend on. A reference to a version that no longer exists is a finding during deployment.
