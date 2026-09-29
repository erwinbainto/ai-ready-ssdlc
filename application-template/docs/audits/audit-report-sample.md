# Code Review & Security Audit Report

**Application:** <APPLICATION_NAME>  
**Date:** 2026-09-29  
**Reviewed by:** security-auditor + code-reviewer agents  
**Status:** OPEN (findings require remediation)  
**Review scope:** Backend API controllers, database layer, dependency scan  

---

## Executive Summary

This audit reviewed the recently implemented invoice import feature ([PR #142](https://example.com/pr/142)) for correctness, security compliance, and architectural pattern adherence.

**Findings summary:**
- ✅ **0 Critical** — All blockers resolved
- ⚠️ **2 High** — Require remediation before production
- 📋 **3 Medium** — Backlog items for next sprint
- ℹ️ **1 Low** — Code quality, non-blocking

**Overall status:** READY FOR STAGING (after High findings resolved)

**Next step:** Tech lead reviews this report and approves remediation plan.

---

## Critical Findings

**None.** All critical-severity items have been resolved.

---

## High-Severity Findings

### H001: Missing SQL Parameterization in Legacy Reconciliation Query

**Component:** `ReconcileInvoiceJob.java:142`

**Evidence:**
```java
// INSECURE: String concatenation allows SQL injection
String sql = "SELECT * FROM invoice WHERE invoice_dt > '" + startDate + "'";
```

**Finding:** The reconciliation query constructs SQL via string concatenation, allowing SQL injection attacks.

**Proposal:**
Use parameterized queries (PreparedStatement or JPA Criteria):
```java
// SECURE: Parameterized query
String sql = "SELECT * FROM invoice WHERE invoice_dt > ?";
preparedStatement.setDate(1, startDate);
```

**Consequence if not fixed:**
- **Risk:** Attacker could modify query to extract or delete invoice data
- **Severity:** CRITICAL (regulatory violation, data breach risk)
- **Detection:** OWASP Dep-Check, SonarQube SQL injection scanner

**Remediation effort:** 4 hours (identify all affected queries, convert to parameterized form)

**Related ADR:** [ADR-009: Sargable Date Predicates](../architecture/adr/ADR-009-database-indexes-date-range-predicates.md)

**Timeline:** Fix before production deployment (blocking)

---

### H002: Unvalidated User Input on Batch Upload Endpoint

**Component:** `InvoiceImportController.java:67`

**Evidence:**
```java
@PostMapping("/import")
public ResponseEntity<ImportResult> importInvoices(@RequestParam MultipartFile file) {
    // INSECURE: No file size or type validation
    ZipFile zipFile = new ZipFile(file.getInputStream());
    // ... process entries directly
}
```

**Finding:** The import endpoint accepts file uploads without validating file size, type, or content structure. An attacker could:
- Upload files larger than available disk space (DoS attack)
- Upload non-ZIP files, causing parser errors
- Upload ZIP bombs (highly compressed files expanding to massive size)

**Proposal:**
1. Enforce file size limit (max 1GB):
   ```java
   if (file.getSize() > 1_000_000_000) {
       throw new ValidationException("File exceeds 1GB limit");
   }
   ```

2. Validate file type:
   ```java
   if (!file.getContentType().equals("application/zip")) {
       throw new ValidationException("Only ZIP files allowed");
   }
   ```

3. Validate ZIP structure before processing:
   ```java
   try (ZipFile zipFile = new ZipFile(file.getInputStream())) {
       zipFile.getFileHeader("required_manifest.txt"); // Verify expected structure
   }
   ```

4. Set JVM limits for ZIP processing.

**Consequence if not fixed:**
- **Risk:** Denial of service, resource exhaustion, processing errors
- **Severity:** HIGH (operational impact, availability risk)

**Remediation effort:** 6 hours (add validators, write tests for edge cases)

**Related ADR:** [ADR-001: Input Validation](../architecture/adr/ADR-001-secure-defaults.md)

**Timeline:** Fix before production deployment (blocking)

---

## Medium-Severity Findings

### M001: Missing Transactional Boundary on Batch Writes

**Component:** `ImportInvoiceJob.java:89`

**Evidence:**
```java
// POTENTIAL ISSUE: No @Transactional on batch commit points
public void processBatch(List<Invoice> batch) {
    batch.forEach(invoice -> repository.save(invoice));
    // If an error occurs mid-loop, partial data is committed
}
```

**Finding:** Each `save()` call within the loop creates a separate transaction, allowing partial batch commits if an error occurs mid-loop. This violates the atomicity expectation.

**Proposal:**
Wrap batch operations in a single transaction with appropriate boundary:
```java
@Transactional(propagation = Propagation.REQUIRES_NEW)
public void processBatch(List<Invoice> batch) {
    batch.forEach(invoice -> repository.save(invoice));
}
```

Or use batch insert for better performance.

**Consequence if not fixed:**
- **Risk:** Partial imports if process crashes; data inconsistency
- **Severity:** MEDIUM (correctness issue, not a blocker for staging)

**Remediation effort:** 3 hours (add @Transactional, write tests for partial failure scenarios)

**Related ADR:** [ADR-007: Purge Batch Deletion Requires New](../architecture/adr/ADR-007-purge-batch-deletion-requires-new.md)

**Timeline:** Include in next sprint (not blocking, but important)

---

### M002: Test Coverage Below Target (78% vs 80% requirement)

**Component:** Full backend codebase

**Evidence:**
```
JaCoCo Report Summary
Branches: 76%
Instructions: 78%
Lines: 78%
Target: 80%
Status: BELOW TARGET
```

**Finding:** Line coverage is 2 percentage points below the CI gate threshold. Missing tests for:
- `InvoiceImportController.handleException()` — error scenario
- `ReconcileInvoiceService.reconcile()` — edge case for zero invoices

**Proposal:**
Add tests for the two identified gaps:
```java
@Test
void testImportWithZeroInvoices() {
    // Test behavior when invoice batch is empty
}

@Test
void testControllerExceptionHandling() {
    // Test error response formatting
}
```

**Consequence if not fixed:**
- **Risk:** Code path may have bugs (low risk, as logic is mostly tested)
- **Severity:** MEDIUM (CI gate blocker, easily fixed)

**Remediation effort:** 2 hours (write 2 tests)

**Timeline:** Include in next code review cycle (blocking PR merge until fixed)

---

### M003: Deprecation Warnings in Frontend Dependencies

**Component:** `package.json`

**Evidence:**
```
npm audit
High: 1 package (ng-bootstrap@14.x using Angular 18 APIs)
Recommendation: Upgrade to ng-bootstrap@16.x for Angular 19 compatibility
```

**Finding:** Frontend dependencies have deprecation warnings. Not a security issue, but creates technical debt.

**Proposal:**
Upgrade `ng-bootstrap` to v16 and test component rendering.

**Effort:** 1 hour (dependency update + smoke tests)

**Timeline:** Deferred to next minor release (not blocking)

---

## Low-Severity Findings

### L001: Unused Import in Import Job

**Component:** `ImportInvoiceJob.java:5`

**Evidence:**
```java
import com.rrd.ir.utils.DateUtilsLegacy; // Unused since refactoring
```

**Finding:** Dead code; no functional impact.

**Proposal:** Remove unused import.

**Timeline:** Include in next code quality pass (not blocking)

---

## Dependency Scan Results

### CVE Summary

| CVE | Component | Severity | Status |
|---|---|---|---|
| CVE-2024-1234 | jackson-databind 2.17.0 | HIGH | ⚠️ Unpatched |
| CVE-2024-5678 | spring-framework 6.1.0 | MEDIUM | ✅ Patched in 6.1.2 |
| CVE-2024-9999 | log4j 2.21.0 | LOW | ✅ Patched in 2.21.1 |

**Action:** Upgrade jackson-databind to 2.17.1+ before production deployment.

---

## Code Style Compliance

| Check | Status | Details |
|---|---|---|
| Checkstyle | ✅ PASS | 0 violations |
| ESLint | ✅ PASS | 0 errors, 2 warnings (unused variable, fixable) |
| SpotBugs | ⚠️ WARNINGS | 1 potential null pointer, 1 resource leak (investigate) |

---

## Performance Analysis

| Metric | Value | Baseline | Status |
|---|---|---|---|
| API latency (p99) | 512ms | 500ms | ⚠️ +2.4% (acceptable) |
| Memory usage | 1.2GB | 1.1GB | ⚠️ +9% (within threshold) |
| Database queries per request | 3 | 2 | ⚠️ +1 query (investigate) |

**Finding:** Extra database query is due to new reconciliation check. Trade-off is acceptable for correctness.

---

## Security Checklist

| Item | Status | Notes |
|---|---|---|
| No hardcoded credentials | ✅ PASS | All secrets use environment variables |
| HTTPS enforced | ✅ PASS | TLS 1.2+ required |
| CORS configured | ✅ PASS | Specific origins allowed |
| SQL injection protected | ⚠️ PARTIAL | See High finding H001 |
| XSS protections | ✅ PASS | Angular auto-escaping enabled |
| CSRF tokens | ✅ PASS | Enabled for POST/PUT/DELETE |
| Rate limiting | ✅ PASS | 100 requests/minute per IP |
| Authentication | ✅ PASS | JWT + Cognito |
| Authorization | ✅ PASS | Role-based access control |

---

## Architectural Compliance

| ADR | Status | Notes |
|---|---|---|
| ADR-001: Composite Key | ✅ PASS | Invoice composite key properly enforced |
| ADR-007: REQUIRES_NEW | ⚠️ PARTIAL | See Medium finding M001 |
| ADR-009: Sargable Predicates | ⚠️ PARTIAL | See High finding H001 |
| ADR-011: Chunk-flush | ✅ PASS | Memory bounded correctly |
| ADR-013: Defense-in-depth | ✅ PASS | Cognito + TYK gateway configured |

---

## Remediation Plan

### Immediate (Blocking Production)

| Finding | Owner | Timeline | Status |
|---|---|---|---|
| H001: SQL Parameterization | Backend team | 1 day | 📋 OPEN |
| H002: Input Validation | Backend team | 1 day | 📋 OPEN |
| CVE-2024-1234: jackson-databind | Backend team | 4 hours | 📋 OPEN |

### Short-term (Next Sprint)

| Finding | Owner | Timeline | Status |
|---|---|---|---|
| M001: Transactional Boundary | Backend team | 3 hours | 📋 BACKLOG |
| M002: Test Coverage | QA team | 2 hours | 📋 BACKLOG |
| SpotBugs warnings | Backend team | 2 hours | 📋 BACKLOG |

### Deferred

| Finding | Owner | Timeline | Status |
|---|---|---|---|
| M003: ng-bootstrap upgrade | Frontend team | Next minor release | 📋 DEFERRED |
| L001: Unused import | Backend team | Next code quality pass | 📋 DEFERRED |

---

## Sign-offs Required

- [ ] **Security team:** High-severity CVE and input validation findings reviewed and approved
- [ ] **Tech lead:** Remediation plan acceptable; production deployment approved after blockers resolved
- [ ] **QA team:** Test coverage plan reviewed; retesting required after fixes

---

## Related Documentation

- **Relevant ADRs:** [ADR-007](../architecture/adr/ADR-007-purge-batch-deletion-requires-new.md), [ADR-009](../architecture/adr/ADR-009-database-indexes-date-range-predicates.md), [ADR-013](../architecture/adr/ADR-013-cognito-tyk-defense-in-depth-profiled-security.md)
- **Specifications:** [API Reference](../specs/api-reference.md), [Security specs](../specs/business-specs.md#Security)
- **Testing:** [Test plan](../testing/test-plan.md#Import-Job-Scenarios)
- **Previous audits:** [audit-report-2026-09-01.md](./audit-report-2026-09-01.md)

---

## Appendix: Tool Outputs

### Full SonarQube Report

[SonarQube link: example.com/sonarqube/invoice-retention](example.com/sonarqube/invoice-retention)

### JaCoCo Coverage Report

[JaCoCo link: example.com/jacoco/coverage.html](example.com/jacoco/coverage.html)

### Dependency Check Report

[OWASP Dep-Check: example.com/dc/dependency-check.html](example.com/dc/dependency-check.html)

---

## Next Steps

1. **Dev team:** Review findings, estimate effort for each item
2. **Tech lead:** Approve remediation plan or request changes
3. **Security team:** Approve security-related findings (H001, H002)
4. **Dev team:** Implement fixes for blocking items (H001, H002, CVE)
5. **QA team:** Re-run audit after fixes; verify blockers resolved
6. **Tech lead:** Final approval for staging/production deployment

---

## Sign-off

| Role | Name | Date | Status |
|---|---|---|---|
| Security reviewer | [Name] | 2026-09-29 | ⏳ Pending |
| Tech lead | [Name] | 2026-09-29 | ⏳ Pending |
| QA lead | [Name] | 2026-09-29 | ⏳ Pending |
