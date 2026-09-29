# Specifications & Requirements

This folder contains the project specifications, business rules, API contracts, and requirements that define what the application does and how it must behave.

---

## Contents

### Requirements (Functional & Non-Functional)

**`functional-requirements.md`** — What the system does
- User-facing features and system behaviors
- Acceptance criteria for each requirement
- Traceability links (code paths, tests, ADRs)
- Status tracking (`[CONFIRM]` / APPROVED / BLOCKED)

**`non-functional-requirements.md`** — How the system behaves
- Quality attributes: performance, availability, security, scalability, maintainability
- Measurable criteria (latency, throughput, uptime SLAs, coverage targets)
- Links to monitoring dashboards and test procedures
- Responsible teams and owners

### Business Specifications & Contracts

- **`business-specs.md`** — Business rules and operational policies
  - What business problem does the application solve?
  - Key workflows and processes
  - Constraints and assumptions
  - Retention policies or lifecycle rules

- **`api-reference.md`** — REST/GraphQL API endpoint definitions
  - Endpoint paths and HTTP methods
  - Request/response schemas
  - Authentication and authorization requirements
  - Error response formats (RFC 7807)
  - Rate limiting and pagination
  - Example requests and responses

### Architecture & Compliance Planning

- **`architecture-plan.md`** — Design decisions and component specifications
  - Data model and schema overview
  - Batch job architecture (if applicable)
  - Security architecture and authentication flows
  - Frontend state management
  - Integration points with external systems

- **`cve-mitigation-plan.md`** — Known vulnerabilities and patching strategy
  - Dependency versions and known CVEs
  - Severity levels and patch timelines
  - Compliance requirements (PCI-DSS, HIPAA, SOC2, etc.)

---

## Structure: Functional vs Non-Functional Requirements

### Functional Requirements (FR)
**What the system does.** User-facing and system behaviors; can be directly tested.

| Aspect | Detail |
|---|---|
| **Author** | Product team, business stakeholders |
| **Change frequency** | Per feature release or product update |
| **Agents use it for** | Understanding *what* to build (feature scope) |
| **Examples** | "Search items by date", "Delete expired records", "Upload batch file" |
| **Verification** | Automated test passes; manual acceptance test |

### Non-Functional Requirements (NFR)
**How the system behaves.** Quality attributes: performance, security, availability, scalability.

| Aspect | Detail |
|---|---|
| **Author** | Architecture, security, ops teams |
| **Change frequency** | Per infrastructure update or compliance change |
| **Agents use it for** | Understanding *constraints* and *quality gates* (performance targets, security rules, scalability limits) |
| **Examples** | "API response p99 < 2s", "No hardcoded secrets", "Batch jobs complete within 1 hour", "99.9% uptime SLA" |
| **Verification** | Metrics + audits (load test, security scan, monitoring dashboard) |

### How to Use Them Together

**When implementing a feature, read both:**
1. **FR** tells you *what* to build (e.g., FR-001: Search records by date range)
2. **NFR** tells you *how well* to build it (e.g., NFR-002: Response time p99 < 500ms, NFR-004: No hardcoded secrets)

**Example workflow:**
- FR-001: "Users can search records by date range"
- NFR-002: "Search API response time p99 < 500ms"
- NFR-004: "No hardcoded credentials in code or config"
- Related test: `docs/testing/test-plan.md#Search-Scenarios`

---

## Status Indicators

Look for these markers while reading specs:

- **`[CONFIRM]`** — Item awaiting verification or stakeholder sign-off
  - Example: `[CONFIRM] retention period`
  - **Blocks all agent work on that requirement** until resolved
  
- **`Status: DRAFT`** — Document is incomplete and under active development

- **`Status: APPROVED`** — Document has been reviewed and signed by stakeholders

- **`Status: BLOCKED`** — Cannot implement until `[CONFIRM]` items are resolved

---

## When to Add or Update Here

Update a spec when:
- Business requirements change (features, policies, retention rules)
- A new endpoint or batch job is being defined
- Compliance or legal requirements change
- You're documenting an operational constraint or assumption
- An API contract evolves or is versioned

**Do NOT add here:**
- How-to guides or learning materials (→ `docs/guides/`)
- Architecture decisions or design rationale (→ `docs/architecture/`)
- Audit findings or verification evidence (→ `docs/audits/`)
- Test plans or scenarios (→ `docs/testing/`)
- Agent workflow pipeline (→ `docs/agent-workflow/`)

---

## Access & Authority

### Audience
- Development team (implements features)
- Product team (defines features)
- Legal/compliance stakeholders (retention periods, data handling)
- Operations team (understands operational constraints)

### Authority
- **Business owner** — Owns functional requirements and business rules
- **Product lead** — Owns API contracts and feature definitions
- **Tech lead** — Owns architecture planning and NFR definitions
- **Security team** — Owns security requirements and CVE mitigation
- **Legal/compliance** — Owns retention periods and compliance rules

### Change Control
Any update to `Status: APPROVED` specs requires sign-off from the owning stakeholder.

---

## Critical Dependencies

⚠️ **These specs are used by every agent before producing code.** Always check:

1. **Before starting work:**
   - Are there any `[CONFIRM]` items blocking this requirement?
   - Has the business owner approved the functional requirement?
   - Has the tech lead approved the non-functional requirement?

