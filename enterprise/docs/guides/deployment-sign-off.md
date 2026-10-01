# Deployment Sign-Off Form

**Formal approval & evidence tracking for enterprise harness deployment.**

Use this form to record approvals, decisions, and evidence before deployment goes to production.

---

## Part 1: Deployment Information

### Deployment Details

| Field | Value |
|---|---|
| **Deployment Date** | ________________ |
| **Environment** | [ ] Test  [ ] Staging  [ ] Production |
| **Deployment Window** | Start: ________ End: ________ |
| **Rollback Plan** | [ ] Documented  [ ] Tested |
| **Communication** | [ ] Sent to team  [ ] Posted in #engineering |

### Enterprise Harness Version

| Field | Value |
|---|---|
| **Version Number** | ________________ |
| **Git Commit Hash** | ________________ |
| **Release Date** | ________________ |
| **Change Summary** | ________________ |

---

## Part 2: Pre-Deployment Verification

### Readiness Checklist Completion

- [ ] Pre-deployment readiness checklist completed
- [ ] All critical items (8/8) marked YES
- [ ] Total score: _____ / 29
- [ ] Decision: [ ] GO  [ ] CAUTION  [ ] REVIEW  [ ] STOP
- [ ] Pre-deployment sign-off completed (see below)

### Infrastructure Verification

- [ ] Target machines identified: _____ machines
- [ ] MDM / admin console access verified
- [ ] Test machine deployment successful
- [ ] Rollback mechanism tested
- [ ] Network connectivity verified
- [ ] OTLP endpoint reachable (if applicable)

### Configuration Verification

- [ ] D4_Enterprise_Harness_Form.md completed
- [ ] All sections (0-11) filled
- [ ] Plugin validated: `claude plugin validate enterprise`
- [ ] managed-settings.json created & reviewed
- [ ] managed-mcp.json created & reviewed
- [ ] CLAUDE.md reviewed & approved

---

## Part 3: Risk Assessment

### Identified Risks

**Risk 1:**
- Description: ________________________________
- Severity: [ ] Critical  [ ] High  [ ] Medium  [ ] Low
- Mitigation: ________________________________
- Owner: ________________

**Risk 2:**
- Description: ________________________________
- Severity: [ ] Critical  [ ] High  [ ] Medium  [ ] Low
- Mitigation: ________________________________
- Owner: ________________

**Risk 3:**
- Description: ________________________________
- Severity: [ ] Critical  [ ] High  [ ] Medium  [ ] Low
- Mitigation: ________________________________
- Owner: ________________

### Risk Acceptance

All identified risks have been:
- [ ] Documented
- [ ] Mitigated or accepted
- [ ] Communicated to stakeholders

---

## Part 4: Approvals & Sign-Offs

### Pre-Deployment Sign-Offs

**Technical Lead** (responsible for form completion & validation)
- Name: ________________
- Email: ________________
- Signature: ________________  Date: ________
- Confirmation: [ ] I have reviewed all documentation and verified configuration
- Notes: ________________________________

**Security Lead** (responsible for policy review & compliance)
- Name: ________________
- Email: ________________
- Signature: ________________  Date: ________
- Confirmation: [ ] Security policies reviewed and approved
- Notes: ________________________________

**Infrastructure Lead** (responsible for deployment & rollback)
- Name: ________________
- Email: ________________
- Signature: ________________  Date: ________
- Confirmation: [ ] Infrastructure is ready; rollback plan tested
- Notes: ________________________________

**Executive Sponsor** (accountable for business outcomes)
- Name: ________________
- Email: ________________
- Signature: ________________  Date: ________
- Confirmation: [ ] Approved to proceed with deployment
- Notes: ________________________________

---

## Part 5: Deployment Execution

### Pre-Deployment (Day Before)

- [ ] Final readiness meeting held
- [ ] All team members briefed on rollback procedure
- [ ] Communications tested (Slack, email, on-call)
- [ ] Backup systems verified
- [ ] Success criteria defined and agreed

### Deployment Day

**Start Time:** ________  
**Expected Duration:** ________  
**Maintenance Window:** ________

### Deployment Steps Completed

| Step | Completed | Time | Notes |
|---|---|---|---|
| Deploy to test machine | [ ] | ______ | ________________ |
| Run /status command | [ ] | ______ | ________________ |
| Run /context command | [ ] | ______ | ________________ |
| Run /doctor command | [ ] | ______ | ________________ |
| Run write-attempt test | [ ] | ______ | ________________ |
| Deploy to staging (if applicable) | [ ] | ______ | ________________ |
| Run all verification checks | [ ] | ______ | ________________ |
| Deployment to production | [ ] | ______ | ________________ |
| Post-deployment verification | [ ] | ______ | ________________ |

### On-Call Contacts

**During Deployment:**
- Technical Lead: ________________ Phone: ________
- Security Lead: ________________ Phone: ________
- Infrastructure Lead: ________________ Phone: ________
- Escalation Contact: ________________ Phone: ________

**After Deployment (First Week):**
- Daily check-in: [ ] Scheduled for ________ at ________
- Issues hotline: ________________
- Escalation procedure: ________________________________

---

## Part 6: Post-Deployment Verification

