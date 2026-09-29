# <APPLICATION_NAME>

Extends the enterprise harness instructions. Everything in the enterprise set applies
here and is not restated.

## What this application is

<One paragraph in business terms. What it does, for whom, why it matters.>

## Repository map

| Area | Path | Responsibility |
|---|---|---|
| <entry point> | `<path>` | <what it does> |
| <core module> | `<path>` | <what it does> |
| <generated> | `<path>` | **Generated. Never hand-edit.** |

## Commands

The declared command contract is in `.claude/context/commands.md`. Use those commands and
no others when producing receipts.

## Domain terms

See `.claude/context/glossary.md` for terms an outsider would misread.

## Hazards

See `.claude/context/hazards.md`. Read it before proposing changes in those areas.

## Local conventions

Where this application departs from the enterprise standard, each with a reason:

- <convention> — <why>

## Narrowed rules

Where this application is stricter than the enterprise set:

- <rule> — <why>

## Write boundary

Read-only. Write, commit, merge, pipeline trigger and deployment are denied by policy.
Gated actions escalate to <NAMED_APPROVER>.
