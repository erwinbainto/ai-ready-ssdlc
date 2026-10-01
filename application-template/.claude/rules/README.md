# Rules — App-Specific Standards

**Purpose:** Rules are path-scoped guidance that narrows enterprise standards. They're enforced during code review and can block commits if violations are detected.

**Key Rule:** App rules can only narrow enterprise rules, never widen them. A rule that permits something the enterprise forbids is ignored in favor of the enterprise rule.

---

## Files in This Directory

| File | Scope | How Often Updated | Who Owns |
|---|---|---|---|
| `10-app.md` | App-specific conventions, naming, patterns | Quarterly | Dev Lead + Tech Lead |
| `security-guardrails.md` | Mandatory security controls for this app | Quarterly | Security Lead + Dev Lead |

---

## Understanding Rules

### Rule Scope & Format

Each rule file has a YAML frontmatter specifying when it applies:

```markdown
---
description: Security guardrails for this application
paths: ["src/**", "backend/**", "frontend/**"]
---

# Security Guardrails — <APPLICATION_NAME>

Content of the rule...
```

**`paths:`** — File globs where the rule applies
- `["src/**"]` — All files under src/ and subdirectories
- `["backend/**/*.java"]` — Only Java files in backend
- `["frontend/src/app/**"]` — React components
- Supports standard glob syntax: `*`, `**`, `?`, `[abc]`

**Test your glob:**
```bash
find . -path "<your-glob>"  # Lists files matching your glob
```

### Enterprise vs. App Rules

**Enterprise rules** (read-only):
- Organization-wide standards
- Apply to ALL applications
- Updated once centrally
- Override app rules if conflict

**App rules** (you author):
- More specific than enterprise
- Apply only to this app
- Updated per-app as needed
- Can narrow but never widen enterprise

**Example:**
```markdown
Enterprise rule: "All database queries must use parameterized statements"
App rule (narrows it): "All queries must use JPA @Query annotations; no native SQL"

This is fine: JPA is stricter than just "parameterized"

App rule (widens it): "Dynamic query building OK if developer reviews it"
This is NOT OK: It violates the enterprise rule; will be ignored
```

---

## How to Create App-Specific Rules

### Step 1: Identify Stack & Patterns

Ask your team:
- What languages/frameworks? (Java, Node.js, React, Python, etc.)
- What are common anti-patterns we keep finding in reviews?
- What conventions do we want enforced?

**Example answers:**
- "We're Java Spring Boot + React"
- "We keep seeing hardcoded strings instead of config properties"
- "We need to enforce `@Transactional` on service methods that write"

### Step 2: Narrow Enterprise Rules

Read the enterprise security rules:
```
@enterprise/rules/secure-coding.md
@enterprise/rules/database-policy.md
```

Example narrowing:

**Enterprise rule:** "Use parameterized queries"  
**App rule (narrow it for Java):** "All queries must use JpaRepository or @Query with :named parameters"

### Step 3: Add Stack-Specific Guidance

What patterns does YOUR stack need?

**For Java/Spring Boot:**
```markdown
---
description: Java Spring Boot conventions
paths: ["backend/src/**/*.java"]
---

# Java Conventions — <APPLICATION_NAME>

## Dependency Injection
- Use constructor injection (not field injection)
- Example:
  ✅ public UserService(UserRepository repo) { this.repo = repo; }
  ❌ @Autowired private UserRepository repo;

## Transaction Boundaries
- All service methods that write MUST have @Transactional
- Example:
  ✅ @Transactional public void saveUser(User u) { repo.save(u); }
  ❌ public void saveUser(User u) { repo.save(u); }  // Missing @Transactional!
```

**For React/TypeScript:**
```markdown
---
description: React component conventions
paths: ["frontend/src/app/**"]
---

# React Conventions — <APPLICATION_NAME>

## Component Structure
- Use functional components, not class components
- Example:
  ✅ export const UserCard = ({ user }) => <div>{user.name}</div>;
  ❌ class UserCard extends React.Component { ... }

## Hook Usage
- Hooks must be at top level of component
- Never call hooks conditionally
```

### Step 4: Document with Examples

For each rule, provide:
1. **What to do** (✅ example)
2. **What NOT to do** (❌ counter-example)
3. **Why** (reasoning)

