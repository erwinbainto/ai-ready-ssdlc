# ADR-001: <Decision Title>

**Date:** YYYY-MM-DD  
**Status:** ACCEPTED (or SUPERSEDED, DEPRECATED)  
**Supercedes:** ADR-NNN (if applicable)

---

## Context

Describe the problem or constraint that motivated this decision:
- What was the business or technical need?
- What were the constraints (performance, compliance, team skill, timeline)?
- What options were being considered?
- Why is this decision important?

### Background
Provide any historical context:
- How did we get here?
- What decisions led to this point?
- What has changed in the environment (new requirements, technology, team size)?

### Stakeholders
Who needs to be involved in this decision?
- Development team
- Security team
- Operations/DevOps
- Product/business owners
- Legal/compliance (if applicable)

---

## Decision

**We decided to [CHOICE] because [RATIONALE].**

### High-Level Approach

Describe the chosen approach clearly and concisely:
- What pattern or technology did we select?
- How does it work?
- What problem does it solve?

### Implementation

Outline how this decision will be implemented:
- What code changes are required?
- What configuration or infrastructure changes?
- What team or skill involvement is needed?
- What's the rollout plan (big bang vs phased)?

### Enforcement

How do we ensure this decision is followed?
- Code review checklist items
- Linting or build-time rules
- Architecture guardrails or constraints
- Documentation or training

---

## Consequences

### Benefits

Positive outcomes of this decision:
- Performance improvement (e.g., "reduces query time from 5s to 500ms")
- Maintainability ("new team members onboard 2x faster")
- Reliability ("99.99% uptime SLA achievable")
- Compliance ("meets PCI-DSS requirement 3.4")
- Developer experience ("IDE support for type checking")

### Trade-offs & Drawbacks

What we're giving up or what becomes harder:
- Cost: "license fees $50k/year" or "additional infrastructure $10k/month"
- Complexity: "10% code increase but 50% faster queries"
- Learning curve: "requires 2 weeks of team training"
- Flexibility: "cannot easily switch database vendors"
- Lock-in: "tied to vendor X's APIs"

### Risks

What could go wrong, and how do we mitigate?
- **Risk:** Database migration from old system fails
  - **Mitigation:** Rollback procedure tested in staging; backward compatibility maintained for 30 days
- **Risk:** Performance degrades under load
  - **Mitigation:** Load testing required before production; monitoring in place; scaling policy defined

---

## Alternatives Considered

### Option A: <Alternative Name>

**Approach:**
How would this work?

**Pros:**
- Pro 1
- Pro 2

**Cons:**
- Con 1 (critical show-stopper)
- Con 2

**Why rejected:** Briefly explain why this wasn't chosen.

---

### Option B: <Alternative Name>

**Approach:**
How would this work?

**Pros:**
- Pro 1
- Pro 2

**Cons:**
- Con 1
- Con 2

**Why rejected:** Briefly explain why this wasn't chosen.

---

### Option C: <Alternative Name>

**Approach:**
How would this work?

**Pros:**
- Pro 1
- Pro 2

**Cons:**
- Con 1
- Con 2

**Why rejected:** Briefly explain why this wasn't chosen.

---

## Related Decisions

- **ADR-NNN:** Title of related ADR (explain relationship)
- **ADR-MMM:** Title of related ADR (explain relationship)

## Related Code

- Backend: `src/main/java/com/company/product/domain/` (link to implementation)
- Frontend: `src/app/modules/domain/` (link to implementation)
- Configuration: `.claude/rules/architectural-patterns.md` (where this pattern is enforced)

## Related Tests

- Test plan: `docs/testing/test-plan.md#Section` (test scenarios that verify this pattern)
- Example test: `src/test/java/com/company/product/domain/IntegrationTest.java` (specific test class)

## Reference Documentation

- [External reference 1](#) (e.g., Spring documentation, RFC, vendor guide)
- [External reference 2](#) (research paper, architectural pattern, best practice guide)

---

## Discussion

### Questions Asked During Review

**Q: How does this affect performance?**  
A: Benchmarks show a 30% improvement in query time for the main use case. Trade-off: 5% increase in memory usage.

**Q: Can we migrate from the old system without downtime?**  
A: Yes, via a dual-write period. Both systems write for 2 weeks, then we cut over to the new system.

**Q: What's the cost?**  
A: Initial setup is 4 engineer-weeks. Long-term operations cost is 2% of current infrastructure spend.

---

## Implementation Checklist

- [ ] Code changes implemented (link to PR or branch)
- [ ] Configuration updates deployed
- [ ] Monitoring and alerts set up
- [ ] Runbook created for on-call team
- [ ] Team training completed (dates, attendees)
- [ ] Enforcement rules added to CI/CD or code review checklist
- [ ] Documentation updated
- [ ] Related ADRs linked and updated

---

## Rollout Timeline

| Date | Milestone | Owner | Status |
|---|---|---|---|
| YYYY-MM-DD | Design review and decision | Tech lead | ✅ Complete |
| YYYY-MM-DD | Implementation sprint | Dev team | 🔄 In progress |
| YYYY-MM-DD | Staging deployment | DevOps | ⏱️ Planned |
| YYYY-MM-DD | Production rollout | DevOps | ⏱️ Planned |

---

## Lessons Learned (Post-Implementation)

*To be filled in after implementation and monitoring.*

**What went well:**
- Aspect 1
- Aspect 2

**What could be improved:**
- Aspect 1
- Aspect 2

**Metrics:**
- KPI 1: Baseline vs actual
- KPI 2: Baseline vs actual

---

## Revisions

| Date | Author | Change |
|---|---|---|
| YYYY-MM-DD | Name | Initial decision |
| YYYY-MM-DD | Name | Clarified section X after implementation |

---

## How to Use This ADR

1. **Understanding the decision:** Read "Context" and "Decision" sections
2. **Implementing the pattern:** See "Implementation" and "Related Code"
3. **Verifying compliance:** Check "Enforcement" and related code review rules
4. **Challenging the decision:** See "Alternatives Considered" and "Trade-offs"
5. **Updating the decision:** File a new ADR that supersedes this one; link them together
