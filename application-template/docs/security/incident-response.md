# Incident Response Plan — <APPLICATION_NAME>

**Purpose:** Define procedures for detecting, responding to, and recovering from security incidents.

**Last Updated:** <YYYY-MM-DD>  
**Owner:** <Security Lead>  
**Review Frequency:** Quarterly or after every incident

---

## 1. Incident Classification

### Critical (SEV-1)

**Characteristics:**
- Active data breach (cardholder data, PII, trade secrets exposed)
- Ransomware or malware infection
- System completely unavailable (users cannot access service)
- Unauthorized administrative access
- Active exploitation in progress

**Response Time:** Immediate (within 15 minutes)  
**Escalation:** Page security lead + CTO + legal immediately

**Examples:**
- Payment card data accessed by attacker
- Ransomware deployed on production servers
- API down for more than 1 hour
- Attacker has admin credentials and is actively using them

### High (SEV-2)

**Characteristics:**
- Confirmed unauthorized access (but not active exploitation)
- Data exfiltration (data copied but not yet public)
- Failed brute force attempts detected
- Known CVE exploit detected in logs
- Encryption key compromise

**Response Time:** Within 1 hour  
**Escalation:** Notify security lead + team lead

**Examples:**
- Unusual number of failed login attempts (brute force attempt)
- SQL injection attempt detected and blocked
- Unpatched critical CVE found in use
- Suspicious account activity (impossible travel)

### Medium (SEV-3)

**Characteristics:**
- Suspicious activity detected (unknown but not confirmed malicious)
- Configuration mistake (e.g., S3 bucket briefly public)
- Minor security policy violation
- Phishing email received
- Access with expired credentials

**Response Time:** Within 4 hours  
**Escalation:** Notify team lead + security team

**Examples:**
- Suspicious download of user database (but not exfiltrated externally)
- Database backup found unencrypted (but not accessed)
- Admin made config change without approval (but not harmful)

### Low (SEV-4)

**Characteristics:**
- Policy violation with no security impact
- Minor vulnerability in non-critical system
- Outdated dependency (not yet exploited)
- Documentation gap

**Response Time:** Within 1 business day  
**Escalation:** Document in Jira (Security label)

**Examples:**
- Outdated SSL certificate not yet expired
- Code comment mentions a password (not actually used)
- Developer left debug logging enabled (minor info leak)

---

## 2. Incident Response Team

### Core Team

| Role | Name | Title | Phone | Email | Availability |
|---|---|---|---|---|---|
| **Incident Commander** | <name> | Security Lead | <phone> | <email> | 24/7 on-call |
| **Technical Lead** | <name> | DevOps / Platform Lead | <phone> | <email> | Business hours |
| **Developer** | <name> | Backend Lead | <phone> | <email> | Business hours |
| **Communications** | <name> | Product / Operations Lead | <phone> | <email> | Business hours |

### Extended Team (By Incident Type)

| Incident Type | Additional Resources | Contact |
|---|---|---|
| Payment data breach | Compliance Officer, Legal, Payment Processor | <contact> |
| Customer data breach | Privacy Officer, Customer Support, Legal | <contact> |
| Infrastructure compromise | Cloud provider support, hosting team | <contact> |
| Malware / ransomware | Forensics team, law enforcement (FBI) | <contact> |

---

## 3. Incident Detection

### Automated Alerts

| Alert | Threshold | Action | Owner |
|---|---|---|---|
| Failed login attempts | >5 attempts/minute per IP | Rate limiting + alert security team | Auto |
| Unauthorized API access | 401/403 spike | Page on-call engineer | Auto |
| Database access anomaly | Unusual queries detected | Page DBA + alert security team | Auto |
| Certificate expiration | <30 days to expiry | Alert ops team | Auto |
| Dependency CVE | Critical severity found | Block deployment + alert security team | Auto |

**Where alerts go:**
- Prod incidents: `#incidents` Slack channel (webhooks)
- Security incidents: `#security-incidents` Slack channel (email + phone)
- All incidents: `security-incidents@company.com` (email list)

### Manual Detection

- Customer reports suspicious activity
- Developer notices unusual code behavior
- Security audit finds misconfiguration
- Monitoring dashboard shows anomaly

**How to report:** 
- Slack: `#security-incidents` (mention @security-lead)
- Email: `security@company.com`
- Phone: <on-call number>

---

## 4. Initial Response (First 15 Minutes)

### Step 1: Confirm the Incident

**Questions to ask:**
- What triggered the alert / report?
- When did it start?
- What systems are affected?
- Is it still happening?
- Do you have evidence?

