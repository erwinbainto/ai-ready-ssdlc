# Testing & Verification

This folder contains test plans, test scenarios, and verification procedures for the application. These are the **requirements** for what must be tested and how; the **actual test code** lives in the repository (backend `src/test/`, frontend `src/**/*.spec.ts`).

---

## Contents

### Test Plans & Strategies

- **`test-plan.md`** — Comprehensive test strategy
  - Test pyramid (unit, integration, end-to-end)
  - Coverage targets and enforcement gates
  - Critical scenarios that must not regress
  - Test scenario descriptions for each feature
  - Performance and load testing procedures

### Feature Test Scenarios

Test requirements organized by feature or component:
- Search and filtering test scenarios
- Create/edit/delete workflows
- Batch job execution and error handling
- API endpoint contracts
- Frontend component interactions
- Authentication and authorization flows

### Critical Invariants

Scenarios tied to architectural decisions that must always be verified:
- Data integrity constraints (composite keys, uniqueness)
- Transactional boundaries (ACID properties)
- Performance patterns (batch processing, pagination)
- Security patterns (no hardcoded secrets, parameterized queries)

---

## Test Pyramid

```
        E2E (end-to-end)
       /              \
      /  Integration   \
     /____________________\
    /                      \
   / Unit Tests (fast)      \
  /____________________________\

- Bottom (Unit): Fast, many tests, isolated, 70% of tests
- Middle (Integration): Moderate speed, 20% of tests
- Top (E2E): Slow, few tests, full workflow, 10% of tests
```

**Target coverage:**
- **Unit tests:** 80%+ line coverage (backend Java, frontend TypeScript)
- **Integration tests:** 80%+ code path coverage
- **E2E tests:** 100% of critical user workflows

---

## Test Naming Conventions

### Backend (JUnit)

```java
// Pattern: Test[ComponentName][Method][Scenario]
class SearchServiceTest {
    @Test
    void testSearchByDateRange_WithValidDates_ReturnsMatchingRecords() { }
    
    @Test
    void testSearchByDateRange_WithEmptyResults_ReturnsEmptyList() { }
    
    @Test
    void testSearchByDateRange_WithInvalidDateOrder_ThrowsException() { }
}

// Pattern for Spring Boot integration tests
@SpringBootTest
class SearchControllerIntegrationTest {
    @Test
    void testSearchEndpoint_WithValidQuery_Returns200AndResults() { }
}
```

### Frontend (Jasmine)

```typescript
// Pattern: describe.it pattern matching test intent
describe('SearchComponent', () => {
  it('should display search results when user types query', () => { });
  it('should display no results message when search returns empty', () => { });
  it('should apply date filter when user selects date range', () => { });
});
```

### Test IDs

Use semantic test IDs for E2E tests:
```html
<!-- HTML -->
<button data-testid="search-submit-button">Search</button>
<input data-testid="search-date-start" />

// E2E test
cy.get('[data-testid="search-submit-button"]').click();
```

---

## Coverage Requirements

| Component | Tool | Target | CI Gate |
|---|---|---|---|
| Backend (Java) | JaCoCo | 80% line coverage | Enforced by `mvn test` |
| Frontend (TypeScript) | Istanbul | 80% line coverage | Enforced by `npm test` |
| Backend lint | Checkstyle | No violations | Enforced in CI |
| Frontend lint | ESLint | No errors | Enforced in CI |

### Checking Coverage Locally

```bash
# Backend coverage report
cd backend
mvn clean test
open target/site/jacoco/index.html  # View HTML report

# Frontend coverage report
cd frontend
npm run test -- --coverage
open coverage/index.html  # View HTML report
```

---

## Critical Test Scenarios (Must Not Regress)

⚠️ These are tied to architectural decisions, business logic, or security requirements. **All must pass before any PR merge:**

### Backend Critical Scenarios

- **Data Integrity:**
  - Composite key uniqueness enforced (no duplicate records)
  - Foreign key constraints preserved
  - Cascade delete works correctly

- **Batch Processing (if applicable):**
  - Transactional boundaries respected (REQUIRES_NEW pattern)
  - Partial failures don't corrupt state (all-or-nothing semantics)
  - Chunk flush prevents memory exhaustion
  - Page-0 deletion loop works (always reset page to 0 after delete)

- **Query Correctness:**
  - Sargable predicates used (no YEAR() or DATEPART() functions)
  - Date range queries are inclusive on both ends
  - Pagination returns correct record count
  - Sorting is deterministic (no random ordering)

- **Security:**
  - SQL injection prevented (parameterized queries)
  - XSS prevented (output encoding)
  - CSRF tokens validated
  - Authentication required on protected endpoints
  - Authorization checked per-user

### Frontend Critical Scenarios

- **Component Rendering:**
  - Standalone components initialized correctly
  - Data binding two-way (input ↔ component ↔ service)
  - Forms validate user input before submission
  - Error messages display on validation failure

