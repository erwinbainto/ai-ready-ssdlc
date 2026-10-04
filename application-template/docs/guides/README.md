# Guides & Learning Materials

This folder contains how-to guides, tutorials, and learning materials for working with this application and its Claude Code setup.

---

## Contents

### 🆕 AI SSDLC Phase D4: Harness Setup

**Complete setup for Claude Code configuration and governance**

- **`developer-setup-guide.md`** — Master reference guide (2,900+ lines)
  - All 8 phases of harness setup (foundation, architecture, security, configuration, source code, agents, workflow, verification)
  - Activity checklist with time estimates and owners
  - Common workflows and patterns
  - Troubleshooting guide

- **`phase-prompts.md`** — Ready-to-copy prompts (3,600+ lines)
  - Complete copy-paste prompts for all 8 phases
  - Recommended Claude models for each task (Haiku 4.5, Opus 5.5, /fast)
  - Model recommendations: when to use which model for best results

- **`phase-prompts-interactive.md`** — Interactive fill-in-the-blank (2,500+ lines)
  - Customize prompts for your specific project
  - Fill in project details → get personalized prompts
  - Same 8 phases as developer-setup-guide.md

- **`d4-completion-checklist.md`** — Verification & sign-off checklist (400+ lines)
  - Comprehensive verification of all D4 configuration
  - Team sign-offs (Tech Lead, Security Lead, Dev Lead)
  - Readiness assessment before Phase D5 deployment

- **`project-info-lifecycle.md`** — PROJECT_INFO.md lifecycle (350+ lines)
  - What happens to PROJECT_INFO.md through all phases
  - When to use it, update it, archive it
  - How it feeds into configuration files

### AI SSDLC Phase D5: Deploy

- **`d5-deploy-phase.md`** — Deployment to staging (500+ lines)
  - Build artifact creation
  - Staging infrastructure setup
  - Deployment process (manual, automated, container-based)
  - Comprehensive testing (smoke, integration, E2E, performance, security, compliance)
  - Documentation and runbooks
  - Monitoring & alerting setup
  - QA sign-off procedures

---

### Getting Started

- **`getting-started.md`** — Entry point for new team members
  - Project overview and architecture bird's-eye view
  - Local development environment setup (prerequisites, IDE configuration)
  - Running the application locally (build commands, dev server startup)
  - Verifying your setup (smoke tests, "hello world" walkthrough)
  - Links to next steps by role (backend dev, frontend dev, DevOps, QA)

### Agent & Command Guides

- **`agent-guide.md`** — Which Claude Code agent or slash command to use for each scenario
  - Choosing the right command for your task (new feature vs bug fix vs security scan)
  - Supported slash commands and what each one does
  - Agent roles and their responsibilities (dev-coordinator, security-auditor, etc.)
  - How to invoke agents and interpret their output

- **`command-reference.md`** — Complete slash command reference with examples
  - Full list of available commands (e.g., `/new-feature`, `/security-scan`, `/code-review`)
  - Parameters and options for each command
  - Expected output and next steps after running each command
  - Chaining sequences (running one command after another)
  - Troubleshooting common issues

- **`agent-skill-mapping.md`** — How agents use skills and playbooks
  - Which skills are available in `.claude/skills/`
  - How agents invoke skills automatically
  - Autonomy levels: when agents can write vs when they need approval
  - How to request custom skills for your workflow

- **`agent-prompt-examples.md`** — Example prompts and patterns for invoking agents
  - Copy-paste examples for common workflows
  - How to phrase requirements for agents to understand
  - Common mistakes and how to avoid them
  - Escalation patterns (when to contact human reviewers)

### System & Setup Guides

- **`project-structure-guide.md`** — Annotated walkthrough of the repository
  - What each directory contains (src/, docs/, .claude/, etc.)
  - The harness structure (.claude/agents/, .claude/skills/, .claude/commands/, .claude/rules/)
  - How to navigate the codebase for different purposes
  - Where to find tests, configuration, and documentation

- **`development-workflow.md`** — Day-to-day development steps
  - Creating a feature branch
  - Running tests locally before committing
  - Making a pull request
  - Responding to code review feedback
  - Merging and deploying

- **`debugging-guide.md`** — How to debug common issues
  - Setting up IDE debugger (breakpoints, watches, etc.)
  - Reading stack traces and identifying root causes
  - Common error messages and solutions
  - Enabling verbose logging
  - Using diagnostic tools (logs, metrics, traces)

