# Phase Prompts — Interactive Fill-in-the-Blank

**For teams that want to customize prompts for their specific project**

This file helps you build project-specific prompts by filling in your project details first, then showing you the complete prompt to use with Claude.

**How it works:**
1. Fill in the blanks for your project
2. Copy the completed prompt
3. Paste into Claude Code
4. Execute!

**Related file:** `phase-prompts.md` — Ready-to-copy version for busy teams

---

## 📑 Table of Contents

### PHASE 1: Project Foundation
- [Setup: Project Information](#setup-project-information-fill-these-in-first)
- [Task 1.1: Answer Project Details](#task-11-answer-project-details)
- [Task 1.2: Identify Technology Stack](#task-12-identify-technology-stack)
- [Task 1.3: Assess Compliance Requirements](#task-13-assess-compliance-requirements)

### PHASE 2: Architecture & Specifications
- [Task 2.1: Complete `.claude/context/architecture.md`](#task-21-complete-claudecontextarchitecturemd)
- [Task 2.2: Complete `docs/architecture/ARCHITECTURE.md` (Detailed)](#task-22-complete-docsarchitecturearchitecturemd-detailed)
- [Task 2.3: Create Architectural Decision Records](#task-23-create-architectural-decision-records)

### PHASE 3: Security & Compliance
- [Task 3.1: Complete `.claude/context/security-posture.md`](#task-31-complete-claudecontextsecurity-posturemd)
- [Task 3.2: Complete `docs/security/threat-model.md`](#task-32-complete-docssecuritythreat-modelmd)
- [Task 3.3: Complete `docs/security/compliance-mapping.md`](#task-33-complete-docssecuritycompliance-mappingmd)

### PHASE 4: Configure `.claude/` Folder
- [Task 4.1: Complete `.claude/context/glossary.md`](#task-41-complete-claudecontextglossarymd)
- [Task 4.2: Complete `.claude/context/commands.md`](#task-42-complete-claudecontextcommandsmd)
- [Task 4.3: Complete `.claude/context/hazards.md`](#task-43-complete-claudecontexthazardsmd)
- [Task 4.4: Complete `.claude/rules/10-app.md`](#task-44-complete-clauderules10-appmd)
- [Task 4.5: Complete `.claude/rules/security-guardrails.md`](#task-45-complete-clauderulessecurity-guardrailsmd)
- [Task 4.6: Configure `.claude/hooks/session-start.sh`](#task-46-configure-claudehookssession-startsh)
- [Task 4.7: Configure `.claude/settings.json`](#task-47-configure-claudesettingsjson)
- [Task 4.8: Complete `CLAUDE.md` (Root)](#task-48-complete-claudemd-root)

### PHASE 5: Source Code & Application Structure
- [Task 5.1: Create/Import Existing Source Code](#task-51-createimport-existing-source-code)
- [Task 5.2: Create Build Artifacts](#task-52-create-build-artifacts)

### PHASE 6: Agents & Skills (Optional)
- [Task 6.1: Plan Custom Agents](#task-61-plan-custom-agents-optional)
- [Task 6.2: Plan Custom Skills](#task-62-plan-custom-skills-optional)

### PHASE 7: Agent Workflow (Optional)
- [Task 7.1: Document Agent Workflow](#task-71-document-agent-workflow)

### PHASE 8: Verification & Sign-Off
- [Task 8.1: Verify Setup](#task-81-verify-setup)
- [Task 8.2: Run First Development Task](#task-82-run-first-development-task)
- [Task 8.3: Team Sign-Off](#task-83-team-sign-off)
- [Task 8.4: Final Commit & Tag](#task-84-final-commit--tag)

### Quick Reference
- [Model Recommendation Chart](#model-recommendation-chart)
- [Workflow Summary](#summary)

---

## Setup: Project Information (Fill These In First!)

Before you start the phases, gather these details about your project:

```markdown
## Your Project Details

**Project Name:** ___________________
**Project Description:** ___________________
**Primary Language:** ___________________
**Build Tool:** ___________________
**Primary Database:** ___________________
**Authentication Method:** ___________________
**Tech Lead Name & Email:** ___________________
**Security Lead Name & Email:** ___________________
**Development Lead Name & Email:** ___________________
**Main Approver Name & Email:** ___________________

**Compliance Frameworks Required:**
- [ ] PCI DSS (Payment card data?)
- [ ] GDPR (EU personal data?)
- [ ] HIPAA (Health records?)
- [ ] SOX (Public company?)
- [ ] Other: ___________________

**Technology Stack:**
- Backend Language: ___________________
- Backend Framework: ___________________
- Frontend Language: ___________________
- Frontend Framework: ___________________
- Database: ___________________
- Cache Layer: ___________________
- Message Queue: ___________________
```

**💡 Tip:** Save these answers in `docs/PROJECT_INFO.md` for reference throughout the setup.

---

## Model Recommendation Chart

Before each prompt, you'll see a model recommendation:

- **🟢 Haiku 4.5** → Quick tasks, simple forms (default)
- **🔵 Opus 5.5** → Complex analysis, architecture, security (⚡ `/fast` for faster output)
- **⚡ /fast** → Opus 5.5 with faster output (good middle ground)

---

## PHASE 1: Project Foundation

### Task 1.1: Answer Project Details

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 15 min  

**Fill in your project details:**

```markdown
PROJECT NAME: ___________________
BUSINESS PURPOSE: ___________________
USERS/STAKEHOLDERS: ___________________
TECH LEAD: ___________________ (name & email)
DEV LEAD: ___________________ (name & email)
SECURITY LEAD: ___________________ (name & email)
WRITE APPROVER: ___________________ (name & email)
```

**📋 Your Prompt:**

Once filled above, copy and paste this to Claude:

```
I'm setting up a new project called "[PROJECT NAME]" using the <APPLICATION_NAME> AI SSDLC template.

Project Details:
- Name: [PROJECT NAME]
- Business Purpose: [BUSINESS PURPOSE]
- Users: [USERS/STAKEHOLDERS]
- Tech Lead: [TECH LEAD]
- Dev Lead: [DEV LEAD]
- Security Lead: [SECURITY LEAD]
- Write Approver: [WRITE APPROVER]

Please confirm these details are complete and clear for documentation.
```

**✅ Save output to:** `docs/PROJECT_INFO.md`

---

### Task 1.2: Identify Technology Stack

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 20 min

**Fill in your tech stack:**

```markdown
BACKEND LANGUAGE: ___________________
BACKEND FRAMEWORK: ___________________
FRONTEND LANGUAGE: ___________________
FRONTEND FRAMEWORK: ___________________
PRIMARY DATABASE: ___________________
CACHE LAYER: ___________________
MESSAGE QUEUE: ___________________
AUTHENTICATION: ___________________
```

**📋 Your Prompt:**

```
I'm documenting the technology stack for my project "[PROJECT NAME]".

My technology stack is:

Backend:
- Language: [BACKEND LANGUAGE]
- Framework: [BACKEND FRAMEWORK]

Frontend:
- Language: [FRONTEND LANGUAGE]
- Framework: [FRONTEND FRAMEWORK]

Infrastructure:
- Primary database: [PRIMARY DATABASE]
- Cache layer: [CACHE LAYER]
- Message queue: [MESSAGE QUEUE]
- Authentication: [AUTHENTICATION]

Please organize this for storage in my project documentation.
```

**✅ Save output to:** `docs/PROJECT_INFO.md` (Tech Stack section)

---

### Task 1.3: Assess Compliance Requirements

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 15 min

**Fill in your compliance requirements:**

```markdown
PCI DSS Required? YES / NO
GDPR Required? YES / NO
HIPAA Required? YES / NO
SOX Required? YES / NO
OTHER FRAMEWORKS: ___________________
```

**📋 Your Prompt:**

```
I'm identifying compliance requirements for my project "[PROJECT NAME]".

Compliance applicability:
- PCI DSS (processes payment card data?): [YES/NO]
- GDPR (stores EU resident data?): [YES/NO]
- HIPAA (handles health records?): [YES/NO]
- SOX (public company?): [YES/NO]
- Other frameworks: [OTHER FRAMEWORKS]

Please confirm which compliance frameworks apply and suggest baseline controls for each.
```

**✅ Save output to:** `docs/PROJECT_INFO.md` (Compliance section)

---

## PHASE 2: Architecture & Specifications

### Task 2.1: Complete `.claude/context/architecture.md`

**🤖 Model:** Opus 5.5 (⚡ `/fast` recommended)  
**⏱️ Time:** 45 min

**Fill in your system architecture:**

```markdown
SYSTEM NAME: ___________________
SYSTEM PURPOSE (2-3 sentences): ___________________
UPSTREAM SYSTEMS (who calls me?): ___________________
DOWNSTREAM SYSTEMS (who do I call?): ___________________
EXTERNAL INTEGRATIONS: ___________________

MAJOR COMPONENTS:
1. Name: ___________ Technology: ___________ Responsibility: ___________
2. Name: ___________ Technology: ___________ Responsibility: ___________
3. Name: ___________ Technology: ___________ Responsibility: ___________

KEY DECISION 1: [AREA] → [CHOICE] → [WHY]
KEY DECISION 2: [AREA] → [CHOICE] → [WHY]

DATA ASSETS:
1. [ASSET NAME] - Owner: _____ Storage: _____ Retention: _____
2. [ASSET NAME] - Owner: _____ Storage: _____ Retention: _____
```

**📋 Your Prompt:**

```
I'm creating system architecture documentation for my project "[PROJECT NAME]".

Here's my system architecture:

**System Purpose:**
[SYSTEM PURPOSE]

**How It Fits:**
- Upstream: [UPSTREAM SYSTEMS]
- Downstream: [DOWNSTREAM SYSTEMS]
- External: [EXTERNAL INTEGRATIONS]

**Internal Structure:**
Component 1: [Name] using [Technology]
  Responsibility: [RESPONSIBILITY]

Component 2: [Name] using [Technology]
  Responsibility: [RESPONSIBILITY]

Component 3: [Name] using [Technology]
  Responsibility: [RESPONSIBILITY]

**Key Decisions:**
1. [AREA]: We chose [CHOICE] because [WHY]
2. [AREA]: We chose [CHOICE] because [WHY]

**Data Assets:**
[LIST YOUR DATA]

Please help me structure this into `.claude/context/architecture.md` format.
```

**✅ Output goes to:** `.claude/context/architecture.md`  
**✅ Then commit:** `git add .claude/context/architecture.md && git commit -m "docs: complete architecture.md"`

---

### Task 2.2: Complete `docs/architecture/ARCHITECTURE.md` (Detailed)

**🤖 Model:** Opus 5.5 (⚡ `/fast` recommended)  
**⏱️ Time:** 1 hour

**Fill in detailed architecture:**

```markdown
DEPLOYMENT INFRASTRUCTURE: ___________________
EXPECTED TRAFFIC/LOAD: ___________________
SCALING STRATEGY: ___________________
PERFORMANCE BOTTLENECKS: ___________________
NETWORK SECURITY BOUNDARIES: ___________________
DISASTER RECOVERY PLAN: ___________________
```

**📋 Your Prompt:**

```
I'm creating detailed architecture documentation for "[PROJECT NAME]".

My system architecture details:

**Deployment Infrastructure:**
[DEPLOYMENT INFRASTRUCTURE]

**Performance & Scalability:**
- Expected traffic/load: [EXPECTED TRAFFIC]
- Scaling strategy: [SCALING STRATEGY]
- Known bottlenecks: [PERFORMANCE BOTTLENECKS]

**Security Architecture:**
- Network boundaries: [NETWORK SECURITY BOUNDARIES]
- Authentication method: [FROM PHASE 1]
- Data encryption: [At-rest? In-transit?]

**Disaster Recovery:**
[DISASTER RECOVERY PLAN]

Please help me expand this into a comprehensive `docs/architecture/ARCHITECTURE.md`.
```

**✅ Output goes to:** `docs/architecture/ARCHITECTURE.md`  
**✅ Then commit:** `git add docs/architecture/ARCHITECTURE.md && git commit -m "docs: detailed architecture"`

---

### Task 2.3: Create Architectural Decision Records

**🤖 Model:** Opus 5.5  
**⏱️ Time:** 30 min

**Fill in major decisions:**

```markdown
DECISION 1 TITLE: ___________________
DECISION 1 REASONING: ___________________
DECISION 1 ALTERNATIVES REJECTED: ___________________

DECISION 2 TITLE: ___________________
DECISION 2 REASONING: ___________________
DECISION 2 ALTERNATIVES REJECTED: ___________________

DECISION 3 TITLE: ___________________
DECISION 3 REASONING: ___________________
DECISION 3 ALTERNATIVES REJECTED: ___________________
```

**📋 Your Prompt:**

```
I'm creating Architectural Decision Records (ADRs) for "[PROJECT NAME]".

My major decisions:

**Decision 1: [DECISION 1 TITLE]**
- Why: [DECISION 1 REASONING]
- Alternatives we rejected: [DECISION 1 ALTERNATIVES]
- Consequences: [Positive? Negative?]

**Decision 2: [DECISION 2 TITLE]**
- Why: [DECISION 2 REASONING]
- Alternatives we rejected: [DECISION 2 ALTERNATIVES]
- Consequences: [Positive? Negative?]

**Decision 3: [DECISION 3 TITLE]**
- Why: [DECISION 3 REASONING]
- Alternatives we rejected: [DECISION 3 ALTERNATIVES]
- Consequences: [Positive? Negative?]

Please help me structure these as ADRs in the format:
ADR-001.md, ADR-002.md, ADR-003.md
```

**✅ Output goes to:** `docs/architecture/adr/ADR-*.md`  
**✅ Then commit:** `git add docs/architecture/adr/ && git commit -m "docs: add ADRs"`

---

## PHASE 3: Security & Compliance

### Task 3.1: Complete `.claude/context/security-posture.md`

**🤖 Model:** Opus 5.5 (⚡ `/fast` acceptable)  
**⏱️ Time:** 45 min

**Fill in security baseline:**

```markdown
AUTHENTICATION PROVIDER: ___________________
AUTHORIZATION MODEL: ___________________
TOKEN TTL (e.g., 1 hour): ___________________
TOKEN STORAGE (e.g., HttpOnly Cookie): ___________________
SENSITIVE DATA TYPES: ___________________
ENCRYPTION AT-REST: ___________________
ENCRYPTION IN-TRANSIT: ___________________
DATA RETENTION POLICY: ___________________
SECRETS STORAGE (e.g., AWS Secrets Manager): ___________________
```

**📋 Your Prompt:**

```
I'm documenting security posture for "[PROJECT NAME]".

My security baseline:

**Authentication & Authorization:**
- Provider: [AUTHENTICATION PROVIDER]
- Model: [AUTHORIZATION MODEL]
- Token TTL: [TOKEN TTL]
- Token storage (frontend): [TOKEN STORAGE]

**Data Protection:**
- Sensitive data types: [SENSITIVE DATA TYPES]
- Encryption at-rest: [ENCRYPTION AT-REST]
- Encryption in-transit: [ENCRYPTION IN-TRANSIT]
- Data retention: [DATA RETENTION POLICY]

**Secrets Management:**
- Secrets storage: [SECRETS STORAGE]
- Rotation frequency: [How often?]

**Compliance frameworks:** [FROM PHASE 1]

Please help me structure this into `.claude/context/security-posture.md`.
```

**✅ Output goes to:** `.claude/context/security-posture.md`  
**✅ Then commit:** `git add .claude/context/security-posture.md && git commit -m "docs: complete security-posture.md"`

---

### Task 3.2: Complete `docs/security/threat-model.md`

**🤖 Model:** Opus 5.5  
**⏱️ Time:** 1 hour

**Fill in threat analysis:**

```markdown
PRIMARY ASSETS TO PROTECT: ___________________
EXTERNAL ENTRY POINTS: ___________________
KNOWN VULNERABILITIES: ___________________
PAST INCIDENTS: ___________________
HIGHEST RISK AREAS: ___________________
CURRENT MITIGATIONS: ___________________
```

**📋 Your Prompt:**

```
I'm creating a threat model for "[PROJECT NAME]" using STRIDE.

My threat model information:

**Assets to Protect:**
[PRIMARY ASSETS TO PROTECT]

**External Entry Points:**
[EXTERNAL ENTRY POINTS]

**Known Vulnerabilities:**
[KNOWN VULNERABILITIES]

**Past Incidents (Lessons Learned):**
[PAST INCIDENTS]

**Highest Risk Areas:**
[HIGHEST RISK AREAS]

**Current Mitigations:**
[CURRENT MITIGATIONS]

Please help me structure this using the STRIDE methodology
(Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
```

**✅ Output goes to:** `docs/security/threat-model.md`  
**✅ Then commit:** `git add docs/security/threat-model.md && git commit -m "docs: threat model"`

---

### Task 3.3: Complete `docs/security/compliance-mapping.md`

**🤖 Model:** Opus 5.5  
**⏱️ Time:** 1 hour

**Fill in compliance mapping:**

```markdown
APPLICABLE FRAMEWORKS (FROM PHASE 1): ___________________

FRAMEWORK 1 KEY CONTROLS:
- Control: ___________ Implementation: ___________ Evidence: ___________
- Control: ___________ Implementation: ___________ Evidence: ___________

FRAMEWORK 2 KEY CONTROLS:
- Control: ___________ Implementation: ___________ Evidence: ___________
- Control: ___________ Implementation: ___________ Evidence: ___________
```

**📋 Your Prompt:**

```
I'm mapping compliance controls to implementation for "[PROJECT NAME]".

My applicable frameworks: [APPLICABLE FRAMEWORKS]

**[FRAMEWORK 1] Controls:**
- [Control 1]: Implemented by [where?]. Evidence: [code/config file]
- [Control 2]: Implemented by [where?]. Evidence: [code/config file]

**[FRAMEWORK 2] Controls:**
- [Control 1]: Implemented by [where?]. Evidence: [code/config file]
- [Control 2]: Implemented by [where?]. Evidence: [code/config file]

Please help me structure compliance mapping with evidence links to my codebase.
```

**✅ Output goes to:** `docs/security/compliance-mapping.md`  
**✅ Then commit:** `git add docs/security/compliance-mapping.md && git commit -m "docs: compliance mapping"`

---

## PHASE 4: Configure `.claude/` Folder

### Task 4.1: Complete `.claude/context/glossary.md`

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 30 min

**Fill in domain terms:**

```markdown
BUSINESS TERM 1: ___________ Means: ___________ NOT: ___________
BUSINESS TERM 2: ___________ Means: ___________ NOT: ___________

TECHNICAL TERM 1: ___________ Means: ___________ Used in: ___________
TECHNICAL TERM 2: ___________ Means: ___________ Used in: ___________

ACRONYM 1: ___________ = ___________ Used in: ___________
ACRONYM 2: ___________ = ___________ Used in: ___________

OVERLOADED TERM: ___________ Can mean: (a) ___________ OR (b) ___________
```

**📋 Your Prompt:**

```
I'm creating a glossary for "[PROJECT NAME]" project domain.

My domain terms:

**Business Terms:**
- [TERM]: Means [DEFINITION] in our context, NOT [what it's not]
- [TERM]: Means [DEFINITION] in our context, NOT [what it's not]

**Technical Terms:**
- [TERM]: Means [DEFINITION], used in [where]
- [TERM]: Means [DEFINITION], used in [where]

**Acronyms:**
- [ACRONYM] = [Meaning], used in [where]
- [ACRONYM] = [Meaning], used in [where]

**Overloaded Terms:**
- "[TERM]" can mean: (a) [meaning 1] OR (b) [meaning 2]

Please help me structure this glossary for `.claude/context/glossary.md`.
```

**✅ Output goes to:** `.claude/context/glossary.md`  
**✅ Then commit:** `git add .claude/context/glossary.md && git commit -m "docs: glossary"`

---

### Task 4.2: Complete `.claude/context/commands.md`

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 20 min

**Fill in available commands:**

```markdown
BUILD COMMAND: ___________ Expected: ___________ Duration: ___________ Status: ✅/❌
TEST COMMAND: ___________ Expected: ___________ Duration: ___________ Status: ✅/❌
LINT COMMAND: ___________ Expected: ___________ Duration: ___________ Status: ✅/❌
SECURITY COMMAND: ___________ Expected: ___________ Duration: ___________ Status: ✅/❌
RUN SERVER COMMAND: ___________ Expected: ___________ Duration: ___________ Status: ✅/❌
```

**📋 Your Prompt:**

```
I'm documenting available commands for "[PROJECT NAME]".

My project commands:

| Purpose | Command | Expected Output | Duration | Status |
|---------|---------|-----------------|----------|--------|
| Build | [BUILD COMMAND] | [EXPECTED] | [TIME] | [✅/❌] |
| Test | [TEST COMMAND] | [EXPECTED] | [TIME] | [✅/❌] |
| Lint | [LINT COMMAND] | [EXPECTED] | [TIME] | [✅/❌] |
| Security | [SECURITY COMMAND] | [EXPECTED] | [TIME] | [✅/❌] |
| Run Server | [RUN SERVER COMMAND] | [EXPECTED] | [TIME] | [✅/❌] |

Please format this as `.claude/context/commands.md`.
```

**✅ Output goes to:** `.claude/context/commands.md`  
**✅ Then commit:** `git add .claude/context/commands.md && git commit -m "docs: commands"`

---

### Task 4.3: Complete `.claude/context/hazards.md`

**🤖 Model:** Opus 5.5  
**⏱️ Time:** 45 min

**Fill in security hazards:**

```markdown
SECURITY HAZARD 1: ___________ Location: ___________ Mitigation: ___________
SECURITY HAZARD 2: ___________ Location: ___________ Mitigation: ___________

DO NOT TOUCH AREA 1: ___________ Location: ___________ Owner: ___________
DO NOT TOUCH AREA 2: ___________ Location: ___________ Owner: ___________

PAST INCIDENT 1: ___________ When: ___________ Lesson: ___________
PAST INCIDENT 2: ___________ When: ___________ Lesson: ___________

KNOWN DEBT 1: ___________ Why accepted: ___________ Remediation: ___________ Target: ___________
KNOWN DEBT 2: ___________ Why accepted: ___________ Remediation: ___________ Target: ___________
```

**📋 Your Prompt:**

```
I'm documenting security hazards for "[PROJECT NAME]".

**Security Hazards:**
1. [HAZARD 1]: Located at [LOCATION]. Mitigation: [MITIGATION]
2. [HAZARD 2]: Located at [LOCATION]. Mitigation: [MITIGATION]

**Do Not Touch Without Review:**
1. [AREA 1]: Located at [LOCATION]. Owner: [OWNER]
2. [AREA 2]: Located at [LOCATION]. Owner: [OWNER]

**Incident History:**
1. [INCIDENT 1]: Happened in [WHEN]. Lesson: [LESSON]
2. [INCIDENT 2]: Happened in [WHEN]. Lesson: [LESSON]

**Known Technical Debt:**
1. [DEBT 1]: Accepted because [WHY]. Remediation: [HOW]. Target: [WHEN]
2. [DEBT 2]: Accepted because [WHY]. Remediation: [HOW]. Target: [WHEN]

**Surprising Behaviour:**
- [BEHAVIOR]: Why this way: [WHY]. Reference: [WHERE IN CODE]

Please help me structure this into `.claude/context/hazards.md`.
```

**✅ Output goes to:** `.claude/context/hazards.md`  
**✅ Then commit:** `git add .claude/context/hazards.md && git commit -m "docs: hazards"`

---

### Task 4.4: Complete `.claude/rules/10-app.md`

**🤖 Model:** Opus 5.5  
**⏱️ Time:** 45 min

**Fill in code conventions:**

```markdown
LANGUAGE: ___________ [FROM PHASE 1]
PACKAGE STRUCTURE: ___________________
NAMING CONVENTION FOR CLASSES: ___________________
NAMING CONVENTION FOR METHODS: ___________________
NAMING CONVENTION FOR CONSTANTS: ___________________

KEY PATTERN 1: ___________ Rule: ___________________
KEY PATTERN 2: ___________ Rule: ___________________

DATABASE QUERY REQUIREMENT: ___________________
ERROR HANDLING REQUIREMENT: ___________________
LOGGING REQUIREMENT: ___________________
```

**📋 Your Prompt:**

```
I'm documenting code conventions for "[PROJECT NAME]" ([LANGUAGE] project).

**Code Structure:**
- Package structure: [PACKAGE STRUCTURE]

**Naming Conventions:**
- Classes: [NAMING CONVENTION FOR CLASSES]
- Methods: [NAMING CONVENTION FOR METHODS]
- Constants: [NAMING CONVENTION FOR CONSTANTS]

**Key Patterns:**
- [KEY PATTERN 1]: [RULE]
- [KEY PATTERN 2]: [RULE]

**Database Queries:**
[DATABASE QUERY REQUIREMENT]

**Error Handling:**
[ERROR HANDLING REQUIREMENT]

**Logging:**
[LOGGING REQUIREMENT]

Please help me create comprehensive `.claude/rules/10-app.md` for [LANGUAGE].
```

**✅ Output goes to:** `.claude/rules/10-app.md`  
**✅ Then commit:** `git add .claude/rules/10-app.md && git commit -m "docs: conventions"`

---

### Task 4.5: Complete `.claude/rules/security-guardrails.md`

**🤖 Model:** Opus 5.5  
**⏱️ Time:** 45 min

**Fill in security rules:**

```markdown
MANDATORY RULE 1: ___________ Enforcement: ___________________
MANDATORY RULE 2: ___________ Enforcement: ___________________
MANDATORY RULE 3: ___________ Enforcement: ___________________

SECRETS MANAGEMENT RULE: ___________________
QUERY SAFETY RULE: ___________________
AUTHENTICATION RULE: ___________________
ENCRYPTION RULE: ___________________
LOGGING RULE: ___________________
```

**📋 Your Prompt:**

```
I'm documenting mandatory security rules for "[PROJECT NAME]".

**Mandatory Security Rules:**

**Secrets Management:**
Rule: [SECRETS MANAGEMENT RULE]
Enforcement: [How verified?]

**Database Queries:**
Rule: [QUERY SAFETY RULE]
Enforcement: [How verified?]

**Authentication & Authorization:**
Rule: [AUTHENTICATION RULE]
Enforcement: [How verified?]

**Encryption:**
Rule: [ENCRYPTION RULE]
Enforcement: [How verified?]

**Logging & Audit Trails:**
Rule: [LOGGING RULE]
Enforcement: [How verified?]

Please help me create `.claude/rules/security-guardrails.md` with these mandatory controls.
```

**✅ Output goes to:** `.claude/rules/security-guardrails.md`  
**✅ Then commit:** `git add .claude/rules/security-guardrails.md && git commit -m "docs: security rules"`

---

### Task 4.6: Configure `.claude/hooks/session-start.sh`

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 30 min

**Fill in prerequisite checks:**

```markdown
LANGUAGE TO CHECK: ___________ VERSION: ___________________
BUILD TOOL TO CHECK: ___________ COMMAND: ___________________
CONFIG FILE TO CHECK: ___________ LOCATION: ___________________
ADDITIONAL CHECKS: ___________________
```

**📋 Your Prompt:**

```
I need a session startup hook for "[PROJECT NAME]" written in bash.

Checks needed:
- Verify [LANGUAGE] [VERSION] installed
- Verify [BUILD TOOL] installed
- Verify Git installed
- Check for [CONFIG FILE] at [LOCATION]
- [ADDITIONAL CHECKS]

Please provide a shell script that performs these checks and prints status.
```

**✅ Output goes to:** `.claude/hooks/session-start.sh`  
**✅ Then:** `chmod +x .claude/hooks/session-start.sh`  
**✅ Test:** `bash .claude/hooks/session-start.sh`  
**✅ Then commit:** `git add .claude/hooks/session-start.sh && git commit -m "docs: session-start hook"`

---

### Task 4.7: Configure `.claude/settings.json`

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 20 min

**Fill in permissions:**

```markdown
FILES TO DENY ACCESS: ___________________
FILES/COMMANDS TO ALLOW: ___________________
ENVIRONMENT VARIABLES: ___________________
BUILD COMMANDS: ___________________
```

**📋 Your Prompt:**

```
I need to configure permissions in `.claude/settings.json` for "[PROJECT NAME]".

**Deny (Claude cannot access):**
- [FILES TO DENY ACCESS]

**Allow (Claude can use):**
- Commands: [BUILD COMMANDS]
- Read paths: [READ PATHS]
- Edit paths: [EDIT PATHS]

**Environment Variables:**
- [ENVIRONMENT VARIABLES]

Please generate the `.claude/settings.json` configuration for my project.
```

**✅ Output goes to:** `.claude/settings.json`  
**✅ Verify:** `python3 -m json.tool .claude/settings.json` (should show valid JSON)  
**✅ Then commit:** `git add .claude/settings.json && git commit -m "docs: settings.json"`

---

### Task 4.8: Complete `CLAUDE.md` (Root)

**🤖 Model:** Opus 5.5 (⚡ `/fast` acceptable)  
**⏱️ Time:** 30 min

**Fill in project instructions:**

```markdown
PROJECT NAME: ___________________
BUSINESS PURPOSE: ___________________
ENTRY POINTS: ___________ at ___________________

KEY CONVENTION 1: ___________ Why: ___________________
KEY CONVENTION 2: ___________ Why: ___________________

KEY RULE 1 (STRICTER THAN ENTERPRISE): ___________ Why: ___________________
KEY RULE 2 (STRICTER THAN ENTERPRISE): ___________ Why: ___________________

WRITE BOUNDARY: [Read-only / Gated to PERSON]
APPROVER: ___________ Email: ___________________
```

**📋 Your Prompt:**

```
I'm completing CLAUDE.md for "[PROJECT NAME]".

**Project:**
- Name: [PROJECT NAME]
- Purpose: [BUSINESS PURPOSE]
- Entry points: [ENTRY POINTS] at [PATHS]

**Local Conventions:**
- [KEY CONVENTION 1]: [WHY]
- [KEY CONVENTION 2]: [WHY]

**Narrowed Rules (Stricter than Enterprise):**
- [KEY RULE 1]: [WHY]
- [KEY RULE 2]: [WHY]

**Write Boundary:**
[Read-only / Gated to APPROVER]
Approver: [APPROVER NAME] - [EMAIL]

Please help me create CLAUDE.md with this information.
```

**✅ Output goes to:** `CLAUDE.md` (project root)  
**✅ Then commit:** `git add CLAUDE.md && git commit -m "docs: complete CLAUDE.md"`

---

## PHASE 5: Source Code & Application Structure

### Task 5.1: Create/Import Existing Source Code

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 1-4 hours  

**Fill in your code structure:**

```markdown
ENTRY POINT FILE: ___________ at ___________________
PACKAGE STRUCTURE: ___________________
TEST LOCATION: ___________________
BUILD ARTIFACT OUTPUT: ___________________
```

**📋 Your Prompt:**

```
I'm setting up the source code structure for "[PROJECT NAME]" ([LANGUAGE]).

**Entry Point:** [ENTRY POINT FILE] at [LOCATION]

**Package/Module Structure:**
[PACKAGE STRUCTURE]

**Tests:**
Location: [TEST LOCATION]
Runner: [TEST RUNNER]

**Build Output:**
[BUILD ARTIFACT OUTPUT]

Please help me create the directory structure for this project.
```

**✅ Create directories and add code**  
**✅ Then commit:** `git add src/ && git commit -m "feat: add source code"`

---

### Task 5.2: Create Build Artifacts

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 1-2 hours

**Fill in build details:**

```markdown
BUILD COMMAND: ___________________
TEST COMMAND: ___________________
LINT COMMAND: ___________________
SECURITY SCAN COMMAND: ___________________
```

**📋 Your Prompt:**

```
I need to verify my "[PROJECT NAME]" project builds correctly.

My commands:
- Build: [BUILD COMMAND]
- Test: [TEST COMMAND]
- Lint: [LINT COMMAND]
- Security: [SECURITY SCAN COMMAND]

Please verify each command works and report any issues.
```

**✅ Fix any build failures**  
**✅ Update** `.claude/context/commands.md` with actual commands  
**✅ Then commit:** `git add . && git commit -m "feat: add build configuration"`

---

## PHASE 6-7: Optional (Agents, Skills, Workflows)

**If creating custom agents or skills, fill these:**

```markdown
CUSTOM AGENT 1: ___________ Purpose: ___________________
CUSTOM SKILL 1: ___________ Purpose: ___________________
WORKFLOW TRIGGER: ___________ Step 1: ___________________
```

[See `phase-prompts.md` Phases 6-7 for detailed prompts]

---

## PHASE 8: Verification & Sign-Off

### Task 8.1: Verify Setup

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 15 min

**📋 Your Checklist:**

```bash
# Test session-start hook
bash .claude/hooks/session-start.sh
# Should show ✅ Environment ready!

# Verify context loads
claude context
# Should list your files

# Verify settings.json
python3 -m json.tool .claude/settings.json
# Should show valid JSON

# Verify git status
git status
# Should be clean or only expected changes
```

---

### Task 8.2: Run First Development Task

**🤖 Model:** Opus 5.5 (or Haiku 4.5 for simple tasks)  
**⏱️ Time:** 1-2 hours

**Fill in your first task:**

```markdown
FIRST TASK DESCRIPTION: ___________________
ACCEPTANCE CRITERIA: ___________________
```

**📋 Your Prompt:**

```
I'm testing my Claude Code setup by completing a real development task for "[PROJECT NAME]".

**Task:** [FIRST TASK DESCRIPTION]

**Requirements:**
[ACCEPTANCE CRITERIA]

**Context to use:**
- Architecture: `.claude/context/architecture.md`
- Conventions: `.claude/rules/10-app.md`
- Security rules: `.claude/rules/security-guardrails.md`
- Commands available: `.claude/context/commands.md`

Please help me complete this task following all project conventions.
```

**✅ Complete the task**  
**✅ Run tests**  
**✅ Then commit:** `git add . && git commit -m "[Your feature]"`

---

### Task 8.3: Team Sign-Off

**✅ Manual checklist:**

```
- [ ] Dev Lead: "Configuration complete"
- [ ] Security Lead: "Security baseline in place"
- [ ] Tech Lead: "Architecture documented"
- [ ] QA Lead: "Tests passing"
- [ ] All: "Ready to develop"
```

---

### Task 8.4: Final Commit & Tag

**🤖 Model:** Haiku 4.5  
**⏱️ Time:** 10 min

**📋 Your Prompt:**

```
I'm completing Phase D4 setup for "[PROJECT NAME]".

Please help me:
1. Check git status (should be clean)
2. Create a tag: git tag -a d4-harness-complete -m "Phase D4 complete"
3. Push tag: git push origin d4-harness-complete
4. List tags to confirm

All setup steps are complete. Time to start development!
```

---

## Summary

**Total Estimated Time:** 9-17 hours

| Phase | Time | Model | Status |
|-------|------|-------|--------|
| 1. Foundation | 1h | Haiku | [ ] |
| 2. Architecture | 2h | Opus 5.5 | [ ] |
| 3. Security | 1.5h | Opus 5.5 | [ ] |
| 4. Configure .claude/ | 2h | Mixed | [ ] |
| 5. Source Code | 1-4h | Haiku | [ ] |
| 6. Agents/Skills | 0-2h | Opus 5.5 | [ ] |
| 7. Workflow | 0-1h | Opus 5.5 | [ ] |
| 8. Verification | 1h | Haiku | [ ] |

---

**How to use these files together:**

- **This file (`phase-prompts-interactive.md`)**: Fill in blanks, get customized prompts
- **Other file (`phase-prompts.md`)**: Copy-paste ready prompts for quick reference
- **Setup Guide (`developer-setup-guide.md`)**: Deep reference material with examples

**Recommended workflow:**
1. Start with this file — fill in your project details
2. Use the generated prompts with Claude Code
3. Keep `phase-prompts.md` bookmarked for reference
4. Check `developer-setup-guide.md` if you need detailed explanation

---

**Last Updated:** 2026-10-04  
**Related:** `phase-prompts.md` (ready-to-copy version), `developer-setup-guide.md` (deep reference)
