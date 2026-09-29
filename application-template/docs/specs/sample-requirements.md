# Sample Specification: Search & Filtering

**Document status:** APPROVED  
**Last updated:** 2026-09-29  
**Owner:** Product Lead, Tech Lead  
**Related artifacts:** ADR-009, test-plan.md#SearchScenarios, API dashboard

---

## Functional Requirements

### FR-001: Users can search records by multiple criteria

**Status:** APPROVED

**User story:**
"As a business user, I want to search for records using multiple criteria (date range, status, tags), so that I can find what I need quickly without scrolling through thousands of records."

**Acceptance criteria:**
- [ ] Search supports date range filter (start date, end date)
- [ ] Search supports status filter (single or multi-select)
- [ ] Search supports text search (searches name and description fields)
- [ ] Results display with pagination (default 20 per page)
- [ ] Results include total count in header (X-Total-Count)
- [ ] Empty search returns error, not all records
- [ ] Search executes within 500ms (see NFR-002)
- [ ] Results are sorted by relevance (date descending by default)
- [ ] User can save search preferences as a shortcut

**Business rules:**
- Date range is inclusive on both start and end dates
- Status filter uses AND logic if multiple selections (e.g., "active AND verified")
- Text search is case-insensitive
- Null/empty values are treated as missing (not searched)

**Related NFRs:**
- NFR-002: API response time p99 < 500ms
- NFR-004: No hardcoded credentials
- NFR-006: Search results paginated (no more than 1000 records per response)

**Related tests:**
- `docs/testing/test-plan.md#Search-happy-path`
- `docs/testing/test-plan.md#Search-date-range-validation`
- `docs/testing/test-plan.md#Search-empty-results`

**Related code:**
- Backend: `src/main/java/com/app/invoice/controller/SearchController.java`
- Backend: `src/main/java/com/app/invoice/service/SearchService.java`
- Frontend: `src/app/modules/search/search.component.ts`
- Frontend: `src/app/modules/search/search-filter.component.ts`

**Related ADRs:**
- [ADR-009: Sargable Date Predicates](../architecture/adr/ADR-009-database-indexes-date-range-predicates.md) — Explains why we use `date >= :start AND date < :end` instead of `YEAR()` functions

**API endpoint:**
```
GET /api/search?
  startDate=2026-01-01
  endDate=2026-12-31
  status=active,verified
  query=test
  page=0
  pageSize=20
```

**Related processes:**
- Reconciliation workflow depends on accurate search (uses same predicates)
- Reporting depends on search results being sortable

**Dependencies:**
- Requires FR-005 (database indexed) to be complete
- Depends on ADR-009 decision (sargable predicates)

**Blocked by:**
- None

---

### FR-002: Search filters persist in local storage

**Status:** APPROVED

**User story:**
"As a business user, I want my search filters to be remembered, so that I don't have to enter them again on my next visit."

**Acceptance criteria:**
- [ ] Search criteria saved to browser localStorage
- [ ] Saved criteria restored on next page visit
- [ ] User can clear saved criteria with "Clear preferences" button
- [ ] Clear preferences doesn't affect search results, only stored preferences
- [ ] Preferences persist across browser sessions
- [ ] Preferences are specific to the logged-in user (not shared device-wide)

**Technical notes:**
- Use localStorage with key `search_preferences_<userId>`
- Max size: 5 KB
- Prefer cloud sync (user settings API) if available (see NFR-007)

**Related tests:**
- `docs/testing/test-plan.md#Search-filter-persistence`

**Related code:**
- Frontend: `src/app/modules/search/search-state.service.ts` (NgRx store)
- Frontend: `src/app/core/services/local-storage.service.ts` (utility)

---

## Non-Functional Requirements

### NFR-002: API search response time p99 < 500ms

**Status:** APPROVED

**Requirement:**
Search API must perform responsively on all browsers and network conditions. This is a critical user experience metric.

**Measurable criteria:**
- **99th percentile latency:** < 500ms (meaning 99% of requests are faster)
- **50th percentile (median) latency:** < 100ms
- **Throughput:** Support 100 concurrent users searching simultaneously
- **Cardinality:** Return results even for large result sets (up to 1 million records)