### Security & Compliance

- **`security-best-practices.md`** — Security checklist for developers
  - No hardcoded credentials (secrets management)
  - Parameterized SQL queries (SQL injection prevention)
  - Input validation and output encoding (XSS prevention)
  - Authentication and authorization checks
  - Secure dependency management (CVE scanning)

- **`compliance-requirements.md`** — Regulatory and compliance requirements
  - Data protection rules (PII handling, retention periods)
  - Audit logging requirements
  - Role-based access control (RBAC) enforcement
  - Encryption requirements (in-transit, at-rest)
  - Regulatory links and reference documentation

### Operational Runbooks

- **`deployment-runbook.md`** — Step-by-step deployment procedures
  - Pre-deployment checklist
  - Deployment commands and monitoring
  - Post-deployment verification
  - Rollback procedures
  - Escalation contacts

- **`incident-response.md`** — How to respond to production incidents
  - Incident identification and severity classification
  - Communication procedures
  - Investigation and root-cause analysis
  - Mitigation and recovery steps
  - Post-incident review process

- **`performance-tuning.md`** — How to optimize application performance
  - Identifying bottlenecks (profiling, metrics)
  - Database query optimization
  - Caching strategies
  - Resource limits and scaling
  - Load testing procedures

### Training Materials

- **`training-guide.md`** — Training curriculum for new team members
  - Week 1: Onboarding (environment setup, codebase walkthrough)
  - Week 2: Architecture (system design, ADRs, key concepts)
  - Week 3: Development (how to use agents, making your first feature)
  - Week 4: Integration (deploying to staging, running in production)
  - Post-training: Resources, feedback, career progression

- **`training-checklist.md`** — Checklist for onboarding new team members
  - Pre-start (hardware, accounts, access)
  - Day 1 (welcome, setup, introduction to team)
  - Week 1 (environment, codebase, culture)
  - Week 2–4 (hands-on learning, pair programming)
  - Sign-off (readiness to work independently)

### Readiness & Audits

- **`claude-readiness-audit.md`** — Verification that Claude Code harness is set up correctly
  - Pre-flight checklist (agents installed, skills available, permissions configured)
  - Running verification commands (`/status`, `/context`, `/mcp`, etc.)
  - Interpreting verification results
  - Troubleshooting common setup issues
  - Sign-off criteria

- **`executive-summary.md`** — High-level overview for stakeholders
  - What Claude Code is and why it matters
  - Benefits (speed, quality, consistency)
  - Governance and controls (read-only core, approval gates)
  - Metrics and success criteria
  - Risk mitigation and compliance

---

## Claude Model Recommendations (D4 & D5)

**Built into all Phase D4 & D5 guide prompts**

| Task Type | Recommended Model | Why | Performance |
|-----------|------------------|-----|-------------|
| **Quick clarifications** | 🟢 Haiku 4.5 | Fast, simple form-filling | Very fast |
| **Architecture & design** | 🔵 Opus 5.5 | Complex analysis, trade-offs | Slower but better |
| **Security decisions** | 🔵 Opus 5.5 | Nuanced threat analysis | Slower but more thorough |
| **Code generation** | 🟢 Haiku 4.5 | Fast generation after specs | Very fast |
| **Compliance mapping** | 🔵 Opus 5.5 | Complex cross-domain analysis | Slower but comprehensive |
| **Fast iteration** | ⚡ `/fast` mode | Opus 5.5 with faster output | Fast + comprehensive |

**Where to find recommendations:**
- `phase-prompts.md` — 🤖 indicator with each prompt
- `phase-prompts-interactive.md` — 🤖 indicator with each section

---

## When to Add Here

Add a guide when:
- You've documented a repeatable workflow or best practice
- You're explaining how to use an agent, command, or skill
- You're teaching someone new to the project how to get started
- You're providing a reference for common tasks or troubleshooting
- You're sharing onboarding materials with new team members

**Do NOT add here:**
- Business rules or specifications (→ `docs/specs/`)
- Architecture decisions or system design (→ `docs/architecture/`)
- Audit findings or verification evidence (→ `docs/audits/`)
- Test plans or scenarios (→ `docs/testing/`)
- Agent workflow pipeline (→ `docs/agent-workflow/`)

---

## Guide Templates

### How-To Guide Template

