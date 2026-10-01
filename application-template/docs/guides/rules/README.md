# Rules — App-Specific Standards Guide

**Full detailed guide for creating `.claude/rules/` files.**

For the quick reference in `.claude/rules/`, see the actual files:
- `10-app.md` — App-specific conventions (auto-loaded)
- `security-guardrails.md` — Mandatory security controls (auto-loaded)

---

## Understanding Rules

### Rule Scope & Format

Each rule file has YAML frontmatter specifying when it applies:

```markdown
---
description: Security guardrails for this application
paths: ["src/**", "backend/**", "frontend/**"]
---

# Security Guardrails — <APPLICATION_NAME>

Content of the rule...
```

**`paths:`** — File globs where the rule applies
- `["src/**"]` — All files under src/
- `["backend/**/*.java"]` — Only Java files in backend
- Test your glob: `find . -path "<your-glob>"`

### Enterprise vs. App Rules

**Enterprise rules:** Organization-wide, apply to ALL apps, read-only  
**App rules:** More specific, apply only to this app, you author

**Example:**
```markdown
Enterprise: "All database queries must use parameterized statements"
App rule (narrows): "All queries must use JPA @Query annotations; no native SQL"
✅ This is fine: JPA is stricter

App rule (widens): "Dynamic query OK if developer reviews it"
❌ NOT OK: Violates enterprise rule; ignored
```

---

## How to Create App-Specific Rules

### Step 1: Identify Stack & Patterns

Ask your team:
- What languages/frameworks? (Java, Node.js, React, Python, etc.)
- What anti-patterns keep appearing in reviews?
- What conventions should we enforce?

### Step 2: Narrow Enterprise Rules

Read the enterprise security rules:
- `@enterprise/rules/secure-coding.md`
- `@enterprise/rules/database-policy.md`

Example narrowing:

**Enterprise rule:** "Use parameterized queries"  
**App rule (narrow for Java):** "All queries must use JpaRepository or @Query with :named parameters"

### Step 3: Add Stack-Specific Guidance

**For Java/Spring Boot:**
```markdown
---
description: Java Spring Boot conventions
paths: ["backend/src/**/*.java"]
---

# Java Conventions — <APPLICATION_NAME>

## Dependency Injection

Use constructor injection (not field injection).

✅ CORRECT:
```java
public UserService(UserRepository repo) { this.repo = repo; }
```

❌ WRONG:
```java
@Autowired private UserRepository repo;
```

## Transaction Boundaries

All service methods that write MUST have @Transactional.

✅ CORRECT:
```java
@Transactional public void saveUser(User u) { repo.save(u); }
```

❌ WRONG:
```java
public void saveUser(User u) { repo.save(u); }  // Missing @Transactional!
```
```

**For React/TypeScript:**
```markdown
---
description: React component conventions
paths: ["frontend/src/app/**"]
---

# React Conventions — <APPLICATION_NAME>

## Component Structure

Use functional components, not class components.

✅ CORRECT:
```typescript
export const UserCard = ({ user }) => <div>{user.name}</div>;
```

❌ WRONG:
```typescript
class UserCard extends React.Component { ... }
```
```

### Step 4: Document with Examples

For each rule:
1. **What to do** (✅ example)
2. **What NOT to do** (❌ counter-example)
3. **Why** (reasoning)

**Good example:**
```markdown
## No Hardcoded Strings

✅ CORRECT — Use configuration:
```java
String apiUrl = environment.getProperty("stripe.api.url");
```

❌ WRONG — Hardcoded:
```java
String apiUrl = "https://api.stripe.com";
```

**Why:** Configuration allows changes without recompiling; tests can mock different values.
```

---

## Enforcement Methods

### 1. Code Review (Manual)

Reviewers check compliance using rule as rejection reason.

### 2. Automated Linting

SAST tools catch violations:

**SonarQube example:**
```
Java rule: "Detect missing @Transactional"
Triggers: Method in *Service class writes without @Transactional
Severity: Major
Action: Fail PR
```

**ESLint example:**
```json
{
  "no-conditional-hooks": "error",
  "react/hook-use-state": "error"
}
```

### 3. Pre-Commit Hooks

```bash
#!/bin/bash
grep -r "@Transactional" backend/src/ || {
  echo "❌ Found service methods without @Transactional"
  exit 1
}
```

