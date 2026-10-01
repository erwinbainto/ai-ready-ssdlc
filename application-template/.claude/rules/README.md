# Rules — Quick Reference

These files define **application-specific rules and guardrails** that narrow (never widen) the enterprise harness policy.

**For detailed guidance on authoring rules**, see `../../docs/guides/rules/README.md`.

## Files in This Directory

| File | Purpose | Scope | When to Update |
|------|---------|-------|-----------------|
| `10-app.md` | App-specific conventions: naming patterns, coding standards, anti-patterns | Path-scoped to `**/*` | When team standards change |
| `security-guardrails.md` | Mandatory security rules: no hardcoded secrets, authentication patterns, data handling | Path-scoped (language-specific) | After security audit or incident |

## Rule Hierarchy

```
Enterprise policy (from plugin)
    ↓ (cannot be widened)
Application rules (these files)
    ↓ (narrows only)
Claude Code enforcement (prevents violations)
```

If a rule in this directory appears to permit something the enterprise forbids, the enterprise rule wins and this file is wrong.

## Getting Started

1. **First time?** Read `../../docs/guides/rules/README.md` (detailed authoring guide)
2. **Review examples?** See the placeholder sections in `10-app.md` and `security-guardrails.md`
3. **Test rules?** Use `/doctor` in Claude Code to verify rules are loaded correctly

## Examples

See `../../docs/guides/` for:
- Fintech application security guardrails (PCI DSS)
- Healthcare application rules (HIPAA)
- Language-specific patterns (Java, Python, Node.js)

## Verification

Run this Claude Code command to verify rules are active:

```
/status    # Shows enterprise policy + app rules loaded
/doctor    # Diagnoses any rule loading issues
```
