# AI Agent Workflow Pipeline — <APPLICATION_NAME>

**Example Workflow Diagram**

This is a template showing the structure of a complete agent workflow for your application. Replace `<APPLICATION_NAME>` and adjust stages/agents based on your actual setup.

---

## Legend

| Symbol | Category |
|---|---|
| ⬜ | Trigger / source |
| 🟦 | AI (Claude Agent) |
| 🟧 | Human approval gate |
| 🟩 | Testing |
| 🟪 | CI/CD · deploy |
| 🟫 | Gate / result |

---

## Stage 0 · Developer Trigger — Slash Command

Developer initiates workflow using a slash command from `.claude/commands/`

| `/new-feature` | `/new-batch-job` | `/security-scan` | `/update-pipeline` |
|---|---|---|---|
| End-to-end feature | Background job | OWASP + CVE audit | CI/CD configuration |
| Routes to `dev-coordinator` | Routes to `job-specialist` | Routes to `security-auditor` | Routes to `devops-engineer` |
| Plan first, no files touched | Scaffold + patterns | Read-only — no file edits | Review proposed changes |

↓

---

## Stage 1 · AI Planning & Coordination

**Agent:** `dev-coordinator`

Reads project context (business specs, architecture ADRs, API contracts) and produces an execution plan.

### Actions
- Read `.claude/context/architecture.md`
- Read `.claude/context/glossary.md`
- Read `docs/specs/functional-requirements.md`
- Read `docs/architecture/adr/` (relevant ADRs)
- Decompose task into implementation steps
- Identify required specialists and skill invocations
- Draft execution plan with sequencing

### Deliverable
Structured execution plan (outline, dependencies, estimated effort)

↓

---

## 🟧 Human Approval Gate 1 — Review Execution Plan

**Gating Criteria:**
- Plan is clear and well-sequenced
- Identified specialists match the work scope
- No ambiguity about which files will be created/modified
- Estimated effort is reasonable

**Developer Response Required:**
- `approve` — Proceed to implementation
- `reject — [reason]` — Send back to planning
- `approve with conditions: [notes]` — Approve with guidance

⚠️ **Note:** Responses like "yes", "ok", "continue" are **NOT valid approvals**. Use the exact phrases above.

↓

---

## Stage 2 · AI Implementation

**Agents:** Specialist agents (determined by plan)  
**Skills:** Triggered based on task type (e.g., `/scaffold-workspace`, `/db-migration`, `/security-hardening`)

### Implementation Pattern

**Example: New Feature Flow**
1. Scaffold workspace (folder structure, boilerplate)
2. Generate domain model and repository layer
3. Create service layer with business logic
4. Generate API controller (OpenAPI-first)
5. Create Angular component (standalone, strongly typed)
6. Write integration between frontend and backend

**Example: Batch Job Flow**
1. Scaffold batch job class with framework pattern
2. Add transactional boundaries and error handling
3. Integrate with scheduler (Quartz, Spring Scheduler)
4. Add logging and monitoring hooks
5. Create job trigger endpoint or cron configuration

### Success Criteria
- All files follow project naming conventions
- No hardcoded credentials, secrets, or API keys
- Code structure matches architecture ADRs
- Boilerplate is correct and compilable

↓

---

## 🟧 Human Approval Gate 2 — Review Generated Code

**Gating Criteria:**
- Code structure matches approved plan
- All files follow naming and packaging conventions
- No immediate security issues (hardcoded secrets, insecure dependencies)
- Code is compilable/syntactically valid

**Developer Actions:**
- Review generated files
- Run local build (`mvn clean compile` / `npm install`)
- Spot-check for any obvious issues
- Request fixes if needed, or approve to proceed

↓

---

## Stage 3 · Security & Performance Scan

**Agents:** `security-auditor` (read-only), specialist auditors  
**Action:** Scan code for CVEs, hardcoded secrets, insecure patterns

### Scans Performed

