# PROJECT_INFO.md Lifecycle

**What happens to the project information document through all phases**

---

## Overview

`docs/PROJECT_INFO.md` is created in **Phase 1** of the setup and serves different purposes throughout the D4 harness setup process.

This document explains its lifecycle and how to use it effectively.

---

## Timeline: Where PROJECT_INFO.md Fits

```
PHASE 1 (Create)
   ↓
   Project details gathered and documented
   └─→ Created: docs/PROJECT_INFO.md
   └─→ Status: Active working document
   
PHASES 2-4 (Use & Reference)
   ↓
   Information used to populate:
   ├─ .claude/context/* files
   ├─ .claude/rules/* files
   ├─ CLAUDE.md
   └─ docs/security/* files
   └─→ Status: Reference document during setup
   
PHASE 5 (Validate)
   ↓
   Verify information accuracy before deploy
   └─→ Status: Validation checkpoint
   
PHASES 6-7 (Archive)
   ↓
   Keep for future reference and onboarding
   └─→ Status: Archive & reference document

PRODUCTION (Ongoing)
   ↓
   Used for:
   ├─ New team member onboarding
   ├─ Project documentation
   ├─ Compliance audits
   └─ Future setup of related projects
```

---

## Phase 1: Creation

**When:** During Phase 1 tasks 1.1, 1.2, 1.3  
**Created by:** Dev Lead + Tech Lead + Security Lead  
**Duration:** 1 hour

### What Gets Documented

```markdown
# rrd-ir Project Information

## Application Purpose
[2-3 sentence business description]

## Technology Stack

### Backend
- Language: [e.g., Java 21]
- Framework: [e.g., Spring Boot 3.0]
- ORM: [e.g., JPA]

### Frontend
- Language: [e.g., TypeScript]
- Framework: [e.g., React 18]

### Infrastructure
- Database: [e.g., PostgreSQL 15]
- Cache: [e.g., Redis]
- Message Queue: [e.g., RabbitMQ]
- Authentication: [e.g., OAuth 2.0 via AWS Cognito]

## Team Members
- Tech Lead: [Name] ([email])
- Dev Lead: [Name] ([email])
- Security Lead: [Name] ([email])
- Write Approver: [Name] ([email])

## Compliance Requirements
- [ ] PCI DSS (payment card data)
- [ ] GDPR (EU personal data)
- [ ] HIPAA (health records)
- [ ] SOX (financial)
- [ ] Other: [frameworks]

## Build Commands
- Build: [mvn clean package]
- Test: [mvn test]
- Lint: [mvn checkstyle:check]
- Deploy: [mvn spring-boot:run]
```

### Status After Phase 1
✅ **Active document** — Will be referenced throughout setup  
📋 **Primary audience** — Tech Lead, Dev Lead, entire team  
🔄 **Next step** — Feed information into Phases 2-4

---

## Phases 2-4: Active Use

**When:** During architecture, security, and configuration phases  
**Used by:** Tech Lead, Security Lead, Dev Lead  
**Purpose:** Reference source for populating configuration files

### How It's Used

**Phase 2 (Architecture):**
- Reference: Technology Stack → Choose database, cache, queue
- Reference: Team Members → Identify architecture owner
- Output: `.claude/context/architecture.md` (uses PROJECT_INFO tech stack)

**Phase 3 (Security & Compliance):**
- Reference: Compliance Requirements → Identify frameworks
- Reference: Authentication → Define auth method
- Output: `.claude/context/security-posture.md` (uses compliance info)

**Phase 4 (Configure .claude/):**
- Reference: Build Commands → Populate `.claude/context/commands.md`
- Reference: Team Members → Set permissions in `.claude/settings.json`
- Reference: Application Purpose → Complete `CLAUDE.md`

### Information Flow

```
PROJECT_INFO.md (Phase 1)
    ↓
    ├─→ Phase 2: Use Tech Stack → .claude/context/architecture.md
    ├─→ Phase 3: Use Compliance → .claude/context/security-posture.md
    ├─→ Phase 4: Use Build Commands → .claude/context/commands.md
    ├─→ Phase 4: Use Team Members → .claude/settings.json
    └─→ Phase 4: Use Purpose → CLAUDE.md
```

