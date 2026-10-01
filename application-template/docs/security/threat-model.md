# Threat Model — <APPLICATION_NAME>

**Purpose:** Identify what this application is protecting, who might attack it, and how. Used to prioritize security investments and validate controls.

**Last Updated:** <YYYY-MM-DD>  
**Owner:** <Security Lead>  
**Review Frequency:** Quarterly or after major architecture changes

---

## 1. Assets — What We're Protecting

List the valuable assets this application owns or manages.

| Asset | Type | Value | Owner |
|---|---|---|---|
| User credentials | Data | High | Authentication team |
| User PII (email, name) | Data | High | Data privacy team |
| Payment information | Data | Critical | Compliance team |
| API keys (third-party) | Secrets | High | DevOps team |
| Transaction logs | Data | Medium | Audit team |
| Application availability | Service | Medium | Platform team |

**How to fill:**
- **Asset**: What data or service is valuable?
- **Type**: Data / Secrets / Service / Infrastructure / Reputation
- **Value**: Critical / High / Medium / Low
- **Owner**: Who is accountable for protecting it?

**Example for Payment Processing App:**
| Cardholder data (PAN, CVV) | Data | Critical | Payments team |
| Customer transaction history | Data | High | Compliance |
| Internal audit logs | Data | Medium | Security team |
| API uptime | Service | High | Platform team |

---

## 2. Data Flow — How Assets Move

Diagram or describe how data flows through the system.

```
[User Client] 
    → HTTPS → 
[API Gateway (TLS termination)]
    → Internal network → 
[Backend Service (Java)]
    → Encrypted connection → 
[Database (AES-256 encryption)]
    ↓
[Backup storage (S3, encrypted)]
```

**Critical flows to highlight:**
- Where is user input accepted?
- Where is data encrypted?
- Where is data logged?
- What external systems are called?

---

## 3. Threat Landscape — Who/What Might Attack

### External Threats

| Threat | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|
| <threat> | <Low/Med/High> | <Low/Med/High> | <control> | <Open/Mitigated> |

**Common external threats:**
- Credential stuffing (leaked password databases)
- SQL injection via API
- Malicious API clients (bots, scrapers)
- Third-party compromise (payment processor, auth provider)
- Network interception (man-in-the-middle)
- Ransomware via compromised dependencies

**Example:**
| Credential stuffing attacks on login | High | Medium | Rate limiting (5 attempts/min per IP) | Mitigated |
| SQL injection in search | Medium | Critical | Parameterized queries + SAST | Mitigated |
| Dependency compromise | Low | Critical | Vulnerability scanning + version pinning | Mitigated |
| Payment processor breach | Very Low | Critical | PCI DSS compliance + tokenization | Mitigated |

### Internal Threats

| Threat | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|
| <threat> | <Low/Med/High> | <Low/Med/High> | <control> | <Open/Mitigated> |

**Common internal threats:**
- Insider with production access (disgruntled employee)
- Accidental credential exposure in logs
- Unencrypted backup files on shared storage
- Temporary security exceptions left in place too long
- Development/test database with production data

**Example:**
| Admin keys left in unencrypted backup | Medium | Critical | Automated backup encryption + rotation | Planned (due 2026-10-15) |
| Production data in dev database | High | High | Anonymization of dev data | Mitigated |
| Secrets in git history | Low | High | Secret scanning + pre-commit hooks | Mitigated |

---

## 4. Attack Vectors — How Could They Attack

Describe the most likely attack paths.

### Vector 1: Credential Compromise

**Attack Path:**
1. Attacker obtains user password (phishing, credential stuffing, breach)
2. Attempts login via `/api/auth/login`
3. If successful, gains access to user data and API

**Likelihood:** High (credentials are commonly breached)  
**Impact:** User account takeover, data access, fraud  
**Current Mitigations:**
- MFA (multi-factor authentication): <YES/NO>
- Rate limiting on login: <YES/NO>
- Unusual activity detection: <YES/NO>

**Additional Controls Needed:**
- [ ] Implement MFA (SMS or authenticator app)
- [ ] Add login anomaly detection (unusual location/device)
- [ ] Require password reset every 90 days

---

### Vector 2: SQL Injection

**Attack Path:**
1. Attacker crafts malicious input (e.g., `'; DROP TABLE users; --`)
2. Input is concatenated into SQL query (dynamic query building)
3. Query executes attacker's commands

