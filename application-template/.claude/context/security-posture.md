# Security Posture — <APPLICATION_NAME>

Compliance baseline and security controls. Complete with security lead.

**Last Updated:** <YYYY-MM-DD>  
**Owner:** <Security Lead>  
**Full Details:** `docs/security/security-posture.md`

---

## Compliance Requirements

| Framework | Required | Mapping | Owner |
|---|---|---|---|
| PCI DSS | <YES/NO> | `docs/security/compliance-mapping.md` | <name> |
| NIST CSF | <YES/NO> | `docs/security/compliance-mapping.md` | <name> |
| ISO 27001 | <YES/NO> | `docs/security/compliance-mapping.md` | <name> |
| GDPR | <YES/NO> | `docs/security/compliance-mapping.md` | <name> |

---

## Authentication & Authorization

| Aspect | Value | Notes |
|---|---|---|
| Method | <OAuth 2.0 / SAML / JWT / Cognito / Other> | |
| Provider | <service name or URL> | |
| Authorization Model | <RBAC / ABAC / ACL> | |
| Default Access | <DENY all / ALLOW all> | |
| Token Storage (Frontend) | <localStorage / HttpOnly Cookie / Other> | |
| Token TTL | <N minutes> | |

---

## Data Classification

| Data Type | Classification | Storage | Encryption | Retention | Access |
|---|---|---|---|---|---|
| <data> | <Confidential/Sensitive/Internal/Public> | <where> | <algorithm> | <duration> | <who> |

---

## Known Security Risks

| Risk | Level | Impact | Mitigation | Status | Owner | Target |
|---|---|---|---|---|---|---|
| <risk> | <H/M/L> | <consequence> | <control> | <Open/Mitigated> | <name> | <date> |

Full analysis: `docs/security/threat-model.md`

---

## Secrets Management

| Aspect | Value |
|---|---|
| Storage | <AWS Secrets Manager / Vault / K8s Secrets / Other> |
| Secrets in scope | DB passwords, API keys, OAuth secrets, signing keys, certificates |
| Rotation | <Automatic / Manual> every <N days> |
| Last rotated | <YYYY-MM-DD> |
| Access restricted to | <roles/teams> |
| Audit trail | <CloudTrail / other location> |

---

## Incident Response

| Aspect | Value |
|---|---|
| Security Lead | <Name, email, phone> |
| Classification levels | Critical / High / Medium / Low (see runbook) |
| Escalation | See `docs/security/incident-response.md` |
| Runbook | `docs/security/incident-response.md` |

---

## Status

- Last reviewed: <YYYY-MM-DD>
- Next review: <YYYY-MM-DD>
- Compliance checklist: `docs/security/security-posture.md`

---

## References

- Compliance mapping: `docs/security/compliance-mapping.md`
- Threat model: `docs/security/threat-model.md`
- Incident response: `docs/security/incident-response.md`
- Security guardrails: `.claude/rules/security-guardrails.md`