### Status During Phases 2-4
📖 **Reference document** — Frequently consulted  
✏️ **May be updated** — If new information discovered  
🔄 **Next step** — Validation before deployment

---

## Phase 5: Validation Checkpoint

**When:** Before deploying to staging  
**Used by:** DevOps, QA, Tech Lead  
**Purpose:** Verify project information accuracy

### Validation Checklist

- [ ] Application name matches configured app
- [ ] Technology stack matches actual code
- [ ] Build commands work without errors
- [ ] Team members and contacts are current
- [ ] Compliance requirements reflect reality
- [ ] No information conflicts with `.claude/` configuration

### If Discrepancies Found

**Option A: Update PROJECT_INFO.md**
```bash
# If PROJECT_INFO was wrong
git add docs/PROJECT_INFO.md
git commit -m "docs: update PROJECT_INFO.md with correct information"
```

**Option B: Update Configuration Files**
```bash
# If configuration was wrong
git add .claude/context/*.md .claude/rules/*.md
git commit -m "docs: sync configuration with actual project details"
```

### Status After Phase 5 Validation
✅ **Validated** — Information is accurate  
🔒 **Locked** — Major changes require re-validation  
📤 **Ready for deploy** — Can proceed to Phase D5

---

## Phases 6-7: Archive & Reference

**When:** After deployment to staging and production  
**Audience:** Entire team, auditors, new team members  
**Purpose:** Project documentation and compliance evidence

### Use Cases in Production

**1. New Team Member Onboarding**
```
Onboarding task: "Read PROJECT_INFO.md to understand the project"
→ New developer quickly grasps:
  - What the application does
  - Technology stack
  - Key team members
  - Compliance requirements
```

**2. Compliance Audits**
```
Auditor question: "What compliance frameworks apply to this system?"
→ Evidence: docs/PROJECT_INFO.md (Compliance Requirements section)
→ Cross-reference: docs/security/compliance-mapping.md (detailed controls)
```

**3. Future Projects/Derivatives**
```
New project: "Create a companion service"
→ Reference: docs/PROJECT_INFO.md (similar tech stack, same team)
→ Reuse: Similar setup process, same tools
```

**4. Architecture Reviews**
```
Review question: "What's the current tech stack?"
→ Source of truth: PROJECT_INFO.md (documented baseline)
→ Compare to: Current `docs/architecture/ARCHITECTURE.md` (for drift)
```

### Status in Production
📚 **Archive document** — Primary reference is `.claude/` configuration  
🔍 **Historical record** — Shows what was decided and why  
📋 **Compliance evidence** — Demonstrates governance from day 1  
👥 **Onboarding aid** — Fast-track for new team members

---

## Special Cases: When to Update PROJECT_INFO.md

### Case 1: Technology Changes
```markdown
**Scenario:** Team decides to migrate from MongoDB to PostgreSQL

**Action:**
1. Update PROJECT_INFO.md (Infrastructure section)
2. Update .claude/context/architecture.md (Component table)
3. Update .claude/context/commands.md (New build/test commands)
4. Commit together:

git commit -m "docs: migrate database from MongoDB to PostgreSQL"
```

### Case 2: Team Changes
```markdown
**Scenario:** New Tech Lead assigned

**Action:**
1. Update PROJECT_INFO.md (Team Members section)
2. Update .claude/settings.json (Permissions if approver changed)
3. Commit:

git commit -m "docs: update Tech Lead in PROJECT_INFO.md"
```

### Case 3: Compliance Changes
```markdown
**Scenario:** New regulation requires CCPA compliance

**Action:**
1. Update PROJECT_INFO.md (Compliance Requirements)
2. Update .claude/context/security-posture.md (New framework)
3. Update docs/security/compliance-mapping.md (New controls)
4. Commit:

git commit -m "docs: add CCPA compliance requirement"
```

