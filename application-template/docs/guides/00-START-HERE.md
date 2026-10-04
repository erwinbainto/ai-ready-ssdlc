# Application Guides — Start Here

**Complete documentation for setting up the application harness (Tier 3)**

5 comprehensive guides covering context, rules, hooks, and getting started.

---

## Quick Navigation

### 🚀 Just Getting Started? (Phase D4: Harness Setup)

**Are you setting up the project harness (Claude Code configuration)?**

1. **Start here:** `developer-setup-guide.md` (2,900+ lines)
   - Complete reference guide for all 8 setup phases
   - Follow along with Phase 1-8 activity checklist
   - Examples for every step

2. **Use prompts to complete setup:**
   - `phase-prompts.md` — Ready-to-copy prompts for each phase
   - `phase-prompts-interactive.md` — Fill-in-the-blank prompts for customization
   - **Both recommend appropriate Claude models** (Haiku 4.5 vs. Opus 5.5)

3. **Verify completion:**
   - `d4-completion-checklist.md` — Full verification checklist
   - `project-info-lifecycle.md` — What happens to PROJECT_INFO.md

4. **Ready for deployment?**
   - `d5-deploy-phase.md` — Phase D5 deployment procedures

---

### 📚 Then Getting Into Details?

1. **Read this first:** `getting-started-sample.md` (561 lines)
   - Complete example walkthrough
   - How to fill out each section
   - Real-world patterns

2. **Then read:** `README.md` (301 lines)
   - Navigation hub for all guides
   - Task-based routing

### 📚 Full Documentation

**Core Guides (4 guides):**
- `context/README.md` (283 lines) — How to complete `.claude/context/` files
- `rules/README.md` (373 lines) — How to create app-specific rules
- `hooks/README.md` (349 lines) — How to wire lifecycle hooks
- `getting-started-sample.md` (561 lines) — Complete example walkthrough

**Navigation:**
- `README.md` (301 lines) — Master navigation hub

---

## Reading by Role

### Dev Lead (Setting up this application)

**In order:**
1. `getting-started-sample.md` — See complete example
2. `context/README.md` — Complete architecture, commands, glossary, hazards
3. `rules/README.md` — Create app-specific rules
4. `hooks/README.md` — Wire lifecycle automation

**Reference:**
- `README.md` — Task-based lookup

### Team Members (Working in this application)

**In order:**
1. `getting-started-sample.md` — Get oriented
2. `README.md` — Find what you need

**Reference as needed:**
- `context/README.md` — Understanding the app
- `rules/README.md` — Coding standards
- `hooks/README.md` — Automation & gates

### Security Lead (Reviewing this application)

**In order:**
1. `getting-started-sample.md` — See what's documented
2. `context/README.md` — Check security-posture section
3. `rules/README.md` — Review security rules

### DevOps (Managing this application)

**In order:**
1. `hooks/README.md` — Understand lifecycle automation
2. `getting-started-sample.md` — See full setup

---

## File Directory

### 🆕 Phase D4: Harness Setup (NEW!)

| File | Lines | Purpose | Audience |
|---|---|---|---|
| **developer-setup-guide.md** | 2,900+ | Complete setup reference (all 8 phases) | Dev leads, Tech leads |
| **phase-prompts.md** | 3,600+ | Ready-to-copy prompts for all phases | Busy teams |
| **phase-prompts-interactive.md** | 2,500+ | Fill-in-the-blank custom prompts | Teams wanting personalization |
| **d4-completion-checklist.md** | 400+ | Verification checklist before Phase D5 | Tech lead, QA |
| **project-info-lifecycle.md** | 350+ | What happens to PROJECT_INFO.md | Everyone |
| **d5-deploy-phase.md** | 500+ | Deployment to staging procedures | DevOps, QA, Tech lead |

### Core Guides

