# Sample Test Plan: Search Feature

**Feature:** Search and filter records by multiple criteria  
**Status:** In Development  
**Owner:** QA Team Lead  
**Related Spec:** [specs/sample-requirements.md](../specs/sample-requirements.md)  
**Related Architecture:** [ADR-009: Sargable Date Predicates](../architecture/adr/ADR-009-database-indexes-date-range-predicates.md)

---

## Test Scope

### In Scope
- Search API endpoint (`GET /api/search`)
- Search component UI (Angular component)
- Date range filtering
- Status filtering
- Text search
- Pagination
- Sorting
- Error handling
- Performance under load (100 concurrent users)

### Out of Scope
- Cloud sync of search preferences (future feature)
- Advanced search syntax (saved searches, complex filters)
- Full-text search indexing optimization
- Internationalization / multi-language UI

---

## Test Strategy

### Test Pyramid

| Level | Count | Speed | Tools | Coverage |
|---|---|---|---|---|
| **Unit tests** | 30+ | Fast (< 5ms each) | JUnit 5, Mockito, Jest | Business logic, utilities |
| **Integration tests** | 15+ | Moderate (< 1s each) | Spring Boot Test, Jasmine | API endpoints, database |
| **E2E tests** | 5+ | Slow (5-30s each) | Cypress, Playwright | Full workflows |
| **Load/Performance** | 1+ | Very slow (1+ hour) | JMeter, Gatling | 100 concurrent users |

**Total:** 50+ tests, 95%+ code path coverage

---

## Unit Test Scenarios

### Backend Unit Tests

#### SearchService Tests

```java
class SearchServiceTest {
    // Happy path
    @Test
    void testSearchByDateRange_WithValidDates_ReturnsMatchingRecords() {
        // Arrange: Set up mocked repository, test data
        LocalDate startDate = LocalDate.of(2026, 1, 1);
        LocalDate endDate = LocalDate.of(2026, 12, 31);
        
        // Act: Call search service
        List<Record> results = searchService.searchByDateRange(startDate, endDate);
        
        // Assert: Verify results
        assertThat(results).hasSize(150);
        assertThat(results).allMatch(r -> r.getCreatedDate().isAfterOrEqual(startDate));
        assertThat(results).allMatch(r -> r.getCreatedDate().isBefore(endDate));
    }
    
    // Edge cases
    @Test
    void testSearchByDateRange_WithSameDates_ReturnsOnlyThatDay() {
        // Only records created on startDate should be included
        LocalDate date = LocalDate.of(2026, 6, 15);
        List<Record> results = searchService.searchByDateRange(date, date.plusDays(1));
        
        assertThat(results).allMatch(r -> 
            r.getCreatedDate().equals(date)
        );
    }
    
    @Test
    void testSearchByDateRange_WithReverseOrder_ThrowsException() {
        // startDate > endDate should fail fast
        LocalDate startDate = LocalDate.of(2026, 12, 31);
        LocalDate endDate = LocalDate.of(2026, 1, 1);
        
        assertThrows(IllegalArgumentException.class, () ->
            searchService.searchByDateRange(startDate, endDate)
        );
    }
    
    @Test
    void testSearchByDateRange_WithNullDates_ThrowsNullPointerException() {
        assertThrows(NullPointerException.class, () ->
            searchService.searchByDateRange(null, null)
        );
    }
    
    @Test
    void testSearchByStatus_WithMultipleStatuses_ReturnsMatchingRecords() {
        // Verify AND logic: status1 AND status2 AND status3
        List<String> statuses = List.of("active", "verified", "archived");
        List<Record> results = searchService.searchByStatus(statuses);
        
        assertThat(results).allMatch(r -> 
            statuses.contains(r.getStatus())
        );
    }
    
    @Test
    void testSearchByText_CaseInsensitive_ReturnsMatches() {
        // Search should be case-insensitive
        List<Record> results1 = searchService.searchByText("TEST");
        List<Record> results2 = searchService.searchByText("test");
        List<Record> results3 = searchService.searchByText("Test");
        
        assertThat(results1).hasSameSizeAs(results2).hasSameSizeAs(results3);
    }
    
    @Test
    void testSearchByText_WithEmptyString_ReturnsEmpty() {
        List<Record> results = searchService.searchByText("");
        assertThat(results).isEmpty();
    }
    
    @Test
    void testSearchByText_WithNullString_ThrowsException() {
        assertThrows(NullPointerException.class, () ->
            searchService.searchByText(null)
        );
    }
    
    // Performance
    @Test
    void testSearch_UsesParameterizedQueries_NotConcatenation() {
        // Verify SQL injection prevention: must use prepared statements
        Mockito.verify(repository, times(1))
            .findByDateRange(
                eq(startDate),
                eq(endDate)
            );
        // Not mocking raw SQL concatenation
    }
}
```

