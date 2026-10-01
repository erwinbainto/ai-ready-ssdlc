# Context — Knowledge Connection for <APPLICATION_NAME>

**Purpose:** These documents contain the knowledge Claude Code needs to understand your application: its structure, commands, domain terminology, hazards, and security posture.

**Key Rule:** This knowledge base **cannot be templated**. It must be authored with the team that owns this application. A draft that's never corrected is worse than nothing, because it reads as authoritative.

---

## Files in This Directory

| File | Purpose | Who Completes | When | Effort |
|---|---|---|---|---|
| `architecture.md` | System structure, components, data flow, decisions | Tech Lead + Architects | Week 1 | 2-3h |
| `commands.md` | Available commands & their behavior contracts | Dev Lead | Week 1 | 1h |
| `glossary.md` | Domain terms, acronyms, non-obvious concepts | Domain Expert | Week 1 | 1h |
| `hazards.md` | Known risks, security vulnerabilities, incident history | Security Lead + Team | Week 1-2 | 2h |
| `security-posture.md` | Compliance baseline, authentication, data protection | Security Lead + Team | Week 1-2 | 2-3h |

---

## How to Complete Each File

### 1. `architecture.md` — Application Structure

**Audience:** Architects, senior developers, Claude Code  
**Used by:** All agents, to understand context  
**Update frequency:** When architecture changes

**What to include:**

```markdown
# Architecture — <APPLICATION_NAME>

## What it is
<One paragraph: business purpose, users, value it creates>

## How it fits
<Who calls this app, who does it call, upstream/downstream dependencies>

## Internal structure
<Key components, their responsibilities, how they communicate>
- Component A (Java service): Handles user authentication
- Component B (React frontend): Displays user dashboard
- Component C (PostgreSQL database): Stores user data

## Interfaces
| Interface | Type | Consumers | Contract |
|---|---|---|---|
| `/api/users` | REST | Frontend | `docs/api/users.md` |
| `user-events` | Queue (RabbitMQ) | Analytics service | Async event format |

## Data and state
<What data does this app own, what does it read from others, where state lives>

## Decisions worth knowing
<Architecture decisions explaining why code looks this way>
- ADR-001: Microservices vs monolith → Monolith chosen for startup phase
- ADR-002: React vs Angular → React for smaller bundle size

## Unowned or unclear
<Components whose owner nobody could confirm — name them honestly>
- Legacy payment integration: unmaintained, migration planned for Q4 2026
```

**Example for E-commerce App:**
```markdown
## What it is
Online store where customers browse products, add to cart, and checkout.
Handles payments via Stripe, ships via FedEx integration.

## Internal structure
- Frontend (React): Product catalog, shopping cart UI
- Backend (Node.js): Product API, order service, payment processing
- Database (PostgreSQL): Products, orders, users
- Search (Elasticsearch): Product search index

## Interfaces
| `/api/products` | REST | Frontend + Search indexer | List/detail |
| `/api/orders` | REST | Frontend | Create order, list user's orders |
| `payment-webhook` | HTTPS | Stripe | Payment confirmation |
```

---

### 2. `commands.md` — Available Operations

**Audience:** Team members using Claude Code  
**Used by:** `/help` command, command discovery  
**Update frequency:** When new commands added

**What to include:**

```markdown
# Commands — <APPLICATION_NAME>

Commands available when working in this repository. Reference the enterprise set for 
org-wide commands; only list app-specific ones here.

## Development Commands

### `/build` — Build the application
Runs Maven (backend) and npm (frontend) builds.
- Input: None (or `--clean` to delete artifacts)
- Output: Docker image, deployment manifest
- Fails if: Tests fail, linting errors, type errors

### `/test` — Run all tests
Executes unit + integration tests
- Backend: `mvn test -Plocal`
- Frontend: `npm test`
- Coverage: Must meet 80% threshold

### `/security-scan` — Scan for vulnerabilities
Runs SAST (SonarQube) and dependency check (Snyk)
- Fails if: Critical CVEs found
- Output: Report in `docs/audits/security-scan-v*.md`

## Deployment Commands

### `/deploy-staging` — Deploy to staging environment
- Requires: Dev lead approval
- Triggers: Integration tests, smoke tests
- Rollback: `git revert` if issues found

## Documentation Commands

### `/generate-api-docs` — Generate OpenAPI docs
Creates Swagger/OpenAPI specification from code annotations

---

## Contract Format

Each command must specify:
- **Purpose:** Why does this command exist?
- **Input:** What parameters / options?
- **Output:** What artifact does it create?
- **Preconditions:** What must be true first?
- **Postconditions:** What state changes?
- **Failure modes:** When does it fail?

Example:
```
Command: /build
Purpose: Create deployable Docker images and manifests
Input: (none) or --clean to remove artifacts
Output: backend.tar (Jib Docker image), deployment.yaml (K8s manifest)
Preconditions: Java 21 + Node.js 20 installed; no uncommitted changes
Postconditions: Images tagged with git commit SHA; manifests in deploy/ dir
Fails if: Tests fail, Checkstyle violations, TypeScript errors, CVEs found
```
```

