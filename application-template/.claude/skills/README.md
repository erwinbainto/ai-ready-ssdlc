# Skills

This directory optionally contains skill definitions for this application. It is empty
by default; the five seed skills (advisory-writeup, vuln-patch-triage, containerization-assessment,
receipt-check, repo-onboarding-brief) are defined in the enterprise harness and available globally.

Use this directory only to define application-specific skills that do not exist in the
enterprise set.

## Authoring rules

- A skill is a **folder** containing `SKILL.md`. A loose `.md` file in `skills/` does not load.
- `description` decides whether the model invokes it. Write it like a search query.
- `disable-model-invocation: true` makes a skill user-only.
- Bundled files in the skill folder are read on demand.

## Verify with

```
/skills
```

The seed skills plus any application-specific skills will be listed.