| Scan | Tool | What it checks | Blocks on |
|---|---|---|---|
| **Dependency CVE** | OWASP Dep-Check, npm audit, Maven | Known vulnerable libraries | Critical CVEs |
| **Hardcoded Secrets** | TruffleHog, regex patterns | API keys, credentials, tokens | Any found |
| **OWASP Top 10** | SonarQube, Checkmarx | SQL injection, XSS, CSRF | Critical findings |
| **Performance** | Code analysis | N+1 queries, memory leaks, batch patterns | High severity issues |

### Critical Escalations (Must Resolve Before Gate 3 Approval)
- Any critical CVEs in dependencies
- Hardcoded credentials (database passwords, API keys, tokens)
- SQL injection vulnerabilities
- Unvalidated user input in API endpoints
- Plaintext transmission of sensitive data

↓

---

## 🟧 Human Approval Gate 3 — Review Security Findings

**Gating Criteria:**
- All **Critical** findings are resolved
- All **High** findings have documented remediation plans
- No unresolved hardcoded credentials
- CVE patching roadmap is clear

**Developer Actions:**
- Review security-auditor findings
- Fix all Critical issues
- Create tickets for High/Medium findings (with timeline)
- Get security team sign-off on remediation plan

↓

---

## Stage 4 · Test Generation

**Agent:** `qa-engineer`  
**Skill:** `/spec-synthesizer` (generates test scenarios)

Generates test cases covering:
- Happy path execution
- Error scenarios and exception handling
- Edge cases (boundary conditions, null values)
- Integration points (database, APIs, message queues)
- Security scenarios (authentication, authorization, input validation)

### Target Coverage
- Backend: 80% line coverage (JaCoCo)
- Frontend: 80% line coverage (Istanbul)
- All batch job patterns tested
- All API endpoints tested

### Test Types Generated
| Type | Tool | Coverage |
|---|---|---|
| Unit tests | JUnit 5 + Mockito | Business logic, utilities |
| Integration tests | Spring Boot Test | Database, repositories, transactions |
| API tests | Spring Test MVC | Controllers, endpoint contracts, error handling |
| Frontend tests | Jasmine + Karma | Components, services, state management |

↓

---

## 🟧 Human Approval Gate 4 — Review Test Coverage

**Gating Criteria:**
- Backend test coverage ≥ 80% (verified by `mvn test -Plocal` + JaCoCo report)
- Frontend test coverage ≥ 80% (verified by `nx test` + Istanbul report)
- All batch job scenarios tested
- All API endpoints have at least one test

**Developer Actions:**
- Run test suite locally
- Review coverage report
- Request additional tests if coverage gaps exist
- Approve when targets met

↓

---

## Stage 5 · Code Review & PR Packaging

**Agents:** `code-reviewer`, `/pr-packager` skill  
**Action:** Review code style, create atomic commits, package Bitbucket PR

### Code Review Checks

| Category | Standard | Tool |
|---|---|---|
| **Formatting** | Project style guide (Checkstyle, ESLint) | Checkstyle, ESLint |
| **Type safety** | No raw types, no `any` in TypeScript | IDE + compilation gate |
| **Security guards** | No hardcoded credentials, safe SQL patterns | Custom lint rules |
| **Reusability** | DRY principle, no unnecessary duplication | Manual review |
| **Documentation** | Public APIs documented, complex logic explained | JavaDoc, TSDoc |

### PR Packaging
- Creates atomic, logical commits (1 feature = 1 commit, or logical sub-features)
- Each commit has clear, meaningful message
- PR description includes:
  - Jira ticket link
  - Summary of changes
  - Testing notes
  - Breaking changes (if any)
  - Links to related documentation

↓

---

## 🟧 Human Approval Gate 5 — Bitbucket PR Review

**Gating Criteria:**
- At least one peer approves the PR
- Security-aware reviewer if changes affect auth, data, or APIs
- CI checks pass (build, tests, lint)
- No force-push to `develop` or `main`

**Reviewers:**
- Peer developer (code quality, correctness)
- Security reviewer (if auth/data/API changes)
- Architecture lead (if schema/API contract changes)

↓

---

## Stage 6 · CI/CD — Build, Test, Deploy