### Case 4: Build Process Changes
```markdown
**Scenario:** Switch from Maven to Gradle

**Action:**
1. Update PROJECT_INFO.md (Build Commands section)
2. Update .claude/context/commands.md (New build command)
3. Update .claude/hooks/session-start.sh (Check for Gradle)
4. Commit:

git commit -m "docs: update build process to use Gradle"
```

---

## Location & Access

**File:** `docs/PROJECT_INFO.md`  
**Git tracking:** ✅ Tracked in version control  
**Access:** 🟢 No restrictions (public project info)  
**Format:** Markdown  
**Update frequency:** As needed (average: quarterly)

---

## Related Documents

| Document | Relationship to PROJECT_INFO.md |
|----------|----------------------------------|
| `CLAUDE.md` | Uses project name & purpose from PROJECT_INFO |
| `.claude/context/architecture.md` | Uses tech stack from PROJECT_INFO |
| `.claude/context/security-posture.md` | Uses compliance from PROJECT_INFO |
| `.claude/context/commands.md` | Uses build commands from PROJECT_INFO |
| `.claude/settings.json` | Uses team members from PROJECT_INFO |
| `docs/architecture/ARCHITECTURE.md` | Detailed expansion of PROJECT_INFO tech stack |
| `docs/security/compliance-mapping.md` | Detailed expansion of PROJECT_INFO compliance |
| `docs/security/threat-model.md` | Based on PROJECT_INFO compliance frameworks |

---

## Summary: PROJECT_INFO.md Lifecycle

| Phase | Status | Purpose | Audience |
|-------|--------|---------|----------|
| **Phase 1** | 🆕 Created | Gather project information | Tech/Dev/Security Lead |
| **Phases 2-4** | 📖 Active Reference | Populate configuration | Dev Team |
| **Phase 5** | ✅ Validated | Verify accuracy | DevOps/QA |
| **Phases 6-7** | 📚 Archive | Compliance & reference | Team/Auditors |
| **Production** | 🔍 Historical Record | Onboarding & audits | New hires/Auditors |

---

## Best Practices

### DO ✅
- ✅ Keep PROJECT_INFO.md updated when major decisions change
- ✅ Reference it when onboarding new team members
- ✅ Use it as evidence in compliance audits
- ✅ Update it alongside configuration changes
- ✅ Include it in project handoff documentation

### DON'T ❌
- ❌ Let PROJECT_INFO.md drift from reality (verify quarterly)
- ❌ Use PROJECT_INFO as source of truth after D4 (use CLAUDE.md)
- ❌ Forget to update related config files when PROJECT_INFO changes
- ❌ Delete PROJECT_INFO.md (keep for compliance history)
- ❌ Store sensitive data in PROJECT_INFO (uses docs/ folder, may be shared)

---

## Q&A

**Q: Is PROJECT_INFO.md the "source of truth"?**  
A: Not after Phase 1. During setup it's the working document. After that, `.claude/context/*.md` files are the source of truth for Claude Code. PROJECT_INFO is used for human reference and compliance.

**Q: Should we keep updating PROJECT_INFO.md in production?**  
A: Yes, but focus on major changes. Think of it as a historical record. Day-to-day updates go into the specific configuration files (CLAUDE.md, `.claude/` files, etc.).

**Q: Can we delete PROJECT_INFO.md after harness setup?**  
A: No. Keep it for compliance audits and future reference. It's evidence of your governance from Day 1.

**Q: Who should have access to PROJECT_INFO.md?**  
A: Everyone on the team (it's in `docs/` which is tracked in git). Never put sensitive data in PROJECT_INFO.

**Q: How often should we update PROJECT_INFO.md?**  
A: As needed when major decisions change (tech stack, team, compliance). Suggest quarterly review.

---

**Last Updated:** 2026-10-04  
**Maintained by:** Tech Lead  
**Related:** `phase-prompts.md`, `developer-setup-guide.md`, `d4-completion-checklist.md`