**Likelihood:** Medium (if queries are not parameterized)  
**Impact:** Database compromise, data theft, data loss  
**Current Mitigations:**
- [ ] Parameterized queries: <YES/NO>
- [ ] SAST scanning for SQL injection: <YES/NO>
- [ ] SQL Server parameter limit (2100): <YES/NO>

**Example (Vulnerable):**
```java
String query = "SELECT * FROM users WHERE email = '" + userInput + "'";
// Attacker input: ' OR '1'='1
// Result: SELECT * FROM users WHERE email = '' OR '1'='1'  ← returns all users!
```

---

### Vector 3: API Abuse / Scraping

**Attack Path:**
1. Attacker discovers API endpoint (e.g., `/api/users/{id}`)
2. Writes automated script to enumerate user IDs (1, 2, 3, ...)
3. Extracts all user data, emails, phone numbers

**Likelihood:** High (APIs are discoverable)  
**Impact:** Data breach, user privacy violation  
**Current Mitigations:**
- Rate limiting: <YES/NO>
- API key authentication: <YES/NO>
- Pagination limits: <YES/NO>

**Controls Needed:**
- [ ] Implement rate limiting (e.g., 100 requests/minute per user)
- [ ] Add request throttling after suspicious activity
- [ ] Log and alert on enumeration attempts

---

### Vector 4: Insecure Dependency

**Attack Path:**
1. Your app includes an npm package with a known vulnerability (e.g., RCE)
2. Attacker exploits the vulnerability when the app loads that package
3. Attacker executes arbitrary code on your server

**Likelihood:** Low-Medium (depends on dependency update practices)  
**Impact:** Complete system compromise  
**Current Mitigations:**
- [ ] Dependency scanning enabled: <YES/NO>
- [ ] Automated updates: <YES/NO>
- [ ] CVE alerts: <YES/NO>

**Controls in Place:**
- CI/CD fails if critical CVE found (Snyk / Dependabot)
- Weekly dependency update check
- Patch schedule: Critical (48h), High (1 week), Medium (2 weeks)

---

### Vector 5: Unauthorized Data Access

**Attack Path:**
1. Attacker gains API credentials (stolen, intercepted, or default)
2. Attempts to access resources they shouldn't (e.g., another user's data)
3. If authorization checks are weak, succeeds

**Likelihood:** Medium (depends on RBAC implementation)  
**Impact:** Data breach, privacy violation  
**Current Mitigations:**
- [ ] RBAC enforcement: <YES/NO>
- [ ] API authorization checks: <YES/NO>
- [ ] Audit logging of data access: <YES/NO>

**Example (Vulnerable):**
```java
// ❌ WRONG — no authorization check
@GetMapping("/api/invoices/{id}")
public Invoice getInvoice(@PathVariable int id) {
    return invoiceService.findById(id);  // Any user can fetch any invoice!
}

// ✅ RIGHT — authorization check
@GetMapping("/api/invoices/{id}")
public Invoice getInvoice(@PathVariable int id, @AuthenticationPrincipal User user) {
    Invoice invoice = invoiceService.findById(id);
    if (!invoice.getOwnerId().equals(user.getId())) {
        throw new AccessDeniedException("Not authorized");
    }
    return invoice;
}
```

---

## 5. Attack Surface — Where Can They Attack

Document all points where external input enters the system.

### Public Endpoints (No Authentication Required)

| Endpoint | Input Type | Validation | Notes |
|---|---|---|---|
| `GET /health` | None | N/A | Health check, safe |
| `POST /api/auth/login` | JSON (email, password) | Email format, length limits | Rate limited |
| `POST /api/auth/register` | JSON (email, password, name) | Email, password strength | Duplicate check |
| `GET /api/public/{id}` | URL param (ID) | Numeric, range check | Returns public data |

### Authenticated Endpoints (Authentication Required)

| Endpoint | Input Type | Authorization | Validation |
|---|---|---|---|
| `GET /api/users/{id}` | URL param (ID) | User can only access own | ID format validation |
| `POST /api/invoices` | JSON (data) | Admin or owner | Schema validation |
| `PUT /api/settings` | JSON (settings) | User can modify own | Type checking |

### External Integrations