---

### 3. `glossary.md` — Domain Terminology

**Audience:** New team members, developers unfamiliar with domain  
**Used by:** Claude to understand problem space  
**Update frequency:** When domain changes

**What to include:**

```markdown
# Glossary — <APPLICATION_NAME>

Domain-specific terms, acronyms, and concepts that would be misread by an outsider.

## Business Terms

**Invoice**: A record of items sold to a customer, with payment terms
- Related: Line item, tax, discount, payment status
- Not to be confused with: Purchase order (PO)

**Cardholder Data (CHD)**: Payment card information (PAN, CVV, expiration)
- Always encrypted at rest
- Never logged or cached
- Governed by PCI DSS requirements

**Retention Period**: How long an invoice is kept after payment
- Legal requirement: 7 years for tax compliance
- Default: 10 years for historical analysis

## Technical Terms

**MMYY Table Partitioning**: Monthly tables for invoice images
- Each month gets a table: SLT000_INVIMG_202610, SLT000_INVIMG_202611
- Reason: Performance (queries faster on smaller tables)
- Router: `TableNameResolver.toMmyy(date)`

**JDBC Job Store**: Quartz scheduler using database for cluster-safe execution
- Allows multiple servers to run jobs without conflicts
- Requires explicit `PROPAGATION_REQUIRES_NEW` for batch saves
- See `BatchJobSpecialist` agent role

**Chunk-Flush Pattern**: Import large batches by flushing periodic chunks
- Accumulate N records (default 100)
- Call `saveChunk()` with REQUIRES_NEW scope
- Clear batch, continue
- Prevents heap exhaustion on large imports

## Acronyms

| Acronym | Meaning | Context |
|---|---|---|
| PCI DSS | Payment Card Industry Data Security Standard | Compliance, payment handling |
| CHD | Cardholder Data | Payment, encryption, logging |
| MMYY | Month-Year (MM/YY) | Table partitioning, date handling |
| RTO | Recovery Time Objective | Disaster recovery, SLAs |
| RPO | Recovery Point Objective | Backup strategy, data loss tolerance |

## Common Confusions

**Invoice vs. PO**: 
- Invoice: Seller → Buyer (we send this)
- Purchase Order (PO): Buyer → Seller (we receive this)

**Charged vs. Paid**:
- Charged: Attempted payment (may fail)
- Paid: Payment succeeded and cleared

**Archived vs. Purged**:
- Archived: Moved to backup storage, still queryable
- Purged: Deleted permanently, cannot recover
```

---

### 4. `hazards.md` — Known Risks & Incident History

**Audience:** All developers (MUST read before changes)  
**Used by:** Code review, architecture decisions  
**Update frequency:** After incidents, when risks discovered

**What to include:**

