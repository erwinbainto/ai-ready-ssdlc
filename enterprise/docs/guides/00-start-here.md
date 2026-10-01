# Enterprise Guides — Start Here

**Complete documentation for the AI-Ready SSDLC Harness (Enterprise Layer)**

16 comprehensive guides covering readiness, setup, deployment, forms, and examples.

---

## Quick Navigation

### 🚀 Just Getting Started?

1. **Read this first:** `quick-start.md` (224 lines)
   - One-page command sequence
   - Phases 1-4 overview
   - Common issues

2. **Then read:** `README.md` (274 lines)
   - Navigation hub for all guides
   - Task-based routing

### 📚 Full Documentation

**Pre-Deployment & Approval (2 guides):**
- `pre-deployment-readiness.md` (250+ lines) — Readiness checklist (complete BEFORE starting)
- `deployment-sign-off.md` (300+ lines) — Sign-off form & governance approval

**Setup & Deployment (4 guides):**
- `setup.md` (401 lines) — How to complete enterprise form sections 0-11
- `deployment.md` (393 lines) — Deployment procedures (Route A & B)
- `architecture.md` (534 lines) — Enterprise folder structure explained
- `deployment-guide.md` (1,029 lines) — Complete deployment procedures with all phases

**Understanding & Reference (5 guides):**
- `ai-ready-ssdlc-harness-guide.md` (754 lines) — Complete architecture overview
- `enterprise-vs-application.md` (931 lines) — How enterprise and app harnesses differ
- `enterprise-form-reusability.md` (531 lines) — Form reusability patterns
- `index.md` (468 lines) — Master index of all documents
- `usage.md` (362 lines) — Usage patterns and workflows

**How-To Guides (2 guides):**
- `forms-and-automation.md` (333 lines) — Working with forms
- (Others as needed)

**Examples (2 guides):**
- `example-completed-enterprise-form.md` (520 lines) — Filled-out enterprise form example
- `example-completed-application-form.md` (480 lines) — Filled-out application form example

---

## Reading by Role

### Technical Lead (Setting up enterprise)

**In order:**
1. `pre-deployment-readiness.md` — Verify readiness BEFORE starting (critical)
2. `quick-start.md` — Get oriented
3. `setup.md` — Complete enterprise form
4. `deployment.md` — Deploy to machines
5. `deployment-sign-off.md` — Record approvals & evidence
6. `example-completed-enterprise-form.md` — See what a completed form looks like

**Reference:**
- `architecture.md` — Understand structure
- `ai-ready-ssdlc-harness-guide.md` — Deep dive into architecture

### Dev Lead (Setting up applications)

**In order:**
1. `quick-start.md` — Get oriented
2. `enterprise-vs-application.md` — Understand differences
3. Check `example-completed-application-form.md` — See completed example
4. `deployment-guide.md` Phase 2 — Deploy your app

**Reference:**
- `ai-ready-ssdlc-harness-guide.md` — How enterprise works
- `enterprise-form-reusability.md` — How to customize

### Security Team (Reviewing policies)

**In order:**
1. `architecture.md` — Understand structure
2. `enterprise-vs-application.md` — Policy inheritance model
3. `example-completed-enterprise-form.md` — See policies in context

### DevOps (Deploying to fleet)

**In order:**
1. `quick-start.md` — Get oriented
2. `deployment.md` — Deployment procedures
3. `deployment-guide.md` Phase 1 — Full procedures
4. `architecture.md` — Understand what's being deployed

---

## File Directory

| File | Lines | Purpose | Audience |
|---|---|---|---|
| **00-START-HERE.md** | — | This file | Everyone |
| **README.md** | 274 | Navigation hub | Everyone |
| **QUICK_START.md** | 224 | 1-page command sequence | Impatient users |
| **setup.md** | 401 | Enterprise form guide | Technical leads |
| **deployment.md** | 393 | Deployment procedures | DevOps |
| **architecture.md** | 534 | Folder structure | Enterprise team |
| **ai-ready-ssdlc-harness_guide.md** | 754 | Architecture deep dive | Understanding harness |
| **DEPLOYMENT_GUIDE.md** | 1,029 | Full procedures + phases | Complete reference |
| **ENTERPRISE_VS_APPLICATION.md** | 931 | Policy inheritance | Dev leads, Security |
| **ENTERPRISE_FORM_REUSABILITY.md** | 531 | Form patterns | Form authors |
| **INDEX.md** | 468 | Master index | Navigation |
| **USAGE.md** | 362 | Usage patterns | Users |
| **FORMS_AND_AUTOMATION.md** | 333 | Form workflows | Technical leads |
| **EXAMPLE_COMPLETED_ENTERPRISE_FORM.md** | 520 | Filled form example | Technical leads |
| **EXAMPLE_COMPLETED_APPLICATION_FORM.md** | 480 | Filled form example | Dev leads |

