# Application Template — Secure SDLC Harness

**Tier 3 application-specific configuration** for the AI-Ready Secure Software Development Lifecycle (SSDLC) harness.

Copy this directory into each application repository and complete it per the checklists below. One copy per application.

---

## Directory Structure

```
<app-repo>/
├── CLAUDE.md                        # Application instructions (extends enterprise set)
├── .mcp.json                        # MCP servers (admitted catalogue only)
├── .worktreeinclude                 # Untracked build artifacts
│
├── .claude/
│   ├── settings.json                # Permissions (narrowed, never looser)
│   ├── settings.local.json          # Local development overrides
│   │
│   ├── context/
│   │   ├── README.md                # [NEW] How to complete context documents
│   │   ├── architecture.md          # App structure, components, decisions
│   │   ├── commands.md              # Available commands & contracts
│   │   ├── glossary.md              # Domain terminology
│   │   ├── hazards.md               # Known risks, incident history, debt
│   │   └── security-posture.md      # [NEW] Compliance baseline, auth, data classification
│   │
│   ├── rules/
│   │   ├── README.md                # [NEW] How to create app-specific rules
│   │   ├── 10-app.md                # App-specific conventions & guardrails
│   │   └── security-guardrails.md   # [NEW] Mandatory security rules
│   │
│   ├── hooks/
│   │   ├── README.md                # [NEW] How to wire and test hooks
│   │   └── [lifecycle-hooks]        # session-start, pre-tool-use, etc.
│   │
│   ├── agents/                      # App-specific agent roles (usually empty)
│   ├── skills/                      # App-specific skills (usually empty)
│   └── (evals/ reserved below)      # ↓
│
├── evals/                           # [FUTURE] Skill validation gates (WP2/D11)
│   ├── README.md                    # When and how to use evals for skill publication
│   └── [empty until skills ready]   # Each skill gets: <skill-name>/prompt.md + graders.md
│
└── docs/
    ├── architecture/
    │   ├── README.md
    │   └── adr/                     # Architectural Decision Records
    │
    ├── security/                    # [NEW] Security documentation
    │   ├── README.md                # Navigation guide for security docs
    │   ├── threat-model.md          # App threat landscape
    │   ├── compliance-mapping.md    # PCI/NIST/ISO controls → implementation
    │   └── incident-response.md     # Incident procedures & escalation
    │
    ├── specs/
    │   └── README.md
    │
    ├── guides/
    │   └── README.md
    │
    ├── testing/
    │   └── README.md
    │
    ├── audits/                      # Compliance & security audit logs
    │   └── README.md
    │
    └── agent-workflow/
        └── README.md
```

---

## Deployment Checklist

**Prerequisite:** Enterprise plugin installed and version recorded  
**Owner:** Dev Lead + Tech Lead  
**Duration:** 2-4 hours  

### Phase 1: Essentials (Complete First)

- [ ] **Record enterprise plugin version** in `.claude/settings.json` → `enterpriseVersion: "x.y.z"`
- [ ] **Copy this directory** to app repo root
- [ ] **Rename placeholders:**
  - `<APPLICATION_NAME>` → actual app name (in `.claude/context/`, `docs/`, `CLAUDE.md`)
  - `<STACK>` → languages/frameworks in use (Java, Node.js, React, etc.)
- [ ] **Review and complete** `docs/guides/context/README.md` — instructions for completing knowledge base
- [ ] **Author** `.claude/context/architecture.md` with tech lead (cannot be templated)

### Phase 2: Security & Compliance

- [ ] **Complete** `.claude/context/security-posture.md` with security lead
  - Check PCI DSS applicability
  - Define authentication method
  - Classify data types
  - Document known risks
- [ ] **Customize** `.claude/rules/security-guardrails.md` for your tech stack
  - Add language-specific security patterns
  - Tighten controls based on threat model
- [ ] **Define** `docs/security/threat-model.md` with architects
  - Identify assets
  - List threats by STRIDE / kill chain
  - Validate mitigations
- [ ] **Map compliance** in `docs/security/compliance-mapping.md`
  - PCI DSS requirements → implementation
  - NIST CSF controls → code/config locations