| File | Lines | Purpose | Audience |
|---|---|---|---|
| **00-START-HERE.md** | — | This file | Everyone |
| **README.md** | 301 | Navigation hub | Everyone |
| **getting-started-sample.md** | 561 | Complete example | Dev leads |
| **context/README.md** | 283 | Context completion | Dev leads |
| **rules/README.md** | 373 | Rules creation | Dev leads |
| **hooks/README.md** | 349 | Hooks wiring | DevOps |

**Total: 11,300+ lines (core + D4 setup)**

---

## Common Tasks

### "How do I set up the `.claude/context/` folder?"
→ Read `context/README.md`
→ Reference `getting-started-sample.md` for examples

### "What coding rules should I add?"
→ Read `rules/README.md`
→ Reference `getting-started-sample.md` for stack examples

### "How do I configure hooks?"
→ Read `hooks/README.md`
→ Reference `getting-started-sample.md` for hook examples

### "I'm new to this team, where do I start?"
→ Read `getting-started-sample.md` (15 min)
→ Read `README.md` (10 min)
→ Then you know where to find everything else

### "I want to see a complete example"
→ Read `getting-started-sample.md` (end-to-end example)

### "I need to understand the rules"
→ Read `rules/README.md`
→ Check `getting-started-sample.md` for your stack

### "Where do I find the security posture?"
→ See `context/README.md` (security-posture.md section)

---

## Organization Structure

```
rrd-ir/docs/guides/

🆕 00-START-HERE.md (this file)
   └─ Navigation & task routing

🔧 PHASE D4: HARNESS SETUP (NEW!)
  ├─ developer-setup-guide.md (complete 8-phase reference)
  ├─ phase-prompts.md (ready-to-copy prompts)
  ├─ phase-prompts-interactive.md (fill-in-the-blank prompts)
  ├─ d4-completion-checklist.md (verification checklist)
  ├─ project-info-lifecycle.md (PROJECT_INFO.md reference)
  └─ d5-deploy-phase.md (deployment procedures)

📍 Navigation & Examples
  ├─ README.md (hub)
  └─ getting-started-sample.md (complete example)

📚 Core Guides
  ├─ context/README.md (architecture, commands, glossary, hazards)
  ├─ rules/README.md (naming, patterns, security)
  └─ hooks/README.md (session-start, pre-tool-use, automation)
```

---

## Recommended Reading Order (Complete)

### 🆕 For Setting Up Phase D4 Harness (9-17 hours)

**Complete setup sequence:**

1. `developer-setup-guide.md` — Read full guide (1 hour)
2. `phase-prompts.md` OR `phase-prompts-interactive.md` — Choose workflow (30 min)
3. Follow Phase 1-8 prompts using Claude Code (8-16 hours)
4. `d4-completion-checklist.md` — Verify completion (1-2 hours)
5. `d5-deploy-phase.md` — Next phase deployment (reference as needed)

**For new dev leads setting up this application (2-3 hours total after setup):**

1. `getting-started-sample.md` (30 min) — See the big picture
2. `context/README.md` (30 min) — How to complete context files
3. `rules/README.md` (30 min) — How to create rules
4. `hooks/README.md` (30 min) — How to configure hooks
5. `README.md` (10 min) — Understand navigation

**For team members (30 minutes):**

1. `getting-started-sample.md` (20 min) — Get oriented
2. `README.md` (10 min) — Know where to find things

---

## What Each Guide Covers

### `getting-started-sample.md`

**Complete end-to-end example with:**
- Business purpose and system structure
- Available commands (build, test, lint, etc.)
- Domain terminology and glossary
- Known hazards and incident history
- Security posture (compliance, auth, data classification)
- Coding conventions and anti-patterns
- Security rules for your stack
- Lifecycle hooks (session-start, pre-tool-use)

**Use this:** First thing you read. See how everything fits together.

### `context/README.md`

**How to complete `.claude/context/` files:**
- `architecture.md` — System structure and decisions
- `commands.md` — Available commands and contracts
- `glossary.md` — Business and technical terms
- `hazards.md` — Known risks and incident history
- `security-posture.md` — Compliance and data classification

