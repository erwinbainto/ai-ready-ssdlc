---
description: Mandatory security controls for <APPLICATION_NAME>
paths: ["src/**", "backend/**", "frontend/**"]
---

# Security Guardrails — <APPLICATION_NAME>

Mandatory security rules. Narrower than enterprise; specific to this app's tech stack and threat model.

**Last Updated:** <YYYY-MM-DD>  
**Owner:** <Security Lead>  
**Reference:** `@enterprise/rules/secure-coding.md` (enterprise standards)

---

## Secrets Management — MANDATORY

| Rule | Enforcement |
|---|---|
| Never commit credentials, keys, tokens | Pre-commit hooks + secret scanning |
| Use environment variables for secrets | Block hardcoded passwords in CI/CD |
| Rotate secrets regularly | Automatic rotation every <N days> |

See: `.claude/context/security-posture.md` (secrets management section)

---

## SQL & Database Queries — MANDATORY

| Rule | Enforcement |
|---|---|
| Parameterized queries only | SAST scanning + code review |
| No string concatenation in SQL | Pre-commit hooks |
| Sargable predicates on indexes | Performance test + review |

Example (Java):
```java
✅ @Query("SELECT * FROM users WHERE email = :email")
❌ "SELECT * FROM users WHERE email = '" + email + "'"
```

---

## Authentication & Authorization

| Rule | Enforcement |
|---|---|
| All admin endpoints require auth | Code review + integration tests |
| Token validation enforced | SAST scanning |
| Audit logging on permission denied | Integration tests |

---

## Encryption

| Rule | Enforcement |
|---|---|
| Sensitive data encrypted at rest | Infrastructure validation |
| HTTPS only for transit | Load balancer config + tests |
| Never log passwords/tokens | Code review + SAST |

---

## Access Logging & Audit Trails

| Rule | Enforcement |
|---|---|
| All auth attempts logged | Integration tests |
| Authorization decisions logged | Code review |
| Logs immutable (no delete/modify) | Infrastructure validation |

---

## Rate Limiting & DDoS Protection

| Rule | Enforcement |
|---|---|
| `/login` — max 5 attempts/minute per IP | Integration tests |
| `/api/*` — max 100 requests/minute per user | Load testing |
| Throttle response includes retry-after | Code review |

---

## Dependency Scanning

| Rule | Enforcement |
|---|---|
| All dependencies scanned for CVEs | CI/CD pipeline gate |
| Critical CVEs patched within 48h | JIRA tickets + monitoring |
| EOL versions not allowed | Policy check in pipeline |

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

---

## Exceptions

| Rule | Code Location | Reason | Approved By | Expires |
|---|---|---|---|---|
| <rule> | `<file:line>` | <why> | <name> | <YYYY-MM-DD> |

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

---

## References

- Security posture: `.claude/context/security-posture.md`
- Threat model: `docs/security/threat-model.md`
- Incident response: `docs/security/incident-response.md`
- Enterprise rules: `@enterprise/rules/secure-coding.md`
- Full guidance: `docs/guides/rules/README.md`

---

**Last Review:** <YYYY-MM-DD>  
**Next Review:** <YYYY-MM-DD> (quarterly)