- **State Management (NgRx/Redux):**
  - Actions dispatched correctly
  - Reducers update state immutably
  - Selectors memoized (no unnecessary re-renders)
  - Effects handle async operations

- **API Integration:**
  - HTTP interceptors add auth headers
  - Error responses handled (4xx, 5xx)
  - Loading states display during requests
  - Retry logic works on transient failures

---

## When to Add Test Scenarios

Add to this folder when:
- Designing a new feature (add test scenarios **before** implementation)
- Designing a batch job (add scenario covering happy path, error cases, edge cases)
- Defining a new API endpoint (add API test scenarios)
- Documenting a critical invariant (add test that verifies it)
- Preparing a lab exercise for training (add scenario with step-by-step instructions)

**Do NOT add here:**
- Actual test code (JUnit, Jasmine) — that lives in `src/test/` and `src/**/*.spec.ts`
- How-to guides (→ `docs/guides/`)
- Business requirements (→ `docs/specs/`)
- System design and architecture (→ `docs/architecture/`)
- Audit findings (→ `docs/audits/`)

---

## Test Execution

### Running All Tests Locally

```bash
# Backend unit tests
cd backend
mvn clean test

# Frontend unit tests
cd frontend
npm run test

# Both with coverage
cd backend && mvn clean test && cd ../frontend && npm run test -- --coverage
```

### Running Specific Tests

```bash
# Backend: Run single test class
mvn test -Dtest=SearchServiceTest

# Backend: Run single test method
mvn test -Dtest=SearchServiceTest#testSearchByDateRange_WithValidDates_ReturnsMatchingRecords

# Frontend: Run single suite
npm run test -- --include='**/search.component.spec.ts'
```

### CI/CD Test Execution

Tests run automatically on:
1. **Pre-commit hook:** Quick smoke tests (fast unit tests only)
2. **Pull request:** Full test suite + coverage check
3. **Merge to develop:** Full test suite + integration tests + code style
4. **Deployment to prod:** Full test suite + E2E smoke tests

---

## Performance Testing

### Load Test Procedure

```bash
# 1. Generate load test script (if using JMeter)
# 2. Start application locally
# 3. Run load test
jmeter -t src/test/jmeter/search-load-test.jmx \
  -Jusers=100 \
  -Jduration=3600 \
  -Jrampup=60

# 4. Analyze results
# - Check P99 latency (target: < 500ms for search)
# - Check error rate (target: < 0.1%)
# - Check throughput (target: > X requests/sec)
```

### Performance Baselines

Captured before major changes to detect regressions:
- API latency (p50, p95, p99)
- Database query time
- Memory usage under load
- CPU usage under load
- Disk space usage

---

## Test Data Management

### Local Test Database

```bash
# Seed test data
sql/seed-test-data.sql

# Reset to known state
mvn flyway:clean flyway:migrate  # (or liquibase equivalent)
```

### Fixtures

Keep reusable test data fixtures:
- Factory methods for creating test objects
- Builders for complex object construction
- Mock data generators for performance testing

---

## Flaky Test Handling

If a test fails intermittently:

1. **Identify the flakiness:** Run test 10x in a row
2. **Investigate root cause:** Timing issue? External dependency? Random data?
3. **Fix the test:** Usually by:
   - Adding synchronization/wait conditions
   - Mocking external dependencies
   - Using deterministic test data (not random)
4. **Mark as resolved:** Document the fix in the test comment
5. **Monitor:** Keep eye on it for re-occurrence

---

## Related

- **`docs/specs/`** — Business requirements that these tests verify
- **`docs/architecture/`** — ADRs that define test requirements (e.g., batch patterns, sargable predicates)
- **`docs/guides/`** — How to run tests and debug (in guides, runbooks)
- **`docs/audits/`** — Test execution results and coverage reports
- **`docs/agent-workflow/`** — Stage 4 of the workflow generates tests
- **`.claude/skills/qa-engineer`** — QA agent that generates test code from these scenarios

---

## Quick Reference

| Task | Command | Notes |
|---|---|---|
| Run all tests | `mvn test && npm test` | Both backend and frontend |
| Check coverage | `mvn test && npm test -- --coverage` | Ensure 80%+ coverage |
| Run specific test | `mvn test -Dtest=ClassName` | Replace ClassName |
| Load test | `jmeter -t test.jmx` | Requires JMeter installed |
| View results | `open target/site/jacoco/index.html` | Backend coverage report |

---

## Success Criteria for PR Merge

All of these must pass before PR is merged:

- [ ] 80%+ backend unit test coverage (JaCoCo)
- [ ] 80%+ frontend unit test coverage (Istanbul)
- [ ] All unit tests pass (no failures)
- [ ] Code lint passes (Checkstyle, ESLint)
- [ ] No new critical vulnerabilities introduced
- [ ] All critical test scenarios pass
- [ ] No regressions in existing tests
- [ ] Performance acceptable (no P99 latency regression > 10%)