**Good example:**
```markdown
## No Hardcoded Strings

Hardcoded strings are difficult to change, impossible to mock in tests, and error-prone.

✅ CORRECT — Use configuration:
```java
String apiUrl = environment.getProperty("stripe.api.url");
```

❌ WRONG — Hardcoded:
```java
String apiUrl = "https://api.stripe.com";  // What if URL changes?
```

**Why:** Configuration allows changes without recompiling; tests can mock different values.
```

### Step 5: Test Your Rules

Rules are only effective if enforced:

- [ ] **Code review:** Can reviewers use this rule to reject PRs?
- [ ] **SAST tool:** Can automated linting catch violations?
- [ ] **Tests:** Can you write tests that would fail if rule is violated?

**Example SAST rule (SonarQube):**
```
Java rule: "Detect missing @Transactional"
Triggers: Method in *Service class writes to database without @Transactional
Severity: Major
Action: Fail PR until fixed
```

---

## Example: Complete App Rule File

### Example 1: Java Spring Boot App

```markdown
---
description: Java conventions for Invoice Retention system
paths: ["backend/src/**/*.java"]
---

# Java Conventions — Invoice Retention

Narrows the enterprise standards to Spring Boot + JDBC patterns used here.

## Dependency Injection

**Rule:** Constructor injection only; no field injection.

**Why:** Constructor injection is testable (easy to inject mocks), explicit about dependencies, prevents NPE.

✅ CORRECT:
```java
@Service
public class InvoiceService {
    private final InvoiceRepository repo;
    
    public InvoiceService(InvoiceRepository repo) {
        this.repo = repo;  // Explicit dependency
    }
}
```

❌ WRONG:
```java
@Service
public class InvoiceService {
    @Autowired
    private InvoiceRepository repo;  // Field injection is implicit, hard to test
}
```

## Transaction Boundaries

**Rule:** All service methods that modify data MUST have `@Transactional`.

**Why:** Ensures ACID properties, prevents half-written data, handles rollback on error.

✅ CORRECT:
```java
@Service
public class InvoiceService {
    @Transactional  // ← Required for write operations
    public void saveInvoice(Invoice inv) {
        repo.save(inv);
    }
    
    public Invoice findById(Long id) {  // ← No @Transactional needed; read-only
        return repo.findById(id).orElseThrow();
    }
}
```

❌ WRONG:
```java
@Service
public class InvoiceService {
    public void saveInvoice(Invoice inv) {  // Missing @Transactional!
        repo.save(inv);
    }
}
```

## Database Queries

**Rule:** Use JpaRepository or `@Query` with named parameters. Never string concatenation.

✅ CORRECT:
```java
@Repository
public interface InvoiceRepository extends JpaRepository<Invoice, Long> {
    @Query("SELECT i FROM Invoice i WHERE i.invoiceNr = :nr AND i.invoiceDt >= :start")
    List<Invoice> findByNrAndDateRange(@Param("nr") String nr, @Param("start") LocalDate start);
}
```

❌ WRONG:
```java
String query = "SELECT * FROM INVOICE WHERE INVOICE_NR = '" + nr + "'";  // SQL injection!
```

## Exception Handling

**Rule:** Never swallow exceptions. Log and re-throw or wrap.

✅ CORRECT:
```java
try {
    repo.save(invoice);
} catch (DataAccessException e) {
    logger.error("Failed to save invoice", e);
    throw new ApplicationException("Invoice save failed", e);
}
```

❌ WRONG:
```java
try {
    repo.save(invoice);
} catch (Exception e) {
    // Silently ignoring the error; causes mysterious failures downstream!
}
```
```

### Example 2: React/TypeScript App

```markdown
---
description: React component conventions
paths: ["frontend/src/app/**"]
---

# React Conventions — <APPLICATION_NAME>

## Functional Components Only

**Rule:** Use functional components with hooks. No class components.

**Why:** Functional components are simpler, easier to test, more composable.

✅ CORRECT:
```typescript
interface UserCardProps {
  user: User;
  onDelete?: (id: string) => void;
}

export const UserCard: React.FC<UserCardProps> = ({ user, onDelete }) => {
  const [isLoading, setIsLoading] = React.useState(false);
  
  return <div>{user.name}</div>;
};
```

❌ WRONG:
```typescript
class UserCard extends React.Component {  // Use functional components instead
  render() { return <div>{this.props.user.name}</div>; }
}
```

## Hook Rules

**Rule:** Hooks only at component top level. Never call conditionally.

✅ CORRECT:
```typescript
export const UserForm = () => {
  const [name, setName] = React.useState("");  // ← Top level
  const [email, setEmail] = React.useState("");
  
  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};