**Use this:** When you're writing context files.

### `rules/README.md`

**How to create app-specific rules:**
- Naming conventions (camelCase, snake_case, PascalCase)
- Code patterns (DI, async/await, error handling)
- Security patterns (parameterized queries, validation)
- Stack-specific examples (Java, Node.js, Python, React)
- Enforcement methods (linting, pre-commit, tests)

**Use this:** When you're writing rules for your stack.

### `hooks/README.md`

**How to wire lifecycle automation:**
- `session-start.sh` — Prerequisites checking (Java 21?, Node 20?, etc.)
- `pre-tool-use.sh` — Permission gates (block .env edits)
- `pre-<action>-approved.sh` — Post-approval automation
- Testing and debugging hooks
- Stack-specific examples (Java, Node.js, Python)

**Use this:** When you're setting up automation.

### `README.md`

**Master navigation hub:**
- 10 available guides mapped by task
- Quick reference table by scenario
- File structure and purposes
- When to use each guide
- Links to related docs

**Use this:** Whenever you need to find something.

---

## Using These Guides

### Best Practices

✅ **DO:**
- Start with `getting-started-sample.md` (always)
- Use `README.md` for ongoing navigation
- Reference examples while filling forms
- Keep these open while working on `.claude/`

❌ **DON'T:**
- Skip `getting-started-sample.md`
- Try to memorize (reference as needed)
- Work without examples open
- Assume all stacks use same patterns

### Printing

- **Quick reference:** Print `README.md`
- **Setup:** Print `context/README.md` + `rules/README.md` + `hooks/README.md`
- **Complete guide:** Print entire guides folder (1,867 lines ≈ 12-15 pages)

---

## Integration with Enterprise

**These guides are Tier 3 (application-specific).**

**Related enterprise guides:**
- Enterprise setup: See `../../enterprise/docs/guides/00-START-HERE.md`
- Enterprise architecture: See `../../enterprise/docs/guides/ai-ready-ssdlc-harness_guide.md`
- Enterprise vs. application: See `../../enterprise/docs/guides/ENTERPRISE_VS_APPLICATION.md`

**Key principle:** Application guides extend enterprise guides, never replace them.

---

## Next Steps

1. **Read:** `getting-started-sample.md` (this takes 30 minutes)
2. **Navigate:** Use `README.md` to find what you need
3. **Work through:** Each guide in order (context → rules → hooks)
4. **Reference:** Keep these open while filling `.claude/context/` files

---

## Understanding D4 and D5

**D = Development Phase** (part of the AI-Ready Secure Software Development Lifecycle)

| Phase | Name | What | Duration | Owner |
|-------|------|------|----------|-------|
| **D4** | **Harness** | Setup Claude Code configuration & governance | 1-2 weeks | Dev Lead + Tech Lead |
| **D5** | **Deploy** | Release to staging environment | 2-4 weeks | DevOps + QA |
| **D6** | **Gate** | Compliance audit & sign-off | 1-2 weeks | Security Lead |
| **D7** | **Operate** | Production monitoring & support | Ongoing | DevOps + SRE |

**You are in Phase D4.** This folder has everything you need to complete it!

---

## Document Status

**Created:** 2026-10-01  
**Last Updated:** 2026-10-04  
**Total Lines:** 11,300+ (core + D4 setup guides)  
**Status:** Complete reference suite for application setup + D4 harness configuration  

---

## Quick Links

- **Enterprise setup?** → Go to `../../enterprise/docs/guides/00-START-HERE.md`
- **Need architecture overview?** → Go to `../../enterprise/docs/guides/ai-ready-ssdlc-harness_guide.md`
- **Understanding harness?** → Go to `../../README.md` (project root)
- **Deployment procedures?** → Go to `../../DEPLOYMENT_GUIDE.md`

---

**Ready?** Start with `getting-started-sample.md` — it shows you exactly what to do! 🚀