### 4. Tests

```java
@Test
public void should_fail_if_service_method_modifies_without_transactional() {
    Method method = InvoiceService.class.getMethod("saveInvoice", Invoice.class);
    assertTrue(
        method.isAnnotationPresent(Transactional.class),
        "saveInvoice must have @Transactional"
    );
}
```

---

## Maintenance Workflow

### Quarterly Review

- [ ] Rules still relevant?
- [ ] Any rules violated regularly? (Adjust or enforce differently)
- [ ] New stack adopted? (Add new rules)
- [ ] Team feedback? (Are rules helpful?)

### After Code Review

If same issue appears in 3+ PRs:
1. Document as new rule
2. Add examples
3. Announce to team
4. Add to CI/CD check if possible
5. Review in next sprint planning

---

## Common Rule Anti-Patterns

| Anti-Pattern | Problem | Better |
|---|---|---|
| Too vague ("Write good code") | Unmeasurable | Specific with examples |
| Opinion-based ("Use camelCase") | Subjective | Only rules preventing bugs/security |
| Never enforced | Ignored, reduces trust | Add to linting or review checklist |
| Violated by 90% of code | Unrealistic | Adjust or enforce incrementally |
| No examples | Team guesses intent | Include ✅ correct and ❌ wrong |

---

## Example Rule Files

### Java/Spring Boot

```markdown
---
description: Java conventions for Invoice system
paths: ["backend/src/**/*.java"]
---

# Java Conventions — Invoice Retention

## Dependency Injection

**Rule:** Constructor injection only; no field injection.

✅ CORRECT:
```java
@Service
public class InvoiceService {
    private final InvoiceRepository repo;
    public InvoiceService(InvoiceRepository repo) { this.repo = repo; }
}
```

## Transaction Boundaries

**Rule:** All service methods that modify data MUST have @Transactional.

✅ CORRECT:
```java
@Transactional public void saveInvoice(Invoice inv) { repo.save(inv); }
```

❌ WRONG:
```java
public void saveInvoice(Invoice inv) { repo.save(inv); }  // Missing!
```

## Database Queries

**Rule:** Use JpaRepository or @Query with named parameters. Never string concatenation.

✅ CORRECT:
```java
@Query("SELECT i FROM Invoice i WHERE i.invoiceNr = :nr")
List<Invoice> findByNr(@Param("nr") String nr);
```

❌ WRONG:
```java
String query = "SELECT * FROM INVOICE WHERE INVOICE_NR = '" + nr + "'";
```
```

### React/TypeScript

```markdown
---
description: React component conventions
paths: ["frontend/src/app/**"]
---

# React Conventions — <APPLICATION_NAME>

## Functional Components Only

**Rule:** Use functional components with hooks. No class components.

✅ CORRECT:
```typescript
export const UserCard: React.FC<UserCardProps> = ({ user }) => {
  const [isLoading, setIsLoading] = React.useState(false);
  return <div>{user.name}</div>;
};
```

## Hook Rules

**Rule:** Hooks only at component top level. Never call conditionally.

✅ CORRECT:
```typescript
export const UserForm = () => {
  const [name, setName] = React.useState("");  // Top level
  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};
```

## Prop Drilling Prevention

**Rule:** Use Context for > 2 levels of nesting.

✅ CORRECT (shallow):
```typescript
<Header user={user}><Title userName={user.name} /></Header>
```

✅ CORRECT (deep → use Context):
```typescript
<UserContext.Provider value={user}>
  <Sidebar />  // doesn't need user prop
</UserContext.Provider>
```
```

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| Glob doesn't match files | Syntax error | Test: `find . -path "<glob>"` |
| Rule ignored in PR review | Path glob doesn't match | Expand glob or update path |
| Team bypasses rule | Not automated | Add to SAST linting or CI/CD |
| Rule contradicts enterprise | App rule widened enterprise | Narrow it further |

---

## Related Documentation

- **Enterprise rules:** `@enterprise/rules/` — organization-wide
- **Security guardrails:** `security-guardrails.md` — mandatory controls
- **Conventions:** `10-app.md` — naming, patterns
- **Context hazards:** `.claude/context/hazards.md` — fragile areas

---

**Owned by:** <Tech Lead / Platform Team>  
**Last updated:** <YYYY-MM-DD>  
**Review frequency:** Quarterly