```markdown
# How to [Task]

## Overview
[1-2 sentences on what this guide covers]

## Prerequisites
- Item 1
- Item 2

## Step-by-step
1. Do this
2. Then do this
3. Verify with this command

## Troubleshooting
- **Issue:** ...
  **Solution:** ...

## Related
- Link 1
- Link 2
```

### Runbook Template

```markdown
# [System/Process] Runbook

## Overview
What is this runbook for?

## Severity Levels
- Critical: [describe]
- High: [describe]
- Medium: [describe]

## Detection
How do you know there's a problem?

## Response Steps
1. Immediate action
2. Investigation
3. Remediation

## Escalation
When and how to escalate?

## Communication
Who to notify? How to notify?
```

### Checklist Template

```markdown
# [Task] Checklist

## Pre-[Task]
- [ ] Item 1
- [ ] Item 2

## During [Task]
- [ ] Step 1
- [ ] Step 2

## Post-[Task]
- [ ] Verification
- [ ] Sign-off

## Rollback
- [ ] Rollback procedure if needed
```

---

## Audience

Different audiences should start with different guides:

### Setting Up Phase D4 (Harness Configuration)

| Audience | Start here | Prompts | Verify |
|---|---|---|---|
| **Dev Lead** | developer-setup-guide.md | phase-prompts.md (busy) or phase-prompts-interactive.md (thorough) | d4-completion-checklist.md |
| **Tech Lead** | developer-setup-guide.md | phase-prompts.md (busy) or phase-prompts-interactive.md (thorough) | d4-completion-checklist.md |
| **Security Lead** | developer-setup-guide.md (Phase 3) | phase-prompts.md (Phase 3) | d4-completion-checklist.md |
| **DevOps** | d5-deploy-phase.md | Reference developer-setup-guide.md Phase 5 | d4-completion-checklist.md |

### Regular Development

| Audience | Start here | Then read | Finally |
|---|---|---|---|
| **New backend developer** | getting-started.md | project-structure-guide.md | agent-guide.md |
| **New frontend developer** | getting-started.md | development-workflow.md | agent-guide.md |
| **New QA engineer** | getting-started.md | testing-guide.md | d5-deploy-phase.md |
| **DevOps/Ops** | d5-deploy-phase.md | deployment-runbook.md | incident-response.md |
| **Manager/stakeholder** | executive-summary.md | deployment-runbook.md | compliance-requirements.md |
| **Security team** | security-best-practices.md | compliance-requirements.md | d4-completion-checklist.md |

---

## Update Frequency

Update guides when:
- Workflows or commands change (frequent)
- Architecture or patterns evolve (per sprint)
- Deployment procedures are refined (per release)
- New tools or processes are introduced (as needed)
- Training materials are outdated (quarterly review)

---

## Maintenance

### Keeping Guides Current

1. **Link rot prevention:** Check external links quarterly
2. **Screenshot updates:** Update command output and UI screenshots when they change
3. **Command reference:** Keep in sync with actual `.claude/commands/` directory
4. **Tool versions:** Update tool names and versions when they change
5. **Contact info:** Keep escalation contacts and team emails current

### Deprecated Guides

If a guide is no longer relevant:
1. Mark at top: "⚠️ DEPRECATED: See [new guide] instead"
2. Move to `archived/` subdirectory (do not delete)
3. Update links to point to the new guide
4. Remove from the main README.md list

---

## Related

- **`.claude/`** — The actual agent/skill/rule/command files referenced here
- **`docs/architecture/`** — System design authority; guides reference architectural decisions
- **`docs/specs/`** — Business rules and API contracts; guides may link to specific specs
- **`docs/audits/`** — Evidence of guide compliance; verification results and audit findings
- **`docs/testing/`** — Test plans and procedures; guides should link to related test scenarios
- **`CLAUDE.md`** — Project instructions; guides expand on CLAUDE.md rules

---

## Quick Links

- **For developers:** [getting-started.md](getting-started.md) → [project-structure-guide.md](project-structure-guide.md) → [agent-guide.md](agent-guide.md)
- **For debugging:** [debugging-guide.md](debugging-guide.md)
- **For deployment:** [deployment-runbook.md](deployment-runbook.md)
- **For incidents:** [incident-response.md](incident-response.md)
- **For onboarding:** [training-guide.md](training-guide.md) + [training-checklist.md](training-checklist.md)
- **For security:** [security-best-practices.md](security-best-practices.md) + [compliance-requirements.md](compliance-requirements.md)
