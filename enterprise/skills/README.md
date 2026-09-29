# Seed skills

Five skills, all read-only, each a folder containing `SKILL.md` and any bundled files.

| Skill | Invocation | Feeds |
|---|---|---|
| `repo-onboarding-brief` | model or `/repo-onboarding-brief` | enablement, pilots |
| `vuln-patch-triage` | model or `/vuln-patch-triage` | vulnerability and patch analysis |
| `containerization-assessment` | model or `/containerization-assessment` | containerization report |
| `receipt-check` | user only | verification |
| `advisory-writeup` | model or `/advisory-writeup` | consolidation |

## Authoring rules

- A skill is a **folder** containing `SKILL.md`. A loose `.md` file in `skills/` does not
  load. This is the most common reason a skill never appears.
- `description` decides whether the model invokes it. Write it like a search query, naming
  the situation and the artefacts, not a title. Vague descriptions fire on everything or
  never.
- `disable-model-invocation: true` makes a skill user-only. Use it where a human should
  choose to run the thing.
- Bundled files in the skill folder are read on demand. Put long templates there rather
  than in `SKILL.md`.

## Before publishing anything new

Write an eval suite. See `../evals/README.md`. A skill without a measured contribution is
not published at this engagement.

Verify with `/skills`.