**Trigger:** Bitbucket merge to `develop` branch

**Pipeline Stages:**

| Stage | Action | Gate | Tool |
|---|---|---|---|
| **Compile** | Build backend + frontend | Compilation succeeds | `mvn compile`, `npm run build` |
| **Unit Tests** | Run all unit tests | Coverage ≥ 80%, all tests pass | JUnit 5, Jasmine |
| **Lint** | Style and security checks | No errors (warnings allowed) | Checkstyle, ESLint, SonarQube |
| **Package** | Create deployable artifacts | JAR and Docker image built | Maven, Jib (containerization) |
| **Deploy to DEV** | Deploy to development environment | Kubernetes rollout succeeds | Helm, K3s |
| **Smoke Tests** | Basic functional validation | APIs respond, database connected | Custom test suite |
| **Cluster Health** | Verify cluster state and health | Liveness/readiness probes healthy | Kubernetes probes, custom checks |

### Artifacts
- Spring Boot JAR (backend)
- Angular build output (frontend, SPA)
- Docker image (pushed to registry via Jib)
- Helm release (deployed to K3s `<app>-dev` namespace)

### Health Checks
- `GET /actuator/health` (backend health)
- Frontend service availability
- Database connectivity
- Message queue connectivity (if applicable)

↓

---

## 🟧 Human Approval Gate 6 — DEV Environment Sign-Off

**Gating Criteria:**
- Smoke tests pass
- Cluster health checks pass
- No errors in application logs
- Performance metrics acceptable

**Tech Lead Actions:**
- Review deployment logs
- Verify smoke test results
- Approve promotion to Test environment

↓

---

## ✅ Workflow Complete — Ready for Next Stage

### Checklist

- [x] Unit tests pass · 80%+ coverage confirmed (JaCoCo + Istanbul)
- [x] Security scan complete · zero Critical CVEs · no hardcoded credentials
- [x] Code style checks pass (Checkstyle, ESLint)
- [x] Bitbucket PR merged to `develop`
- [x] Container image built and pushed to registry
- [x] Kubernetes deployment healthy (probes passing)
- [x] DEV environment smoke tests passing
- [x] Tech lead sign-off received

**Next:** Promotion to Test environment (or staging, based on your pipeline)

---

## Agent Autonomy Summary

| Stage | Agent | Human touchpoint | Autonomy level |
|---|---|---|---|
| 0 — Trigger | Developer | Types slash command | Human-initiated |
| 1 — Planning | dev-coordinator | Reviews & approves plan | AI plans, human gates |
| 2 — Implementation | Specialist agents + skills | Reviews generated code | AI implements, human reviews |
| 3 — Security scan | security-auditor (read-only) | Reviews findings, resolves Criticals | AI audits, human fixes |
| 4 — Test generation | qa-engineer + /spec-synthesizer | Reviews coverage report | AI generates, human validates |
| 5 — Code review + PR | code-reviewer + /pr-packager | Reviews Bitbucket PR diff | AI packages, human approves |
| 6 — CI/CD | CI/CD pipeline (automated) | Reviews logs, approves promotion | Fully automated build/deploy, human gates promotion |

---

## Notes for Your Application

1. **Replace placeholder names**: Update agent names, skill names, and command names to match your `.claude/agents/` and `.claude/commands/` directories
2. **Adjust stages**: Your workflow may not need all six stages, or may have additional ones (e.g., compliance review, performance testing)
3. **Update tools and patterns**: Replace references to Spring Boot, Quartz, Angular, etc. with your actual tech stack
4. **Link to your ADRs**: Replace generic "architecture ADRs" with specific links to your `docs/architecture/adr/` files
5. **Customize CVE/security tooling**: Replace Checkstyle/ESLint/SonarQube with tools actually in your pipeline

## Related

- **`README.md`** — Overview and key concepts for the agent workflow folder
- **`docs/guides/`** — How to invoke agents and slash commands
- **`docs/architecture/`** — System design and decision records
- **`.claude/agents/`** — Agent role definitions and tool scopes
- **`.claude/commands/`** — Slash command implementations