### Verification Checklist

- [ ] VERIFY.md checklist completed (all 12 items)
- [ ] /status shows enterprise source
- [ ] /context loads enterprise CLAUDE.md
- [ ] /mcp shows admitted servers only
- [ ] /agents shows 5 roles
- [ ] /skills shows seed skills
- [ ] /hooks shows enterprise hooks
- [ ] /doctor reports no problems
- [ ] Write-attempt test refuses edit (with trace)
- [ ] Team can access guidance documents

### Evidence Collected

| Item | Evidence Location | Date Collected |
|---|---|---|
| /status output | ________________ | ________ |
| /context output | ________________ | ________ |
| /mcp output | ________________ | ________ |
| /doctor output | ________________ | ________ |
| Write-attempt trace | ________________ | ________ |
| Team feedback | ________________ | ________ |

---

## Part 7: Success Metrics

### KPI Baseline (Pre-Deployment)

| KPI | Baseline Value | Target | Measurement |
|---|---|---|---|
| KPI 1: __________ | ________ | ________ | ________________ |
| KPI 2: __________ | ________ | ________ | ________________ |
| KPI 3: __________ | ________ | ________ | ________________ |

### KPI Measurement (Post-Deployment)

Measured on: ________ (1 week after deployment)

| KPI | Week 1 Value | Status | Notes |
|---|---|---|---|
| KPI 1 | ________ | [ ] ✅ On track | ________________ |
| KPI 2 | ________ | [ ] ✅ On track | ________________ |
| KPI 3 | ________ | [ ] ✅ On track | ________________ |

---

## Part 8: Issues & Resolutions

### Issues Encountered During Deployment

**Issue 1:**
- Description: ________________________________
- Severity: [ ] Critical  [ ] High  [ ] Medium  [ ] Low
- Resolution: ________________________________
- Time to resolve: ________ minutes
- Permanent fix: [ ] Applied  [ ] Pending

**Issue 2:**
- Description: ________________________________
- Severity: [ ] Critical  [ ] High  [ ] Medium  [ ] Low
- Resolution: ________________________________
- Time to resolve: ________ minutes
- Permanent fix: [ ] Applied  [ ] Pending

---

## Part 9: Rollback Decision

### Rollback Assessment (Complete if issues occur)

- [ ] Issue occurred that requires rollback
- Issue: ________________________________
- **Severity:** [ ] Critical  [ ] High  [ ] Medium  [ ] Low

**Rollback Decision:**
- [ ] ROLLBACK INITIATED
- [ ] Time started: ________
- [ ] Time completed: ________
- [ ] Status: [ ] Successful  [ ] Partial  [ ] Failed

**If rollback needed:**
- Reason: ________________________________
- Impact: ________________________________
- Mitigation steps: ________________________________
- Follow-up plan: ________________________________

---

## Part 10: Post-Deployment Review (1 Week After)

### Team Feedback

**What went well:**
- ________________________________
- ________________________________
- ________________________________

**What could be improved:**
- ________________________________
- ________________________________
- ________________________________

**Lessons learned:**
- ________________________________
- ________________________________

### Post-Deployment Sign-Offs

**Technical Lead** (confirms deployment successful)
- Signature: ________________  Date: ________
- Status: [ ] ✅ Deployed Successfully  [ ] ⚠️ Deployed with issues  [ ] ❌ Rolled back

**Security Lead** (confirms policies enforced)
- Signature: ________________  Date: ________
- Status: [ ] ✅ Policies active  [ ] ⚠️ Partial enforcement  [ ] ❌ Not enforced

**Executive Sponsor** (confirms KPIs on track)
- Signature: ________________  Date: ________
- Status: [ ] ✅ KPIs met  [ ] ⚠️ KPIs trending  [ ] ❌ KPIs missed

---

## Part 11: Deployment Archive

### Documentation Stored

- [ ] This form archived in: ________________
- [ ] Pre-deployment readiness checklist filed in: ________________
- [ ] Deployment log filed in: ________________
- [ ] Risk register updated in: ________________
- [ ] Post-incident review (if needed) filed in: ________________

### Approval to Close

All items completed. Deployment officially closed on: ________

Closed by: ________________ (Technical Lead)

---

## Quick Reference

### Success Criteria

✅ **Deployment is successful when:**
- All critical items in pre-deployment checklist are YES
- All approvers have signed off
- VERIFY.md checklist all passed
- Write-attempt test refuses edits
- Team can access and understand policies
- KPIs are on track or trending positively

### Failure Criteria

❌ **Rollback is triggered when:**
- Critical security policy not enforcing
- Write boundary is not working (edits are allowed)
- /doctor reports unresolved problems
- Infrastructure not reachable
- KPIs significantly below baseline

---

## 📝 Notes

- **Keep this form for audit records** — evidence of governance
- **File with pre-deployment checklist** — forms a complete deployment record
- **Update during deployment** — don't wait until the end to capture info
- **Share with stakeholders** — transparency builds confidence
- **Review in post-incident** — if issues arise later, this is your starting point

---

**Last Updated:** 2026-10-01  
**Version:** 1.0  
**Use with:** `pre-deployment-readiness.md` and `deployment-guide.md`
