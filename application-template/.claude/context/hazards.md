# Hazards — <APPLICATION_NAME>

Fragile areas, security risks, incident history. **Read before proposing changes.**

**Last Updated:** <YYYY-MM-DD>  
**Owner:** <Security Lead>

---

## Security Hazards

| Vulnerability | Path | Why Critical | Impact | Mitigation | Status | Owner |
|---|---|---|---|---|---|---|
| <risk> | `<path>` | <blast radius> | <consequence> | <control> | <Open/Mitigated> | <name> |

See `docs/security/threat-model.md` for full threat analysis.

---

## Do Not Touch Without Review

| Area | Path | Why | Owner |
|---|---|---|---|
| <fragile area> | `<path>` | <reason> | <name> |

---

## Incident History

| What Happened | Area | When | Lesson |
|---|---|---|---|
| <incident> | `<path>` | <YYYY-MM-DD> | <implication> |

Full logs: `docs/audits/incidents/`

---

## Surprising Behaviour

Non-obvious behavior that may cause bugs:

- <behavior>: <why it works this way>

---

## Known Debt

| Debt | Area | Why Accepted | Remediation | Target |
|---|---|---|---|---|
| <debt> | `<path>` | <reason> | <plan> | <date> |

Full list: `docs/architecture/DEBT.md`

---

## Before Making Changes

- [ ] I've read this entire hazards document
- [ ] I understand the security implications
- [ ] I've consulted with the owner listed above
- [ ] My changes maintain or improve mitigations

See: `.claude/rules/security-guardrails.md` (mandatory rules)
