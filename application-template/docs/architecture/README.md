# Architecture & Design Decisions

This folder contains the authoritative system design documentation, architectural diagrams, and decision records for this application.

---

## Contents

### System Architecture
- **`ARCHITECTURE.md`** — Complete system design document
  - System scope and monorepo topology
  - Component structure (backend, frontend, databases, message queues)
  - API layer definitions and contracts
  - Data model and persistence strategy
  - Security architecture
  - Integration points with external systems

### Architecture Decision Records (ADRs)

ADRs document **why** architectural decisions were made, not just **what** was decided. Each ADR includes:
- **Context:** The problem or constraint that motivated the decision
- **Decision:** What was chosen and why
- **Consequences:** Trade-offs, benefits, and drawbacks
- **Alternatives considered:** Why other approaches were rejected

#### Creating a New ADR

File naming: `ADR-NNN-descriptive-title.md` (e.g., `ADR-015-event-sourcing-for-audit-trail.md`)

Template structure:
```markdown
# ADR-NNN: <Title>

## Context
[What problem are we solving? What constraints do we face?]

## Decision
[What did we decide? Why?]

## Consequences
[What are the benefits? What are the trade-offs?]

## Alternatives
[What else did we consider? Why did we reject it?]

## Related
[Links to related ADRs, code, tests]
```

### Process Flows

Detailed walkthroughs of critical workflows:
- **`ImportProcess.md`** — How data enters the system
- **`ExportProcess.md`** — How data leaves the system  
- **`BatchJobProcess.md`** — How batch jobs are executed and monitored
- **`SecurityComponent.md`** — Authentication, authorization, and secrets management

### Design Artifacts

Supporting diagrams and visualizations:
- C4 component diagrams (system context, containers, components)
- Sequence diagrams (call flows, state transitions)
- Entity relationship diagrams (data model)
- Deployment architecture (Kubernetes, environments)

### Testing Subdirectory

Linked test plans and acceptance criteria:
- `ImportProcessTestPlan.md` — Test scenarios for import workflow
- `BatchJobTestPlan.md` — Test scenarios for batch jobs
- etc.

---

## Reading Guide

### For a new team member:
1. Start with `ARCHITECTURE.md` for system scope and topology
2. Skim ADR titles in the `adr/` folder to understand past decisions
3. Read ADRs relevant to the area you'll work on (backend APIs, batch jobs, frontend state, etc.)

### For architectural questions:
1. Check `ARCHITECTURE.md` for system-level answers (topology, layers, components)
2. Search ADRs by keyword or topic to understand the reasoning behind decisions
3. Use `grep` to find related code references

### For implementing a feature:
1. Read the relevant process flow (e.g., `ImportProcess.md`)
2. Check related ADRs for constraints and patterns
3. Review any design artifacts (diagrams) for visual clarity
4. Link to this architecture in your PR description and code comments (where non-obvious)

### For making a new architectural decision:
1. Identify the problem and context
2. Evaluate alternatives (at least 3)
3. Choose one and document it as a new ADR
4. Link the ADR in `ARCHITECTURE.md` and relevant process flows
5. Reference the ADR in code comments and pull request descriptions

---

## ADR Numbering & Organization

ADRs are numbered sequentially starting from 001. Organize them by topic or function:

**Example categories:**
- **001–010:** Data persistence (schema, indexes, partitioning)
- **011–020:** Batch processing (job patterns, transactional boundaries)
- **021–030:** API design (contracts, versioning, error handling)
- **031–040:** Frontend state management (NgRx, component patterns)
- **041–050:** Security (authentication, encryption, secret management)
- **051–060:** Operations (logging, monitoring, health checks)

*Your project may have different groupings — adapt as needed.*

---

## When to Create an ADR

Create an ADR when:
- You're making a significant architectural decision (affects multiple components, hard to reverse)
- The decision involves trade-offs worth documenting (performance vs maintainability, complexity vs flexibility)
- The decision constrains future work (e.g., "all batch jobs must use the X pattern")
- The decision was contested or required stakeholder approval
- You want to preserve the rationale for future maintainers

