# Phase Prompts — Ready-to-Copy

**For teams that want ready-made prompts to execute immediately**

This file contains complete, copy-paste-ready prompts for each phase of the developer setup guide. Each prompt includes:
- ✅ Ready-to-use text (copy directly)
- 🤖 Recommended Claude Code model
- ⏱️ Estimated execution time
- 📋 What to do with the output

**Related file:** `phase-prompts-interactive.md` — Interactive, fill-in-the-blank version

---

## How to Use This File

1. **Find your current phase** (Phase 1-8 below)
2. **Pick a task** within that phase
3. **Copy the prompt** marked with `📋 PROMPT:`
4. **Choose the recommended model** (see 🤖 below)
5. **Execute in Claude Code**
6. **Save the output** as indicated

### Model Recommendations

- **🟢 Haiku 4.5** — Quick clarifications, simple forms, fast execution (default)
- **🔵 Opus 5.5** — Complex analysis, architecture, security decisions, comprehensive documentation (recommended for heavy lifting)
- **⚡ /fast mode** — Opus 5.5 with faster output (good middle ground)

---

## 📑 Table of Contents

### PHASE 1: Project Foundation (1 hour)
- [Task 1.1: Answer Project Details](#task-11-answer-project-details)
- [Task 1.2: Identify Technology Stack](#task-12-identify-technology-stack)
- [Task 1.3: Assess Compliance Requirements](#task-13-assess-compliance-requirements)

### PHASE 2: Architecture & Specifications (2 hours)
- [Task 2.1: Complete `.claude/context/architecture.md`](#task-21-complete-claudecontextarchitecturemd)
- [Task 2.2: Complete `docs/architecture/ARCHITECTURE.md` (Detailed)](#task-22-complete-docsarchitecturearchitecturemd-detailed)
- [Task 2.3: Create Architectural Decision Records](#task-23-create-architectural-decision-records)

### PHASE 3: Security & Compliance (1.5 hours)
- [Task 3.1: Complete `.claude/context/security-posture.md`](#task-31-complete-claudecontextsecurity-posturemd)
- [Task 3.2: Complete `docs/security/threat-model.md`](#task-32-complete-docssecuritythreat-modelmd)
- [Task 3.3: Complete `docs/security/compliance-mapping.md`](#task-33-complete-docssecuritycompliance-mappingmd)

### PHASE 4: Configure `.claude/` Folder (2 hours)
- [Task 4.1: Complete `.claude/context/glossary.md`](#task-41-complete-claudecontextglossarymd)
- [Task 4.2: Complete `.claude/context/commands.md`](#task-42-complete-claudecontextcommandsmd)
- [Task 4.3: Complete `.claude/context/hazards.md`](#task-43-complete-claudecontexthazardsmd)
- [Task 4.4: Complete `.claude/rules/10-app.md`](#task-44-complete-clauderules10-appmd)
- [Task 4.5: Complete `.claude/rules/security-guardrails.md`](#task-45-complete-clauderulessecurity-guardrailsmd)
- [Task 4.6: Configure `.claude/hooks/session-start.sh`](#task-46-configure-claudehookssession-startsh)
- [Task 4.7: Configure `.claude/settings.json`](#task-47-configure-claudesettingsjson)
- [Task 4.8: Complete `CLAUDE.md` (Root)](#task-48-complete-claudemd-root)

### PHASE 5: Source Code & Application Structure (Variable)
- [Task 5.1: Create/Import Existing Source Code](#task-51-createimport-existing-source-code)
- [Task 5.2: Create Build Artifacts](#task-52-create-build-artifacts)

### PHASE 6: Set Up Agents, Skills & Hooks (Optional/As-Needed)
- [Task 6.1: Plan Custom Agents](#task-61-plan-custom-agents-optional)
- [Task 6.2: Plan Custom Skills](#task-62-plan-custom-skills-optional)
- [Task 6.3: Create Evals for Custom Skills](#task-63-create-evals-for-custom-skills-when-publishing)
- [Task 6.4: Configure Additional Hooks](#task-64-configure-additional-hooks-as-needed)

### PHASE 7: Agent Workflow Setup (Optional)
- [Task 7.1: Document Agent Workflow](#task-71-document-agent-workflow)
- [Task 7.2: Create Agent Specifications](#task-72-create-agent-specifications-if-custom)
- [Task 7.3: Document Workflow in `.claude/agents/`](#task-73-document-workflow-in-claudeagents)

### PHASE 8: Verification & Sign-Off (1 hour)
- [Task 8.1: Verify Claude Code Setup](#task-81-verify-claude-code-setup)
- [Task 8.2: Run First Development Task](#task-82-run-first-development-task)
- [Task 8.3: Team Sign-Off](#task-83-team-sign-off)
- [Task 8.4: Final Commit & Tag](#task-84-final-commit--tag)

---

## PHASE 1: Project Foundation (1 hour)

### Task 1.1: Answer Project Details

**🤖 Recommended Model:** Haiku 4.5 (or `/fast`)  
**⏱️ Time:** 15 minutes  
**📤 Output:** Document answers in `docs/PROJECT_INFO.md`

**📋 PROMPT:**

```
I'm setting up a new project using the rrd-ir AI SSDLC template. 
I need to answer foundational questions about my project.

Please help me document these answers (you don't need to provide answers, 
just confirm what information I should gather):

1. Application name: What is this project called?
2. Business purpose: In 2-3 sentences, what does it do and who uses it?
3. Users/stakeholders: Who are the main users?
4. Tech lead name & email: Who's responsible for technical decisions?
5. Dev lead name & email: Who's responsible for the dev team?
6. Security lead name & email: Who owns security decisions?
7. Approver for write operations: Who signs off on commits/merges?

For each, I'll provide my project's details, and you confirm they're complete.
```

**✅ Next steps:** 
- Gather answers to these 7 questions
- Save to `docs/PROJECT_INFO.md`
- Proceed to Task 1.2

---

### Task 1.2: Identify Technology Stack

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 20 minutes  
**📤 Output:** Update `docs/PROJECT_INFO.md` with tech stack section

**📋 PROMPT:**

```
I'm documenting my project's technology stack for the rrd-ir template.

Please help me organize this information for storage in my project:

Backend:
- Language: [e.g., Java 21, Python 3.11, Go 1.21]
- Framework: [e.g., Spring Boot, FastAPI, Gin]
- ORM/Database access: [e.g., JPA, SQLAlchemy, GORM]

Frontend:
- Language: [e.g., TypeScript, JavaScript]
- Framework: [e.g., React 18, Vue 3, Angular 16]
- Build tool: [e.g., Webpack, Vite]

Data & Infrastructure:
- Primary database: [e.g., PostgreSQL 15, MySQL 8, MongoDB]
- Cache layer: [e.g., Redis, Memcached]
- Message queue: [e.g., RabbitMQ, Kafka, AWS SQS]
- Authentication: [e.g., OAuth 2.0, SAML, JWT via AWS Cognito]

Confirm this structure is complete and suggest any gaps I should fill.
```

**✅ Next steps:**
- Add tech stack details to `docs/PROJECT_INFO.md`
- Proceed to Task 1.3

---

### Task 1.3: Assess Compliance Requirements

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 15 minutes  
**📤 Output:** Update `docs/PROJECT_INFO.md` with compliance section

**📋 PROMPT:**

```
I'm documenting compliance requirements for my project.

For each framework below, I need to determine if it applies:

- PCI DSS: Does my application process, store, or transmit credit card data? (YES/NO)
- GDPR: Does my application store personal data of EU residents? (YES/NO)
- HIPAA: Does my application handle protected health information? (YES/NO)
- SOX: Am I a public company with financial reporting requirements? (YES/NO)
- CCPA: Does my application handle California resident personal data? (YES/NO)
- Other frameworks specific to my industry: [describe]

For each "YES", please suggest what baseline controls I should document.
```

**✅ Next steps:**
- Update `docs/PROJECT_INFO.md` with compliance requirements
- Proceed to Phase 2

---

## PHASE 2: Architecture & Specifications (2 hours)

### Task 2.1: Complete `.claude/context/architecture.md`

**🤖 Recommended Model:** Opus 5.5 (⚡ `/fast` mode acceptable)  
**⏱️ Time:** 45 minutes  
**📤 Output:** Fill `.claude/context/architecture.md`

**📋 PROMPT:**

```
I'm creating system architecture documentation for the Claude Code context.

Please help me structure and fill this template. I'll provide the answers 
after you confirm the template is clear:

## Architecture — [Project Name]

**Last Updated:** [DATE]
**Owner:** [Tech Lead Name]
**Full Details:** docs/architecture/ARCHITECTURE.md

---

## What it is

[2-3 sentence business description of the system]

**Example:**
"This is a real-time revenue recognition system that processes financial 
transactions for SaaS companies. It calculates revenue recognition based on 
ASC 606 standards and provides compliance reporting to finance teams and auditors."

---

## How it fits

[Who calls this system? What systems does it call?]

**Example:**
"Upstream: Billing systems call our Revenue Recognition API
Downstream: We call the General Ledger system for posting entries
External: We integrate with Salesforce via REST API for subscription data"

---

## Internal structure

| Component | Technology | Responsibility |
|-----------|-----------|-----------------|
| [Name] | [Tech] | [What it does] |

Example rows:
| API Layer | Spring Boot REST | Handles incoming transaction requests |
| Processing Engine | Java with Drools | Applies revenue recognition rules |
| Database | PostgreSQL | Stores transactions and calculations |

---

## Interfaces

| Interface | Type | Consumers | Details |
|-----------|------|-----------|---------|
| [Path/Event] | REST/Event | [Who uses it] | [What it does] |

---

## Key Decisions

| Area | Chosen | Why | Record |
|------|--------|-----|--------|
| [Area] | [Choice] | [Reasoning] | [ADR reference] |

---

## Data & State

| Data | Owner | Storage | Retention |
|------|-------|---------|-----------|
| [What] | [Who manages] | [Where stored] | [How long] |

---

Does this template match your system? I'm ready to fill it with your details.
```

**✅ Next steps:**
- Answer the template questions
- Run: `git add .claude/context/architecture.md && git commit -m "docs: complete architecture.md"`
- Proceed to Task 2.2

---

### Task 2.2: Complete `docs/architecture/ARCHITECTURE.md` (Detailed)

**🤖 Recommended Model:** Opus 5.5 (⚡ `/fast` mode recommended)  
**⏱️ Time:** 1 hour  
**📤 Output:** Create detailed `docs/architecture/ARCHITECTURE.md`

**📋 PROMPT:**

```
I'm creating detailed architecture documentation for my project.

Please help me create a comprehensive architecture document with these sections:

1. System Overview
   - Purpose and business value
   - Key constraints and requirements
   
2. Component Architecture
   - Major components and their responsibilities
   - Technology choices for each component
   - Component interactions diagram (ASCII or text description)
   
3. Data Flow
   - Request flow (user request → response)
   - Background processes
   - Integration points with external systems
   
4. Deployment Architecture
   - Infrastructure layout (servers, databases, caches, etc.)
   - Network topology
   - Scaling strategy
   
5. Technology Stack Rationale
   - Why each major technology was chosen
   - Trade-offs considered
   - Alternatives rejected and why
   
6. Performance & Scalability
   - Expected traffic/load
   - Bottlenecks identified
   - Scaling approach
   
7. Security Architecture
   - Authentication and authorization
   - Data encryption (at-rest and in-transit)
   - Network security boundaries
   
Please provide a template structure I can fill with my project details.
```

**✅ Next steps:**
- Fill in the template with your project details
- Run: `git add docs/architecture/ARCHITECTURE.md && git commit -m "docs: detailed architecture documentation"`
- Proceed to Task 2.3

---

### Task 2.3: Create Architectural Decision Records (ADRs)

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 30 minutes  
**📤 Output:** Create `docs/architecture/adr/ADR-001.md`, `ADR-002.md`, etc.

**📋 PROMPT:**

```
I'm creating Architectural Decision Records (ADRs) for major decisions in my project.

For each major technical decision, please help me structure an ADR with:

## ADR-001: [Decision Title]

### Status: Accepted | Pending | Deprecated

### Context
[What problem were we solving?]
[What options did we consider?]
[What constraints were we under?]

### Decision
[What did we decide and why?]

### Consequences
**Positive:**
+ Benefit 1
+ Benefit 2

**Negative/Trade-offs:**
- Trade-off 1
- Trade-off 2

### Implementation Notes
[How is this implemented in the code?]
[References to relevant code files]

---

I need ADRs for these decisions:
1. [Your major decision 1 - e.g., "Why we chose PostgreSQL over MongoDB"]
2. [Your major decision 2 - e.g., "Why we use RabbitMQ for async processing"]
3. [Your major decision 3 - e.g., "Why we chose Spring Boot over Quarkus"]

Please help me structure and fill each ADR.
```

**✅ Next steps:**
- Create ADRs in `docs/architecture/adr/`
- Run: `git add docs/architecture/adr/ && git commit -m "docs: add architectural decision records"`
- Proceed to Phase 3

---

## PHASE 3: Security & Compliance (1.5 hours)

### Task 3.1: Complete `.claude/context/security-posture.md`

**🤖 Recommended Model:** Opus 5.5 (⚡ `/fast` mode acceptable)  
**⏱️ Time:** 45 minutes  
**📤 Output:** Fill `.claude/context/security-posture.md`

**📋 PROMPT:**

```
I'm documenting my project's security posture and compliance baseline.

Please help me fill this security posture document:

## Compliance Requirements

| Framework | Required | Mapping | Owner |
|-----------|----------|---------|-------|
| PCI DSS | YES/NO | [Link to docs] | [Name] |
| GDPR | YES/NO | [Link to docs] | [Name] |
| HIPAA | YES/NO | [Link to docs] | [Name] |
| SOX | YES/NO | [Link to docs] | [Name] |

---

## Authentication & Authorization

| Aspect | Value | Notes |
|--------|-------|-------|
| Method | [OAuth 2.0, SAML, JWT, etc.] | |
| Provider | [AWS Cognito, Okta, Auth0, etc.] | |
| Authorization Model | [RBAC, ABAC, etc.] | |
| Default Access | [DENY all / ALLOW all] | Explicit allowlist? |
| Token Storage (Frontend) | [HttpOnly Cookie, localStorage, etc.] | |
| Token TTL | [Duration] | Auto-refresh? |

---

## Data Classification

| Data Type | Classification | Storage | Encryption | Retention | Access |
|-----------|---|---|---|---|---|
| [Type] | [Public/Internal/Confidential] | [Where] | [At-rest/In-transit] | [How long] | [Who] |

---

## Secrets Management

| Secret Type | Storage | Rotation | Owner |
|-----------|---------|----------|-------|
| API Keys | [AWS Secrets Manager, HashiCorp Vault, etc.] | [Frequency] | [Owner] |
| Database Passwords | [Storage] | [Frequency] | [Owner] |
| OAuth Credentials | [Storage] | [Frequency] | [Owner] |

---

Please help me fill this with my project's security baseline.
```

**✅ Next steps:**
- Complete `.claude/context/security-posture.md`
- Run: `git add .claude/context/security-posture.md && git commit -m "docs: complete security-posture.md"`
- Proceed to Task 3.2

---

### Task 3.2: Complete `docs/security/threat-model.md`

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 1 hour  
**📤 Output:** Create threat model document

**📋 PROMPT:**

```
I'm creating a threat model for my project using the STRIDE methodology.

Please help me structure a comprehensive threat model with:

## Assets Being Protected
[List: databases, APIs, user data, intellectual property, etc.]

## STRIDE Threats

### Spoofing (Identity)
| Threat | Attack Vector | Impact | Mitigation |
|--------|---|---|---|
| [Example: Attacker impersonates admin] | [How?] | [Result?] | [How prevented?] |

### Tampering (Integrity)
| Threat | Attack Vector | Impact | Mitigation |
|--------|---|---|---|

### Repudiation (Accountability)
| Threat | Attack Vector | Impact | Mitigation |
|--------|---|---|---|

### Information Disclosure (Confidentiality)
| Threat | Attack Vector | Impact | Mitigation |
|--------|---|---|---|

### Denial of Service
| Threat | Attack Vector | Impact | Mitigation |
|--------|---|---|---|

### Elevation of Privilege
| Threat | Attack Vector | Impact | Mitigation |
|--------|---|---|---|

---

## Attack Surface

[Describe external entry points: APIs, databases, files, etc.]

## Risk Rating

| Threat | Likelihood | Impact | Priority | Status |
|--------|-----------|--------|----------|--------|

---

Please help me identify threats and fill this for my project.
```

**✅ Next steps:**
- Complete threat model
- Run: `git add docs/security/threat-model.md && git commit -m "docs: complete threat model"`
- Proceed to Task 3.3

---

### Task 3.3: Complete `docs/security/compliance-mapping.md`

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 1 hour  
**📤 Output:** Create compliance mapping document

**📋 PROMPT:**

```
I'm mapping compliance controls to implementation in my project.

For each applicable framework (PCI DSS, GDPR, HIPAA, etc.), I need to:
1. List the control requirement
2. Link to code/config that implements it
3. Verify it's actually in place

Please help me structure a compliance mapping with:

## PCI DSS Controls (if applicable)

| Control | Requirement | Implementation | Evidence | Status |
|---------|-------------|-----------------|----------|--------|
| 3.4 | Render PAN unreadable anywhere it is stored | [Where in code?] | [File/line] | ✅/❌ |
| 6.5.1 | Prevent SQL injection | [Prepared statements in...] | [File/line] | ✅/❌ |

## GDPR Controls (if applicable)

| Control | Requirement | Implementation | Evidence | Status |
|---------|-------------|-----------------|----------|--------|
| Art. 32 | Data protection by design | [Encryption at...] | [File/line] | ✅/❌ |
| Art. 17 | Right to erasure | [Delete function at...] | [File/line] | ✅/❌ |

## [Other frameworks]

[Similar mapping]

---

Please help me map my compliance controls to evidence in my codebase.
```

**✅ Next steps:**
- Complete compliance mapping
- Run: `git add docs/security/compliance-mapping.md && git commit -m "docs: complete compliance mapping"`
- Proceed to Phase 4

---

## PHASE 4: Configure `.claude/` Folder (2 hours)

### Task 4.1: Complete `.claude/context/glossary.md`

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 30 minutes  
**📤 Output:** Fill `.claude/context/glossary.md`

**📋 PROMPT:**

```
I'm creating a glossary of domain-specific terms for my project.

Please help me organize these terms for my project's domain:

## Business Terms

| Term | Means Here | Does NOT Mean |
|------|-----------|-----------------|
| [Example: ASC 606] | [Accounting Standards for Revenue Recognition] | [What it's not] |
| [Your term 1] | [Your definition] | [What it's not] |

## Technical Terms

| Term | Means Here | Used In |
|------|-----------|---------|
| [Example: Allocation Engine] | [The component that applies rules] | [Where it appears] |
| [Your term 1] | [Your definition] | [Where it's used] |

## Acronyms

| Acronym | Meaning | Used In |
|---------|---------|---------|
| [ASC 606] | [Accounting Standards...] | [Finance docs] |

## Overloaded Terms (Same word, different meanings)

**"Transaction"** can mean:
- Database transaction (ACID unit of work)
- Business transaction (customer purchase)

Always clarify which you mean.

---

Please help me list domain terms from my project.
```

**✅ Next steps:**
- Complete `.claude/context/glossary.md`
- Run: `git add .claude/context/glossary.md && git commit -m "docs: complete glossary.md"`

---

### Task 4.2: Complete `.claude/context/commands.md`

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 20 minutes  
**📤 Output:** Fill `.claude/context/commands.md`

**📋 PROMPT:**

```
I'm documenting the commands available in my project.

Please help me create a commands contract table:

## Command Contract

| Purpose | Command | Expected Output | Duration | Status Today |
|---------|---------|-----------------|----------|--------------|
| Build application | [e.g., mvn clean package] | exit 0 | [time] | ✅/❌ |
| Run tests | [e.g., mvn test] | exit 0, >90% coverage | [time] | ✅/❌ |
| Lint code | [e.g., mvn checkstyle:check] | exit 0, no warnings | [time] | ✅/❌ |
| Security scan | [e.g., mvn dependency-check:check] | exit 0 | [time] | ✅/❌ |
| Start local server | [e.g., mvn spring-boot:run] | Server listening on :8080 | [time] | ✅/❌ |

---

Please help me document the actual build/test/lint commands for my project.
```

**✅ Next steps:**
- Complete `.claude/context/commands.md`
- Run: `git add .claude/context/commands.md && git commit -m "docs: complete commands.md"`

---

### Task 4.3: Complete `.claude/context/hazards.md`

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 45 minutes  
**📤 Output:** Fill `.claude/context/hazards.md`

**📋 PROMPT:**

```
I'm documenting security hazards and dangerous areas in my project.

Please help me structure a comprehensive hazards document:

## Security Hazards

| Vulnerability | Path | Why Critical | Impact | Mitigation | Status | Owner |
|---|---|---|---|---|---|---|
| [e.g., SQL Injection] | src/api/TransactionController.java:42 | User input in WHERE clause | Full database compromise | Use PreparedStatement | Open | [Owner] |

## Do Not Touch Without Review

| Area | Path | Why | Owner |
|---|---|---|---|
| Revenue recognition rules | src/main/resources/rules/asc606.drl | Small change = big financial impact | Finance Lead |
| Payment processing | src/api/PaymentController.java | PCI compliance risk | Security Lead |

## Incident History

| What Happened | Area | When | Lesson |
|---|---|---|---|
| API leaked customer data in error messages | src/api/ErrorHandler.java | 2026-08-15 | Never include customer data in errors |

## Surprising Behaviour

- **MRR calculation:** We recognize revenue monthly, but charges are pro-rated daily.
  Why: Customer contracts specify monthly recognition but billing is daily.
  Reference: src/engine/ProrationEngine.java

## Known Debt

| Debt | Area | Why Accepted | Remediation | Target |
|---|---|---|---|---|
| No automated tests for rule engine | src/test/java/engine/ | Drools testing is complex | Write 20 sample test cases | 2026-12-31 |

---

Please help me identify hazards, incidents, and debt in my project.
```

**✅ Next steps:**
- Complete `.claude/context/hazards.md`
- Run: `git add .claude/context/hazards.md && git commit -m "docs: complete hazards.md"`

---

### Task 4.4: Complete `.claude/rules/10-app.md`

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 45 minutes  
**📤 Output:** Fill `.claude/rules/10-app.md`

**📋 PROMPT:**

```
I'm documenting code conventions for my project.

Please help me create a comprehensive conventions document for [LANGUAGE]:

---
description: [Project name] code conventions
paths: ["src/**/*.[ext]"]
---

# [Project Name] Conventions

**Last Updated:** [DATE]
**Owner:** [Tech Lead]

---

## Package/Folder Structure

[For Java: src/main/java/com/company/app/ with api/, service/, model/, etc.]
[For Python: src/ with api/, service/, model/, etc.]
[For Node: src/ with controllers/, services/, models/, etc.]

---

## Naming Conventions

| Item | Pattern | Example |
|------|---------|---------|
| Classes | PascalCase | UserService |
| Methods/functions | camelCase | calculateRevenue() |
| Constants | UPPER_CASE | DEFAULT_TIMEOUT |
| Database tables | snake_case | user_accounts |
| Booleans | is/has prefix | isActive, hasError |

---

## Design Patterns

### Dependency Injection
[How to do DI in your framework]

### Transaction Boundaries
[When to use @Transactional, transactions, etc.]

### Error Handling
[How to handle errors - what to log, what to expose]

---

## Database Queries

[Prepared statements only? Named parameters? Examples?]

---

## Logging Standards

| Level | Usage | Example |
|-------|-------|---------|
| TRACE | Very detailed | "Entering method X with params Y" |
| DEBUG | Development debugging | "Query returned 42 results" |
| INFO | Interesting business events | "Transaction created: ID=123" |
| WARN | Potential problems | "Retry attempt 3 of 5" |
| ERROR | Error but recoverable | "Failed to call external API" |

---

## Do Not

- ❌ [Anti-pattern 1]
- ❌ [Anti-pattern 2]
- ❌ [Anti-pattern 3]

---

## Code Review Checklist

- [ ] Follows naming conventions
- [ ] Design patterns applied correctly
- [ ] Error messages clear and safe
- [ ] Logging is appropriate
- [ ] Tests included
- [ ] No security warnings

---

Please help me document conventions for [LANGUAGE] in my project.
```

**✅ Next steps:**
- Complete `.claude/rules/10-app.md`
- Run: `git add .claude/rules/10-app.md && git commit -m "docs: complete 10-app.md"`

---

### Task 4.5: Complete `.claude/rules/security-guardrails.md`

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 45 minutes  
**📤 Output:** Fill `.claude/rules/security-guardrails.md`

**📋 PROMPT:**

```
I'm creating mandatory security rules for my project.

Please help me structure security guardrails:

---
description: Mandatory security controls for [Project Name]
paths: ["src/**"]
---

# Security Guardrails — [Project Name]

**Last Updated:** [DATE]
**Owner:** [Security Lead]

---

## Secrets Management — MANDATORY

| Rule | Enforcement |
|------|-------------|
| Never commit credentials, keys, tokens | Pre-commit hooks + secret scanning |
| Use environment variables for secrets | Block hardcoded passwords in CI/CD |
| [Your rule] | [How enforced] |

---

## Database Queries — MANDATORY

| Rule | Enforcement |
|------|-------------|
| Parameterized queries only | SAST scanning + code review |
| No string concatenation in SQL | Pre-commit hook rejects patterns |

---

## Authentication & Authorization

| Rule | Enforcement |
|------|-------------|

---

## Encryption

| Rule | Enforcement |
|------|-------------|

---

## Logging & Audit Trails

| Rule | Enforcement |
|------|-------------|

---

## Code Review Security Checklist

- [ ] No hardcoded secrets
- [ ] All DB queries parameterized
- [ ] Auth/authz checks present
- [ ] User input validated
- [ ] Errors don't leak sensitive info
- [ ] Logging doesn't include secrets

---

Please help me document security guardrails for my project.
```

**✅ Next steps:**
- Complete `.claude/rules/security-guardrails.md`
- Run: `git add .claude/rules/security-guardrails.md && git commit -m "docs: complete security-guardrails.md"`

---

### Task 4.6: Configure `.claude/hooks/session-start.sh`

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 30 minutes  
**📤 Output:** Create `.claude/hooks/session-start.sh`

**📋 PROMPT:**

```
I'm creating a session startup hook for my project.

Please provide a shell script that checks prerequisites when Claude Code starts:

1. Check [Language] version (e.g., Java 21)
2. Check build tool installed (e.g., Maven, npm)
3. Check Git installed
4. Check .env or config file exists
5. Print available commands

For my project:
- Primary language: [Language] [version]
- Build tool: [Maven/npm/gradle/etc.]
- Build command: [mvn clean package / npm run build / etc.]
- Config file: [.env / application.properties / etc.]

Please provide a ready-to-use bash script that performs these checks.
```

**✅ Next steps:**
- Save as `.claude/hooks/session-start.sh`
- Run: `chmod +x .claude/hooks/session-start.sh`
- Test: `bash .claude/hooks/session-start.sh`
- Run: `git add .claude/hooks/session-start.sh && git commit -m "docs: configure session-start.sh hook"`

---

### Task 4.7: Configure `.claude/settings.json`

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 30 minutes  
**📤 Output:** Fill `.claude/settings.json`

**📋 PROMPT:**

```
I'm configuring permissions and environment for my project.

Please help me fill .claude/settings.json with:

{
  "_comment_scope": "Tier 3. Narrows enterprise policy for [Project Name].",
  
  "permissions": {
    "deny": [
      "Read(.env)",
      "Read(src/main/resources/secrets/*)",
      "Edit(.env)",
      "Edit(src/main/resources/secrets/*)"
    ],
    "allow": [
      "Bash([mvn/npm command]:*)",
      "Read(src/**)",
      "Read(docs/**)",
      "Edit(src/**)",
      "Edit(docs/**)"
    ]
  },
  
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  },
  
  "env": {
    "[PROJECT]_APP_NAME": "[Project name]",
    "[PROJECT]_HARNESS_VERSION": "1.0.0",
    "ENVIRONMENT": "development"
  }
}

Please help me fill this with my project details.
```

**✅ Next steps:**
- Update `.claude/settings.json`
- Test: `python3 -m json.tool .claude/settings.json` (should show valid JSON)
- Run: `git add .claude/settings.json && git commit -m "docs: configure settings.json"`

---

### Task 4.8: Complete `CLAUDE.md` (Root)

**🤖 Recommended Model:** Opus 5.5 (⚡ `/fast` mode acceptable)  
**⏱️ Time:** 30 minutes  
**📤 Output:** Fill `CLAUDE.md`

**📋 PROMPT:**

```
I'm completing CLAUDE.md (project root instructions) for my project.

Please help me fill this template:

# [Project Name]

Extends the enterprise harness instructions. Everything in the enterprise set applies here.

## What this application is

[2-3 sentences: Business purpose, users, value]

**Example:**
"rrd-ir is a revenue recognition system that processes financial transactions 
for SaaS companies. It calculates revenue recognition based on ASC 606 standards 
and provides compliance reporting to finance teams and auditors."

---

## Repository map

| Area | Path | Responsibility |
|---|---|---|
| API Layer | src/main/java/api/ | REST endpoints |
| Business Logic | src/main/java/service/ | Core algorithms |
| Data Models | src/main/java/model/ | JPA entities |
| Tests | src/test/ | Unit & integration tests |
| Docs | docs/ | Architecture & security |

---

## Commands

Available commands are defined in `.claude/context/commands.md`.

---

## Domain terms

See `.claude/context/glossary.md`. Key terms:
- [Term 1]: [Definition]
- [Term 2]: [Definition]

---

## Hazards

See `.claude/context/hazards.md`:
- Security hazards: [brief list]
- Do not touch: [brief list]
- Incidents: [brief list]

**Critical:** Always read hazards before making changes to [sensitive area].

---

## Local conventions

Where this application departs from enterprise standard:

- [Convention 1] — [Why]
- [Convention 2] — [Why]

---

## Narrowed rules

Where this application is stricter than enterprise set:

- [Rule 1] — [Why]
- [Rule 2] — [Why]

---

## Write boundary

[Read-only or gated operations?]

**Gated actions escalate to:** [Name] — [email]

---

Please help me complete CLAUDE.md with my project details.
```

**✅ Next steps:**
- Complete `CLAUDE.md`
- Run: `git add CLAUDE.md && git commit -m "docs: complete CLAUDE.md"`
- Proceed to Phase 5

---

## PHASE 5: Source Code & Application Structure (Variable)

### Task 5.1: Create/Import Existing Source Code

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 1-4 hours (depends on project size)  
**📤 Output:** Application code in `src/`

**📋 PROMPT:**

```
I'm setting up the source code structure for my [LANGUAGE] project.

Please help me create the directory structure for [LANGUAGE]:

Backend ([LANGUAGE]):
- Entry point: [Main class / main function location]
- Package structure: [Java: com.company.app / Python: app.* / Node: src/*]
- Build artifact: [JAR / EXE / bundle]

Frontend (if applicable) ([LANGUAGE]):
- Entry point: [index.html / main.tsx / etc.]
- Build output: [dist/ / build/]
- Package structure: [How organized?]

Tests:
- Unit tests: [src/test/ or test/ or __tests__/]
- Integration tests: [Location]
- Test runner: [JUnit / pytest / Jest / etc.]

Configuration:
- Application config: [application.properties / config.yaml / .env]
- Database migrations: [Where stored?]
- Build file: [pom.xml / package.json / Cargo.toml / etc.]

---

Please create the initial directory structure so I can add code files.
```

**✅ Next steps:**
- Create or import source code
- Commit: `git add src/ && git commit -m "feat: add initial application source code"`

---

### Task 5.2: Create Build Artifacts

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 1-2 hours  
**📤 Output:** Working build, tests, and linting

**📋 PROMPT:**

```
I need to verify my project builds correctly.

Please check these commands in my project:

1. Build: [e.g., mvn clean package or npm run build]
   Expected: exit 0
   
2. Tests: [e.g., mvn test or npm test]
   Expected: All tests pass, >80% coverage
   
3. Lint: [e.g., mvn checkstyle:check or npm run lint]
   Expected: No errors or warnings
   
4. Security scan: [e.g., mvn dependency-check:check or npm audit]
   Expected: No critical vulnerabilities

Please run each command and report any failures.
```

**✅ Next steps:**
- Fix any build failures
- Update `.claude/context/commands.md` with actual command names
- Commit: `git add . && git commit -m "feat: add build configuration and tests"`
- Proceed to Phase 6

---

## PHASE 6: Set Up Agents, Skills & Hooks (Optional/As-Needed)

### Task 6.1: Plan Custom Agents (Optional)

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 30 minutes  
**📤 Output:** Document in `docs/agents/README.md` (optional)

**📋 PROMPT:**

```
I'm planning custom AI agents for my team's development workflow.

For each custom agent, describe:

**Agent 1: [Name]**
- Purpose: What problem does this agent solve?
- Trigger: When/how would a developer invoke it?
- Input: What does it need from the developer?
- Output: What does it produce?
- Tools: What tools does it have access to?
- Success criteria: How do we know it worked?

**Agent 2: [Name]**
[Same structure]

---

Is planning agents worth the effort for my team right now, or should I skip this phase?
```

**✅ Next steps:**
- Document agent ideas (optional)
- Proceed to Phase 7

---

### Task 6.2: Plan Custom Skills (Optional)

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 30 minutes  
**📤 Output:** Document in `docs/guides/` (optional)

**📋 PROMPT:**

```
I'm planning custom skills (reusable automations) for my team.

For each custom skill, describe:

**Skill 1: [Name]**
- Purpose: What repetitive task does this automate?
- Input: What does a developer provide?
- Output: What does the skill produce?
- When used: In what workflow step?

**Skill 2: [Name]**
[Same structure]

---

Should my team invest in custom skills now, or focus on core setup first?
```

**✅ Next steps:**
- Document skill ideas (optional)
- Proceed to Phase 7

---

## PHASE 7: Agent Workflow Setup (Optional)

### Task 7.1: Document Agent Workflow

**🤖 Recommended Model:** Opus 5.5  
**⏱️ Time:** 1 hour (if doing this phase)  
**📤 Output:** Create `docs/agent-workflow/workflow.md`

**📋 PROMPT:**

```
I'm documenting how AI agents work in my team's development workflow.

Please help me create a flowchart showing:

1. Trigger point: What starts the workflow?
2. Agent 1: First AI agent and what it does
3. Decision point: What gets evaluated?
4. Agent 2: Second AI agent (if applicable)
5. Approval gate: Where does a human decide?
6. Output: Final result
7. Feedback loop: What happens if something fails?

For example:
Developer: "Implement feature X"
         ↓
Agent 1: Design the feature
         ↓
[HUMAN REVIEW]
         ↓
Agent 2: Generate code
         ↓
[TESTS]
         ↓
If pass → Merge
If fail → Agent 2 fixes code

---

Please help me document my team's workflow.
```

**✅ Next steps:**
- Create workflow documentation (if applicable)
- Proceed to Phase 8

---

## PHASE 8: Verification & Sign-Off (1 hour)

### Task 8.1: Verify Claude Code Setup

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 15 minutes  
**📤 Output:** Verification checklist

**📋 PROMPT:**

```
I'm verifying my Claude Code setup is complete.

Please confirm I should run these checks:

1. Test session-start hook:
   bash .claude/hooks/session-start.sh
   [Should show ✅ Environment ready!]

2. Verify context loads:
   claude context
   [Should list architecture.md, commands.md, etc.]

3. Verify settings.json:
   python3 -m json.tool .claude/settings.json
   [Should show valid JSON]

4. Verify git status:
   git status
   [Should be clean or only expected changes]

Please help me run these and confirm everything is ready.
```

**✅ Next steps:**
- Run all verification checks
- Document results
- Proceed to Task 8.2

---

### Task 8.2: Run First Development Task

**🤖 Recommended Model:** Opus 5.5 (for complex task) or Haiku 4.5 (for simple task)  
**⏱️ Time:** 1-2 hours  
**📤 Output:** First completed feature using Claude Code

**📋 PROMPT:**

```
I'm testing my Claude Code setup by completing a real development task.

For my first task, I need to: [Your actual first task - e.g., "Create a new API endpoint"]

Please help me:
1. Design the solution (following .claude/context/architecture.md)
2. Generate code (following .claude/rules/10-app.md conventions)
3. Add tests (following .claude/context/commands.md)
4. Verify security (following .claude/rules/security-guardrails.md)

The task: [Your task description]
Acceptance criteria: [What success looks like]
```

**✅ Next steps:**
- Complete the task
- Verify code quality
- Run tests
- Commit: `git add . && git commit -m "[Your feature]"`

---

### Task 8.3: Team Sign-Off

**🤖 Recommended Model:** N/A (manual task)  
**⏱️ Time:** 30 minutes (team review)  
**📤 Output:** Sign-off signatures

**📋 CHECKLIST:**

```
- [ ] Dev Lead: "Configuration is complete and correct"
- [ ] Security Lead: "Security baseline is in place and documented"
- [ ] Tech Lead: "Architecture is clear and documented"
- [ ] QA/Test Lead: "Build process works and tests pass"
- [ ] Team: "Ready to start development"
```

**✅ Next steps:**
- Get sign-offs from all leads
- Proceed to Task 8.4

---

### Task 8.4: Final Commit & Tag

**🤖 Recommended Model:** Haiku 4.5  
**⏱️ Time:** 10 minutes  
**📤 Output:** Git tag marking Phase D4 completion

**📋 PROMPT:**

```
I'm completing Phase D4 of the AI SSDLC and tagging the milestone.

Please run these commands:

1. Check git status:
   git status
   [Should be clean]

2. Create a tag:
   git tag -a d4-harness-complete -m "Phase D4: Harness configuration complete and verified"

3. Push tag:
   git push origin d4-harness-complete

4. List tags:
   git tag
   [Should show d4-harness-complete]

Please confirm all steps completed successfully.
```

**✅ Next steps:**
- Phase D4 complete! 🎉
- Ready for Phase D5 (Deploy)

---

## Quick Reference

**Total Time: 9-17 hours** (depending on complexity)

| Phase | Completed? | Time | Owner |
|-------|-----------|------|-------|
| 1. Project Foundation | [ ] | 1h | Tech/Dev Lead |
| 2. Architecture & Specs | [ ] | 2h | Tech Lead |
| 3. Security & Compliance | [ ] | 1.5h | Security Lead |
| 4. Configure .claude/ | [ ] | 2h | Tech Lead |
| 5. Source Code | [ ] | 1-4h | Dev Team |
| 6. Agents & Skills | [ ] | 0-2h (optional) | Tech Lead |
| 7. Agent Workflow | [ ] | 0-1h (optional) | Tech Lead |
| 8. Verification | [ ] | 1h | All |

---

**Last Updated:** 2026-10-04  
**Related:** `phase-prompts-interactive.md` — Interactive fill-in-the-blank version