#### SearchController Tests

```java
@WebMvcTest(SearchController.class)
class SearchControllerTest {
    @MockBean
    private SearchService searchService;
    
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    void testSearchEndpoint_WithValidQuery_Returns200() throws Exception {
        // Mock service response
        List<Record> mockResults = List.of(
            new Record("1", "Record A", "active", LocalDate.of(2026, 1, 15)),
            new Record("2", "Record B", "verified", LocalDate.of(2026, 2, 20))
        );
        when(searchService.searchByDateRange(any(), any()))
            .thenReturn(mockResults);
        
        // Execute request
        mockMvc.perform(
                get("/api/search")
                    .param("startDate", "2026-01-01")
                    .param("endDate", "2026-12-31")
                    .param("page", "0")
                    .param("pageSize", "20")
                    .contentType(MediaType.APPLICATION_JSON)
            )
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.records", hasSize(2)))
            .andExpect(jsonPath("$.totalCount").value(2));
    }
    
    @Test
    void testSearchEndpoint_WithInvalidDateFormat_Returns400() throws Exception {
        mockMvc.perform(
                get("/api/search")
                    .param("startDate", "invalid-date")
                    .param("endDate", "2026-12-31")
            )
            .andExpect(status().isBadRequest());
    }
    
    @Test
    void testSearchEndpoint_WithoutAuthentication_Returns401() throws Exception {
        mockMvc.perform(get("/api/search"))
            .andExpect(status().isUnauthorized());
    }
    
    @Test
    void testSearchEndpoint_IncludesXTotalCountHeader() throws Exception {
        when(searchService.searchByDateRange(any(), any()))
            .thenReturn(mockResults);
        
        mockMvc.perform(
                get("/api/search")
                    .param("startDate", "2026-01-01")
                    .param("endDate", "2026-12-31")
            )
            .andExpect(header().exists("X-Total-Count"))
            .andExpect(header().string("X-Total-Count", "150")); // Mocked total
    }
}
```

### Frontend Unit Tests