**Action:** Gather facts; don't assume

### Step 2: Classify the Incident

- SEV-1: Immediate all-hands
- SEV-2: Notify security lead + team lead
- SEV-3: Notify team lead + document
- SEV-4: Document in Jira

**Action:** Create incident ticket with classification

### Step 3: Activate Incident Response Team

**For SEV-1/2:** Page team members immediately  
**For SEV-3:** Send email + Slack  
**For SEV-4:** Jira ticket only

**Create incident war room:**
- Slack channel: `#incident-<YYYYMMDD-HH>` (e.g., `#incident-20261001-14`)
- Conference line: <bridge URL>
- Shared doc: <Google Doc template>

---

## 5. Investigation & Containment

### Investigation Timeline

| Time | Activity | Owner | Status |
|---|---|---|---|
| +0min | Classify incident | Incident Commander | Start |
| +15min | Activate response team | Incident Commander | Start |
| +30min | Gather facts & timeline | Technical Lead | Start |
| +60min | Determine root cause (preliminary) | Dev Lead | Start |
| +120min | Mitigation strategy defined | Technical Lead | Start |

### Containment Actions (Stop the Bleeding)

**If credentials compromised:**
- [ ] Reset affected user password immediately
- [ ] Revoke active sessions / tokens
- [ ] Check for unauthorized actions in audit logs
- [ ] Force re-authentication for sensitive operations

**If data exposed:**
- [ ] Isolate affected database / storage
- [ ] Enable immutable backups (stop writes if necessary)
- [ ] Block external data exfiltration (firewall rules)
- [ ] Enable audit logging if not already on

