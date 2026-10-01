# Hazards — <APPLICATION_NAME>

Fragile areas, incident history, high blast radius, security risks. Read before proposing changes here.

## Security Hazards — High Risk Areas

Areas with security implications. Changes here require security review before merge.

| Vulnerability | Path | Why Critical | Impact | Mitigation | Status | Who to Ask |
|---|---|---|---|---|---|---|
| <vulnerability> | `<path>` | <blast radius> | <consequence if exploited> | <control> | <Open/Mitigated> | <name> |

**Examples:**

| SQL injection in search | `src/api/SearchController.java` | Dynamic query building | Data breach affecting all users | Parameterized queries + SAST scanning | Mitigated | Backend Lead |
| Missing rate limiting | `src/auth/LoginEndpoint.java` | Brute force attacks possible | Account takeover | IP-based rate limit (5 attempts/min) | Open | Security Lead |
| Hardcoded secrets in config | `src/config/application.properties` | Credentials exposed if repo leaked | Full system compromise | Use environment variables | Mitigated | DevOps Lead |
| Unencrypted user data | `src/user/UserRepository.java` | Data exposure at rest | Privacy violation, compliance breach | AES-256 encryption at rest | In Progress | DBA |

---

## Do not touch without review

| Area | Path | Why | Who to ask |
|---|---|---|---|
| <area> | `<path>` | <reason> | <name> |

---

## Incident history

| What happened | Area | Lesson | Date |
|---|---|---|---|
| <incident> | `<path>` | <what it means for future changes> | <YYYY-MM-DD> |

**Example:**

| Brute force attack on login | `src/auth/LoginEndpoint.java` | Rate limiting must be enforced on auth endpoints; always test with load | 2026-09-15 |
| Backup found unencrypted in S3 | `infrastructure/backup-config.yaml` | All backups must be encrypted at rest; add encryption check to deployment | 2026-08-20 |

---

## Surprising Behaviour

Things that work in a way an experienced engineer would not expect. The retry that is not idempotent. The config read once at start. The timeout that is actually two timeouts.

<Add unexpected behaviors specific to this app>

**Example:**
- User sessions are cached in-memory for performance; they don't immediately reflect database changes. Cache invalidates after 5 minutes or on logout.
- Database connection pooling max connections is capped at 20; high traffic bursts can exhaust the pool and block new connections (not fail gracefully).

---

## Known Debt

Debt the team is aware of and has chosen to live with, so it is not re-reported as a discovery every time someone new reads the code.

| Debt | Area | Why Accepted | Remediation Plan | Owner | Target Date |
|---|---|---|---|---|---|
| <debt> | `<path>` | <business reason> | <how to fix> | <name> | <YYYY-MM-DD> |

**Example:**
| Legacy authentication system has no MFA | `src/auth/` | Migrating to OAuth 2.0; MFA will be enabled post-migration | Complete OAuth migration first (Q4 2026) | Auth Team | 2026-12-31 |
| Batch job has no timeout; can hang indefinitely | `src/jobs/BatchProcessor.java` | Rare in practice; high effort to refactor; monitoring alerts if stuck | Add timeout wrapper in scheduler | Platform Team | 2026-11-30 |

---

## Security Review Checklist

Before proposing changes to hazard areas, verify:

- [ ] I've read this entire hazards document
- [ ] I understand the security implications
- [ ] I've consulted with the "Who to Ask" owner
- [ ] I've included security tests in my PR
- [ ] My changes maintain or improve the current mitigations
- [ ] I've updated the mitigation status if relevant

**See also:** 
- `.claude/rules/security-guardrails.md` for mandatory security rules
- `.claude/context/security-posture.md` for compliance obligations
- `docs/security/threat-model.md` for threat landscape