```typescript
describe('SearchComponent', () => {
  let component: SearchComponent;
  let fixture: ComponentFixture<SearchComponent>;
  let searchService: jasmine.SpyObj<SearchService>;
  let store: jasmine.SpyObj<Store>;

  beforeEach(async () => {
    const searchServiceSpy = jasmine.createSpyObj('SearchService', ['search']);
    const storeSpy = jasmine.createSpyObj('Store', ['dispatch', 'select']);

    await TestBed.configureTestingModule({
      imports: [SearchComponent],
      providers: [
        { provide: SearchService, useValue: searchServiceSpy },
        { provide: Store, useValue: storeSpy }
      ]
    }).compileComponents();

    component = fixture.componentInstance;
    searchService = TestBed.inject(SearchService) as jasmine.SpyObj<SearchService>;
    store = TestBed.inject(Store) as jasmine.SpyObj<Store>;
  });

  it('should create search component', () => {
    expect(component).toBeTruthy();
  });

  it('should display search form on init', () => {
    fixture.detectChanges();
    const form = fixture.debugElement.query(By.css('form'));
    expect(form).toBeTruthy();
  });

  it('should display search results when user types query', fakeAsync(() => {
    const mockResults = [
      { id: '1', name: 'Record A', status: 'active' },
      { id: '2', name: 'Record B', status: 'verified' }
    ];
    searchService.search.and.returnValue(of({ records: mockResults, totalCount: 2 }));

    component.searchQuery = 'test';
    component.onSearch();
    tick();

    fixture.detectChanges();
    const resultsList = fixture.debugElement.queryAll(By.css('[data-testid="result-item"]'));
    expect(resultsList).toHaveLength(2);
  }));

  it('should display "no results" message when search returns empty', fakeAsync(() => {
    searchService.search.and.returnValue(of({ records: [], totalCount: 0 }));

    component.searchQuery = 'nonexistent';
    component.onSearch();
    tick();

    fixture.detectChanges();
    const noResultsMsg = fixture.debugElement.query(By.css('[data-testid="no-results-message"]'));
    expect(noResultsMsg).toBeTruthy();
    expect(noResultsMsg.nativeElement.textContent).toContain('No results');
  }));

  it('should apply date filter when user selects date range', () => {
    const startDateInput = fixture.debugElement.query(By.css('[data-testid="search-date-start"]'));
    const endDateInput = fixture.debugElement.query(By.css('[data-testid="search-date-end"]'));

    startDateInput.nativeElement.value = '2026-01-01';
    endDateInput.nativeElement.value = '2026-12-31';

    component.startDate = new Date('2026-01-01');
    component.endDate = new Date('2026-12-31');
    component.onSearch();

    expect(searchService.search).toHaveBeenCalledWith(
      jasmine.objectContaining({
        startDate: new Date('2026-01-01'),
        endDate: new Date('2026-12-31')
      })
    );
  });

  it('should persist search preferences to localStorage', () => {
    spyOn(localStorage, 'setItem');

    component.startDate = new Date('2026-01-01');
    component.status = ['active'];
    component.saveSearchPreferences();

    expect(localStorage.setItem).toHaveBeenCalledWith(
      'search_preferences',
      jasmine.stringContaining('active')
    );
  });
});
```

---

## Integration Test Scenarios