**Total: 7,234 lines**

---

## Common Tasks

### "How do I set up enterprise?"
1. **Start here:** `pre-deployment-readiness.md` (verify readiness FIRST)
2. Read `quick-start.md`
3. Read `setup.md` (form sections 0-11)
4. Read `deployment.md`
5. **Record approvals:** `deployment-sign-off.md`
6. Reference `example-completed-enterprise-form.md`

### "How do I set up an application?"
1. Read `quick-start.md`
2. Read `enterprise-vs-application.md`
3. Reference `example-completed-application-form.md`
4. See `deployment-guide.md` Phase 2

### "I need to understand the architecture"
1. Read `architecture.md` (30 min)
2. Read `ai-ready-ssdlc-harness-guide.md` (60 min)
3. Read `enterprise-vs-application.md` (45 min)

### "Something's broken"
1. Check `deployment-guide.md` troubleshooting section
2. Check `deployment.md` troubleshooting section
3. Escalate with information from guide

### "I want to see a completed example"
1. `example-completed-enterprise-form.md` (enterprise setup)
2. `example-completed-application-form.md` (app setup)

---

## Organization Structure

```
enterprise/docs/guides/
│
├── 00-START-HERE.md (this file)
│   └─ Navigation & task routing
│
├── Quick Reference
│   ├─ README.md (hub)
│   ├─ QUICK_START.md (1-pager)
│   └─ INDEX.md (master index)
│
├── Setup & Deployment
│   ├─ setup.md (form guide)
│   ├─ deployment.md (procedures)
│   ├─ DEPLOYMENT_GUIDE.md (complete)
│   └─ architecture.md (structure)
│
├── Understanding
│   ├─ ai-ready-ssdlc-harness_guide.md (architecture)
│   ├─ ENTERPRISE_VS_APPLICATION.md (policies)
│   ├─ ENTERPRISE_FORM_REUSABILITY.md (patterns)
│   └─ USAGE.md (workflows)
│
├── How-To
│   └─ FORMS_AND_AUTOMATION.md (forms)
│
└── Examples
    ├─ EXAMPLE_COMPLETED_ENTERPRISE_FORM.md
    └─ EXAMPLE_COMPLETED_APPLICATION_FORM.md
```

---

## Recommended Reading Order (Complete)

**For complete understanding (4-5 hours):**

1. `quick-start.md` (15 min) — Get oriented
2. `README.md` (10 min) — Navigation overview
3. `architecture.md` (30 min) — How enterprise works
4. `ai-ready-ssdlc-harness-guide.md` (60 min) — Deep architecture
5. `setup.md` (30 min) — How to complete form
6. `deployment.md` (30 min) — How to deploy
7. `enterprise-vs-application.md` (45 min) — Policy model
8. `example-completed-enterprise-form.md` (20 min) — See working example

---

## Using These Guides

### Best Practices

✅ **DO:**
- Start with `quick-start.md` (always)
- Use `README.md` for navigation
- Refer to examples while filling forms
- Bookmark `deployment-guide.md` for troubleshooting

❌ **DON'T:**
- Start with `deployment-guide.md` (too much detail initially)
- Skip `quick-start.md`
- Try to memorize everything (reference as needed)
- Work without opening examples alongside

### Printing

- **Quick reference:** Print `quick-start.md` + `README.md`
- **Setup:** Print `setup.md` + `deployment.md`
- **Complete guide:** Print entire guides folder (7,234 lines ≈ 40-50 pages)

---

## Next Steps

1. **Read:** `quick-start.md` (this takes 15 minutes)
2. **Navigate:** Use `README.md` to find what you need
3. **Reference:** Open examples while working on forms
4. **Deploy:** Follow `deployment-guide.md` for full procedures

---

## Document Status

**Created:** 2026-10-01  
**Last Updated:** 2026-10-01  
**Total Lines:** 7,234 (14 files)  
**Status:** Complete reference suite  

---

**Questions?** See the appropriate guide for your task, or check `index.md` for a master reference.