2. **Key blockers to watch:**
   - Retention periods (affects data lifecycle jobs)
   - Data retention policies (affects purge/cleanup logic)
   - API contracts (affects controller response structure)
   - Security requirements (affects validation, encryption, authentication)

3. **Linked documentation:**
   - Each requirement should link to tests (`docs/testing/test-plan.md`)
   - Each requirement should link to related ADRs (`docs/architecture/adr/`)
   - Each requirement should link to monitoring/SLO dashboards

---

## Common Patterns

### Requirement Template (FR)

```markdown
### FR-NNN: <Requirement Title>

**Status:** APPROVED (or [CONFIRM], BLOCKED)

**User story:**
"As a [user role], I want to [action], so that [benefit]"

**Acceptance criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Related NFRs:**
- NFR-001: Performance
- NFR-004: Security

**Related tests:**
- `docs/testing/test-plan.md#TestScenario`

**Related code:**
- Backend: `src/main/java/com/.../Service.java`
- Frontend: `src/app/modules/.../component.ts`

**Related ADRs:**
- ADR-001: Architectural decision related to this FR

**Dependencies:**
- FR-NNN (this FR depends on the other being complete)

**Blocked by:**
- [CONFIRM] Item 1 — awaiting stakeholder decision
```

### Requirement Template (NFR)

```markdown
### NFR-NNN: <Quality Attribute>

**Status:** APPROVED (or [CONFIRM], BLOCKED)

**Requirement:**
[What quality attribute are we specifying? E.g., performance, security, scalability]

**Measurable criteria:**
- Metric 1: [target value] (e.g., "API latency p99 < 500ms")
- Metric 2: [target value]
- Metric 3: [target value]

**How we measure it:**
- Tool/process to verify (e.g., load test, security scan, monitoring dashboard)
- Baseline or current state
- Target state

**Related FRs:**
- FR-001: Feature that must meet this NFR
- FR-002: Another feature affected

**Related tests:**
- `docs/testing/test-plan.md#PerformanceTestScenario`

**Related ADRs:**
- ADR-001: Architectural decision supporting this NFR

**Responsible team:**
- Backend: Performance, database query optimization
- DevOps: Infrastructure, scaling, monitoring
- Security: Encryption, authentication
```

---

## Change Management

### Adding a New Requirement

1. **Create the requirement** using the template above
2. **Mark it** `Status: DRAFT`
3. **Link it** to related documents (FRs, NFRs, ADRs, tests)
4. **Get stakeholder sign-off** (business owner for FR, tech lead for NFR)
5. **Update status** to `Status: APPROVED`
6. **Link from agent instructions** (`.claude/rules/`, `CLAUDE.md`)

### Updating an Existing Requirement

1. **Update the content** directly in the file
2. **Update the status** if it changes (e.g., APPROVED → BLOCKED)
3. **Link any new dependencies** (new ADRs, new tests)
4. **Notify stakeholders** of changes (email, Slack)
5. **Update related documentation** (guides, agent rules)

### Deprecating a Requirement

1. **Mark at top:** `Status: DEPRECATED — See FR-NNN instead`
2. **Link to replacement** (if FR/NFR is replaced by another)
3. **Keep old text** (do not delete)
4. **Remove from active list** in README

---

## Traceability

Each requirement should link to:
- **Code:** Specific implementation files or classes
- **Tests:** Test scenarios that verify it (`docs/testing/test-plan.md`)
- **ADRs:** Architectural decisions that enable it (`docs/architecture/adr/`)
- **Monitoring:** Dashboard or alert that tracks it (if applicable)

### Example Traceability Chain

```
FR-001: Users can search records by date range
├── Code: InvoiceController.search()
├── Tests: test-plan.md#SearchScenarios
├── ADRs: ADR-009 (sargable predicates)
└── Monitoring: Grafana dashboard "API latency"
```

---

## When Requirements Block Work

If a requirement has `[CONFIRM]` items or `Status: BLOCKED`:

1. **Don't start implementation** — Wait for confirmation
2. **Flag to tech lead** — In standup or Slack
3. **Create a ticket** for stakeholder follow-up
4. **Check back regularly** — Status may change
5. **Once approved:** Remove blocker and proceed with implementation

---

## Related

- **`docs/guides/`** — How-to guides reference these specs
- **`docs/architecture/`** — ADRs provide architectural context for these specs
- **`docs/audits/`** — Audit findings verify compliance with these specs
- **`docs/testing/`** — Test plans verify these specs are implemented correctly
- **`CLAUDE.md`** — Project instructions reference these specs as constraints for agents
- **`.claude/rules/`** — Agent rules may enforce NFR requirements (e.g., no hardcoded secrets)

---

## Quick Links

- **Functional requirements:** [functional-requirements.md](functional-requirements.md)
- **Non-functional requirements:** [non-functional-requirements.md](non-functional-requirements.md)
- **Business rules:** [business-specs.md](business-specs.md)
- **API contracts:** [api-reference.md](api-reference.md)
- **Architecture plan:** [architecture-plan.md](architecture-plan.md)
- **CVE mitigation:** [cve-mitigation-plan.md](cve-mitigation-plan.md)
