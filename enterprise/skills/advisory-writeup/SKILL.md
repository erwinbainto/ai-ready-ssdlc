---
name: advisory-writeup
description: Format raw findings into the agreed advisory shape so output is comparable across applications. Use when findings exist but are not yet in the required format.
argument-hint: "[findings or file]"
---

# Advisory writeup

Format into the agreed shape: $ARGUMENTS

## Steps

1. Separate the input into discrete findings. One issue per finding.
2. For each, apply the five-part shape from `rules/00-advisory-format.md`.
3. Where evidence is missing, go and get it. Do not write a finding without a file and line,
   command output or ticket reference.
4. Where evidence cannot be obtained, mark the finding as unevidenced rather than dropping
   or softening it.

## Output

Findings in the advisory format, ordered by risk.

Consolidation across applications depends on this shape. A well-argued finding in the
wrong format costs someone else an hour later.