### Search API Integration Test

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class SearchControllerIntegrationTest {
    @LocalServerPort
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;

    @Autowired
    private RecordRepository recordRepository;

    @BeforeEach
    void setUp() {
        // Clear database
        recordRepository.deleteAll();

        // Seed test data
        recordRepository.saveAll(List.of(
            new Record("1", "Invoice 001", "active", LocalDate.of(2026, 1, 15)),
            new Record("2", "Invoice 002", "verified", LocalDate.of(2026, 2, 20)),
            new Record("3", "Invoice 003", "archived", LocalDate.of(2026, 3, 25))
        ));
    }

    @Test
    void testSearchAPI_WithValidDateRange_ReturnsFilteredRecords() {
        String url = "http://localhost:" + port + "/api/search?"
            + "startDate=2026-01-01&endDate=2026-02-28&page=0&pageSize=20";

        ResponseEntity<SearchResponse> response = restTemplate.getForEntity(
            url,
            SearchResponse.class
        );

        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(response.getBody().getRecords()).hasSize(2);
        assertThat(response.getHeaders().get("X-Total-Count")).containsExactly("2");
    }

    @Test
    void testSearchAPI_WithPagination_ReturnsCorrectPage() {
        String url = "http://localhost:" + port + "/api/search?"
            + "page=1&pageSize=1"; // Second page, 1 item per page

        ResponseEntity<SearchResponse> response = restTemplate.getForEntity(
            url,
            SearchResponse.class
        );

        assertThat(response.getBody().getRecords()).hasSize(1);
        assertThat(response.getBody().getRecords().get(0).getId()).isEqualTo("2");
    }

    @Test
    void testSearchAPI_DatabaseConnection_Healthy() {
        String url = "http://localhost:" + port + "/api/search";
        
        // Verify database is accessible via API
        ResponseEntity<SearchResponse> response = restTemplate.getForEntity(
            url,
            SearchResponse.class
        );

        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(response.getBody().getRecords()).isNotNull();
    }
}
```

---

## End-to-End Test Scenarios

### Cypress E2E Tests

```typescript
describe('Search Feature E2E', () => {
  beforeEach(() => {
    cy.visit('/search');
  });

  it('should perform a complete search workflow', () => {
    // 1. User enters search criteria
    cy.get('[data-testid="search-date-start"]').type('2026-01-01');
    cy.get('[data-testid="search-date-end"]').type('2026-12-31');
    cy.get('[data-testid="search-status-select"]').select(['active', 'verified']);
    cy.get('[data-testid="search-submit-button"]').click();

    // 2. Results display
    cy.get('[data-testid="result-item"]').should('have.length.greaterThan', 0);
    cy.get('[data-testid="result-count"]').should('contain', 'Found');

    // 3. User clicks on a result
    cy.get('[data-testid="result-item"]').first().click();

    // 4. Detail view opens
    cy.url().should('include', '/detail/');
  });

  it('should persist search preferences across page reloads', () => {
    // Set search preferences
    cy.get('[data-testid="search-date-start"]').type('2026-06-01');
    cy.get('[data-testid="search-submit-button"]').click();

    // Reload page
    cy.reload();

    // Verify preferences are restored
    cy.get('[data-testid="search-date-start"]').should('have.value', '2026-06-01');
  });
});
```

---

## Performance / Load Test Scenarios

### JMeter Load Test

```
Test Plan: Search API Performance Test
├── Thread Group
│   ├── Number of Threads: 100
│   ├── Ramp-up time: 60 seconds
│   ├── Loop count: 10 (10 iterations per thread = 1000 requests)
│   ├── HTTP Request
│   │   ├── GET /api/search?startDate=2026-01-01&endDate=2026-12-31
│   ├── Response Assertion
│   │   ├── Status: 200
│   ├── Constant Timer
│   │   └── Delay: 1000ms (1 second between requests)
├── View Results Tree
├── Summary Report
├── Aggregate Graph
```

**Success Criteria:**
- P99 latency: < 500ms
- P95 latency: < 300ms
- P50 latency: < 100ms
- Error rate: < 0.1%
- Throughput: > 10 requests/second

---

## Critical Regression Tests

These must pass before every PR merge:

- [ ] Search returns correct record count (no duplicates, no missing records)
- [ ] Date range filtering uses sargable predicates (not YEAR() function)
- [ ] Pagination boundary conditions (page 0, last page, beyond last page)
- [ ] SQL injection prevention (parameterized queries tested)
- [ ] XSS prevention (HTML entities escaped in results)
- [ ] Performance baseline (P99 latency < 500ms)
- [ ] Concurrent user handling (100 users simultaneously)

---

## Test Data Requirements

| Scenario | Record count | Date range | Statuses | Text keywords |
|---|---|---|---|---|
| Happy path | 150 | 2026-01-01 to 2026-12-31 | All | Common terms |
| Large result set | 1,000,000+ | Wide range | Mixed | Various |
| Empty results | 0 | Specific date | Specific status | Rare keyword |
| Boundary conditions | 10 | Start/end dates | Edge cases | Null/empty |
| Performance | 100,000 | Full year | All | Various |

---

## Success Criteria for Test Plan

All items must pass for feature to be merged:

- [ ] 30+ unit tests written and passing (backend)
- [ ] 15+ integration tests written and passing
- [ ] 5+ E2E tests written and passing (full workflows)
- [ ] 80%+ code coverage (backend and frontend)
- [ ] All critical regression tests pass
- [ ] Performance baseline met (P99 latency < 500ms)
- [ ] Load test passes (100 concurrent users, < 0.1% error rate)
- [ ] No new flaky tests introduced

---

## Related Documents

- **Specification:** [specs/sample-requirements.md](../specs/sample-requirements.md#functional-requirements)
- **Architecture:** [ADR-009: Sargable Date Predicates](../architecture/adr/ADR-009-database-indexes-date-range-predicates.md)
- **Guides:** [testing/README.md](README.md)
- **CI/CD:** Test execution gates defined in Azure Pipelines