```markdown
# Hazards — <APPLICATION_NAME>

Fragile areas, incident history, high blast radius issues. **Read before proposing changes here.**

## Security Hazards — High Risk Areas

| Vulnerability | Path | Why Critical | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| SQL injection in search | `src/invoice/SearchService.java` | Dynamic query building | Full DB compromise | Parameterized queries | Mitigated |
| Missing auth on export | `src/api/ExportController.java` | Anyone can export all invoices | Data breach | Enforce OAuth 2.0 check | Open |
| Hardcoded API keys | `src/config/RabbitMQ.java` | Exposed in git history | Service compromise | Use Secrets Manager | Mitigated |

## Do Not Touch Without Review

| Area | Path | Why | Who to Ask |
|---|---|---|---|
| Payment processing | `src/payment/*` | Handles CHD; PCI compliance required | Payment team lead |
| Batch import logic | `src/jobs/ImportJob.java` | Performance-critical; tuned for cluster | Batch-job-specialist agent |
| User authentication | `src/auth/*` | Security-critical; changes affect all users | Security lead |

## Incident History

| What Happened | Area | When | Lesson |
|---|---|---|---|
| Brute force attack on login | `src/auth/LoginController.java` | 2026-09-15 | Rate limiting must be enforced; always test with load |
| Backup found unencrypted | `infrastructure/backup.yaml` | 2026-08-20 | All backups must be encrypted; add to deployment checks |
| Database timeout in batch job | `src/jobs/ImportJob.java` | 2026-07-10 | Chunk size tuned too high; reduced from 1000 to 100 items |

## Surprising Behaviour

Things that work unexpectedly:

- **Session caching:** User sessions cached in-memory for 5 minutes. Database changes don't immediately reflect. Cache invalidates on logout or timeout.
- **Batch job hangs:** If import takes > 30 minutes, Quartz may interrupt it. Monitor `JOB_EXECUTION_LOG` for status.
- **Rate limiting bypass:** Same IP but different user agent bypasses rate limit (known issue; on roadmap for Q4 2026).

## Known Technical Debt

| Debt | Area | Why Accepted | Remediation Plan | Owner | Target |
|---|---|---|---|---|---|
| Legacy auth has no MFA | `src/auth/` | Migrating to OAuth; MFA post-migration | Complete OAuth migration (Q4 2026) | Auth Team | 2026-12-31 |
| Payment processor API v1 (deprecated) | `src/payment/Stripe.java` | v2 requires schema changes; low priority | Upgrade to Stripe API v2 | Payments Team | 2026-11-30 |

---

## Security Review Checklist

Before proposing changes to hazard areas:

- [ ] I've read this entire hazards document
- [ ] I understand the security implications
- [ ] I've consulted with the "Who to Ask" owner
- [ ] My changes maintain or improve current mitigations
- [ ] I've included tests verifying the control works
```

---

### 5. `security-posture.md` — Compliance & Security Baseline

**Audience:** Security leads, compliance officers, architects  
**Used by:** Compliance audits, incident response, security reviews  
**Update frequency:** Quarterly or after compliance changes

**See:** `docs/security/security-posture.md` for full template and examples.

---

## Workflow: Completing Context as a Team

### Week 1: Essentials

**Day 1:**
- [ ] Tech lead drafts `architecture.md` (skeleton)
- [ ] Dev lead creates `commands.md` template

**Day 2-3:**
- [ ] Architects review + correct `architecture.md`
- [ ] Team reviews + finalizes `commands.md`

**Day 4:**
- [ ] Domain expert drafts `glossary.md`
- [ ] Team reviews glossary

### Week 2: Security & Hazards

**Day 5-6:**
- [ ] Security lead drafts `security-posture.md`
- [ ] Dev lead + security lead review together

**Day 7-8:**
- [ ] Team reviews `hazards.md` together
- [ ] Document existing risks, incidents, debt

**Day 9:**
- [ ] Final review by tech lead + security lead
- [ ] Sign-off and commitment to maintain

---

## Maintenance & Updates

### Quarterly Review

- [ ] Architecture still accurate? (Update if changed)
- [ ] Commands all documented? (Add any new ones)
- [ ] Glossary up to date? (Add new terms)
- [ ] Hazards section current? (New risks, resolved incidents)
- [ ] Security posture verified? (Compliance controls still working)

### After Major Events

| Event | Action |
|---|---|
| Architecture change | Update `architecture.md` + ADR |
| New compliance requirement | Update `security-posture.md` |
| Security incident | Update `hazards.md` + incident-response doc |
| New command available | Update `commands.md` |
| Term misunderstood in PR review | Add to `glossary.md` |

---

## Cross-References

These documents reference each other:

- **`architecture.md`** → links to ADRs in `docs/architecture/adr/`
- **`security-posture.md`** → links to `docs/security/threat-model.md` for details
- **`hazards.md`** → references `security-guardrails.md` for controls
- **`commands.md`** → references enterprise set for org-wide commands

---

## Quality Checks

Before considering context complete:

- [ ] **Completeness:** No `<LIKE_THIS>` placeholders remain
- [ ] **Accuracy:** Verified against actual code/config (not from memory)
- [ ] **Clarity:** A new team member could read and understand
- [ ] **Maintenance:** Review schedule documented
- [ ] **Ownership:** Each document has a named owner
- [ ] **Sign-off:** Tech lead + security lead have approved

---

## Getting Help

| Question | Answer |
|---|---|
| How much detail in `architecture.md`? | Enough for a new senior eng to navigate; not exhaustive |
| Should `glossary.md` include general tech terms? | No, only domain-specific terms; save general stuff for Google |
| How often update `commands.md`? | When a command changes or new one added; at least quarterly |
| Who approves `security-posture.md`? | Security lead (you should get their explicit sign-off) |
| Can I copy from wiki/Confluence? | Yes, but verify it's current; prefer single source of truth |

---

**Maintained by:** <Tech Lead / Platform Team>  
**Last updated:** <YYYY-MM-DD>  
**Next review:** <YYYY-MM-DD>