**Baseline (current state):**
- p99 latency: 2.5 seconds (SLOW)
- p50 latency: 800ms (SLOW)
- Throughput: 10 concurrent users before degradation
- Root cause: Full table scan, no indexes on search columns

**Target state:**
- p99 latency: < 500ms
- p50 latency: < 100ms
- Throughput: 100 concurrent users at sustained p99 < 500ms
- How: Database indexes (ADR-009), connection pooling, query optimization

**How we measure it:**
- **Monitoring:** Grafana dashboard "Search Performance" (P99, P50, throughput graphs)
- **Testing:** JMeter load test with 100 concurrent users, 1-hour duration
- **CI gate:** P99 latency must not regress from baseline by more than 10%

**Test procedure:**
```bash
# Load test with 100 users over 1 hour
jmeter -t src/test/jmeter/search-load-test.jmx \
  -Jusers=100 \
  -Jduration=3600 \
  -Jrampup=60

# Check results
# Samples: 500,000+ requests
# P99: < 500ms
# Max response time: < 5s
```

**Related FRs:**
- FR-001: Search performance depends on this NFR

**Related ADRs:**
- [ADR-009: Sargable Date Predicates](../architecture/adr/ADR-009-database-indexes-date-range-predicates.md) — Query optimization
- [ADR-002: Month-Partitioned Tables](../architecture/adr/ADR-002-month-partitioned-image-tables.md) — Table partitioning strategy

**Responsible team:**
- Backend engineers: Query optimization, database indexes
- DevOps: Database configuration, connection pooling, monitoring
- QA: Performance testing, regression detection

**Monitoring dashboard:**
- [Grafana: Search Performance](example.com/grafana/search-performance)
- Alert: If P99 > 750ms (warn), > 1000ms (critical)

**Escalation:**
If P99 exceeds 1000ms, page on-call engineer and open incident.

---

### NFR-004: No hardcoded credentials or secrets

**Status:** APPROVED

**Requirement:**
All secrets (database passwords, API keys, JWT secrets, encryption keys) must be stored securely outside the codebase. This is a critical security and compliance requirement.

**Measurable criteria:**
- **Test:** `TruffleHog` scan finds zero hardcoded secrets
- **Test:** `regex` scan for common patterns (AWS_KEY, PASSWORD, TOKEN) finds zero matches
- **Enforcement:** Pre-commit hook blocks commits with detected secrets
- **Audit:** Annual codebase scan by security team

**Secrets to manage:**
- Database credentials (username, password, connection string)
- API keys (external services, webhooks)
- JWT signing key
- Encryption keys (at-rest, in-transit)
- OAuth client secrets
- TLS certificates

**How to store secrets:**
- **Local development:** `.env.local` (in `.gitignore`, never committed)
- **Staging/Production:** AWS Secrets Manager (or equivalent secret store)
- **Access control:** Only authorized services can retrieve secrets

**How to use secrets in code:**
```java
// WRONG: Hardcoded password
String dbPassword = "my_secret_password";

// RIGHT: Environment variable
String dbPassword = System.getenv("DB_PASSWORD");

// RIGHT: Spring property injection
@Value("${spring.datasource.password}")
private String dbPassword;

// RIGHT: Secrets manager
String secret = secretsManager.getSecret("prod/database/password");
```

**Related code:**
- Backend: `.env.example` (template, no secrets)
- Backend: `application-prod.properties` (references secrets manager)
- Frontend: `.env.example` (template, no secrets)

**Related tests:**
- `src/test/java/security/NoHardcodedSecretsTest.java` (runs TruffleHog)
- Pre-commit hook: `.git/hooks/pre-commit` (blocks obvious secrets)

**Responsible team:**
- Security team: Secret rotation, access audit
- Backend/DevOps: Secret injection at deployment time
- All developers: Following the no-hardcoded-secrets rule

**Audit:**
- Pre-merge: Git pre-commit hook scans for secrets
- CI/CD: `mvn security:check` scans for hardcoded strings
- Annual: Manual codebase review by security team

---

### NFR-006: Search results paginated (max 1000 records per response)

**Status:** APPROVED

**Requirement:**
Search results must be paginated to prevent memory exhaustion and ensure consistent API response times.

