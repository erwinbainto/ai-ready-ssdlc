---
name: repo-onboarding-brief
description: Generate a brief, structured overview of a codebase for someone new to it. Maps entry points, key modules, dependencies, and highlights gaps in documentation.
---

# Repository onboarding brief

Generate a brief for someone new to this codebase.

## Steps

1. Locate entry points: main(), CLI entry, HTTP handlers, queue listeners, etc.
2. Map key modules and their responsibilities. Follow imports.
3. Identify major dependencies: external packages, internal modules, data stores.
4. Document interfaces: what this application exposes and consumes.
5. Note gaps: undocumented areas, unusual patterns, missing tests, known debt.

## Output

Structured brief:
- **What it does**: business purpose in one paragraph
- **Entry points**: where execution starts
- **Architecture**: key modules and dependencies, one paragraph
- **Interfaces**: what it exposes (APIs, queues, files) and what it consumes
- **Data**: what it owns, what it reads
- **Gaps**: undocumented areas, missing pieces, areas of concern

Keep it under one page. A comprehensive onboarding brief is better than exhaustive documentation.

The explorer agent runs this routine. You delegate to it when the question is "where do I start?"