**Do NOT create an ADR for:**
- Trivial implementation choices (naming a variable, formatting code)
- Temporary workarounds or hotfixes
- Decisions that reverse a previous ADR (update the previous ADR instead)

---

## When to Update This Folder

Update architecture documentation when:
- You add a new major component (API endpoint, batch job, microservice)
- You change the data model or schema significantly
- You make a significant architectural decision (create an ADR)
- You change deployment topology or infrastructure
- You update security architecture or compliance requirements

---

## Key Constraints & Standards

This section should be customized for your application. Document:

### Technology Stack
List the languages, frameworks, and key libraries:
- Backend: `<Java/Python/Go/Node>` version X.Y + `<Framework>` version A.B
- Frontend: `<Angular/React/Vue>` version X + state management `<NgRx/Redux/Vuex>`
- Database: `<PostgreSQL/MySQL/SQL Server>` version X
- Messaging: `<RabbitMQ/Kafka/SQS>` (if applicable)
- Deployment: `<Kubernetes/Docker Compose/Serverless>` on `<AWS/GCP/Azure/On-premise>`

### Naming Conventions
- **Packages/modules:** `com.company.product.domain` (e.g., `com.rrd.invoice.import`)
- **Classes:** PascalCase, suffixes for type (e.g., `InvoiceService`, `InvoiceController`)
- **Methods:** camelCase, verb-first (e.g., `searchInvoices()`, `computeTaxAmount()`)
- **Database tables:** snake_case, singular noun (e.g., `invoice`, `invoice_image`)
- **API endpoints:** kebab-case, RESTful naming (e.g., `/api/invoices`, `/api/admin/jobs`)

### Code Style & Standards
- **Java:** Checkstyle rules in `pom.xml`; no raw types; explicit null checks
- **TypeScript:** ESLint rules in `.eslintrc`; no `any` types; typed NgRx state
- **Databases:** All migrations via Liquibase; rollback blocks mandatory
- **Tests:** 80%+ line coverage enforced by CI gate

### Security Standards
- No hardcoded credentials (use environment variables or secrets manager)
- All database queries use parameterized statements (prevent SQL injection)
- All external APIs use HTTPS (TLS 1.2+)
- All secrets (keys, passwords, tokens) never logged or transmitted in plaintext
- Sensitive data redacted from logs before archival

---

## Related

- **`.claude/context/architecture.md`** — Application-specific context for agents (references this folder)
- **`docs/specs/`** — Functional and non-functional requirements (driven by architecture)
- **`docs/guides/`** — How to navigate and update this architecture
- **`docs/audits/`** — Audit findings related to architectural decisions
- **`docs/testing/`** — Test plans that verify architecture patterns
- **`CLAUDE.md`** — Project instructions that reference this architecture

---

## Maintenance

### Keeping ADRs Current

- ADRs are **not** meant to be kept "perfectly accurate" — they capture the decision as made
- If a decision is overturned, create a **new ADR** explaining the reversal, don't edit the old one
- Link the new ADR back to the previous one: "Supersedes ADR-NNN"
- Only update an ADR if you're correcting factual errors (typos, wrong links), not reversing the decision

### Deprecating ADRs

If an ADR is no longer applicable:
1. Add a "DEPRECATED" marker at the top
2. Reference the new ADR that replaces it
3. Keep the old ADR in the archive (do not delete)

### Reviewing Architecture Changes

Before merging a PR that changes architecture:
1. Check if any ADRs are affected
2. If a new pattern is introduced, request an ADR
3. Link the ADR in the PR description
4. Require architecture lead sign-off if the change affects multiple systems

---

## Quick Links

- **System design:** See `ARCHITECTURE.md`
- **Data persistence patterns:** See `adr/ADR-001*`, `adr/ADR-002*`
- **Batch job patterns:** See `adr/ADR-010*`, `adr/ADR-011*`
- **API design:** See `adr/ADR-020*`
- **Frontend state:** See `adr/ADR-030*`
- **Security:** See `adr/ADR-040*`, `SecurityComponent.md`
- **Testing:** See `testing/` subdirectory
