# rrd-ir Developer Setup Guide

**Complete step-by-step guide for setting up the rrd-ir project from the AI SSDLC template**

**Audience:** Development teams new to Claude Code and the AI-Ready Secure Software Development Lifecycle (SSDLC) harness

**Duration:** 3-4 hours for initial setup

**Prerequisites:**
- Basic understanding of git and terminal commands
- Claude Code CLI installed (`claude --version`)
- Text editor or IDE (VS Code recommended)
- Basic understanding of JSON format

---

## Table of Contents

1. [What You're Setting Up](#what-youre-setting-up)
2. [Understanding the Project Structure](#understanding-the-project-structure)
3. [What is Claude Code?](#what-is-claude-code)
4. [AI SSDLC Overview](#ai-ssdlc-overview)
5. [Step-by-Step Setup Guide](#step-by-step-setup-guide)
6. [Setting Up `.claude/` Folder](#setting-up-claude-folder)
   - [6.1 Configure `.claude/context/`](#61-configure-claudecontext-knowledge-base)
   - [6.2 Configure `.claude/rules/`](#62-configure-clauderules-code-standards)
   - [6.3 Configure `.claude/hooks/`](#63-configure-claudehooks-automation-scripts)
   - [6.4 Configure `.claude/settings.json`](#64-configure-claudesettingsjson-permissions--environment)
   - [6.5 Create CLAUDE.md](#65-create-claudemd-root-level-instructions)
   - [6.6 Setup `evals/` Folder](#66-setup-evals-folder-custom-skills-validation)
7. [Common Tasks & Workflows](#common-tasks--workflows)
8. [Troubleshooting](#troubleshooting)
9. [Next Steps](#next-steps)

---

## What You're Setting Up

The **rrd-ir** project is a new application built on the **AI-Ready Secure Software Development Lifecycle (SSDLC) harness**. This is a governance and automation framework that:

✅ **Enables AI-assisted development** using Claude Code  
✅ **Enforces security standards** through code analysis and guardrails  
✅ **Manages compliance** with configurable frameworks (PCI DSS, HIPAA, GDPR, etc.)  
✅ **Automates workflows** with hooks and custom agents  
✅ **Provides clear governance** with read/write boundaries and approval gates  

Think of it as a **smart project scaffolding system** that combines:
- Configuration management (what's allowed/denied)
- Documentation standards (knowledge base)
- Security policies (guardrails)
- Automation (hooks)
- Custom AI agents (specialized tools)

---

## Understanding the Project Structure

### Directory Map

```
rrd-ir/
│
├── CLAUDE.md                    ← Project instructions for Claude Code
├── README.md                    ← Project overview & deployment checklist
├── .mcp.json                    ← MCP servers configuration
│
├── .claude/                     ← All Claude Code configuration (CRITICAL)
│   ├── settings.json            ← Permissions & environment
│   ├── settings.local.json      ← Local development overrides
│   │
│   ├── context/                 ← Knowledge base (HOW TO FILL: Section 6.1)
│   │   ├── architecture.md      ← System structure & components
│   │   ├── commands.md          ← Available commands contract
│   │   ├── glossary.md          ← Domain terminology
│   │   ├── hazards.md           ← Security risks & incident history
│   │   └── security-posture.md  ← Compliance baseline
│   │
│   ├── rules/                   ← Code standards (HOW TO FILL: Section 6.2)
│   │   ├── 10-app.md            ← App-specific conventions
│   │   └── security-guardrails.md ← Mandatory security rules
│   │
│   ├── hooks/                   ← Automation scripts (HOW TO FILL: Section 6.3)
│   │   └── session-start.sh     ← Runs on Claude Code startup
│   │
│   ├── agents/                  ← Custom AI agents (advanced)
│   │   └── [agent-definitions]
│   │
│   └── skills/                  ← Custom skills (advanced)
│       └── [skill-definitions]
│
├── docs/
│   ├── guides/                  ← Setup & onboarding documentation
│   │   ├── README.md
│   │   └── developer-setup-guide.md (← YOU ARE HERE)
│   ├── security/                ← Security & compliance documentation
│   │   ├── threat-model.md
│   │   ├── compliance-mapping.md
│   │   └── incident-response.md
│   ├── architecture/            ← System design & decisions
│   ├── forms/                   ← Deployment questionnaires
│   └── audits/                  ← Compliance audit reports
│
└── src/                         ← Your actual application code
    ├── api/                     ← API layer
    └── web/                     ← Frontend/web layer
```

### What Each Folder Does

| Folder | Purpose | Who Edits | When |
|--------|---------|-----------|------|
| **`.claude/`** | Claude Code configuration | Dev Lead, Tech Lead | During setup & maintenance |
| **`docs/`** | Documentation & governance | All team members | Ongoing |
| **`src/`** | Application code | Developers | Daily development |

---

## What is Claude Code?

### The Basics

**Claude Code** is a command-line interface (CLI) that integrates Claude AI into your development workflow. It allows you to:

- 🤖 **Ask Claude** questions about your code while working
- 📝 **Generate code** snippets and complete functions
- 🔍 **Review code** for security and quality issues
- 🧪 **Run tests** and verify implementations
- 📋 **Auto-complete tasks** with AI assistance
- 🔐 **Enforce security** through configured guardrails

### How It Works

```
┌─────────────────────────────────────────────────────┐
│  You: "claude, fix this bug"                        │
│  Or: "/lint" (slash command)                        │
│  Or: Run pre-commit hook                            │
└────────────┬────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────┐
│  Claude Code reads your project configuration:      │
│  - .claude/settings.json (permissions)              │
│  - CLAUDE.md (instructions)                         │
│  - .claude/context/ (project knowledge)             │
│  - .claude/rules/ (code standards)                  │
└────────────┬────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────┐
│  Claude processes your request following:           │
│  - Your project's security rules                    │
│  - Your documentation standards                     │
│  - Enterprise policies                              │
│  - Configured guardrails                            │
└────────────┬────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────┐
│  Claude returns results:                            │
│  - Code suggestions                                 │
│  - Security analysis                                │
│  - Fixes or improvements                            │
│  - Documented recommendations                       │
└─────────────────────────────────────────────────────┘
```

### Key Concepts

**1. Context (`.claude/context/`)**
- Project knowledge that Claude uses to understand your system
- Like having your team's collective brain available to Claude
- Examples: architecture, terminology, security requirements

**2. Rules (`.claude/rules/`)**
- Code standards Claude enforces when writing code
- Prevents security issues and maintains consistency
- Examples: "all queries must use prepared statements", "no hardcoded passwords"

**3. Hooks (`.claude/hooks/`)**
- Automation scripts that run automatically
- Examples: validate git commits, check for secrets before edits

**4. Settings (`.claude/settings.json`)**
- Permissions: what Claude is allowed to do
- Environment variables for your project
- Which hooks to run and when

---

## AI SSDLC Overview

The AI-Ready SSDLC is a **7-phase security and governance framework** that ensures AI-assisted development is safe, compliant, and well-documented.

### The 7 Phases

| Phase | Focus | Outcome | Your Role |
|-------|-------|---------|-----------|
| **D1: Intake** | Understand requirements | Requirements document | Product/PM lead |
| **D2: Shape** | Design solution | Architecture & KPIs | Tech lead |
| **D3: Capability Candidates** | AI assistant specs | Agent/skill definitions | Dev lead |
| **D4: Harness** | Setup governance | `.claude/` configuration (THIS IS YOU) | Dev lead + team |
| **D5: Deploy** | Release to staging | Verified build | DevOps + QA |
| **D6: Gate** | Audit & approval | Compliance sign-off | Security + management |
| **D7: Operate** | Run in production | Monitoring active | DevOps + SRE |

**You are in Phase D4: Harness Setup**

Your goal: Configure the `.claude/` folder so Claude Code works safely and effectively for your team.

### Why This Matters

Each phase builds on the previous one:
- ❌ Skip D1 (intake) → Build the wrong thing
- ❌ Skip D2 (design) → Implement badly
- ❌ Skip D3 (agents) → Have no AI tools
- ❌ Skip D4 (harness) ← **YOU ARE HERE** → No governance or security
- ❌ Skip remaining → Release to production unsafely

---

## Step-by-Step Setup Guide

### Phase 1: Project Initialization (30 minutes)

#### 1.1 Initialize Git Repository

```bash
cd /Users/erwin.t.bainto/ai_projects/rrd-ir

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: rrd-ir project template from application-template"
```

**Why:** You need version control to track changes and enforce write boundaries.

#### 1.2 Verify Project Structure

```bash
# List top-level directories
ls -la

# Should show:
# CLAUDE.md, README.md, .mcp.json
# .claude/, docs/, src/, evals/
```

#### 1.3 Check Claude Code Installation

```bash
# Verify Claude Code is installed
claude --version

# If not installed, see: https://claude.com/claude-code
```

**Example output:**
```
Claude Code version 1.2.0
```

---

### Phase 2: Understanding Your Application (1 hour)

Before you configure `.claude/`, answer these questions:

#### 2.1 What Does This Application Do?

**Question:** In 2-3 sentences, describe your application's business purpose.

**Example answers:**
- "This is a payment processing service that handles credit card transactions for e-commerce platforms. It integrates with payment gateways and manages transaction history."
- "This is an internal HR system that manages employee records, benefits, and payroll. It serves HR teams and executives."
- "This is a real-time analytics dashboard that aggregates data from multiple sources and provides business insights."

**Write your answer:** You'll use this in `CLAUDE.md` and `architecture.md`

#### 2.2 What Are Your Technology Stack?

**Question:** What languages, frameworks, and databases will you use?

**Example:**
- Backend: Java 21, Spring Boot 3.0
- Frontend: React 18, TypeScript
- Database: PostgreSQL 15
- Message Queue: RabbitMQ

**Write your answer:** You'll use this in `10-app.md` rules

#### 2.3 What Are Your Security Requirements?

**Question:** Does your application handle sensitive data that requires compliance?

**Checklist:**
- [ ] Payment card data? → PCI DSS applies
- [ ] Health records? → HIPAA applies
- [ ] EU personal data? → GDPR applies
- [ ] Financial records? → SOX applies
- [ ] Just internal data? → No specific framework

**Write your answer:** You'll use this in `security-posture.md`

#### 2.4 Who Is On Your Team?

**Question:** Who will work on this project?

**Example:**
- Dev Lead: Jane Smith (jane@company.com)
- Tech Lead: Bob Johnson (bob@company.com)
- Security Lead: Alice Chen (alice@company.com)
- DevOps: Charlie Brown (charlie@company.com)

**Write your answer:** You'll assign roles in `.claude/` configuration

---

### Phase 3: Gather Information (30 minutes)

Create a simple document with your answers:

```markdown
# rrd-ir Project Information

## Application Purpose
[Your answer from 2.1]

## Technology Stack
[Your answer from 2.2]

## Security Requirements
[Your answer from 2.3]

## Team Members
[Your answer from 2.4]

## Approval Authority
Who approves write operations? [Name & email]

## Build Commands
- Build: [e.g., mvn clean package]
- Test: [e.g., mvn test]
- Lint: [e.g., mvn checkstyle:check]

## Repository
- URL: [GitHub/GitLab URL]
- Main branch: [main or master]
```

**Save this as: `docs/PROJECT_INFO.md`**

---

### Phase 4: Configure the `.claude/` Folder

This is the main setup work. See **Section 6** for detailed instructions on each subsection.

**Time estimate:** 2-3 hours

---

## Setting Up `.claude/` Folder

This is where the actual configuration happens. Each subsection below is a step-by-step guide.

### 6.1 Configure `.claude/context/` (Knowledge Base)

The context folder contains information **about** your project. Claude reads these files to understand your system.

#### 6.1.1 `architecture.md` — System Structure

**Purpose:** Describe what your system does, how it's built, and key decisions.

**File:** `.claude/context/architecture.md`

**Step-by-step:**

1. Open `.claude/context/architecture.md`

2. Replace placeholders:

```markdown
# Architecture — rrd-ir

**Last Updated:** 2026-10-02
**Owner:** [Tech Lead Name]
**Full Details:** `docs/architecture/ARCHITECTURE.md`

---

## What it is

[Your answer from Section 2.1 - describe the application]

**Example:**
"rrd-ir is a real-time revenue recognition system that processes
financial transactions for SaaS companies. It calculates revenue
recognition based on ASC 606 standards and provides compliance reporting
to finance teams and auditors."

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
| API Layer | Spring Boot REST | Handles incoming transaction requests |
| Processing Engine | Java with Drools | Applies revenue recognition rules |
| Database | PostgreSQL | Stores transactions and calculations |
| Message Queue | RabbitMQ | Async processing of complex transactions |
| Cache | Redis | Caches customer subscription data |

---

## Interfaces

| Interface | Type | Consumers | Details |
|-----------|------|-----------|---------|
| /api/transactions | REST | Billing systems | POST transaction, returns recognition result |
| /api/reports | REST | Finance team | GET ASC 606 compliance reports |
| events.revenue-recognized | Event Queue | General Ledger | Published when revenue is recognized |

---

## Key Decisions

| Area | Chosen | Why | Record |
|------|--------|-----|--------|
| Language | Java 21 | Enterprise standards, Spring Boot maturity | ADR-001 |
| Database | PostgreSQL | Strong financial data support, ACID guarantees | ADR-002 |
| Async Processing | RabbitMQ | Decouples API from slow rule engine | ADR-003 |

---

## Data & State

| Data | Owner | Storage | Retention |
|------|-------|---------|-----------|
| Transactions | Processing Engine | PostgreSQL | 7 years (per compliance) |
| ASC 606 Rules | Finance | Rule Engine (Drools) | Version controlled |
| Calculated Revenue | Processing Engine | PostgreSQL | 7 years |

---

## Unowned or Unclear

- Integration with new ERP systems: Owner TBD
  - Full details: `docs/architecture/UNCLEAR.md`

---

## References

- Architecture Deep Dive: `docs/architecture/ARCHITECTURE.md`
- Architectural Decisions: `docs/architecture/adr/`
- API Specification: `docs/api/`
```

3. Save the file and commit:

```bash
git add .claude/context/architecture.md
git commit -m "docs: complete architecture.md with system structure"
```

**Verification:** Run this to confirm Claude can read it:

```bash
claude context
```

You should see `architecture.md` listed.

---

#### 6.1.2 `security-posture.md` — Compliance & Security Baseline

**Purpose:** Define what security frameworks apply and what controls are in place.

**File:** `.claude/context/security-posture.md`

**Step-by-step:**

1. Open `.claude/context/security-posture.md`

2. Fill the Compliance Requirements section:

```markdown
## Compliance Requirements

| Framework | Required | Mapping | Owner |
|-----------|----------|---------|-------|
| PCI DSS | YES | `docs/security/compliance-mapping.md` | Alice Chen |
| GDPR | YES | `docs/security/compliance-mapping.md` | Alice Chen |
| SOX | NO | N/A | N/A |
| HIPAA | NO | N/A | N/A |

**How to decide:**
- PCI DSS: Do you process/store credit cards? → YES
- GDPR: Do you store data of EU residents? → YES  
- HIPAA: Do you handle health records? → NO
- SOX: Are you a public company? → NO
```

3. Fill Authentication & Authorization:

```markdown
## Authentication & Authorization

| Aspect | Value | Notes |
|--------|-------|-------|
| Method | OAuth 2.0 via AWS Cognito | |
| Provider | AWS Identity Center | |
| Authorization Model | RBAC (Role-Based Access Control) | |
| Default Access | DENY all | Explicit allowlist |
| Token Storage (Frontend) | HttpOnly Cookie | Secure by default |
| Token TTL | 1 hour | Auto-refresh via refresh token |
```

4. Fill Data Classification:

```markdown
## Data Classification

| Data Type | Classification | Storage | Encryption | Retention | Access |
|-----------|---|---|---|---|---|
| Customer Payment Data | Confidential | PostgreSQL | AES-256 at rest, TLS in transit | 7 years | Admins only |
| Transaction Records | Confidential | PostgreSQL | AES-256 at rest, TLS in transit | 7 years | Finance team + Admins |
| API Logs | Sensitive | CloudWatch | Encrypted at rest | 90 days | DevOps + Security |
| Public Documentation | Public | Git | Not encrypted | Indefinite | Everyone |
```

5. Commit your changes:

```bash
git add .claude/context/security-posture.md
git commit -m "docs: complete security-posture.md with compliance requirements"
```

---

#### 6.1.3 `commands.md` — Available Commands Contract

**Purpose:** Define what commands your team can run.

**File:** `.claude/context/commands.md`

**Step-by-step:**

1. Open `.claude/context/commands.md`

2. List your available commands:

```markdown
## Command Contract

| Purpose | Command | Expected | Duration | Passes Today |
|---------|---------|----------|----------|--------------|
| Build application | `/build` | exit 0 | 5m | yes |
| Run tests | `/test` | exit 0, >90% coverage | 10m | no |
| Lint code | `/lint` | exit 0, no warnings | 2m | yes |
| Security scan | `/security-scan` | exit 0 | 15m | yes |
| Deploy to staging | `/deploy-staging` | exit 0 | 20m | yes |
| Run local server | `/serve` | Server listening on :8080 | 30s | yes |

## How to Add Commands

Each command should:
1. Be documented in CLAUDE.md
2. Have a clear purpose
3. Have predictable output
4. Be safe to run repeatedly
5. Have a timeout
```

3. Document what commands actually do:

```markdown
## Currently Passing

- `/build` — Compiles Java code with `mvn clean package`
- `/lint` — Checks code style with `mvn checkstyle:check`
- `/serve` — Starts local server with `java -jar target/app.jar`
- `/security-scan` — Runs OWASP dependency check with `mvn dependency-check:check`

## Currently Failing

- `/test` — Failing due to missing test fixtures in `src/test/resources/`
  - See: `docs/testing/TEST_SETUP.md`

## Reduced Receipt Set

When `/test` is not available:
- Manual verification by: QA Team Lead
- Evidence: PR review checklist
```

4. Commit:

```bash
git add .claude/context/commands.md
git commit -m "docs: complete commands.md with available commands"
```

---

#### 6.1.4 `glossary.md` — Domain Terminology

**Purpose:** Define business and technical terms unique to your system.

**File:** `.claude/context/glossary.md`

**Step-by-step:**

1. Open `.claude/context/glossary.md`

2. Add your domain terms:

```markdown
## Business Terms

| Term | Means Here | Does NOT Mean |
|------|-----------|-----------------|
| ASC 606 | Accounting Standards Codification Topic 606 (Revenue Recognition) | Basic accounting concept |
| MRR | Monthly Recurring Revenue (for SaaS) | Monthly running rate |
| COGS | Cost of Goods Sold | Cost of revenue |
| Subscription | Recurring billing cycle (1 month, 1 year, etc.) | One-time purchase |
| Customer | SaaS client company | Individual person |

## Technical Terms

| Term | Means Here | Used In |
|------|-----------|---------|
| Allocation Engine | The Java Drools component that applies ASC 606 rules | Processing Engine |
| Journal Entry | An accounting transaction (debit/credit pair) | General Ledger integration |
| Recognition Profile | Customer-specific rule set (when to recognize revenue) | Database: customer_profiles |
| Event | Business event published to message queue | RabbitMQ integration |

## Acronyms

| Acronym | Meaning | Used In |
|---------|---------|---------|
| ASC 606 | Accounting Standards Codification Topic 606 | Finance & auditing |
| MRR | Monthly Recurring Revenue | Finance team |
| COGS | Cost of Goods Sold | Accounting |
| RabbitMQ | Message broker | Backend architecture |
| RBAC | Role-Based Access Control | Security architecture |

## Overloaded Terms

**"Transaction"** can mean:
- Database transaction (ACID unit of work) — Used in technical docs
- Business transaction (customer purchase) — Used in business docs
- API transaction request — Used in API docs

Always clarify context when saying "transaction".
```

3. Commit:

```bash
git add .claude/context/glossary.md
git commit -m "docs: complete glossary.md with domain terminology"
```

---

#### 6.1.5 `hazards.md` — Security Risks & Incident History

**Purpose:** Document dangerous areas of the code that need extra review.

**File:** `.claude/context/hazards.md`

**Step-by-step:**

1. Open `.claude/context/hazards.md`

2. Document security hazards:

```markdown
## Security Hazards

| Vulnerability | Path | Why Critical | Impact | Mitigation | Status | Owner |
|---|---|---|---|---|---|---|
| SQL Injection in transaction search | `src/api/TransactionController.java:line 42` | User input in WHERE clause | Full database compromise | Switch to parameterized queries (PreparedStatement) | Open | Bob Johnson |
| Hardcoded API keys in config | `src/main/resources/application.properties` | Keys visible in git history | Unauthorized API access | Move to AWS Secrets Manager | Mitigated | Charlie Brown |
| Unencrypted data in logs | `src/main/java/logging/TransactionLogger.java` | Customer data may be logged | PCI DSS violation | Add log filtering | In Progress | Alice Chen |

## Do Not Touch Without Review

| Area | Path | Why | Owner |
|---|---|---|---|
| Revenue recognition rules | `src/main/resources/rules/asc606.drl` | Small change = big financial impact | Finance Lead |
| Payment processing | `src/api/PaymentController.java` | PCI compliance risk | Security Lead |
| Database schema | `src/main/resources/db/migration/` | Data loss risk | DBA |

## Incident History

| What Happened | Area | When | Lesson |
|---|---|---|---|
| API leaked customer data in error messages | `src/api/ErrorHandler.java` | 2026-08-15 | Never include customer data in errors |
| Revenue calculation was 0.01% off due to rounding | `src/engine/Calculator.java` | 2026-07-20 | Always use BigDecimal for money, not double |

## Surprising Behaviour

- **MRR calculation:** We recognize revenue monthly, but charges are pro-rated daily. This creates reconciliation complexity.
  - Why: Customer contracts specify monthly recognition but billing is daily.
  - Reference: `src/engine/ProrationEngine.java`

- **Rollback transactions:** When a transaction is rolled back, we don't delete it from the database. We mark it as rolled back.
  - Why: Maintains audit trail for compliance.
  - Reference: `src/model/Transaction.java` (status=ROLLED_BACK)

## Known Debt

| Debt | Area | Why Accepted | Remediation | Target |
|---|---|---|---|---|
| No automated tests for rule engine | `src/test/java/engine/` | Drools testing is complex | Write 20 sample rule test cases | 2026-12-31 |
| Configuration in XML (not YAML) | `src/main/resources/` | Legacy Spring format | Migrate to application.yml | 2026-11-30 |
| Manual database backups | DevOps | AWS RDS not set up yet | Enable automated daily snapshots | 2026-10-31 |

## Before Making Changes

- [ ] I've read this entire hazards document
- [ ] I understand the security implications
- [ ] I've consulted with the owner listed above
- [ ] My changes maintain or improve mitigations

See: `.claude/rules/security-guardrails.md` (mandatory rules)
```

3. Commit:

```bash
git add .claude/context/hazards.md
git commit -m "docs: complete hazards.md with security risks and incident history"
```

---

### 6.2 Configure `.claude/rules/` (Code Standards)

Rules define **how** your team should write code. Claude will enforce these.

#### 6.2.1 `10-app.md` — Application-Specific Conventions

**File:** `.claude/rules/10-app.md`

**Purpose:** Define naming conventions, code patterns, and best practices specific to your project.

**Step-by-step:**

1. Open `.claude/rules/10-app.md`

2. Fill in based on your technology stack:

```markdown
---
description: rrd-ir Java/Spring Boot conventions and guardrails
paths: ["src/**/*.java"]
---

# rrd-ir Conventions

App-specific conventions that narrow enterprise standards. Never looser.

**Last Updated:** 2026-10-02
**Owner:** Bob Johnson (Tech Lead)

---

## Java Package Structure

All classes must follow this structure:

```
src/main/java/com/company/rrd/
├── api/           # REST Controllers
├── service/       # Business logic
├── model/         # JPA Entities
├── repository/    # Database access (Spring Data)
├── util/          # Utilities & helpers
└── config/        # Spring configuration
```

**Why:** Clear separation of concerns. Makes code navigable.

## Naming Conventions

| Item | Pattern | Example |
|------|---------|---------|
| Java classes | PascalCase | `TransactionService` |
| Methods | camelCase | `calculateRevenue()` |
| Constants | UPPER_CASE | `DEFAULT_TIMEZONE` |
| Database tables | snake_case | `customer_subscriptions` |
| Booleans | is/has prefix | `isProcessed`, `hasError` |

## Dependency Injection

Use **constructor injection ONLY** (not field injection).

✅ **CORRECT:**
```java
public class TransactionService {
  private final TransactionRepository repo;
  private final RuleEngine engine;
  
  public TransactionService(TransactionRepository repo, RuleEngine engine) {
    this.repo = repo;
    this.engine = engine;
  }
}
```

❌ **WRONG:**
```java
public class TransactionService {
  @Autowired
  private TransactionRepository repo;  // Field injection - BAD
  
  @Autowired
  private RuleEngine engine;          // Field injection - BAD
}
```

**Why:** Constructor injection makes dependencies explicit. Enables testing. Prevents NPE.

## Transaction Boundaries

All **write** operations must have `@Transactional`.

✅ **CORRECT:**
```java
@Transactional
public Transaction createTransaction(Transaction t) {
  return transactionRepository.save(t);
}
```

❌ **WRONG:**
```java
public Transaction createTransaction(Transaction t) {
  return transactionRepository.save(t);  // Missing @Transactional!
}
```

**Why:** Ensures data consistency. Enables rollback on error.

## Error Handling

Never expose internal details in error messages. Never log sensitive data.

✅ **CORRECT:**
```java
try {
  processTransaction(t);
} catch (Exception e) {
  log.error("Failed to process transaction ID: {}", t.getId());
  throw new BusinessException("Transaction processing failed", e);
}
```

❌ **WRONG:**
```java
try {
  processTransaction(t);
} catch (Exception e) {
  log.error("Failed for customer: {} with data: {}", customer.getEmail(), t);  // Logs sensitive data!
  throw new RuntimeException(e.getMessage());  // Exposes internals!
}
```

**Why:** Prevents information disclosure. Maintains security. Improves debugging.

## Database Queries

Use **PreparedStatement via Spring Data or @Query** ONLY. No string concatenation.

✅ **CORRECT:**
```java
@Query("SELECT t FROM Transaction t WHERE t.customerId = :customerId")
List<Transaction> findByCustomer(@Param("customerId") Long customerId);
```

❌ **WRONG:**
```java
// String concatenation = SQL injection risk!
String query = "SELECT * FROM transactions WHERE customer_id = '" + customerId + "'";
return jdbcTemplate.queryForList(query);
```

**Why:** Prevents SQL injection. Most critical security practice.

## Logging Standards

| Level | Usage | Example |
|-------|-------|---------|
| TRACE | Very detailed, low-level | "Entering method X with params Y" |
| DEBUG | Development debugging | "Query returned 42 results" |
| INFO | Interesting business events | "Transaction created: ID=123, amount=$50" |
| WARN | Potential problems | "Retry attempt 3 of 5 for transaction" |
| ERROR | Error but recoverable | "Failed to call external API, retrying" |

✅ **CORRECT:**
```java
log.info("Revenue recognized for transaction ID: {}, amount: ${}", 
  t.getId(), t.getAmount());
```

❌ **WRONG:**
```java
log.info("Transaction: " + transactionObject.toString());  // Could include secrets!
log.debug("Customer email: " + customer.getEmail());      // PII in logs!
```

## Do Not

- ❌ Use `System.out.println()` — Use logging framework
- ❌ Store plaintext passwords anywhere
- ❌ Use `eval()` or dynamic code execution
- ❌ Commit `.env` or secrets files
- ❌ Use default credentials (admin/admin)
- ❌ Ignore compiler warnings
- ❌ Write >100 line methods — Break into smaller functions
- ❌ Skip unit tests for complex logic

## Code Review Checklist

Every PR must pass:

- [ ] Follows naming conventions
- [ ] Uses constructor injection (no @Autowired on fields)
- [ ] All writes have @Transactional
- [ ] No hardcoded secrets
- [ ] All queries use PreparedStatement
- [ ] Error messages don't expose internals
- [ ] Sensitive data not in logs
- [ ] Unit tests pass
- [ ] No security warnings from SonarQube

## Exceptions

None currently approved. All exceptions must be approved by Tech Lead and expire within 90 days.

---

## References

- Security guardrails: `.claude/rules/security-guardrails.md`
- Architecture: `.claude/context/architecture.md`
- Enterprise standards: `@enterprise/rules/coding-standards.md`
```

3. Commit:

```bash
git add .claude/rules/10-app.md
git commit -m "docs: complete 10-app.md with Java/Spring conventions"
```

---

#### 6.2.2 `security-guardrails.md` — Mandatory Security Rules

**File:** `.claude/rules/security-guardrails.md`

**Purpose:** Define non-negotiable security requirements that Claude must enforce.

**Step-by-step:**

1. Open `.claude/rules/security-guardrails.md`

2. Fill based on your compliance requirements and threat model:

```markdown
---
description: Mandatory security controls for rrd-ir (PCI DSS & GDPR compliant)
paths: ["src/**"]
---

# Security Guardrails — rrd-ir

Mandatory security rules. Narrower than enterprise; specific to this app's tech stack and threat model.

**Last Updated:** 2026-10-02
**Owner:** Alice Chen (Security Lead)

---

## Secrets Management — MANDATORY

| Rule | Enforcement |
|------|-------------|
| Never commit credentials, keys, tokens | Pre-commit hooks + secret scanning |
| Use environment variables for secrets | Block hardcoded passwords in CI/CD |
| Rotate secrets every 90 days | Automatic reminder in calendar |
| Keys stored in AWS Secrets Manager | Terraform validates on every deploy |

**Example:**

✅ **CORRECT:**
```java
String apiKey = System.getenv("STRIPE_API_KEY");
```

❌ **WRONG:**
```java
String apiKey = "sk_live_abc123xyz";  // Hardcoded secret!
```

---

## SQL & Database Queries — MANDATORY

| Rule | Enforcement |
|------|-------------|
| Parameterized queries only | SAST scanning (SonarQube) + code review |
| No string concatenation in SQL | Pre-commit hook rejects patterns |
| Sargable predicates on indexes | Performance test required |

**Example:**

✅ **CORRECT:**
```java
// Spring Data with named parameters
@Query("SELECT t FROM Transaction t WHERE t.customerId = :customerId")
List<Transaction> find(@Param("customerId") Long id);
```

❌ **WRONG:**
```java
// String concatenation = SQL injection
String query = "SELECT * FROM transactions WHERE id = " + userId;
```

---

## Authentication & Authorization

| Rule | Enforcement |
|------|-------------|
| All admin endpoints require 2FA | Integration test validates |
| Token validation on every request | Spring Security filters enforce |
| Audit log all permission denied events | Elasticsearch logs every rejection |

---

## Encryption

| Rule | Enforcement |
|------|-------------|
| Sensitive data encrypted at rest | RDS encryption enabled in Terraform |
| HTTPS/TLS 1.3+ for all transit | Load balancer config validated |
| Never log passwords/tokens | Code review + log scanning |

---

## Access Logging & Audit Trails

| Rule | Enforcement |
|------|-------------|
| All auth attempts logged | CloudWatch logs every attempt |
| Authorization decisions logged | Application logs every deny |
| Logs immutable (no delete/modify) | S3 bucket policy enforces |

---

## Rate Limiting & DDoS Protection

| Rule | Enforcement |
|------|-------------|
| `/api/login` — max 5 attempts/minute per IP | Integration test validates |
| `/api/*` — max 100 requests/minute per user | Load testing validates |
| Throttle response includes retry-after | Code review checks headers |

**Example:**

```java
@RateLimiter(permits = 5, window = "1m", errorCode = 429)
@PostMapping("/api/login")
public LoginResponse login(@RequestBody LoginRequest req) {
  // Login logic
}
```

---

## Dependency Scanning

| Rule | Enforcement |
|------|-------------|
| All dependencies scanned for CVEs | CI/CD pipeline gates before merge |
| Critical CVEs patched within 48h | JIRA ticket created, tracked |
| EOL versions not allowed | Maven plugin blocks in build |

---

## Code Review Checklist — Security

Every PR must pass:

- [ ] No hardcoded secrets
- [ ] All DB queries parameterized
- [ ] Auth/authz checks present
- [ ] User input validated
- [ ] Errors don't leak sensitive info
- [ ] Logging doesn't include secrets
- [ ] Sensitive data encrypted
- [ ] Dependencies scanned for CVEs
- [ ] No untrusted deserialization
- [ ] No unsafe reflection

---

## Exceptions

| Rule | Code Location | Reason | Approved By | Expires |
|------|---------------|--------|-------------|---------|
| Plaintext password in dev config | `src/test/resources/test.properties` | Test-only, never in production | Bob Johnson | 2026-12-31 |

All exceptions must be approved by Security Lead and expire within 90 days.

---

## Do NOT

- ❌ Store plaintext passwords or secrets
- ❌ Use eval() or dynamic execution
- ❌ Skip HTTPS for "internal" services
- ❌ Log passwords or API keys
- ❌ Disable security headers
- ❌ Use default credentials in production
- ❌ Merge code with known CVEs
- ❌ Disable auth in shared environments
- ❌ Trust user input — always validate
- ❌ Use weak cryptography (MD5, DES)

---

## References

- Security posture: `.claude/context/security-posture.md`
- Threat model: `docs/security/threat-model.md`
- Incident response: `docs/security/incident-response.md`
- Full guidance: `docs/guides/rules/README.md`

---

**Last Review:** 2026-10-02
**Next Review:** 2026-10-02 + 90 days (quarterly)
```

3. Commit:

```bash
git add .claude/rules/security-guardrails.md
git commit -m "docs: complete security-guardrails.md with mandatory controls"
```

---

### 6.3 Configure `.claude/hooks/` (Automation Scripts)

Hooks run automatically to automate tasks and enforce policy.

#### 6.3.1 `session-start.sh` — Startup Checks

**File:** `.claude/hooks/session-start.sh`

**Purpose:** Verify prerequisites when Claude Code starts.

**Example hook script:**

```bash
#!/usr/bin/env bash
# Session startup hook for rrd-ir
# Runs when Claude Code session starts
# Checks prerequisites and prints status

set -euo pipefail

echo "🚀 Starting rrd-ir development environment..."
echo ""

# Check Java version
echo "✓ Checking Java version..."
JAVA_VERSION=$(java -version 2>&1 | grep version | awk -F'"' '{print $2}')
if [[ "$JAVA_VERSION" == 21* ]]; then
  echo "  ✓ Java $JAVA_VERSION found"
else
  echo "  ✗ Java 21 required, found $JAVA_VERSION"
  echo "  Install from: https://adoptium.net/"
  exit 1
fi

# Check Maven
echo "✓ Checking Maven..."
if command -v mvn &> /dev/null; then
  MVN_VERSION=$(mvn --version | head -1)
  echo "  ✓ $MVN_VERSION"
else
  echo "  ✗ Maven not found. Install with: brew install maven"
  exit 1
fi

# Check Git
echo "✓ Checking Git..."
if command -v git &> /dev/null; then
  echo "  ✓ Git $(git --version | awk '{print $3}')"
else
  echo "  ✗ Git not found"
  exit 1
fi

# Check that .env file exists (optional)
if [ ! -f ".env" ]; then
  echo "⚠️  .env file not found. Using defaults."
fi

# Print available commands
echo ""
echo "📋 Available commands:"
echo "  - /build       Build the application"
echo "  - /test        Run unit tests"
echo "  - /lint        Check code style"
echo "  - /serve       Start local server"
echo "  - /deploy-staging  Deploy to staging"
echo ""

echo "✅ Environment ready!"
```

**How to add this:**

1. Open `.claude/hooks/session-start.sh`

2. Replace the template with the example above (or adapt for your stack)

3. Make it executable:

```bash
chmod +x .claude/hooks/session-start.sh
```

4. Test it:

```bash
bash .claude/hooks/session-start.sh
```

**Expected output:**

```
🚀 Starting rrd-ir development environment...

✓ Checking Java version...
  ✓ Java 21.0.1 found
✓ Checking Maven...
  ✓ Apache Maven 3.9.4
✓ Checking Git...
  ✓ Git 2.42.0

📋 Available commands:
  - /build       Build the application
  - /test        Run unit tests
  - /lint        Check code style
  - /serve       Start local server
  - /deploy-staging  Deploy to staging

✅ Environment ready!
```

5. Commit:

```bash
git add .claude/hooks/session-start.sh
git commit -m "docs: configure session-start.sh hook with prerequisite checks"
```

---

### 6.4 Configure `.claude/settings.json` (Permissions & Environment)

**File:** `.claude/settings.json`

**Purpose:** Define what Claude Code is allowed to do and environment variables.

**Step-by-step:**

1. Open `.claude/settings.json`

2. Update with your real values:

```json
{
  "_comment_scope": "Tier 3. Narrows enterprise policy for rrd-ir application.",
  
  "permissions": {
    "deny": [
      "Read(.env)",
      "Read(src/main/resources/secrets/*)",
      "Edit(.env)",
      "Edit(src/main/resources/secrets/*)"
    ],
    "allow": [
      "Bash(mvn clean package:*)",
      "Bash(mvn test:*)",
      "Bash(mvn checkstyle:check:*)",
      "Bash(mvn dependency-check:check:*)",
      "Read(src/**)",
      "Read(docs/**)",
      "Edit(src/main/java/**)",
      "Edit(src/test/java/**)",
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
    "RRD_APP_NAME": "rrd-ir",
    "RRD_HARNESS_VERSION": "1.0.0",
    "ENVIRONMENT": "development",
    "LOG_LEVEL": "INFO"
  }
}
```

**What each section does:**

| Section | Purpose |
|---------|---------|
| `deny` | Files Claude CANNOT read or edit (secrets, credentials) |
| `allow` | Commands Claude CAN run and files it CAN edit |
| `hooks` | Automation scripts to run at specific times |
| `env` | Environment variables available to Claude |

3. Commit:

```bash
git add .claude/settings.json
git commit -m "docs: configure settings.json with permissions and environment"
```

---

### 6.5 Create CLAUDE.md (Root-Level Instructions)

**File:** `CLAUDE.md` (in project root)

**Purpose:** Tell Claude Code how to work with this specific project.

**Step-by-step:**

1. Open `CLAUDE.md`

2. Fill in with your project details:

```markdown
# rrd-ir

Extends the enterprise harness instructions. Everything in the enterprise set applies here.

## What this application is

**rrd-ir** is a revenue recognition system that processes financial transactions and calculates revenue recognition based on ASC 606 standards. It serves finance teams and provides compliance reporting to auditors.

**Users:** Finance teams, CFO, auditors
**Value:** Automates revenue recognition calculations, reduces manual effort by 80%, ensures compliance

## Repository map

| Area | Path | Responsibility |
|---|---|---|
| API Layer | `src/main/java/com/company/rrd/api/` | REST endpoints for transaction processing |
| Business Logic | `src/main/java/com/company/rrd/service/` | Revenue recognition algorithms |
| Data Models | `src/main/java/com/company/rrd/model/` | JPA entities and database schema |
| Database Access | `src/main/java/com/company/rrd/repository/` | Spring Data repositories |
| Configuration | `src/main/resources/` | Spring Boot configuration, rules, migrations |
| Tests | `src/test/java/` | Unit & integration tests |
| Docs | `docs/` | Architecture, security, compliance documentation |

## Commands

Available commands are defined in `.claude/context/commands.md`. Use only those commands when producing receipts.

## Domain terms

See `.claude/context/glossary.md` for terminology. Key terms:
- **ASC 606:** Revenue Recognition standard
- **MRR:** Monthly Recurring Revenue
- **Journal Entry:** Accounting transaction (debit/credit pair)

## Hazards

See `.claude/context/hazards.md` for:
- **Security hazards:** SQL injection risk, hardcoded keys
- **Do not touch:** Revenue rules engine, payment processing
- **Incident history:** Past data leaks and lessons learned
- **Known debt:** Missing tests, legacy XML configuration

**Critical:** Always read hazards before making changes to revenue recognition logic.

## Local conventions

Where this application departs from enterprise standard:

- **Java packages:** Use reverse domain naming (`com.company.rrd.*`), not `com.enterprise.app.*`
- **Constructor injection:** ONLY method, never @Autowired fields
- **@Transactional:** Required on all write methods, not just service layer
- **Reason:** Better for testing, prevents null pointer exceptions, aligns with Spring best practices

## Narrowed rules

Where this application is stricter than enterprise set:

- **Database queries:** PreparedStatement ONLY, no native SQL concatenation
- **Secrets:** AWS Secrets Manager ONLY, no environment variables for sensitive data
- **Error messages:** Must not contain customer data or internal details
- **Reason:** PCI DSS compliance, GDPR requirements, audit trail requirements

## Write boundary

**Read-only.** Write, commit, merge, and deployment are gated.

**Gated actions escalate to:** Bob Johnson (Tech Lead) — bob@company.com

Only Bob can approve:
- Commits to main branch
- Merges to production
- Deployment actions
- Changes to security-critical files (hazards, security-posture)

**How to request approval:** File a GitHub PR with:
1. Clear description of changes
2. Security impact assessment
3. Test evidence
4. Sign-off checklist
```

3. Commit:

```bash
git add CLAUDE.md
git commit -m "docs: complete CLAUDE.md with project instructions"
```

---

### 6.6 Setup `evals/` Folder (Custom Skills Validation)

**File:** `evals/` (directory structure)

**Purpose:** Validate and test custom skills before publishing them for your team to use.

**Note:** This is for Phase WP2/D11 (future phase when you create custom skills). Skip this section if you're not creating custom skills yet.

---

#### What are Evals?

**Evals** (evaluations) are test suites that verify custom skills work correctly. They're like unit tests but for AI agents/skills.

```
Custom Skill (AI Agent)
        ↓
   Evals (Tests)
        ↓
   Verified ✅
        ↓
   Published to Team
```

#### When You Need Evals

You need evals when:
- ✅ Creating a new custom skill (agent or automation)
- ✅ Publishing a skill for team use
- ✅ Updating an existing skill
- ✅ Before merging skill changes

You don't need evals for:
- ❌ Using built-in skills (already validated by enterprise)
- ❌ Just calling Claude for help
- ❌ Running standard commands (/build, /test, etc.)

---

#### Evals Folder Structure

```
evals/
├── README.md                              # Navigation guide
│
├── [skill-name]/                          # One folder per skill
│   ├── prompt.md                          # The skill definition
│   ├── graders.md                         # Evaluation criteria
│   ├── test-cases.json                    # Sample inputs & expected outputs
│   └── results.md                         # Test run results & evidence
│
├── vuln-patch-triage/                     # Example: Enterprise skill
│   ├── prompt.md
│   ├── graders.md
│   ├── test-cases.json
│   └── results.md
│
└── [future-skills]/                       # Placeholder for upcoming skills
```

---

#### 6.6.1 Create `evals/README.md` Navigation Guide

**File:** `evals/README.md`

```markdown
# Skill Evaluation Suites

This directory contains test suites for custom skills. Each skill must pass evaluations before being published for team use.

## Purpose

Evals verify that custom AI skills (agents, automations) work correctly and safely. They're like unit tests for AI.

## When to Use

- **Creating a new skill:** Add eval before publication
- **Updating a skill:** Run eval to verify changes
- **Publishing for team:** Eval must pass 100%

## Structure

Each skill folder contains:

| File | Purpose |
|------|---------|
| `prompt.md` | The skill definition (what it does, how it works) |
| `graders.md` | Evaluation criteria (how to judge if it works) |
| `test-cases.json` | Sample inputs and expected outputs |
| `results.md` | Test run results and evidence |

## Available Skills

### Enterprise Skills (Already Validated)
- `vuln-patch-triage` — Identify and triage security vulnerabilities
- `code-security-review` — Review code for security issues
- `compliance-audit` — Audit for compliance requirements
- `incident-response` — Coordinate incident response

### Custom Skills (In Development)
- [None yet - create your first skill!]

## How to Create a Skill Eval

### Step 1: Create Skill Folder

```bash
mkdir -p evals/my-new-skill
cd evals/my-new-skill
```

### Step 2: Write prompt.md

This is what the skill does. Example:

```markdown
---
name: invoice-automation
description: Automate invoice processing and data extraction
---

# Invoice Automation Skill

## Purpose

Automatically process incoming invoices by:
1. Extracting vendor info
2. Parsing line items
3. Validating amounts
4. Categorizing expenses

## Input

File: PDF or image of invoice

## Output

JSON object:
{
  "vendor": "Company Name",
  "invoice_date": "2026-10-02",
  "amount": 1500.00,
  "line_items": [...],
  "category": "Software"
}

## Rules

- Must extract all line items
- Amount must match sum of items
- Vendor name required
- Date must be valid
```

### Step 3: Write graders.md

How to judge if the skill works. Example:

```markdown
# Invoice Automation — Grading Criteria

## Evaluation Rubric

### Correctness (50 points)
- [ ] Vendor name extracted correctly (10 pts)
- [ ] Invoice date parsed correctly (10 pts)
- [ ] All line items captured (10 pts)
- [ ] Total amount calculated correctly (10 pts)
- [ ] Category assigned correctly (10 pts)

### Completeness (30 points)
- [ ] No missing fields (15 pts)
- [ ] All fields populated (15 pts)

### Safety (20 points)
- [ ] No sensitive data exposed (10 pts)
- [ ] Handles edge cases gracefully (10 pts)

## Passing Criteria

- **All Correctness criteria MUST pass** (minimum 50/50)
- **Completeness: 25/30 or better**
- **Safety: 20/20 required**
- **Total: 95/100 or better to publish**

## Edge Cases to Test

- [ ] Invoice with no line items
- [ ] Invoice with non-USD currency
- [ ] Corrupted PDF (test graceful failure)
- [ ] Vendor name in different format
- [ ] Missing invoice number
```

### Step 4: Write test-cases.json

Sample inputs and expected outputs:

```json
{
  "test_cases": [
    {
      "name": "Normal invoice",
      "input": "sample-invoice-1.pdf",
      "expected_output": {
        "vendor": "Acme Corp",
        "invoice_date": "2026-09-15",
        "amount": 2500.00,
        "line_items": [
          {"description": "Software License", "amount": 1500.00},
          {"description": "Support", "amount": 1000.00}
        ],
        "category": "Software"
      },
      "grading_focus": ["Correctness", "Completeness"]
    },
    {
      "name": "Invoice with discount",
      "input": "sample-invoice-2.pdf",
      "expected_output": {
        "vendor": "TechVendor Inc",
        "invoice_date": "2026-09-20",
        "amount": 900.00,
        "line_items": [
          {"description": "Product A", "amount": 1000.00},
          {"description": "Discount", "amount": -100.00}
        ],
        "category": "Equipment"
      },
      "grading_focus": ["Correctness"]
    },
    {
      "name": "Corrupted PDF (edge case)",
      "input": "corrupted-invoice.pdf",
      "expected_output": {
        "error": "Unable to parse PDF",
        "status": "failed_gracefully"
      },
      "grading_focus": ["Safety"]
    }
  ]
}
```

### Step 5: Run Tests

```bash
# Run eval suite for your skill
claude eval evals/my-new-skill

# Expected output:
# ✅ Test 1: Normal invoice — PASS (98/100)
# ✅ Test 2: Invoice with discount — PASS (95/100)
# ✅ Test 3: Corrupted PDF — PASS (20/20)
#
# ✅ OVERALL: PASS (95.7/100)
# Ready to publish!
```

### Step 6: Document Results

Save results in `results.md`:

```markdown
# Invoice Automation — Test Results

**Date:** 2026-10-02
**Tester:** Bob Johnson
**Status:** ✅ PASS (95.7/100)

## Test Summary

| Test Case | Score | Status | Notes |
|-----------|-------|--------|-------|
| Normal invoice | 98/100 | ✅ PASS | Minor formatting issue in date |
| Invoice with discount | 95/100 | ✅ PASS | Correctly handled negative amounts |
| Corrupted PDF | 20/20 | ✅ PASS | Gracefully handled error |

## Score Breakdown

- Correctness: 50/50 ✅
- Completeness: 28/30 ✅ (minor field missing in test 2)
- Safety: 20/20 ✅

## Sign-Off

- [ ] All tests pass
- [ ] Edge cases handled
- [ ] Ready for team use
- [ ] Published: [date]

**Approved by:** Alice Chen (Tech Lead)
```

---

#### 6.6.2 Evals Best Practices

**DO:**
- ✅ Include edge cases in test cases
- ✅ Test with real data samples
- ✅ Document unexpected behavior
- ✅ Run evals before publishing
- ✅ Archive test results

**DON'T:**
- ❌ Skip evals for "simple" skills
- ❌ Publish without 95%+ passing score
- ❌ Test with fake data only
- ❌ Forget to handle errors
- ❌ Delete old test results

---

#### 6.6.3 Example: Enterprise Skill Reference

The enterprise provides `vuln-patch-triage` as a reference. Check it out:

```bash
# View example eval
cat evals/vuln-patch-triage/prompt.md
cat evals/vuln-patch-triage/graders.md
cat evals/vuln-patch-triage/test-cases.json
```

This shows how properly structured evals look.

---

#### 6.6.4 Publishing a Skill

Once eval passes:

```bash
# Step 1: Verify eval passes
claude eval evals/my-new-skill
# Should show: ✅ OVERALL: PASS

# Step 2: Add to .claude/skills/
mkdir -p .claude/skills/my-new-skill
cp evals/my-new-skill/prompt.md .claude/skills/my-new-skill/
cp evals/my-new-skill/graders.md .claude/skills/my-new-skill/

# Step 3: Update .claude/skills/README.md
# Add your skill to the list

# Step 4: Commit
git add evals/my-new-skill/results.md
git add .claude/skills/my-new-skill/
git commit -m "feat: publish invoice-automation skill

- Eval passing 95.7/100
- See evals/invoice-automation/results.md for test evidence
- Ready for team use"

# Step 5: Team uses it
# /my-new-skill command becomes available
```

---

### Summary: What You've Configured

✅ **`.claude/context/`**
- architecture.md — System structure
- security-posture.md — Compliance & security
- commands.md — Available commands
- glossary.md — Domain terminology
- hazards.md — Security risks & incident history

✅ **`.claude/rules/`**
- 10-app.md — Code conventions
- security-guardrails.md — Mandatory security rules

✅ **`.claude/hooks/`**
- session-start.sh — Startup checks

✅ **`.claude/settings.json`**
- Permissions (what Claude can do)
- Environment variables

✅ **`CLAUDE.md`**
- Project instructions for Claude Code

✅ **`evals/`** (For custom skills - Phase WP2/D11)
- README.md — Navigation
- [skill-name]/prompt.md — Skill definition
- [skill-name]/graders.md — Evaluation criteria
- [skill-name]/test-cases.json — Test data
- [skill-name]/results.md — Test results

---

---

## Activity Checklist: Complete Setup Sequence

**This is your practical to-do list.** Work through each phase in order. Each phase has prerequisites.

**Estimated Total Time:** 5-8 hours (first-time setup)

---

### PHASE 1: Project Foundation (1 hour)

**Goal:** Establish what this project is and who's on the team

- [ ] **1.1 Answer Project Details**
  - [ ] Application name: _________________ (should be "rrd-ir")
  - [ ] Business purpose (2-3 sentences): _________________
  - [ ] Users/stakeholders: _________________
  - [ ] Tech lead name & email: _________________
  - [ ] Dev lead name & email: _________________
  - [ ] Security lead name & email: _________________
  - [ ] Approver for write operations: _________________ (who signs off?)
  - **Success criteria:** All fields filled, team agrees with answers
  - **Save to:** `docs/PROJECT_INFO.md`

- [ ] **1.2 Identify Technology Stack**
  - [ ] Backend language(s): _________________ (e.g., Java 21)
  - [ ] Backend framework(s): _________________ (e.g., Spring Boot)
  - [ ] Frontend language(s): _________________ (e.g., TypeScript)
  - [ ] Frontend framework(s): _________________ (e.g., React 18)
  - [ ] Database: _________________ (e.g., PostgreSQL 15)
  - [ ] Message queue (if any): _________________
  - [ ] Cache layer (if any): _________________
  - **Success criteria:** Complete tech stack documented
  - **Owner:** Tech Lead
  - **Estimated time:** 30 minutes

- [ ] **1.3 Assess Compliance Requirements**
  - [ ] Does app handle payment data? → PCI DSS: YES / NO
  - [ ] Does app handle health records? → HIPAA: YES / NO
  - [ ] Does app process EU personal data? → GDPR: YES / NO
  - [ ] Does app handle financial data? → SOX: YES / NO
  - [ ] Other compliance frameworks: _________________
  - **Success criteria:** Compliance requirements identified
  - **Owner:** Security Lead
  - **Estimated time:** 30 minutes

- [ ] **1.4 Git Repository Setup**
  ```bash
  cd /Users/erwin.t.bainto/ai_projects/rrd-ir
  git status  # Verify repo exists
  ```
  - [ ] Repository initialized
  - [ ] Team has access
  - [ ] Main branch protected
  - **Success criteria:** `git status` shows clean working tree
  - **Owner:** DevOps/Tech Lead

---

### PHASE 2: Architecture & Specifications (2 hours)

**Goal:** Document system design and requirements

**Prerequisites:** Phase 1 complete

- [ ] **2.1 Complete `.claude/context/architecture.md`**
  - Using Section 6.1.1 of this guide, fill:
    - [ ] System purpose (1 paragraph)
    - [ ] How it fits (upstream/downstream dependencies)
    - [ ] Internal structure (component table)
    - [ ] Interfaces/APIs (with consumers)
    - [ ] Key architectural decisions
    - [ ] Data ownership and retention
  - **Success criteria:** Architecture is clear enough that a new developer could understand the system
  - **Owner:** Tech Lead + Architects
  - **Estimated time:** 45 minutes
  - **Verify:** `cat .claude/context/architecture.md | wc -l` (should be >50 lines of actual content)
  - **Commit:**
    ```bash
    git add .claude/context/architecture.md
    git commit -m "docs: complete architecture.md with system design"
    ```

- [ ] **2.2 Complete `docs/architecture/ARCHITECTURE.md` (Detailed)**
  - Create detailed architecture documentation:
    - [ ] System overview diagram (ASCII or Excalidraw)
    - [ ] Component descriptions (detailed)
    - [ ] Data flow diagrams
    - [ ] Technology choices & trade-offs
    - [ ] Scalability considerations
    - [ ] Performance characteristics
  - **Success criteria:** Could hand this to a new engineer and they understand the system
  - **Owner:** Tech Lead + Architects
  - **Estimated time:** 1 hour
  - **Commit:**
    ```bash
    git add docs/architecture/ARCHITECTURE.md
    git commit -m "docs: detailed architecture documentation"
    ```

- [ ] **2.3 Create Architectural Decision Records (ADRs)**
  - For each major decision, create `docs/architecture/adr/ADR-NNN-*.md`
  - [ ] ADR-001: Why we chose [Tech A] over [Tech B]
  - [ ] ADR-002: Database design choice
  - [ ] ADR-003: [Your major decision]
  - **Success criteria:** Major technical decisions are documented with reasoning
  - **Owner:** Tech Lead
  - **Estimated time:** 30 minutes
  - **Format:**
    ```markdown
    # ADR-001: Technology Choice
    
    ## Status: Accepted
    
    ## Context
    We needed to choose between [Option A] and [Option B]...
    
    ## Decision
    We chose [Option A] because...
    
    ## Consequences
    + Benefit 1
    + Benefit 2
    - Trade-off 1
    - Trade-off 2
    ```

- [ ] **2.4 Complete `docs/specs/` Requirements**
  - [ ] Functional requirements
  - [ ] Non-functional requirements (performance, scalability)
  - [ ] Security requirements
  - [ ] Compliance requirements
  - **Success criteria:** Requirements are specific and testable
  - **Owner:** Product Lead + Tech Lead
  - **Estimated time:** 45 minutes

---

### PHASE 3: Security & Compliance (1.5 hours)

**Goal:** Document security baseline and compliance requirements

**Prerequisites:** Phase 1 complete

- [ ] **3.1 Complete `.claude/context/security-posture.md`**
  - Using Section 6.1.2 of this guide, fill:
    - [ ] Compliance requirements (which frameworks apply?)
    - [ ] Authentication method (OAuth, SAML, JWT?)
    - [ ] Authorization model (RBAC, ABAC?)
    - [ ] Data classification scheme
    - [ ] Secrets management strategy
    - [ ] Incident response contacts
  - **Success criteria:** Security baseline is clear and agreed upon
  - **Owner:** Security Lead
  - **Estimated time:** 45 minutes
  - **Commit:**
    ```bash
    git add .claude/context/security-posture.md
    git commit -m "docs: complete security-posture.md with compliance baseline"
    ```

- [ ] **3.2 Complete `docs/security/threat-model.md`**
  - Using sample from developer guide, fill:
    - [ ] Assets being protected
    - [ ] External threats (by STRIDE)
    - [ ] Internal threats
    - [ ] Attack vectors (how could they attack?)
    - [ ] Attack surface (where can they attack?)
    - [ ] Risk rating matrix
    - [ ] Mitigations for each threat
    - [ ] Sign-off from security team
  - **Success criteria:** Threat model is thorough enough for an audit
  - **Owner:** Security Lead + Architects
  - **Estimated time:** 1.5 hours
  - **Commit:**
    ```bash
    git add docs/security/threat-model.md
    git commit -m "docs: complete threat model with attack vectors and mitigations"
    ```

- [ ] **3.3 Complete `docs/security/compliance-mapping.md`**
  - For each applicable framework (PCI, GDPR, HIPAA, etc.):
    - [ ] Map each control to implementation (code, config, process)
    - [ ] Link to evidence (actual files/configs)
    - [ ] Verify controls are actually in place
  - **Success criteria:** Each control has evidence in code/config
  - **Owner:** Security Lead + Compliance Officer
  - **Estimated time:** 1 hour
  - **Commit:**
    ```bash
    git add docs/security/compliance-mapping.md
    git commit -m "docs: complete compliance mapping with evidence links"
    ```

---

### PHASE 4: Configure `.claude/` Folder (2 hours)

**Goal:** Set up Claude Code configuration for your project

**Prerequisites:** Phase 1-3 complete

- [ ] **4.1 Complete `.claude/context/` Files**
  - [ ] architecture.md (already done in Phase 2.1)
  - [ ] security-posture.md (already done in Phase 3.1)
  - [ ] **glossary.md** — Domain terminology
    - Using Section 6.1.4 of this guide, fill:
      - [ ] Business terms table
      - [ ] Technical terms table
      - [ ] Acronyms
      - [ ] Overloaded terms (same word means different things)
    - **Success criteria:** New team member can understand your domain jargon
    - **Owner:** Tech Lead + Domain Expert
    - **Estimated time:** 30 minutes
    - **Commit:**
      ```bash
      git add .claude/context/glossary.md
      git commit -m "docs: complete glossary.md with domain terminology"
      ```

  - [ ] **commands.md** — Available commands contract
    - Using Section 6.1.3 of this guide, fill:
      - [ ] List all available commands (build, test, lint, deploy, etc.)
      - [ ] What each command does
      - [ ] Expected output
      - [ ] Duration/timeout
      - [ ] Status (passing or failing today?)
    - **Success criteria:** Any team member knows what commands are available
    - **Owner:** Dev Lead
    - **Estimated time:** 30 minutes
    - **Commit:**
      ```bash
      git add .claude/context/commands.md
      git commit -m "docs: complete commands.md with available commands contract"
      ```

  - [ ] **hazards.md** — Security risks & incident history
    - Using Section 6.1.5 of this guide, fill:
      - [ ] Security hazards table
      - [ ] "Do not touch without review" areas
      - [ ] Incident history (lessons learned)
      - [ ] Known technical debt
      - [ ] Surprising behavior
    - **Success criteria:** Critical areas are marked, team knows what's fragile
    - **Owner:** Security Lead + Tech Lead
    - **Estimated time:** 45 minutes
    - **Commit:**
      ```bash
      git add .claude/context/hazards.md
      git commit -m "docs: complete hazards.md with security risks and incident history"
      ```

- [ ] **4.2 Complete `.claude/rules/` Files**
  - [ ] **10-app.md** — Code conventions
    - Using Section 6.2.1 of this guide, fill:
      - [ ] Package/folder structure
      - [ ] Naming conventions
      - [ ] Design patterns (DI, transactions, etc.)
      - [ ] Error handling standards
      - [ ] Database query requirements
      - [ ] Logging standards
      - [ ] Code review checklist
    - **Success criteria:** Code looks consistent across the codebase
    - **Owner:** Tech Lead
    - **Estimated time:** 45 minutes
    - **Commit:**
      ```bash
      git add .claude/rules/10-app.md
      git commit -m "docs: complete 10-app.md with code conventions"
      ```

  - [ ] **security-guardrails.md** — Mandatory security rules
    - Using Section 6.2.2 of this guide, fill:
      - [ ] Secrets management rules
      - [ ] Database query rules (prepared statements)
      - [ ] Authentication/authorization rules
      - [ ] Encryption requirements
      - [ ] Audit logging rules
      - [ ] Rate limiting rules
      - [ ] Dependency scanning rules
      - [ ] Code review security checklist
    - **Success criteria:** Security rules are clear and enforceable
    - **Owner:** Security Lead
    - **Estimated time:** 45 minutes
    - **Commit:**
      ```bash
      git add .claude/rules/security-guardrails.md
      git commit -m "docs: complete security-guardrails.md with mandatory controls"
      ```

- [ ] **4.3 Configure `.claude/hooks/`**
  - [ ] **session-start.sh** — Prerequisite checks
    - Using Section 6.3.1 of this guide, create:
      - [ ] Check Java/Node version
      - [ ] Check Maven/npm installed
      - [ ] Check Git installed
      - [ ] Check environment file exists
      - [ ] Print available commands
    - **Success criteria:** Hook runs without errors, prints status
    - **Owner:** DevOps/Tech Lead
    - **Estimated time:** 30 minutes
    - **Test:**
      ```bash
      bash .claude/hooks/session-start.sh
      # Should show ✅ all checks pass
      ```
    - **Commit:**
      ```bash
      git add .claude/hooks/session-start.sh
      git commit -m "docs: configure session-start.sh with prerequisite checks"
      ```

- [ ] **4.4 Configure `.claude/settings.json`**
  - Using Section 6.4 of this guide, fill:
    - [ ] Deny list (what Claude cannot access: .env, secrets, etc.)
    - [ ] Allow list (what Claude can do: build, test, lint, edit src, etc.)
    - [ ] Hooks configuration (enable session-start)
    - [ ] Environment variables (RRD_APP_NAME, etc.)
  - **Success criteria:** Permissions are clear and secure
  - **Owner:** Security Lead + Tech Lead
  - **Estimated time:** 30 minutes
  - **Test:**
    ```bash
    python3 -m json.tool .claude/settings.json
    # Should show valid JSON
    ```
  - **Commit:**
    ```bash
    git add .claude/settings.json
    git commit -m "docs: configure settings.json with permissions and environment"
    ```

- [ ] **4.5 Complete `CLAUDE.md` (Root)**
  - Using Section 6.5 of this guide, fill:
    - [ ] Application purpose (2-3 sentences)
    - [ ] Repository map (entry points, core modules)
    - [ ] Commands reference (link to .claude/context/commands.md)
    - [ ] Domain terms reference (link to glossary)
    - [ ] Hazards reference (link to hazards.md)
    - [ ] Local conventions
    - [ ] Narrowed rules
    - [ ] Write boundary (who approves? escalation path)
  - **Success criteria:** New developer can understand the project by reading CLAUDE.md
  - **Owner:** Tech Lead
  - **Estimated time:** 30 minutes
  - **Commit:**
    ```bash
    git add CLAUDE.md
    git commit -m "docs: complete CLAUDE.md with project instructions"
    ```

---

### PHASE 5: Source Code & Application Structure (Variable)

**Goal:** Set up actual application code and source directories

**Prerequisites:** Phase 1-4 complete

- [ ] **5.1 Create/Import Existing Source Code**
  - [ ] Backend source code in `src/api/` or `src/main/`
  - [ ] Frontend source code in `src/web/` 
  - [ ] Test code in `src/test/`
  - [ ] Configuration files
  - [ ] Database migrations
  - [ ] Build files (pom.xml, package.json, etc.)
  - **Success criteria:** Code compiles/builds without errors
  - **Owner:** Dev Team
  - **Estimated time:** Variable (1-4 hours depending on project size)
  - **Verify:**
    ```bash
    # For Java/Maven:
    mvn clean compile
    # For Node/npm:
    npm install && npm run build
    ```

- [ ] **5.2 Create Build Artifacts**
  - [ ] Build script works (`mvn clean package` or `npm run build`)
  - [ ] Tests pass (`mvn test` or `npm test`)
  - [ ] Lint passes (`mvn checkstyle:check` or `npm run lint`)
  - [ ] Security scan passes (`mvn dependency-check:check`)
  - **Success criteria:** All builds/tests/lint/security checks pass
  - **Owner:** Dev Team
  - **Estimated time:** 1-2 hours
  - **Update:** `.claude/context/commands.md` with actual command names
  - **Commit:**
    ```bash
    git add src/ pom.xml package.json
    git commit -m "feat: add initial application source code and build configuration"
    ```

---

### PHASE 6: Set Up Agents, Skills & Hooks (Future/As-Needed)

**Goal:** Create custom AI agents and skills for your team

**Prerequisites:** Phase 1-5 complete. This phase is OPTIONAL and done as needed.

- [ ] **6.1 Plan Custom Agents (Optional)**
  - If needed, list what custom agents would help:
    - [ ] Agent idea 1: _________________ (What would it do?)
    - [ ] Agent idea 2: _________________
    - [ ] Agent idea 3: _________________
  - **Success criteria:** Team has identified gaps that agents could fill
  - **Owner:** Tech Lead
  - **Estimated time:** 30 minutes
  - **Reference:** Section 6.6 (Evals)

- [ ] **6.2 Plan Custom Skills (Optional)**
  - If needed, list what custom skills would help:
    - [ ] Skill idea 1: _________________ (What would it automate?)
    - [ ] Skill idea 2: _________________
    - [ ] Skill idea 3: _________________
  - **Success criteria:** Team has identified repeatable tasks that skills could automate
  - **Owner:** Tech Lead
  - **Estimated time:** 30 minutes
  - **Reference:** Section 6.6 (Evals)

- [ ] **6.3 Create Evals for Custom Skills (When Publishing)**
  - For each custom skill you create:
    - [ ] Create `evals/[skill-name]/prompt.md`
    - [ ] Create `evals/[skill-name]/graders.md`
    - [ ] Create `evals/[skill-name]/test-cases.json`
    - [ ] Run tests: `claude eval evals/[skill-name]`
    - [ ] Verify: 95%+ passing score
    - [ ] Create `evals/[skill-name]/results.md` with results
    - [ ] Publish to `.claude/skills/[skill-name]/`
  - **Success criteria:** Custom skills have passing evals and are available to team
  - **Owner:** Dev Team (whoever creates the skill)
  - **Estimated time:** 2-4 hours per skill
  - **Reference:** Section 6.6 of this guide

- [ ] **6.4 Configure Additional Hooks (As Needed)**
  - [ ] `pre-tool-use.sh` — Validate before each tool run (optional)
  - [ ] `pre-commit.sh` — Check before commits (optional)
  - [ ] Custom hooks for your workflow
  - **Success criteria:** Hooks run automatically and provide value
  - **Owner:** DevOps/Tech Lead
  - **Estimated time:** 1-2 hours per hook

---

### PHASE 7: Agent Workflow Setup (When Ready)

**Goal:** Define how AI agents work together in your development process

**Prerequisites:** Phase 1-6 complete (agents/skills optional)

- [ ] **7.1 Document Agent Workflow**
  - [ ] Update `docs/agent-workflow/agent-workflow.md` with:
    - [ ] Trigger point (what starts the workflow?)
    - [ ] Agent 1 (first agent role)
    - [ ] Agent 2 (second agent role)
    - [ ] Agent N (additional agents)
    - [ ] Decision points (where does workflow branch?)
    - [ ] Approval gates (where do humans decide?)
    - [ ] Output/success criteria
  - **Success criteria:** Developer could follow the workflow and know when to ask Claude vs. when to ask a human
  - **Owner:** Tech Lead
  - **Estimated time:** 1 hour
  - **Example workflow:**
    ```
    Developer: "Claude, implement feature X"
         ↓
    Claude Agent: Plan → Design → Code
         ↓
    [MANUAL REVIEW GATE]
         ↓
    Human: Approve/Request changes
         ↓
    Claude Agent: Make changes
         ↓
    [TEST GATE]
         ↓
    If tests pass → Merge & Deploy
    If tests fail → Back to Claude for fixes
    ```

- [ ] **7.2 Create Agent Specifications (If Custom)**
  - For each custom agent:
    - [ ] Agent name & purpose
    - [ ] Input requirements
    - [ ] Output format
    - [ ] Success criteria
    - [ ] Error handling
    - [ ] Tools available to agent
    - [ ] Constraints/limitations
  - **Success criteria:** Agent spec could be handed to developer and they could implement it
  - **Owner:** Tech Lead
  - **Estimated time:** 30 minutes per agent

- [ ] **7.3 Document Workflow in `.claude/agents/`**
  - Create `README.md` explaining:
    - [ ] Available custom agents
    - [ ] When to use each agent
    - [ ] How to invoke each agent
    - [ ] Expected behavior
  - **Success criteria:** Team knows how to use agents in their workflow
  - **Owner:** Tech Lead
  - **Estimated time:** 30 minutes

---

### PHASE 8: Verification & Sign-Off (1 hour)

**Goal:** Verify everything works and team is ready

**Prerequisites:** Phases 1-7 complete (7 optional)

- [ ] **8.1 Verify Claude Code Setup**
  - [ ] Test session-start hook:
    ```bash
    bash .claude/hooks/session-start.sh
    # Should show ✅ Environment ready!
    ```
  - [ ] Verify context loads:
    ```bash
    claude context
    # Should list architecture.md, commands.md, etc.
    ```
  - [ ] Verify settings.json is valid:
    ```bash
    python3 -m json.tool .claude/settings.json
    # Should show valid JSON, no errors
    ```
  - **Success criteria:** All checks pass
  - **Owner:** DevOps/Tech Lead

- [ ] **8.2 Run First Development Task**
  - [ ] Have a developer use Claude for a real task
  - [ ] Ask Claude to: "Build feature X following our conventions"
  - [ ] Verify Claude's response:
    - [ ] Code follows `.claude/rules/10-app.md` conventions
    - [ ] Security rules are respected
    - [ ] Error handling is appropriate
    - [ ] Comments are minimal but helpful
  - **Success criteria:** Developer confirms code quality is good and Claude understood the project
  - **Owner:** Dev Team
  - **Estimated time:** 1-2 hours

- [ ] **8.3 Team Sign-Off**
  - [ ] Dev Lead: "Configuration is complete and correct"
  - [ ] Security Lead: "Security baseline is in place and documented"
  - [ ] Tech Lead: "Architecture is clear and documented"
  - [ ] QA/Test Lead: "Build process works and tests pass"
  - **Success criteria:** All stakeholders have reviewed and approved
  - **Owner:** All leads

- [ ] **8.4 Final Commit & Tag**
  - [ ] All changes committed:
    ```bash
    git status  # Should be clean
    ```
  - [ ] Create git tag for Phase D4 completion:
    ```bash
    git tag -a d4-harness-complete -m "Phase D4: Harness configuration complete"
    git push origin d4-harness-complete
    ```
  - **Success criteria:** Git shows all work is committed and tagged
  - **Owner:** Tech Lead

---

## Activity Checklist Summary

| Phase | Completed? | Owner | Time | Sign-Off |
|-------|-----------|-------|------|----------|
| 1. Project Foundation | [ ] | Tech/Dev Lead | 1h | _____ |
| 2. Architecture & Specs | [ ] | Tech Lead | 2h | _____ |
| 3. Security & Compliance | [ ] | Security Lead | 1.5h | _____ |
| 4. Configure .claude/ | [ ] | Tech Lead | 2h | _____ |
| 5. Source Code | [ ] | Dev Team | 1-4h | _____ |
| 6. Agents & Skills | [ ] | Tech Lead | 0-4h (optional) | _____ |
| 7. Agent Workflow | [ ] | Tech Lead | 1-2h (optional) | _____ |
| 8. Verification & Sign-Off | [ ] | All Leads | 1h | _____ |

**TOTAL: 9-17 hours** (depending on complexity and whether custom agents/skills needed)

---

## Common Activities & Workflows

### Task 1: Write a New API Endpoint

**Scenario:** You need to create a new endpoint `/api/v2/revenue-forecast`

**Step 1: Check the guidelines**

```bash
# Read your conventions
cat .claude/context/architecture.md
cat .claude/rules/10-app.md
cat .claude/context/hazards.md
```

**Step 2: Ask Claude**

```bash
claude code -f /path/to/project

# Then ask:
# "Create a new Spring Boot REST endpoint at /api/v2/revenue-forecast
# that accepts POST with a RevenueQuery object and returns a 
# RevenueForcastResponse. Follow the conventions in .claude/rules/10-app.md"
```

**Step 3: Review the code**

Claude will generate code that:
- Follows your naming conventions
- Uses constructor injection
- Has @Transactional on writes
- Validates input
- Handles errors without leaking data
- Logs appropriately

**Step 4: Commit**

```bash
git add src/main/java/com/company/rrd/api/RevenueForecastController.java
git commit -m "feat: add revenue forecast endpoint"
```

---

### Task 2: Fix a Security Issue

**Scenario:** You find SQL injection risk in transaction search

**Step 1: Understand the hazard**

```bash
# Already documented in hazards.md
grep -A 3 "SQL Injection in transaction search" .claude/context/hazards.md
```

**Step 2: Ask Claude to fix it**

```bash
# Show Claude the problem
cat src/api/TransactionController.java  # Around line 42

# Ask Claude:
# "Fix the SQL injection vulnerability in TransactionController.java:42
# Replace string concatenation with PreparedStatement using Spring Data @Query"
```

**Step 3: Verify the fix**

```bash
# Run tests
mvn test

# Run security scan
mvn dependency-check:check
```

**Step 4: Update hazards document**

```bash
# Edit .claude/context/hazards.md
# Change status from "Open" to "Mitigated"
# Add evidence: "Fixed in commit abc123"
```

**Step 5: Commit**

```bash
git add src/api/TransactionController.java
git add .claude/context/hazards.md
git commit -m "security: fix SQL injection in transaction search

- Replace string concatenation with PreparedStatement
- Use Spring Data @Query with named parameters
- Closes security hazard documented in hazards.md"
```

---

### Task 3: Add a New Rule

**Scenario:** Your team decided all methods must have unit tests

**Step 1: Update the rule**

```bash
# Edit .claude/rules/10-app.md
# Add a new section:

## Unit Test Coverage

All public methods must have at least one unit test.

✅ CORRECT:
@Test
public void testCalculateRevenue_shouldReturnCorrectAmount() {
  // Arrange
  Transaction t = new Transaction(100, "USD");
  // Act
  BigDecimal result = service.calculateRevenue(t);
  // Assert
  assertEquals(new BigDecimal("100.00"), result);
}

❌ WRONG:
public Revenue calculateRevenue(Transaction t) {
  // No tests!
}
```

**Step 2: Update code review checklist**

```bash
# Edit .claude/rules/10-app.md
# Add to "Code Review Checklist":
- [ ] All public methods have unit tests
- [ ] Test coverage > 80%
```

**Step 3: Commit**

```bash
git add .claude/rules/10-app.md
git commit -m "docs: add unit test requirement to conventions"
```

**Step 4: Announce to team**

```bash
# Team meeting: "We now require unit tests for all public methods.
# See .claude/rules/10-app.md for details."
```

---

### Task 4: Document a Lesson Learned

**Scenario:** A bug was found due to missing rounding in revenue calculations

**Step 1: Record the incident**

```bash
# Edit .claude/context/hazards.md
# Add to "Incident History":

| Revenue calculation was 0.01% off due to rounding | Revenue calculation | 2026-07-20 | Always use BigDecimal for money, not double |
```

**Step 2: Fix the code**

```java
// Before (WRONG):
double revenue = transaction.getAmount() * rate;  // Rounding error!

// After (CORRECT):
BigDecimal revenue = transaction.getAmount()
  .multiply(new BigDecimal(rate))
  .setScale(2, RoundingMode.HALF_UP);
```

**Step 3: Add to surprising behavior**

```bash
# Edit .claude/context/hazards.md
# Add:

- **Revenue calculation with decimals:** Always use BigDecimal, never double.
  Why: Double has precision loss. Example: 0.1 + 0.2 ≠ 0.3 in double.
  Reference: src/engine/Calculator.java
```

**Step 4: Update conventions**

```bash
# Edit .claude/rules/10-app.md
# Add section:

## Money & Decimals — Use BigDecimal

✅ CORRECT:
BigDecimal amount = new BigDecimal("100.50");
BigDecimal rate = new BigDecimal("0.15");
BigDecimal result = amount.multiply(rate).setScale(2, RoundingMode.HALF_UP);

❌ WRONG:
double amount = 100.50;   // Precision loss!
double rate = 0.15;
double result = amount * rate;  // Could be 15.074999999 instead of 15.075!
```

**Step 5: Commit**

```bash
git add .claude/context/hazards.md
git add .claude/rules/10-app.md
git commit -m "docs: document revenue rounding lesson and require BigDecimal

- Add incident history: 0.01% calculation error due to double precision
- Add to surprising behavior: why we use BigDecimal
- Update conventions with correct example
- Fixes issue #42"
```

---

## Troubleshooting

### Problem: Claude Code says "Permission denied"

**Cause:** File path is in the `deny` list in `.claude/settings.json`

**Solution:**

```bash
# Check what's denied
grep -A 5 "\"deny\"" .claude/settings.json

# For example, if you see:
"deny": [
  "Read(.env)"
]

# That means Claude cannot read .env files (for security)
# If you need to grant access, edit settings.json:

"allow": [
  "Read(.env)"  # Add this
]

# Then commit:
git add .claude/settings.json
git commit -m "docs: grant Claude Code access to .env file"
```

---

### Problem: session-start.sh hook fails

**Cause:** Prerequisites not installed

**Solution:**

```bash
# Run the hook manually to see the error
bash .claude/hooks/session-start.sh

# Example output might be:
# ✗ Java 21 required, found 11.0.1
# Install from: https://adoptium.net/

# Follow the instructions to install missing prerequisites
```

---

### Problem: Claude doesn't follow my conventions

**Cause:** Conventions not documented clearly enough

**Solution:**

1. Check `.claude/rules/10-app.md` has clear examples

2. Add to code review checklist:

```bash
# Edit .claude/rules/10-app.md
# Verify "Code Review Checklist" includes your convention
```

3. If still not followed, ask Claude explicitly:

```bash
# Ask Claude:
# "Follow the Java conventions in .claude/rules/10-app.md section 'Naming Conventions'"
```

---

### Problem: My security rule isn't being enforced

**Cause:** Rule not in `.claude/rules/security-guardrails.md` or enforcement method not set up

**Solution:**

1. Verify rule is documented:

```bash
grep "Your rule text" .claude/rules/security-guardrails.md
```

2. Verify enforcement method is realistic. For example:

```markdown
| Rule | Enforcement |
|------|-------------|
| All queries use PreparedStatement | Code review + SonarQube scanning |
```

3. Set up the enforcement tool (SonarQube, pre-commit hook, etc.)

4. Have Claude follow it by asking explicitly:

```bash
# Ask Claude:
# "Check that all queries use PreparedStatement before writing SQL"
```

---

## Next Steps

### Immediate (This Week)

1. ✅ **Complete Setup**
   - [ ] Fill all `.claude/context/` files
   - [ ] Fill all `.claude/rules/` files
   - [ ] Test session-start.sh hook
   - [ ] Verify permissions in settings.json

2. ✅ **Team Onboarding**
   - [ ] Share this guide with team
   - [ ] Have team run session-start.sh hook
   - [ ] Review CLAUDE.md together
   - [ ] Review hazards.md for critical items

3. ✅ **Git Setup**
   - [ ] Initialize git repo
   - [ ] Commit all configuration
   - [ ] Set up branch protection on main

### Short-Term (This Month)

1. ✅ **First Development Tasks**
   - [ ] Assign first API endpoint to developer
   - [ ] Have them ask Claude for help
   - [ ] Review code for conventions compliance
   - [ ] Iterate on feedback

2. ✅ **Refine Conventions**
   - [ ] Document lessons learned
   - [ ] Add new rules as needed
   - [ ] Update hazards as risks are discovered
   - [ ] Keep conventions current

3. ✅ **Security Baseline**
   - [ ] Run security scan
   - [ ] Address critical findings
   - [ ] Document mitigations
   - [ ] Schedule compliance review

### Medium-Term (This Quarter)

1. ✅ **Advanced Features**
   - [ ] Create custom agents for specialized tasks
   - [ ] Create custom skills for repeated workflows
   - [ ] Automate more tasks with hooks

2. ✅ **Governance**
   - [ ] Set up compliance reporting
   - [ ] Define approval process
   - [ ] Train team on write boundaries
   - [ ] Document approval evidence

3. ✅ **Production Readiness**
   - [ ] Complete threat model
   - [ ] Complete compliance mapping
   - [ ] Pass security audit
   - [ ] Ready for production deployment

---

## Quick Reference

### Most Important Files (Bookmark These)

| File | Purpose | When to Check |
|------|---------|---------------|
| `CLAUDE.md` | Project instructions | Starting work, confused about project |
| `.claude/context/hazards.md` | Dangerous areas | Before editing critical code |
| `.claude/rules/10-app.md` | Code conventions | Before writing code |
| `.claude/context/glossary.md` | Term definitions | When seeing unfamiliar terms |
| `.claude/context/commands.md` | Available commands | When running tests/builds |

### Most Used Commands

```bash
# Check prerequisites
bash .claude/hooks/session-start.sh

# View Claude Code's knowledge about your project
claude context

# Ask Claude a question
claude code -f /path/to/project

# Run tests
mvn test

# Build
mvn clean package

# Lint
mvn checkstyle:check

# Security scan
mvn dependency-check:check

# View current configuration
cat .claude/settings.json
```

### Key Principles

1. **Read hazards before editing** — Critical code needs extra review
2. **Follow conventions** — Makes code consistent and reviewable
3. **Document decisions** — Why, not just what
4. **Log security events** — Audit trail is critical
5. **Ask Claude** — It knows your project better after reading context
6. **Commit often** — Easier to find issues later

---

## Additional Resources

- **Claude Code CLI:** https://claude.com/claude-code
- **AI SSDLC Framework:** See `docs/architecture/SSDLC_Overview.md`
- **Enterprise Standards:** See `@enterprise/` folder
- **Security Best Practices:** See `docs/security/README.md`
- **Deployment Guide:** See `README.md` deployment checklist

---

## Getting Help

**If you're stuck:**

1. **Check this guide** — Use Ctrl+F to search
2. **Read the relevant `.claude/` file** — It has detailed guidance
3. **Ask Claude** — It can answer questions about the project
4. **Ask your Tech Lead** — Bob Johnson (bob@company.com)
5. **File an issue** — Document the problem and what you tried

---

## Feedback

This guide is living documentation. As you work with the project:

- ✅ Found typos? Fix them and commit
- ✅ Found unclear sections? Improve the wording
- ✅ Discovered new lessons? Add to hazards.md
- ✅ Developed new patterns? Add to conventions

**Keep this guide current so the next person has an even better onboarding experience.**

---

**Last Updated:** 2026-10-02  
**Maintained by:** Bob Johnson (Tech Lead)  
**Next Review:** 2026-12-02 (quarterly)

