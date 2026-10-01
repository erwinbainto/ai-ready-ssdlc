# Context — Knowledge Connection Guide

**Full detailed guide for completing `.claude/context/` files.**

For the quick reference in `.claude/context/`, see the actual files:
- `CLAUDE.md:context` — Auto-loaded by Claude Code
- `architecture.md` — System structure
- `commands.md` — Available commands
- `glossary.md` — Domain terminology
- `hazards.md` — Known risks and incidents
- `security-posture.md` — Compliance baseline

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

## Interfaces

| Interface | Type | Consumers | Details |
|---|---|---|---|
| `/api/users` | REST | Frontend | `docs/api/users.md` |

## Key Decisions

| Area | Chosen | Why | Record |
|---|---|---|---|
| Architecture | Monolith | Startup phase | `docs/architecture/adr/ADR-001.md` |

## Unowned or unclear

- <component>: <status>
```

**Example for E-commerce App:**
```markdown
## What it is
Online store where customers browse products, add to cart, and checkout.

## Internal structure

| Component | Technology | Responsibility |
|---|---|---|
| Frontend | React | Product catalog, shopping cart UI |
| Backend | Node.js | Product API, order service |
| Database | PostgreSQL | Products, orders, users |
```

---

### 2. `commands.md` — Available Operations

**Audience:** Team members using Claude Code  
**Used by:** `/help` command, command discovery  
**Update frequency:** When new commands added

**What to include:**

```markdown
| Purpose | Command | Input | Output | Fails If |
|---|---|---|---|---|
| Build | `/<name>` | <params> | <result> | <conditions> |
| Test | `/<name>` | <params> | <result> | <conditions> |
```

**Currently failing:** <list, or "none">

**Manual verification by:** <role, if command unavailable>

---

### 3. `glossary.md` — Domain Terminology

**Audience:** New team members, developers unfamiliar with domain  
**Used by:** Claude to understand problem space  
**Update frequency:** When domain changes

**What to include:**

```markdown
## Business Terms

| Term | Means Here | Does NOT Mean |
|---|---|---|
| Invoice | Record of items sold to customer | Purchase order (PO) |

## Technical Terms

| Term | Definition | Used In |
|---|---|---|
| MMYY partitioning | Monthly tables for performance | Table routing |

## Acronyms

| Acronym | Meaning | Used In |
|---|---|---|
| CHD | Cardholder Data | Payment handling |
```

---

### 4. `hazards.md` — Known Risks & Incident History

**Audience:** All developers (MUST read before changes)  
**Used by:** Code review, architecture decisions  
**Update frequency:** After incidents, when risks discovered

**What to include:**

```markdown
## Security Hazards

| Vulnerability | Path | Why Critical | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| SQL injection | `src/search` | Dynamic query building | Data breach | Parameterized queries | Mitigated |

## Do Not Touch Without Review

| Area | Path | Why | Owner |
|---|---|---|---|
| Payment processing | `src/payment/*` | PCI compliance | Payment Lead |

## Incident History

| What Happened | Area | When | Lesson |
|---|---|---|---|
| Brute force attack | `src/auth/LoginController.java` | 2026-09-15 | Rate limiting required |

## Surprising Behaviour

- User sessions cached 5 minutes; database changes don't reflect immediately
```

---

### 5. `security-posture.md` — Compliance & Security Baseline

**Audience:** Security leads, compliance officers, architects  
**Used by:** Compliance audits, incident response, security reviews  
**Update frequency:** Quarterly or after compliance changes

**What to include:**

```markdown
## Compliance Requirements

| Framework | Required | Mapping | Owner |
|---|---|---|---|
| PCI DSS | YES | `docs/security/compliance-mapping.md` | Jane Smith |

## Authentication & Authorization

| Aspect | Value |
|---|---|
| Method | OAuth 2.0 |
| Provider | AWS Cognito |

## Data Classification

| Data Type | Classification | Storage | Encryption | Retention |
|---|---|---|---|---|
| User credentials | Confidential | Encrypted DB | AES-256 | 7 years |

## Known Security Risks

| Risk | Level | Impact | Mitigation | Status | Owner | Target |
|---|---|---|---|---|---|---|
| SQL injection | High | Data breach | Parameterized queries | Mitigated | Bob | N/A |
```

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

---

## Cross-References

These documents reference each other and docs/:

- **`architecture.md`** → links to ADRs in `docs/architecture/adr/`
- **`security-posture.md`** → links to `docs/security/threat-model.md`
- **`hazards.md`** → references `.claude/rules/security-guardrails.md`
- **`commands.md`** → references `docs/commands/`

---

## Quality Checks

Before considering context complete:

- [ ] **Completeness:** No `<LIKE_THIS>` placeholders remain
- [ ] **Accuracy:** Verified against actual code/config
- [ ] **Clarity:** New senior eng could understand
- [ ] **Maintenance:** Review schedule documented
- [ ] **Ownership:** Each document has named owner
- [ ] **Sign-off:** Tech lead + security lead approved

---

**Maintained by:** <Tech Lead / Platform Team>  
**Last updated:** <YYYY-MM-DD>  
**Next review:** <YYYY-MM-DD>
