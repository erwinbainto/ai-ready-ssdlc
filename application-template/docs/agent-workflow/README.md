# AI Agent Workflow Pipeline

**Slash Commands · Claude Agents · Skills · Execution Boundary · Testing · CI/CD**

---

## Overview

This folder documents the end-to-end AI agent workflow for this application. It defines:

- **Triggering mechanisms** (slash commands, manual agents)
- **Agent roles and responsibilities** (coordinator, specialists, reviewers)
- **Human approval gates** (planning, implementation, security, testing, code review)
- **Execution flow** (stages 0–6, agent autonomy levels)
- **CI/CD integration** (build, test, deploy gates)

---

## Contents

- **`agent-workflow.md`** — Complete pipeline diagram and stage descriptions
  - Trigger points (slash commands that initiate work)
  - Planning stage (agent decomposes task, identifies specialists)
  - Implementation stage (agents write code and execute skills)
  - Security & performance scanning (read-only verification)
  - Test generation (automated coverage enforcement)
  - Code review & PR packaging (style, security guardrails, atomic commits)
  - CI/CD execution (build, deploy, smoke tests)
  - Autonomy scorecard (AI vs human touchpoints per stage)

---

## When to Read Here

- **New team member?** Start with `agent-workflow.md` to understand how work flows through agents and approval gates
- **Starting a feature?** Refer to the triggering slash commands and human approval points
- **Verifying autonomy levels?** Check the Autonomy Summary table to understand where Claude makes decisions vs where humans review

---

## When to Update

Update this folder when:
- You add a new slash command or agent role
- You change approval gate criteria or staging gates
- You modify CI/CD pipeline stages
- You introduce new specialist agents (e.g., container-assessor, threat-analyst)

**Do NOT add here:**
- How-to guides (→ `docs/guides/`)
- System design or architecture (→ `docs/architecture/`)
- Audit findings or verification evidence (→ `docs/audits/`)
- Test plans (→ `docs/testing/`)
- Business rules or requirements (→ `docs/specs/`)

---

## Structure

Each workflow stage is defined by:
1. **Trigger** — What initiates this stage (slash command, approval gate, automation)
2. **Agents involved** — Which Claude agents participate
3. **Skills invoked** — Playbooks and automation steps
4. **Human touchpoint** — Where humans review or approve
5. **Success criteria** — What must be true before moving to the next stage
6. **Escalations** — What blocks this stage and requires human intervention

---

## Related

- **`docs/guides/`** — How to use agents and slash commands
- **`docs/architecture/`** — System design and technical decisions (ADRs)
- **`docs/specs/`** — Business requirements and API contracts
- **`docs/audits/`** — Execution traces and verification evidence from past agent runs
- **`docs/testing/`** — Test plans and coverage requirements that agents enforce
- **`.claude/commands/`** — The slash command implementations
- **`.claude/agents/`** — Agent role definitions and tool scopes

---

## Key Concepts

### Autonomy Levels

| Level | Agent decides | Human reviews | Example |
|---|---|---|---|
| **Human-initiated** | Developer chooses slash command | N/A | Starting a feature with `/new-feature` |
| **AI plans, human gates** | Agent creates execution plan | Dev lead approves plan | Stage 1 planning requires explicit approval before implementation |
| **AI implements, human reviews** | Agent writes code and tests | Dev reviews generated output | Stage 2 implementation: agent generates, human validates |
| **AI audits, human fixes** | Agent identifies findings | Dev resolves Critical/High items | Stage 3 security scan: agent flags, dev fixes, agent re-scans |
| **AI generates, human validates** | Agent generates tests | Dev confirms coverage target | Stage 4 test generation: agent writes tests, CI gate enforces 80%+ |
| **Fully automated** | Pipeline runs autonomously | Smoke tests + logs reviewed | Stage 6 CI/CD: automated build, test, deploy on Bitbucket merge |

### Execution Boundary

The **read-only core** (stages 1, 3, 4, 5 code-review phase) ensures:
- Agents never write code without human approval of the plan (stage 1)
- Security audits never modify code (stage 3 is read-only)
- Test generation is reviewed before merge (stage 4)
- Code review happens before PR merge (stage 5)

This boundary is enforced by permission mode and MCP catalogue restrictions defined in the harness.

---

## Starting a New Workflow

1. **Trigger:** Developer types a slash command (e.g., `/new-feature`)
2. **Agent reads context:** Agent loads `.claude/context/`, architecture ADRs, business specs
3. **Agent produces plan:** Structured execution plan with identified specialists
4. **Human approval (Gate 1):** Developer reviews and explicitly types `approve` or `approve with conditions`
5. **Agents execute:** Specialists implement the approved plan
6. **Human review (Gate 2):** Dev lead reviews generated output
7. **Security audit (Gate 3):** Read-only scan of code and dependencies
8. **Human signs off (Gate 3):** Dev lead resolves Critical/High findings
9. **Test generation (Gate 4):** Agent writes tests targeting 80%+ coverage
10. **Code review (Gate 5):** Agent packages atomic commits, human reviews PR
11. **CI/CD (Gate 6):** Automated build/test/deploy on Bitbucket merge
12. **Smoke tests:** Tech lead signs off before promotion to next environment

---

## Quick Reference

| Stage | Agent | Human Gate | Outcome |
|---|---|---|---|
| 0 | Developer | Slash command | Workflow initiated |
| 1 | Coordinator | Approval of plan | Approved plan ready for implementation |
| 2 | Specialists + Skills | Review generated code | Implementation complete, ready for security scan |
| 3 | Security Auditor (read-only) | Review findings, fix Criticals | All Criticals resolved, High documented |
| 4 | QA Engineer | Review coverage | 80%+ coverage enforced by CI gate |
| 5 | Code Reviewer + PR Packager | Bitbucket PR review | PR merged to `develop` |
| 6 | Azure Pipelines + CI/CD | Smoke tests, promote to Test | DEV environment validated, ready for Test promotion |

---

## See Also

- **`agent-workflow.md`** — Detailed pipeline with stage-by-stage breakdowns and autonomy scorecards
- **`.claude/agents/`** — Agent role definitions
- **`.claude/commands/`** — Slash command implementations