| System | Direction | Auth | Data | Risk |
|---|---|---|---|---|
| Payment Processor | Outbound | API key (stored in Vault) | Payment tokens | Key exposure |
| Email Service (SendGrid) | Outbound | API key (stored in Vault) | User email addresses | Spam vector |
| Analytics (Mixpanel) | Outbound | Credentials | Event data, user IDs | Privacy |

---

## 6. Sensitive Operations

List operations that have high security impact if abused.

| Operation | Who Can Trigger | Required Checks | Logging |
|---|---|---|---|
| Delete user account | User (own) or Admin | MFA confirmation | Yes, immutable log |
| Export all data | Admin | Admin auth + reason | Yes, with reason |
| Modify user role | Admin | Admin auth + approval | Yes, by whom |
| Reset admin password | Super-admin | 2FA + callback | Yes, immutable log |

---

## 7. Compliance & Regulatory Threats

If applicable, add threats from compliance frameworks.

### PCI DSS (If Handling Payment Data)

- **Threat:** Cardholder data exposure
  - **Attack Vector:** SQL injection, insecure API, unencrypted backup
  - **Likelihood:** Medium
  - **Impact:** Critical (breach notification, fines, reputation)
  - **Mitigation:** Tokenization, encryption, PCI assessment

### GDPR (If Processing EU Personal Data)

- **Threat:** Unauthorized access to EU resident data
  - **Attack Vector:** Credential compromise, insider access
  - **Likelihood:** Medium
  - **Impact:** High (fines up to 4% of revenue)
  - **Mitigation:** Access controls, encryption, data minimization

### HIPAA (If Handling Health Data)

- **Threat:** Unauthorized disclosure of PHI (Protected Health Information)
  - **Attack Vector:** Insecure API, unencrypted transmission
  - **Likelihood:** Medium
  - **Impact:** Critical (fines, loss of license)
  - **Mitigation:** Encryption, audit logging, access controls

---

## 8. Risk Rating Matrix

Prioritize threats by likelihood × impact:

```
IMPACT
   ^
   |  [RED] Critical        [ORANGE] High
   |  - Vector 3 (SQL)      - Vector 1 (Credentials)
   |  - Vector 5 (Authz)    - Vector 4 (Dependency)
   |
   |  [YELLOW] Medium       [GREEN] Low
   |  - Vector 2 (Scraping)
   |
   +-----------------------------------> LIKELIHOOD
```

**Action:**
- **RED (Critical):** Address immediately (within 1 week)
- **ORANGE (High):** Address within 2 weeks
- **YELLOW (Medium):** Address within 1 month
- **GREEN (Low):** Address within 3 months

---

## 9. Control Validation

How do we verify that mitigations are actually in place?

| Control | How Verified | Frequency | Last Verified |
|---|---|---|---|
| Parameterized queries | Code review + SAST | Every PR | <YYYY-MM-DD> |
| Rate limiting | Load test, monitoring | Quarterly | <YYYY-MM-DD> |
| Encryption at rest | Config audit | Quarterly | <YYYY-MM-DD> |
| Audit logging | Log audit trail | Monthly | <YYYY-MM-DD> |
| Dependency scanning | CI/CD pipeline | Every commit | <YYYY-MM-DD> |

---

## 10. Residual Risk Statement

After all mitigations, what risks remain? Which are accepted?

| Threat | Residual Risk | Reason Accepted | Owner | Review Date |
|---|---|---|---|---|
| Third-party compromise | Low | Can't control third parties; encrypted data limits impact | CTO | 2026-12-31 |
| Insider threat | Low | Background checks + access controls | Security Lead | 2026-12-31 |

---

## References

- **Compliance Mapping:** `docs/security/compliance-mapping.md`
- **Incident Response:** `docs/security/incident-response.md`
- **Security Guardrails:** `.claude/rules/security-guardrails.md`
- **Security Posture:** `.claude/context/security-posture.md`
- **Hazards:** `.claude/context/hazards.md`

---

## Sign-Off

| Role | Name | Date | Notes |
|---|---|---|---|
| Security Lead | <name> | <YYYY-MM-DD> | Threat landscape reviewed |
| Dev Lead | <name> | <YYYY-MM-DD> | Mitigations confirmed in place |
| Architect | <name> | <YYYY-MM-DD> | Architecture reflects threat model |

**Next Review Date:** <YYYY-MM-DD> (quarterly or after major changes)