**If system compromised:**
- [ ] Isolate affected servers (disconnect from network)
- [ ] Preserve logs & evidence (don't restart yet)
- [ ] Snapshot the compromised system (forensics)
- [ ] Failover to backup systems if available

**If malware detected:**
- [ ] Quarantine affected server
- [ ] Stop all services on that server
- [ ] Don't restart — preserve for forensics
- [ ] Failover to clean backup

---

## 6. Mitigation & Recovery

### Mitigation Strategy

| Incident Type | Immediate Action | Short-term (24h) | Long-term (1 week) |
|---|---|---|---|
| Credential compromise | Reset password + revoke tokens | 2FA enabled + audit login logs | Implement MFA, auth review |
| SQL injection | Block malicious IP + rate limit | Code patch + SAST scan | Security review of all queries |
| Data exfiltration | Isolate affected systems | Restore from backup if needed | Encryption review + audit |
| Malware | Quarantine + failover | Analyze malware + patch | Endpoint protection review |

### Recovery Procedure

1. **Verify the threat is contained** — Is the attack still happening? Are new alerts firing?
2. **Restore from backup** — If data was modified/deleted, restore clean state
3. **Deploy patched code** — If vulnerable code was exploited, patch and redeploy
4. **Verify functionality** — Confirm systems work correctly post-recovery
5. **Enable monitoring** — Increase log verbosity to catch recurrence

---

## 7. Communication & Notification

### Internal Communication

**During incident (every 30 minutes):**
- Update `#incident-<date>` Slack channel with status
- Estimated time to resolution (ETA)
- Current impact (users affected, data at risk, etc.)
- Next steps

**After containment:**
- Send all-hands email with incident summary
- Explain what happened in business terms
- Actions taken to prevent recurrence
- No details that could help an attacker

### External Communication

**When to notify customers:**
- If their data might be affected (GDPR: within 72 hours)
- If service is down for > 30 minutes
- If their accounts were compromised

**What to say:**
- Clear, non-technical explanation
- What data was affected (be specific)
- What we're doing to fix it
- What customers should do (reset password, monitor account, etc.)
- Timeline for resolution

**Example notification:**
```
Subject: Security Incident Notification

Dear Customers,

Between 2026-10-01 14:00-15:30 UTC, we detected unauthorized access to user emails 
in our system. We immediately isolated the affected systems and verified no payment 
data was accessed.

Actions taken:
- Incident contained and systems secured
- All user sessions invalidated (you'll need to log in again)
- All affected users notified individually

What you should do:
- Reset your password when you next log in
- Monitor your email for suspicious activity
- Contact support if you see unauthorized actions

We apologize for this incident and are implementing additional security controls 
to prevent recurrence.

Security Team
```

---

## 8. Post-Incident Activities

### Immediate (Within 24 hours)

- [ ] All team members involved documented incident start/end time
- [ ] Initial facts captured: timeline, what happened, impact
- [ ] Service restored and verified working
- [ ] Monitoring/alerting increased (watch for recurrence)

### Short-term (Within 1 week)

- [ ] Root cause analysis completed: Why did this happen?
- [ ] Mitigation plan documented: How do we prevent this?
- [ ] Remediation work started: Patches, configuration changes, etc.
- [ ] Lessons learned meeting held with response team

### Long-term (Within 1 month)

- [ ] All remediation completed and verified
- [ ] This incident documented in `docs/audits/incidents/`
- [ ] Procedures updated based on lessons learned
- [ ] Team training conducted on new procedures
- [ ] Incident review presented to leadership

### Root Cause Analysis Template

```markdown
# Incident Post-Mortem: <Incident Name>

## Timeline
- 2026-10-01 14:00 UTC: Unusual login activity detected
- 2026-10-01 14:15 UTC: Security alert fired; team paged
- 2026-10-01 14:30 UTC: Attacker IP blocked; sessions revoked
- 2026-10-01 15:00 UTC: Investigation concluded; contained

## What Happened
[Describe the incident in timeline form]

## Root Cause
[Why did this happen? Single root cause or multiple?]
- Rate limiting was not enabled on login endpoint
- Attacker enumerated user accounts via /api/users/{id}

## Impact
- 150 failed login attempts
- 3 user accounts compromised
- No data exfiltration detected
- 30 minutes of team time

## What We Did Right
- Alert fired immediately
- Team responded quickly
- Escalation procedure worked

## What We Could Improve
- Rate limiting should have been there already
- Detection took 15 minutes; could be faster with SIEM

## Actions to Prevent Recurrence
1. Implement rate limiting on login (48-hour deadline)
2. Add SIEM rule for enumeration attempts (1-week deadline)
3. Security training on API security (1-month deadline)

## Owner: <Security Lead>
```

---

## 9. Incident Log

Keep a running log of all incidents (this is compliance evidence):

| Date | Incident | SEV | Root Cause | Status | Owner |
|---|---|---|---|---|---|
| 2026-10-01 | Brute force login | SEV-2 | Rate limiting missing | Resolved | John Smith |
| 2026-09-15 | Unencrypted backup | SEV-3 | Config mistake | Resolved | Jane Doe |

**Location:** `docs/audits/incidents/incident-log.md`

---

## 10. Escalation Matrix

When to escalate and to whom:

```
SEV-1 (Critical)
├─ Page security lead immediately
├─ Page CTO
├─ Notify legal (if data breach)
├─ Notify CEO (if major impact)
└─ Consider law enforcement

SEV-2 (High)
├─ Notify security lead + team lead
├─ Send email to security list
└─ Create incident ticket

SEV-3 (Medium)
├─ Notify team lead
├─ Send Slack message
└─ Create incident ticket

SEV-4 (Low)
└─ Create Jira ticket (Security label)
```

---

## 11. Contacts & Resources

### Internal Contacts

- **Security On-Call:** <phone number>
- **Ops On-Call:** <phone number>
- **CEO/CTO:** <contact>
- **Legal:** <contact>
- **Compliance Officer:** <contact>

### External Contacts

- **Cloud Provider Support:** <account number / phone>
- **Cybersecurity Incident Response:** <forensics firm contact>
- **Law Enforcement:** FBI Cyber (ic3.gov)
- **Payment Processor (if applicable):** <contact>

### Important Tools/Access

- **Incident war room:** <Zoom/Teams link>
- **Incident log:** `docs/audits/incidents/`
- **Logs/monitoring:** <CloudWatch / Splunk / ELK dashboard>
- **Key vault:** <Vault / Secrets Manager access>

---

## 12. Testing & Drills

Test this plan quarterly:

| Test | Frequency | Scenario | Owner |
|---|---|---|---|
| Tabletop exercise | Quarterly | Simulate SEV-1 incident; test response | Security Lead |
| Failover drill | Quarterly | Restore from backup; verify RTO | DevOps Lead |
| Communication drill | Semi-annually | Send test customer notification | Product Lead |

---

## Document History

| Version | Date | Changes | Author |
|---|---|---|---|
| 1.0 | <YYYY-MM-DD> | Initial document | <name> |

---

## Sign-Off

| Role | Name | Date |
|---|---|---|
| Security Lead | <name> | <YYYY-MM-DD> |
| Incident Commander | <name> | <YYYY-MM-DD> |
| CTO | <name> | <YYYY-MM-DD> |

**Next Review:** <YYYY-MM-DD> (quarterly or after incident)
