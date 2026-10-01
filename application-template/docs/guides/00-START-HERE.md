# Application Guides — Start Here

**Complete documentation for setting up the application harness (Tier 3)**

5 comprehensive guides covering context, rules, hooks, and getting started.

---

## Quick Navigation

### 🚀 Just Getting Started?

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

| File | Lines | Purpose | Audience |
|---|---|---|---|
| **00-START-HERE.md** | — | This file | Everyone |
| **README.md** | 301 | Navigation hub | Everyone |
| **getting-started-sample.md** | 561 | Complete example | Dev leads |
| **context/README.md** | 283 | Context completion | Dev leads |
| **rules/README.md** | 373 | Rules creation | Dev leads |
| **hooks/README.md** | 349 | Hooks wiring | DevOps |

**Total: 1,867 lines**

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
application-template/docs/guides/

🆕 00-START-HERE.md (this file)
   └─ Navigation & task routing

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

**For new dev leads (2-3 hours):**

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

## Document Status

**Created:** 2026-10-01  
**Last Updated:** 2026-10-01  
**Total Lines:** 1,867 (5 files)  
**Status:** Complete reference suite for application setup  

---

## Quick Links

- **Enterprise setup?** → Go to `../../enterprise/docs/guides/00-START-HERE.md`
- **Need architecture overview?** → Go to `../../enterprise/docs/guides/ai-ready-ssdlc-harness_guide.md`
- **Understanding harness?** → Go to `../../README.md` (project root)
- **Deployment procedures?** → Go to `../../DEPLOYMENT_GUIDE.md`

---

**Ready?** Start with `getting-started-sample.md` — it shows you exactly what to do! 🚀
