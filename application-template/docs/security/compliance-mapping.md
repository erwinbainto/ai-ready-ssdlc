# Compliance Mapping — <APPLICATION_NAME>

**Purpose:** Show how this application implements required compliance framework controls.

**Last Updated:** <YYYY-MM-DD>  
**Owner:** <Compliance Officer / Security Lead>  
**Scope:** <PCI DSS v3.2.1 / NIST CSF 1.1 / ISO 27001:2022 / GDPR / HIPAA>

---

## PCI DSS v3.2.1 Compliance (If Applicable)

Use this section if your application processes, stores, or transmits payment card data.

### Requirement 1: Install and Maintain a Firewall Configuration

**Control:** A firewall must protect all systems in the cardholder data environment (CDE).

**How We Implement It:**

| PCI Requirement | Implementation | Evidence | Status |
|---|---|---|---|
| 1.1: Firewall policy | Cloud security groups restrict inbound traffic | `docs/architecture/network-security.md` | ✅ Implemented |
| 1.2: Prohibited direct access | No public internet access to databases | `aws-config/security-groups.yaml` | ✅ Implemented |
| 1.3: Deny inbound traffic | Default deny, allow specific | `aws-config/security-groups.yaml` | ✅ Implemented |

**Notes:** AWS Security Groups enforce network isolation. API Gateway is the single entry point.

---

### Requirement 2: Do Not Use Vendor-Supplied Defaults

**Control:** Default passwords and settings must be changed.

**How We Implement It:**

| PCI Requirement | Implementation | Evidence | Status |
|---|---|---|---|
| 2.1: Change defaults | Database password randomized | `terraform/rds.tf` (random password) | ✅ Implemented |
| 2.2: Configuration standards | Hardened OS images | `docker/Dockerfile` (minimal base) | ✅ Implemented |
| 2.3: Admin access restricted | 2FA required for AWS console | `iam-policy.json` | ✅ Implemented |

---

### Requirement 3: Protect Stored Cardholder Data

**Control:** Cardholder data must be protected using strong encryption and key management.

**How We Implement It:**

| PCI Requirement | Implementation | Evidence | Status |
|---|---|---|---|
| 3.1: Data minimization | Don't store full PAN | `src/payment/CardToken.java` (token only) | ✅ Implemented |
| 3.2: PAN encryption | AES-256 at rest | `rds-encryption-enabled.yaml` | ✅ Implemented |
| 3.4: Key rotation | Automatic key rotation every 90 days | `aws-kms/key-policy.json` | ✅ Implemented |
| 3.5: Key access | Encrypted key escrow | `aws-secrets-manager/policy.json` | ✅ Implemented |

**Evidence Document:** Link to your key management procedure

---

### Requirement 8: Identify and Authenticate Access

**Control:** Users and systems must be identified and authenticated.

**How We Implement It:**

| PCI Requirement | Implementation | Evidence | Status |
|---|---|---|---|
| 8.1: Auth mechanism | OAuth 2.0 via AWS Cognito | `.claude/context/security-posture.md` | ✅ Implemented |
| 8.2: MFA | MFA required for admin users | `cognito/mfa-policy.json` | ✅ Implemented |
| 8.3: Password strength | Min 8 chars, complexity required | `cognito/password-policy.json` | ✅ Implemented |
| 8.5: Access control | RBAC (admin, auditor, viewer) | `src/auth/RoleBasedAccess.java` | ✅ Implemented |

---

### Requirement 10: Track & Monitor Access

**Control:** All access to cardholder data must be logged and monitored.

**How We Implement It:**

| PCI Requirement | Implementation | Evidence | Status |
|---|---|---|---|
| 10.1: Audit logs | All data access logged to CloudWatch | `backend/logging/AuditLogger.java` | ✅ Implemented |
| 10.2: Log retention | Logs retained for 1 year | `cloudwatch/log-retention-policy.json` | ✅ Implemented |
| 10.3: Log protection | Immutable logs, access controlled | `s3/lifecycle-policy.json` | ✅ Implemented |
| 10.7: Monitoring | SIEM alerting on suspicious activity | `cloudwatch/alarms.yaml` | ✅ Implemented |

---

## NIST Cybersecurity Framework (CSF) v1.1

Use this if your organization requires NIST compliance or risk management.

### IDENTIFY Function

**Goal:** Develop an understanding of the environment and assets.

| NIST Control | Implementation | Evidence | Status |
|---|---|---|---|
| ID.AM-1: Inventory of assets | Asset register maintained | `docs/architecture/asset-inventory.md` | ✅ Implemented |
| ID.RA-1: Risk assessment | Annual risk assessment completed | `docs/security/threat-model.md` | ✅ Implemented |

### PROTECT Function

**Goal:** Develop safeguards to prevent or reduce impact.

| NIST Control | Implementation | Evidence | Status |
|---|---|---|---|
| PR.AC-1: Access control | RBAC enforced at API layer | `src/auth/AccessControl.java` | ✅ Implemented |
| PR.DS-1: Data security | Encryption at rest and in transit | `backend/security/encryption.yaml` | ✅ Implemented |
| PR.IP-1: Security practices | Code review process | `.claude/rules/security-guardrails.md` | ✅ Implemented |

### DETECT Function

**Goal:** Develop ability to discover a security incident.

| NIST Control | Implementation | Evidence | Status |
|---|---|---|---|
| DE.AE-1: Anomalies detected | SIEM configured with alerts | `cloudwatch/alarms.yaml` | ✅ Implemented |
| DE.CM-1: Monitoring enabled | Application metrics + security logs | `prometheus/scrape-config.yaml` | ✅ Implemented |

### RESPOND Function

**Goal:** Develop appropriate response procedures.