```

❌ WRONG:
```typescript
export const UserForm = ({ showEmail }) => {
  if (showEmail) {
    const [email, setEmail] = React.useState("");  // ❌ Inside conditional!
  }
  // ... hook called conditionally breaks React's assumptions
};
```

## Prop Drilling Prevention

**Rule:** Pass data via Context for > 2 levels of nesting.

✅ CORRECT (shallow nesting):
```typescript
<Header user={user}>
  <Title userName={user.name} />
</Header>
```

✅ CORRECT (deep nesting → use Context):
```typescript
<UserContext.Provider value={user}>
  <Sidebar />  {/* doesn't need to accept user prop */}
    <NavMenu />  {/* gets user from context */}
</UserContext.Provider>
```
```

---

## Maintenance Workflow

### Quarterly Review

- [ ] Are rules still relevant to how team codes?
- [ ] Any rules we violate regularly? (May need to adjust or enforce differently)
- [ ] New stack adopted? (Add new rules)
- [ ] Team feedback? (Are rules helpful or get in the way?)

### After Code Review

If the same issue appears in 3+ PRs:
1. **Document it** as a new rule
2. **Add examples** showing correct approach
3. **Announce** to team + add to CI/CD check if possible
4. **Review in next sprint** planning

**Example workflow:**
```
Week 1: Reviewer rejects PR for missing @Transactional (3rd time this week)
Week 2: Dev lead adds @Transactional rule to 10-app.md with examples
Week 3: SonarQube rule configured to flag violations
Week 4: Team trained on new rule during standup
```

---

## Enforcement Methods

### 1. Code Review (Manual)

Reviewers check compliance:
- Use rule as rejection reason in PR comments
- Link to specific example in rule file

### 2. Automated Linting

SAST tools catch violations:

**SonarQube example:**
```
Rule: Java methods missing @Transactional on writes
Severity: Major
Pattern: ServiceClass → save/update/delete method → no @Transactional
Action: Fail PR if > 0 violations
```

**ESLint example:**
```json
{
  "no-conditional-hooks": "error",
  "react/hook-use-state": "error"
}
```

### 3. Pre-Commit Hooks

Catch issues before commit:
```bash
#!/bin/bash
# pre-commit hook: check Java files for @Transactional
grep -r "@Transactional" backend/src/ || {
  echo "❌ Found service methods without @Transactional"
  exit 1
}
```

### 4. Tests

Write tests that fail if rule violated:

```java
@Test
public void should_fail_if_service_method_modifies_data_without_transactional() {
    // Reflection check: does saveInvoice have @Transactional?
    Method method = InvoiceService.class.getMethod("saveInvoice", Invoice.class);
    assertTrue(
        method.isAnnotationPresent(Transactional.class),
        "saveInvoice must have @Transactional annotation"
    );
}
```

---

## Common Rule Anti-Patterns

| Anti-Pattern | Problem | Better Approach |
|---|---|---|
| Rule too vague ("Write good code") | Unmeasurable, confusing | Specific with examples (✅ / ❌) |
| Rule about opinion, not quality ("Use camelCase") | Subjective, annoying | Only rules that prevent bugs or security issues |
| Rule never enforced | Ignored, reduces trust | Add to linting or code review checklist |
| Rule violates by 90% of code | Unrealistic | Adjust rule or enforce incrementally |
| No examples | Team guesses at intent | Always include ✅ correct and ❌ wrong examples |

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| Glob doesn't match files | Syntax error in glob | Test with `find . -path "<glob>"` |
| Rule ignored during PR review | Path glob doesn't match | Expand glob or update filename path |
| Team bypasses rule | Not automated | Add to SAST linting or CI/CD gate |
| Rule contradicts enterprise | App rule widened enterprise | Narrow it further or reference enterprise rule |

---

## Related Documentation

- **Enterprise rules:** `@enterprise/rules/` — organization-wide standards
- **Security guardrails:** `security-guardrails.md` — mandatory security controls
- **Conventions:** `10-app.md` — naming, patterns, anti-patterns
- **Context hazards:** `.claude/context/hazards.md` — fragile areas that need careful code review

---

**Owned by:** <Tech Lead / Platform Team>  
**Last updated:** <YYYY-MM-DD>  
**Review frequency:** Quarterly
