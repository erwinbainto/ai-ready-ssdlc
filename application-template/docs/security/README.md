# Security Documentation

This folder contains security-related documentation for **<APPLICATION_NAME>**.

## Purpose

Security documentation captures threat models, compliance requirements, incident procedures, and audit trails. It's reviewed quarterly and updated after any security incident.

## Files in This Directory

| File | Purpose | Audience | Update Frequency |
|---|---|---|---|
| `threat-model.md` | Application-specific threats, assets, attack surface | Architects, Security | Quarterly or after changes |
| `compliance-mapping.md` | Maps app features to PCI DSS, NIST, ISO 27001 controls | Security, Compliance, Dev Leads | After compliance changes |
| `incident-response.md` | Playbooks for security incidents, escalation procedures | All team members | Quarterly or after incident |
| `audit-trails/` | Audit logs, penetration test results, compliance evidence | Security, Compliance | Ongoing |

## Quick Start

### 1. Define the Threat Model

Complete `threat-model.md` with your team:
- What assets does the app protect? (data, services, infrastructure)
- What threats exist? (attackers, threat vectors, attack techniques)
- What's the attack surface? (APIs, authentication, external integrations)
- What mitigations are in place?

**Time to complete:** 2-4 hours with architects + security team

### 2. Map to Compliance Frameworks

Complete `compliance-mapping.md`:
- Does the app handle payment data? → PCI DSS applies
- Does it handle health data? → HIPAA applies
- Does it process EU personal data? → GDPR applies
- Does it need general security? → NIST CSF applies

Link each control to your code or infrastructure.

**Time to complete:** 4-8 hours depending on frameworks

### 3. Document Incident Response

Complete `incident-response.md`:
- Who is the security point of contact?
- What's the escalation path?
- What's the response procedure for each incident type?
- Where are incident logs stored?

**Time to complete:** 2-3 hours

### 4. Set Up Audit Trail Storage

Create `audit-trails/` subdirectories:
- `audit-trails/penetration-tests/` — External pen test reports
- `audit-trails/compliance-audits/` — Third-party audit findings
- `audit-trails/security-reviews/` — Internal security reviews
- `audit-trails/incidents/` — Incident reports and resolutions

**Important:** These files may be sensitive. Restrict access to security + compliance team.

---

## How to Use These Documents

### For Developers

- **Before coding:** Read `threat-model.md` to understand what you're protecting
- **During PR review:** Check `.claude/rules/security-guardrails.md` and apply those checks
- **After security incident:** Update `incident-response.md` with lessons learned

### For Security Team

- **Quarterly review:** Update threat model if architecture changed
- **Audit preparation:** Reference `compliance-mapping.md` to gather evidence
- **Incident response:** Use `incident-response.md` playbooks
- **Post-incident:** Document findings in `audit-trails/incidents/`

### For Compliance Officer

- **Audit:** `compliance-mapping.md` shows how controls are implemented
- **Evidence:** Files in `audit-trails/` provide documentation
- **Control assessment:** Link each control to code, config, or process

---

## Example: PCI DSS Compliance

If your app processes payment cards:

1. **Threat Model** should include:
   - Card data is stored (encrypted)
   - External payment processor integration
   - Attack vectors: credential theft, SQL injection, insider access

2. **Compliance Mapping** should show:
   - Requirement 3.4 (Encryption): "AES-256 encryption at rest, TLS 1.2 in transit" → `backend/config/encryption.yaml`
   - Requirement 8.1 (Auth): "OAuth 2.0 via AWS Cognito" → `.claude/context/security-posture.md`
   - Requirement 10.1 (Logging): "All card access logged to CloudWatch" → `backend/logging.config`

3. **Incident Response** should include:
   - Procedure if card data is exposed
   - Who to notify (PCI compliance officer, payment processor, customers)
   - Timeline for breach notification

4. **Audit Trail** should contain:
   - Last penetration test report
   - Annual compliance certification
   - Incident history (if any)

---

## Templates & Examples

All files in this directory contain clear instructions and sample content.

**To get started:**
1. Open each `.md` file
2. Follow the **"How to fill"** instructions
3. Replace `<PLACEHOLDERS>` with your app's values
4. Add team members and review dates

---

## Review Schedule

| Document | Frequency | Owner | Next Review |
|---|---|---|---|
| `threat-model.md` | Quarterly | Security Lead | <YYYY-MM-DD> |
| `compliance-mapping.md` | After compliance changes | Compliance Officer | <YYYY-MM-DD> |
| `incident-response.md` | After every incident | Security Lead | <YYYY-MM-DD> |
| `audit-trails/` | Ongoing | Security Team | N/A |

---

## Related Documents

- **Security Posture:** `.claude/context/security-posture.md` — Overall security & compliance baseline
- **Security Guardrails:** `.claude/rules/security-guardrails.md` — Mandatory coding rules
- **Hazards:** `.claude/context/hazards.md` — Known security risks for this app
- **Enterprise Security Rules:** `@enterprise/rules/secure-coding.md` — Organization-wide standards

---

## Questions?

- **Threat modeling:** Ask the Security Lead or Solution Architect
- **Compliance requirements:** Ask the Compliance Officer or Legal
- **Incident response:** Ask the Security Team
- **Documentation gaps:** File an issue or PR

Last updated: <YYYY-MM-DD>  
Maintained by: <Security Lead / Dev Lead>
