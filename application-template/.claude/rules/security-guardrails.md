---
description: Security guardrails and mandatory controls for this application
paths: ["src/**", "backend/**", "frontend/**", ".github/**"]
---

# Security Guardrails — <APPLICATION_NAME>

Enforced rules preventing common vulnerabilities. These are narrower than enterprise rules and specific to this application's tech stack and threat model.

**Last Updated:** <YYYY-MM-DD>  
**Owner:** <Security Lead / Dev Lead>  
**Review Frequency:** Quarterly

---

## Secrets Management — MANDATORY

**Rule:** Never commit credentials, API keys, tokens, or private keys to the repository.

**What to flag:**
- Hardcoded connection strings: `password=`, `secret=`, `key=`
- AWS/Azure credentials: `AKIA`, `AZURE_`, `AWS_SECRET`
- Private keys: `.pem`, `.key`, `.pfx` files
- Cognito/OAuth secrets: `client_secret`, `JWKS_URI`
- Database passwords in code

**Enforcement:**
- [ ] Pre-commit hooks scan for secrets (use `git-secrets` or `truffleHog`)
- [ ] CI/CD pipeline blocks commits containing secrets
- [ ] Secret scanning enabled in repo (GitHub / GitLab / Bitbucket)

**If found:**
1. Immediately rotate the exposed secret
2. Remove from git history (use `git filter-branch` or `BFG`)
3. Document in incident log: `docs/security/incident-response.md`
4. Post-mortem: why did this slip through?

**Example:**
```bash
# ❌ WRONG — hardcoded password
db.connection("jdbc:mysql://localhost/app?password=secret123");

# ✅ RIGHT — environment variable
db.connection(System.getenv("DB_PASSWORD"));
```

---

## Authentication & Authorization

**Rule:** All authenticated endpoints require <AUTH_METHOD>. All protected resources validate tokens before granting access.

**Implementation:**
- [ ] Authentication enforced at API gateway / middleware level
- [ ] Authorization checked before returning sensitive data
- [ ] Token expiration enforced (TTL: <N minutes>)
- [ ] Failed auth attempts logged: `docs/audits/security-logs/`

**Token Validation:**
- [ ] Signature verified using public key / JWKS endpoint
- [ ] Expiration (`exp`) claim checked
- [ ] Issuer (`iss`) claim matches expected provider
- [ ] Audience (`aud`) claim matches this application

**Example (Spring Boot):**
```java
// ✅ Correct: middleware validates all requests
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/health", "/login").permitAll()
            .anyRequest().authenticated()
            .and().oauth2ResourceServer().jwt();
        return http.build();
    }
}
```

---

## SQL & Database Queries — MANDATORY

**Rule:** All database queries must use parameterized statements. Never concatenate user input into SQL.

**What to flag:**
- String concatenation in WHERE clauses: `WHERE name = '` + input
- Dynamic table names built from user input
- `eval()` or dynamic SQL construction
- `IN` clauses built via string concatenation

**Enforcement:**
- [ ] Code review checks all queries for parameterization
- [ ] SAST tool (SonarQube, Checkmarx) flags SQL injection patterns
- [ ] Integration tests verify parameterized queries work

**Examples:**

```java
// ❌ WRONG — SQL injection vulnerability
String query = "SELECT * FROM users WHERE email = '" + email + "'";
ResultSet rs = stmt.executeQuery(query);

// ✅ RIGHT — parameterized query
String query = "SELECT * FROM users WHERE email = ?";
PreparedStatement pstmt = conn.prepareStatement(query);
pstmt.setString(1, email);
ResultSet rs = pstmt.executeQuery();

// ❌ WRONG — dynamic table name
String table = request.getParameter("table"); // user input
String query = "SELECT * FROM " + table; // SQL injection!

// ✅ RIGHT — whitelist allowed tables
String table = request.getParameter("table");
if (!ALLOWED_TABLES.contains(table)) throw new IllegalArgumentException();
String query = "SELECT * FROM " + table;
```

---

## Encryption — Data at Rest & In Transit

**Rule:** Sensitive data must be encrypted in transit and at rest.

**In Transit:**
- [ ] All API endpoints use HTTPS (TLS 1.2+)
- [ ] TLS certificate issued by trusted CA
- [ ] Certificate pinning enforced (if calling external APIs)
- [ ] No `http://` URLs in production config

**At Rest:**
- [ ] Database encryption enabled: <algorithm, e.g., AES-256>
- [ ] Sensitive fields encrypted: <list which fields>
- [ ] Key management: <AWS KMS / Azure Key Vault / Vault / other>
- [ ] Backups encrypted: <YES/NO>

**Example Configuration:**
```yaml
# ✅ Encryption at rest (AWS RDS)
engine: MySQL
storage-encryption: enabled
kms-key-id: arn:aws:kms:us-east-1:123456789:key/12345678

# ✅ TLS in transit
minimum-tls-version: 1.2
require-https: true
hsts-enabled: true
hsts-max-age: 31536000
```