**Measurable criteria:**
- Maximum 1000 records per response
- Default page size: 20 records
- Page numbers: 0-indexed (page 0 is the first page)
- Response includes `X-Total-Count` header (total available records)
- Client must handle `X-Total-Count > pageSize` (indicating more results available)

**API contract:**
```
GET /api/search?page=0&pageSize=20

Response:
{
  "records": [ ... 20 items ... ],
  "pageNumber": 0,
  "pageSize": 20,
  "totalCount": 1000  (also in X-Total-Count header)
}

X-Total-Count: 1000
```

**Related tests:**
- `docs/testing/test-plan.md#Pagination-happy-path`
- `docs/testing/test-plan.md#Pagination-boundary-conditions`

**Related code:**
- Backend: `com.app.core.pagination.PageRequest`
- Backend: `com.app.core.pagination.PageResponse`
- Frontend: `src/app/core/services/pagination.service.ts`

---

### NFR-007: Search preferences stored in cloud (optional, nice-to-have)

**Status:** DRAFT [CONFIRM]

**Requirement:**
User's search preferences should sync across devices (laptop, tablet, phone).

**Measurable criteria:**
- Preferences stored in cloud (not just local browser)
- Preferences sync within 30 seconds of change
- Cloud storage size per user: < 10 KB
- Sync works offline (changes queued, sent when reconnected)

**[CONFIRM] Items:**
- [ ] Is cloud sync a requirement for MVP, or is it a future enhancement?
- [ ] Which cloud service should we use (user settings API, S3, cloud database)?
- [ ] Should this be behind a feature flag?

**Note:** Implementation is blocked until stakeholders confirm these decisions.

---

## API Specification

### Endpoint: GET /api/search

**Request:**
```
GET /api/search?
  startDate=2026-01-01
  endDate=2026-12-31
  status=active,verified
  query=keyword
  page=0
  pageSize=20
```

**Parameters:**
| Parameter | Type | Required | Description |
|---|---|---|---|
| `startDate` | ISO date (YYYY-MM-DD) | No | Filter: records on or after this date |
| `endDate` | ISO date (YYYY-MM-DD) | No | Filter: records before this date (exclusive) |
| `status` | Comma-separated enum | No | Filter: status (active, verified, archived) |
| `query` | String | No | Text search in name and description fields |
| `page` | Integer | Yes | Page number (0-indexed) |
| `pageSize` | Integer | No | Records per page (default: 20, max: 1000) |

**Response (200 OK):**
```json
{
  "records": [
    {
      "id": "12345",
      "name": "Record Name",
      "description": "Description",
      "status": "active",
      "createdDate": "2026-01-15",
      "updatedDate": "2026-09-20"
    }
  ],
  "pageNumber": 0,
  "pageSize": 20,
  "totalCount": 150
}
```

**Response headers:**
```
X-Total-Count: 150
Content-Type: application/json
```

**Error responses:**
```
400 Bad Request: Invalid date format or parameter value
401 Unauthorized: Not authenticated
403 Forbidden: Not authorized to search this resource
500 Internal Server Error: Database error or server issue
```

---

## Related Documents

- **Architecture:** [ADR-009: Sargable Date Predicates](../architecture/adr/ADR-009-database-indexes-date-range-predicates.md)
- **Testing:** [test-plan.md#SearchScenarios](../testing/test-plan.md#SearchScenarios)
- **Guides:** [API Best Practices](../guides/api-best-practices.md) (if exists)
- **Monitoring:** [Grafana: Search Performance](example.com/grafana/search-performance)
- **Alerts:** [PagerDuty: Search API latency](example.com/pd/search-api)

---

## Sign-offs

| Role | Name | Date | Status |
|---|---|---|---|
| Product Lead | [Name] | 2026-09-29 | ✅ Approved |
| Tech Lead | [Name] | 2026-09-29 | ✅ Approved |
| Security Lead | [Name] | 2026-09-29 | ✅ Approved |
| Backend Lead | [Name] | 2026-09-29 | ✅ Approved |

---

## Change History

| Date | Author | Change |
|---|---|---|
| 2026-09-29 | [Name] | Initial specification |
| 2026-09-20 | [Name] | Added pagination limits per NFR-006 |
| 2026-08-15 | [Name] | Initial draft, awaiting stakeholder review |
