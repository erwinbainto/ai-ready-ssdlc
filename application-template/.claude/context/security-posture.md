# Security Posture — <APPLICATION_NAME>

**Instructions:** Complete this section with your dev team and security lead. Every field is required to identify compliance obligations and security controls. Leave no placeholders.

---

## Compliance Requirements

Identify which standards apply to this application and document evidence.

| Standard | Required | Evidence | Owner | Review Date |
|---|---|---|---|---|
| PCI DSS | <YES/NO> | `<path-to-mapping>` | <name/role> | <YYYY-MM-DD> |
| NIST CSF | <YES/NO> | `<path-to-mapping>` | <name/role> | <YYYY-MM-DD> |
| ISO 27001 | <YES/NO> | `<path-to-mapping>` | <name/role> | <YYYY-MM-DD> |

**How to fill:**
- **Required**: Do you process payment cards (PCI), health data (HIPAA), EU personal data (GDPR)?
- **Evidence**: Link to the mapping document in `docs/security/compliance-mapping.md`
- **Owner**: Who is accountable for compliance in this area?

---

## Authentication & Authorization

Define how users authenticate and what they can access.

**Method:** <OAuth 2.0 / SAML / JWT / Cognito / API Key / Other>

**Provider:** <Name or URL>

**Authorization Model:** <RBAC / ABAC / ACL>

**Default Access:** <DENY all / ALLOW all>

**Token Storage:** <localStorage / sessionStorage / HttpOnly Cookie / Memory>

**Example:**
```
Method: OAuth 2.0
Provider: AWS Cognito (us-east-1)
Authorization: RBAC (admin, auditor, viewer)
Default Access: DENY all; only /health and /login public
Token Storage: HttpOnly Cookie
```

---

## Data Classification

Define how data is categorized, encrypted, and retained.

| Data Type | Classification | Storage | Encryption | Retention | Access |
|---|---|---|---|---|---|
| User credentials | Confidential | Encrypted DB | AES-256 | 7 years | Admin only |
| User PII | Sensitive | Encrypted DB | AES-256 | 1 year | Team + auth users |
| Audit logs | Internal | Immutable | Signed | 2 years | Compliance |

**Classification levels:**
- Confidential: passwords, API keys, payment data
- Sensitive: user PII, health data, personal information
- Internal: operational logs, metrics, non-sensitive data
- Public: documentation, status pages

---

## Known Security Risks & Mitigations

| Risk | Level | Impact | Mitigation | Status | Owner | Target Date |
|---|---|---|---|---|---|---|
| SQL injection | High | Data breach | Parameterized queries | Mitigated | Backend Lead | N/A |
| Missing rate limit | High | Brute force | IP-based limits | Open | DevOps | 2026-10-15 |
| Unencrypted backup | Medium | Data theft | S3 + KMS | Planned | DevOps | 2026-09-30 |

---

## Secrets Management

**Storage:** <AWS Secrets Manager / Vault / Kubernetes Secrets / Env vars>

**Secrets in scope:**
- Database passwords
- API keys (third-party)
- OAuth client secrets
- JWT signing keys
- TLS certificates

**Rotation policy:**
- Automatic rotation: <YES/NO>
- Frequency: <Every N days>
- Last rotation: <YYYY-MM-DD>

**Example:**
```
Storage: AWS Secrets Manager
Rotation: Automatic, every 30 days
Access: prod-deployer IAM role only
Audit: CloudTrail logs
```

---

## Security Incident Response

**Point of Contact:** <Name, email, phone>

**Escalation:**
1. Developer notices issue → Jira (Security label)
2. On-call security engineer reviews within 1 hour
3. If Critical: page security lead + CTO
4. If High: notify team lead, begin investigation

**Runbook:** `docs/security/incident-response.md`

---

## Compliance Status Checklist

- [ ] All data classified and retention policies documented
- [ ] Authentication & authorization mechanisms deployed
- [ ] Encryption enabled (data at rest and in transit)
- [ ] Secrets management system in place
- [ ] Access logs and audit trails enabled
- [ ] Security incident response plan documented
- [ ] Vulnerability scanning (SAST / DAST) enabled
- [ ] Dependency scanning for CVEs enabled
- [ ] Security training completed by team
- [ ] Last security review: <YYYY-MM-DD>

---

## Review & Approval

| Role | Name | Date |
|---|---|---|
| Dev Lead | <name> | <YYYY-MM-DD> |
| Security Lead | <name> | <YYYY-MM-DD> |

---

## Next Steps

1. Complete this form with your team
2. Create compliance mappings in `docs/security/`
3. Define threat model in `docs/security/threat-model.md`
4. Schedule quarterly reviews
5. Update after any security incident