---

## Access Logging & Audit Trails — MANDATORY

**Rule:** All authentication attempts, authorization decisions, and data access must be logged.

**What to log:**
- Successful login: user, timestamp, IP, method
- Failed login: email attempted, timestamp, IP (don't log password)
- Permission denied: user, resource, timestamp
- Data access: who, what, when, from where
- Configuration changes: by whom, what changed, when

**What NOT to log:**
- Passwords or secrets
- Full credit card numbers (PCI violation)
- API keys or tokens
- Session IDs (use anonymous identifier instead)

**Storage & Retention:**
- [ ] Logs centralized: <CloudWatch / ELK / Splunk / S3>
- [ ] Immutable audit trail: <where>
- [ ] Retention: <N days/years>
- [ ] Accessible to: <audit team / security / compliance>

**Example:**
```json
{
  "timestamp": "2026-10-01T14:32:15Z",
  "event": "auth_failure",
  "user_email": "user@example.com",
  "method": "oauth2",
  "ip_address": "192.168.1.1",
  "reason": "invalid_token"
}
```

---

## Rate Limiting & DDoS Protection

**Rule:** Protect against brute force and automated attacks using rate limits.

**Endpoints to protect:**
- `/login` — max 5 attempts per minute per IP
- `/api/password-reset` — max 3 attempts per hour per user
- `/api/register` — max 10 registrations per hour per IP

**Implementation:**
- [ ] Rate limiting middleware in place
- [ ] Limits enforced per IP or per user
- [ ] Throttle response includes retry-after header
- [ ] Attacks logged: `docs/audits/security-logs/`

**Example (Spring Boot):**
```java
@RestController
@RateLimiter(max = 5, window = "1m")
public class LoginController {
    @PostMapping("/login")
    public ResponseEntity<Token> login(@RequestBody LoginRequest req) {
        // ...
    }
}
```

---

## Dependency Scanning & Vulnerability Management

**Rule:** All dependencies (Maven, npm, pip, etc.) must be scanned for known CVEs. Critical CVEs must be patched within 48 hours.

**Enforcement:**
- [ ] Dependency scanning enabled in CI/CD
- [ ] Tool: <Snyk / WhiteSource / OWASP Dependency-Check>
- [ ] Pipeline fails if critical CVEs found
- [ ] Patch schedule: Critical (48h), High (1 week), Medium (2 weeks)

**Example (`pom.xml`):**
```xml
<!-- Keep Spring Boot and dependencies current -->
<properties>
    <spring-boot.version>3.3.0</spring-boot.version>
    <maven.compiler.source>21</maven.compiler.source>
</properties>

<!-- Regular dependency updates via Dependabot or Renovate -->
```

---

## Code Review Checklist — Security

Every PR must pass this security checklist before merge:

- [ ] No hardcoded secrets, credentials, or API keys
- [ ] All database queries are parameterized
- [ ] Authentication & authorization checks present
- [ ] User input validated and sanitized
- [ ] Error messages don't leak sensitive info
- [ ] Logging doesn't include passwords or tokens
- [ ] No unencrypted storage of sensitive data
- [ ] Dependencies scanned for CVEs
- [ ] Comments explain security reasoning (if non-obvious)

---

## Exception: Security Exemptions

If you must violate a guardrail, document it here:

| Rule | Code Location | Reason | Approved By | Expiration |
|---|---|---|---|---|
| <rule> | `<file:line>` | <why> | <name> | <YYYY-MM-DD> |

**Example:**
| SQL in WHERE | `src/reports/query.sql:42` | Legacy report system, safe due to whitelist | Security Lead | 2026-12-31 |

All exemptions must be approved by the Security Lead and expire within 90 days.

---

## Do NOT

- ❌ Store plaintext passwords or secrets in config files
- ❌ Use `eval()` or dynamic code execution with user input
- ❌ Skip HTTPS for "internal only" services
- ❌ Log user passwords, API keys, or tokens
- ❌ Disable security headers (HSTS, CSP, X-Frame-Options)
- ❌ Use default credentials in production
- ❌ Merge code with known CVEs without exception approval
- ❌ Disable authentication in shared environments (dev/test)

---

## References

- See `.claude/context/security-posture.md` for compliance obligations
- See `.claude/context/hazards.md` for known security risks
- See `docs/security/threat-model.md` for this app's threat landscape
- See `docs/security/incident-response.md` for security incident procedures
- Enterprise security rules: `@enterprise/rules/secure-coding.md`

---

## Last Review

- **Reviewed By:** <name>
- **Date:** <YYYY-MM-DD>
- **Next Review:** <YYYY-MM-DD> (quarterly)