| NIST Control | Implementation | Evidence | Status |
|---|---|---|---|
| RS.RP-1: Response plan | Incident response plan documented | `docs/security/incident-response.md` | ✅ Implemented |
| RS.CO-1: Coordination | Stakeholder notification procedure | `docs/security/incident-response.md` | ✅ Implemented |

### RECOVER Function

**Goal:** Restore capabilities and services to normal operations.

| NIST Control | Implementation | Evidence | Status |
|---|---|---|---|
| RC.RP-1: Recovery plan | Disaster recovery plan | `docs/architecture/disaster-recovery.md` | ✅ Implemented |
| RC.CO-1: Recovery coordination | Backup tested quarterly | `docs/audits/backup-tests/` | ✅ Implemented |

---

## ISO 27001:2022 Compliance (If Applicable)

Use this if your organization is ISO 27001 certified.

### Access Control (A.8)

| ISO Control | Implementation | Evidence | Status |
|---|---|---|---|
| A.8.1: Least privilege | RBAC roles follow principle of least privilege | `src/auth/roles.yaml` | ✅ Implemented |
| A.8.2: User registration | Formal access request process | `docs/policies/access-request.md` | ✅ Implemented |
| A.8.3: User termination | Immediate access revocation on termination | `docs/policies/offboarding.md` | ✅ Implemented |

### Cryptography (A.10)

| ISO Control | Implementation | Evidence | Status |
|---|---|---|---|
| A.10.1: Encryption policy | Encryption required for sensitive data | `.claude/rules/security-guardrails.md` | ✅ Implemented |
| A.10.2: Key management | Key rotation every 90 days | `aws-kms/key-policy.json` | ✅ Implemented |

### Operations Security (A.12)

| ISO Control | Implementation | Evidence | Status |
|---|---|---|---|
| A.12.2: Change management | All changes require approval + testing | `docs/policies/change-management.md` | ✅ Implemented |
| A.12.4: Logging | Audit logs for all privileged operations | `backend/logging/AuditLogger.java` | ✅ Implemented |

---

## GDPR Compliance (If Processing EU Personal Data)

### Data Protection Principles

| GDPR Principle | Implementation | Evidence | Status |
|---|---|---|---|
| Lawfulness | Explicit user consent collected | `frontend/components/ConsentForm.tsx` | ✅ Implemented |
| Purpose limitation | Data used only for stated purpose | `docs/privacy-policy.md` | ✅ Implemented |
| Data minimization | Only necessary data collected | `src/user/UserProfile.java` | ✅ Implemented |
| Integrity & confidentiality | Encryption + access controls | `.claude/rules/security-guardrails.md` | ✅ Implemented |

### User Rights

| GDPR Right | Implementation | Evidence | Status |
|---|---|---|---|
| Right to access | Data export API available | `POST /api/users/export` | ✅ Implemented |
| Right to deletion | Account deletion (data removed after 30 days) | `DELETE /api/users/{id}` | ✅ Implemented |
| Right to portability | Data export in standard format (JSON) | `POST /api/users/export` | ✅ Implemented |

### Data Breach Notification

| Requirement | Implementation | Evidence | Status |
|---|---|---|---|
| Breach detection | SIEM monitors for anomalies | `cloudwatch/alarms.yaml` | ✅ Implemented |
| Notification (72h) | Incident response procedure documented | `docs/security/incident-response.md` | ✅ Implemented |

---

## Security Assessment Status

| Framework | Applicability | Status | Last Assessment | Next Assessment |
|---|---|---|---|---|
| PCI DSS | <YES/NO> | <On Track / At Risk> | <YYYY-MM-DD> | <YYYY-MM-DD> |
| NIST CSF | <YES/NO> | <On Track / At Risk> | <YYYY-MM-DD> | <YYYY-MM-DD> |
| ISO 27001 | <YES/NO> | <On Track / At Risk> | <YYYY-MM-DD> | <YYYY-MM-DD> |
| GDPR | <YES/NO> | <On Track / At Risk> | <YYYY-MM-DD> | <YYYY-MM-DD> |
| HIPAA | <YES/NO> | <On Track / At Risk> | <YYYY-MM-DD> | <YYYY-MM-DD> |

---

## Open Gaps & Remediation Plan

| Control | Gap | Why | Remediation | Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| <framework> / <control> | <what's missing> | <reason> | <action> | <name> | <YYYY-MM-DD> | Open/In Progress |

**Example:**
| PCI DSS 6.5 | SAST scanning not automated | Need to integrate Sonarqube | Add Sonarqube to CI/CD pipeline | DevOps Lead | 2026-10-15 | In Progress |

---

## Evidence Repository

Where compliance evidence is stored:

| Document Type | Location | Retention |
|---|---|---|
| Audit logs | AWS CloudWatch (1 year retention) | 1 year |
| Encryption keys | AWS KMS (encrypted) | Indefinite |
| Risk assessments | `docs/security/` | Annual |
| Penetration test reports | `docs/audits/pen-tests/` | 3 years |
| Incident reports | `docs/audits/incidents/` | 3 years |

---

## References

- **Threat Model:** `docs/security/threat-model.md`
- **Security Guardrails:** `.claude/rules/security-guardrails.md`
- **Security Posture:** `.claude/context/security-posture.md`
- **Incident Response:** `docs/security/incident-response.md`

---

## Sign-Off

| Role | Name | Date | Notes |
|---|---|---|---|
| Compliance Officer | <name> | <YYYY-MM-DD> | Mapping reviewed & approved |
| Security Lead | <name> | <YYYY-MM-DD> | Controls verified in place |
| Dev Lead | <name> | <YYYY-MM-DD> | Implementation confirmed |

**Next Compliance Review:** <YYYY-MM-DD> (annually or after major changes)
