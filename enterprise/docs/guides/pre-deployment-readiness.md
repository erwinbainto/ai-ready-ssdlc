# Pre-Deployment Readiness Checklist

**Things that must be ready BEFORE deployment starts. Complete this before opening D4_Enterprise_Harness_Form.md**

---

## ⚠️ Critical Gate Items (MUST be YES)

These are deal-breakers. If any is "no," stop and resolve before proceeding.

### Executive & Governance

- [ ] **Executive sponsor identified** — Who is accountable for this deployment?
  - [ ] Name & title: ________________
  - [ ] Email: ________________
  - [ ] Sign-off authority? YES / NO

- [ ] **Security leadership engaged** — Does security team understand the policy?
  - [ ] Security lead name: ________________
  - [ ] Security review scheduled? YES / NO
  - [ ] Budget allocated? YES / NO

- [ ] **Compliance/Legal review** — Is this compliant with regulations?
  - [ ] Compliance lead name: ________________
  - [ ] GDPR/HIPAA/SOX applicable? YES / NO
  - [ ] Legal approved? YES / NO

### Architecture & Planning

- [ ] **KPIs defined & frozen** — From D3 (Deployment Design Document)
  - [ ] KPI 1: ________________
  - [ ] KPI 2: ________________
  - [ ] KPI 3: ________________
  - [ ] KPIs documented in D3? YES / NO
  - **→ If NO, escalate and stop. Cannot proceed without this.**

- [ ] **Memory tier definitions agreed** — How Claude Code memory is structured
  - [ ] Session tier defined? YES / NO
  - [ ] Project tier defined? YES / NO
  - [ ] Organization tier defined? YES / NO
  - **→ If NO, escalate and stop. Cannot proceed without this.**

- [ ] **Gating decisions ready** (Section 0 of enterprise form)
  - [ ] 0.1 Gateway routing decided? YES / NO
  - [ ] 0.2 MDM reliability assessed? YES / NO
  - [ ] 0.6 KPIs frozen confirmed? YES / NO
  - [ ] 0.7 Memory tiers confirmed? YES / NO

---

## ✅ Standard Readiness Items (Should be YES)

These are important but can be addressed during deployment with management approval.

### Team & Resources

- [ ] **Technical lead assigned** — Who will lead enterprise setup?
  - Name: ________________
  - Email: ________________
  - Available time: _____ hours
  - Backup: ________________

- [ ] **Security team assigned** — Who will review policies?
  - Name: ________________
  - Email: ________________
  - Available time: _____ hours

- [ ] **DevOps/Infrastructure assigned** — Who will deploy to machines?
  - Name: ________________
  - Email: ________________
  - Available time: _____ hours
  - Access to MDM / admin console? YES / NO

- [ ] **Team trained** — Has team reviewed Claude Code basics?
  - [ ] Technical lead completed Claude Code training? YES / NO
  - [ ] DevOps team knows deployment targets? YES / NO
  - [ ] Security team understands policy model? YES / NO

### Infrastructure & Access

- [ ] **Infrastructure ready** — Can machines receive updates?
  - [ ] MDM or admin console access? YES / NO
  - [ ] System path access (Route A)? YES / NO
  - [ ] OR server-managed delivery (Route B)? YES / NO
  - [ ] At least one test machine available? YES / NO

- [ ] **Claude Code installed** — Is Claude Code already deployed?
  - [ ] Version: ________________
  - [ ] On test machine? YES / NO
  - [ ] On at least 3 target machines? YES / NO

- [ ] **Network & security** — Are connections ready?
  - [ ] Firewall rules for Claude services? YES / NO
  - [ ] Proxy configuration (if needed)? YES / NO
  - [ ] VPN access tested? YES / NO
  - [ ] OTLP endpoint reachable? YES / NO

### Documentation & Planning

- [ ] **Deployment plan drafted** — Do you have a plan?
  - [ ] Timeline: ________________
  - [ ] Rollback plan documented? YES / NO
  - [ ] Escalation contacts identified? YES / NO
  - [ ] Communication plan ready? YES / NO