- [ ] **Prepare** `docs/security/incident-response.md`
  - Define escalation matrix
  - Identify on-call contacts

### Phase 3: Rules & Conventions

- [ ] **Read** `docs/guides/rules/README.md` — guidelines for app-specific rules
- [ ] **Customize** `.claude/rules/10-app.md` with team conventions
- [ ] **Review** `.claude/context/hazards.md` — document known fragile areas
  - Security hazards (high-risk code paths)
  - Incident history (lessons learned)
  - Known technical debt

### Phase 4: Integration

- [ ] **Configure hooks** in `.claude/hooks/` and wire in `settings.json`
  - Read `docs/guides/hooks/README.md` for hook lifecycle
  - Copy/create hooks from enterprise set as needed
- [ ] **Bind MCP servers** in `.mcp.json` (admitted catalogue only)
- [ ] **Narrow permissions** in `.claude/settings.json`
  - Start with enterprise defaults
  - Make stricter for this app if needed (never looser)
- [ ] **Define commands** in `.claude/context/commands.md` — what can team members invoke?

### Phase 5: Verification

- [ ] **Run verification** from parent directory (`../VERIFY.md`)
  - Check `/status` shows enterprise source
  - Verify `/mcp` lists only admitted servers
  - Test `/context` loads enterprise + app docs
- [ ] **Test write boundary:** Attempt a file edit
  - Capture the refusal message (proves read-only boundary holds)
  - Save as evidence: `docs/audits/write-boundary-test-v1.md`
- [ ] **Team sign-off:** Dev lead + security lead confirm setup

### Phase 6: Future Skills (WP2/D11)

- [ ] **Reserve `evals/` directory** — already created, empty until skills are ready
  - When you author app-specific skills in `.claude/skills/`, you'll validate them here
  - See `evals/README.md` for the publication pattern
  - For now, this phase is blocked on "Capability candidates" logging (Phase 7 monitoring)

---

## How to Complete Each Section

### `.claude/context/` — Knowledge Connection

**Start here:** See `docs/guides/context/README.md` for detailed instructions.

| File | Audience | Effort | How to Complete |
|---|---|---|---|
| `architecture.md` | Architects, devs | 2-3h | Author with tech lead; describe system structure, data flow, key decisions |
| `commands.md` | All team | 1h | List commands available (reference enterprise set; add app-specific ones) |
| `glossary.md` | New team members | 1h | Define domain terms, acronyms, non-obvious concepts |
| `hazards.md` | All team | 2h | Identify security risks, incident history, fragile areas |
| `security-posture.md` | Security lead + team | 2-3h | Document compliance baseline, authentication, data protection |

### `.claude/rules/` — Enforced Standards

**Start here:** See `docs/guides/rules/README.md` for detailed instructions.

| File | Scope | How to Complete |
|---|---|---|
| `10-app.md` | Narrower than enterprise | Add app-specific conventions (naming, patterns, anti-patterns) |
| `security-guardrails.md` | Stack & threat-specific | Customize mandatory security rules for your tech stack |

### `.claude/hooks/` — Lifecycle Automation

**Start here:** See `docs/guides/hooks/README.md` for detailed instructions.

| Hook | Purpose | When Configured |
|---|---|---|
| `session-start.sh` | Runs when Claude Code starts | Optional; useful for setup checks |
| `pre-tool-use.sh` | Runs before tools execute | Optional; used for permission gates |
| `*-approved.sh` | Post-approval | Optional; automation after human approval |

---

## Key Principles

### 1. Reference, Never Copy

Enterprise rules and policies are versioned. Copy only what's truly app-specific.

```markdown
❌ WRONG (duplicates enterprise):
- This app follows the enterprise security standard

✅ RIGHT (references):
- See @enterprise/rules/secure-coding.md for org-wide standards
```

### 2. Permissions: Narrow, Never Widen

App settings cannot be looser than enterprise.

```json
{
  "enterpriseVersion": "0.1.0",
  "permissionMode": "read",
  "toolAllowlist": ["Read", "Bash", "Edit"]
  // Never add tools not in enterprise allowlist
}
```

### 3. Placeholders: Complete All

