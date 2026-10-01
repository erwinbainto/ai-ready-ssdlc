# Context — Quick Reference

These files form your **knowledge connection** — loaded by Claude Code as the context for working in this application.

**For detailed authoring instructions**, see `../../docs/guides/context/README.md`.

## Files in This Directory

| File | Purpose | When to Update |
|------|---------|-----------------|
| `architecture.md` | System structure, components, responsibilities, data flow, key decisions | When architecture changes |
| `commands.md` | Available commands and their behavior contracts (build, test, lint, type-check) | When build process changes |
| `glossary.md` | Domain terms, acronyms, non-obvious concepts unique to this app | When terminology changes |
| `hazards.md` | Known risks, security vulnerabilities, fragile areas, incident history | After incidents or security findings |
| `security-posture.md` | Compliance baseline, authentication method, data classification, known risks | When compliance requirements change |

## How These Are Used

Claude Code loads all files in this directory automatically when you open a session. Every agent and skill has access to this knowledge.

## Getting Started

1. **First time?** Read `../../docs/guides/context/README.md` (detailed authoring guide)
2. **Quick reference?** Each `*.md` file has placeholder sections — fill them in with real values
3. **Team sync?** Ownership and update frequency are documented in the guide

## Examples

See `../../docs/guides/getting-started-sample.md` for a worked example of a completed context pack.