- [ ] **Risk assessment completed** — Have you identified risks?
  - Risk 1: ____________________
  - Risk 2: ____________________
  - Risk 3: ____________________
  - [ ] Mitigation plans documented? YES / NO

- [ ] **Business continuity** — What if deployment fails?
  - [ ] Rollback procedure documented? YES / NO
  - [ ] Backup plan? YES / NO
  - [ ] Support contacts 24/7? YES / NO

---

## 📋 Policy & Compliance Readiness

- [ ] **Compliance frameworks identified** — Which apply to your org?
  - [ ] SOC 2? YES / NO
  - [ ] ISO 27001? YES / NO
  - [ ] HIPAA? YES / NO
  - [ ] GDPR? YES / NO
  - [ ] PCI DSS? YES / NO
  - [ ] Other: ____________________

- [ ] **Data classification ready** — How do you classify data?
  - [ ] Public: definition agreed? YES / NO
  - [ ] Internal: definition agreed? YES / NO
  - [ ] Confidential: definition agreed? YES / NO
  - [ ] Restricted/PII: definition agreed? YES / NO

- [ ] **Security baselines defined** — What's the minimum security level?
  - [ ] Authentication requirements? YES / NO
  - [ ] Encryption requirements? YES / NO
  - [ ] Audit logging requirements? YES / NO
  - [ ] Access control model? YES / NO

---

## 🔍 Go/No-Go Assessment

### Scoring

Count your YES answers:

- **Critical Items (8 questions):** How many YES? _____ / 8
- **Standard Items (15 questions):** How many YES? _____ / 15
- **Compliance Items (6 questions):** How many YES? _____ / 6

**TOTAL:** _____ / 29

### Decision Matrix

| Score | Status | Action |
|---|---|---|
| **8/8 critical + 25+/29 total** | ✅ GO | Proceed to D4_Enterprise_Harness_Form.md |
| **8/8 critical + 20-24/29 total** | ⚠️ CAUTION | Proceed with manager approval; address gaps during Phase 1 |
| **8/8 critical + <20/29 total** | 🟡 REVIEW | Escalate for review; address critical gaps |
| **<8/8 critical** | ❌ STOP | Cannot proceed. Resolve critical items first. |

---

## 📝 Readiness Sign-Off

When all critical items (8/8) are YES, sign below to confirm readiness:

```
Technical Lead: ________________  Date: ________
Security Lead: ________________   Date: ________
Infrastructure Lead: ________________  Date: ________
Executive Sponsor: ________________  Date: ________
```

---

## 🚀 Next Steps

### If GO (8/8 critical + 25+/29 total)

1. ✅ Schedule D4_Enterprise_Harness_Form.md session
2. ✅ Open `enterprise/docs/guides/00-start-here.md`
3. ✅ Begin Section 0 (gating decisions)
4. ✅ Reference this checklist as needed

### If CAUTION (8/8 critical + 20-24/29 total)

1. ✅ Document gaps: ____________________
2. ✅ Get manager approval to proceed
3. ✅ Plan to address gaps during Phase 1
4. ✅ Begin D4 form with manager awareness

### If REVIEW or STOP

1. ❌ Resolve critical gaps first
2. ⏸️ Re-run this checklist
3. ⚠️ Escalate to executive sponsor
4. 📅 Reschedule when ready

---

## 📌 Tips

- **Complete this checklist 1 week before deployment starts**
- **Involve all stakeholders** (technical, security, executive)
- **Be honest about gaps** — better to know now than mid-deployment
- **Use this as your readiness scorecard** — share with leadership
- **Keep this document for deployment records** — evidence of readiness

---

## 📄 Related Documents

- **Next:** `D4_Enterprise_Harness_Form.md` — Enterprise configuration form
- **Reference:** `enterprise/docs/guides/00-start-here.md` — Enterprise guides
- **Sign-off:** `deployment-sign-off.md` — Final approval before production

---

**Status:** Ready to deploy when all critical items are YES and team is signed off.

**Last Updated:** 2026-10-01  
**Version:** 1.0