Every `<LIKE_THIS>` must be filled before deployment.

```markdown
❌ DRAFT (has placeholders):
- Owner: <name>
- Compliance status: <PCI DSS: YES/NO>

✅ READY (all filled):
- Owner: Jane Smith
- Compliance status: PCI DSS: YES
```

### 4. Security: Document & Validate

All security controls must be documented AND verified in place.

```markdown
Control: "Rate limiting on login endpoint"
Evidence: src/auth/LoginController.java:line 42 (RateLimiter annotation)
Status: ✅ Implemented and tested
```

---

## Completion Examples

### Example 1: Fintech Application (PCI DSS)

**`.claude/context/security-posture.md`:**
```
Compliance Requirements: PCI DSS YES
Authentication: OAuth 2.0 via AWS Cognito
Data Classification: Payment data → Tokenized (PCI compliant), User PII → AES-256 encrypted
Known Risks: 
  - SQL injection in search → Parameterized queries + SAST
  - Credential stuffing → Rate limiting (5 attempts/min)
```

**`.claude/rules/security-guardrails.md`:**
```
[Customize for Java/Spring Boot]
- All DB queries must use PreparedStatement
- No hardcoded passwords (use AWS Secrets Manager)
- All payment endpoints require MFA
```

### Example 2: Healthcare Application (HIPAA)

**`.claude/context/security-posture.md`:**
```
Compliance Requirements: HIPAA YES
Authentication: SAML 2.0 via corporate IdP
Data Classification: PHI (Protected Health Information) → AES-256 + FIPS 140-2 keys
Audit Requirements: All PHI access logged to immutable SIEM
```

**`.claude/rules/security-guardrails.md`:**
```
[Customize for Python/Django]
- No PHI in logs or error messages
- Encryption enforced for all patient data
- HIPAA-required audit trail enabled
```

---

## Maintenance & Updates

### Quarterly Reviews

- [ ] `.claude/context/hazards.md` — any new incidents?
- [ ] `docs/security/threat-model.md` — architecture changed?
- [ ] `docs/security/compliance-mapping.md` — frameworks updated?

### After Major Changes

- [ ] App architecture changes → update `architecture.md`
- [ ] New compliance requirement → update `security-posture.md`
- [ ] Security incident → update `incident-response.md` + `hazards.md`
- [ ] Enterprise plugin upgraded → verify compatibility

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| CLAUDE.md file isn't loading | Malformed YAML frontmatter | Validate YAML syntax, check for unclosed blocks |
| Rules not applying | Path glob doesn't match files | Test glob with `find . -path <glob>` |
| Security guardrails not enforcing | Missing pre-tool-use hook | Wire hook in `settings.json` + test |
| Context docs not accessible | Not in `.claude/` directory | Verify path is `.claude/context/filename.md` |

---

## Related Documentation

- **Enterprise Set:** `@enterprise/` — organization-wide policies, agents, skills, rules
- **Enterprise Evals:** `@enterprise/evals/` — example skill validation suites (vuln-patch-triage, etc.)
- **Deployment Guide:** `../DEPLOYMENT_GUIDE.md` — step-by-step deployment procedures
- **Verification:** `../VERIFY.md` — post-deployment verification checklist
- **Forms:** `../D4_*_Form.md` — questionnaires that drive harness generation
- **Application Evals:** `evals/README.md` — when to create skill evaluation suites (WP2/D11 phase)

---

## Getting Help

| Question | Reference |
|---|---|
| How do I complete `.claude/context/`? | See `docs/guides/context/README.md` |
| What security rules should I add? | See `docs/guides/rules/README.md` |
| How do hooks work? | See `docs/guides/hooks/README.md` |
| How do I document compliance? | See `docs/security/README.md` |
| What's the deployment process? | See `../DEPLOYMENT_GUIDE.md` |
| When do I use evals? | See `evals/README.md` (future phase: WP2/D11 skill publication) |
| How do I publish a skill? | See `evals/README.md` + `D4_Application_Harness_Form.md` § 7 |

---

**Last Updated:** 2026-10-01  
**Version:** 1.0  
**Maintained by:** Platform / Security Team
