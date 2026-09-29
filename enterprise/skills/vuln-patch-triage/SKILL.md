---
name: vuln-patch-triage
description: Take a vulnerability or patch ticket. Determine what it means for this application, whether the vulnerable path is reachable, and propose remediation.
argument-hint: "[ticket or vulnerability]"
---

# Vulnerability and patch triage

Triage this vulnerability or patch ticket: $ARGUMENTS

## Steps

1. Read the ticket. Establish the affected component and version range.
2. Search the codebase to determine whether this application uses the affected component.
3. If used, determine whether the vulnerable path is actually reachable:
   - Is the vulnerable function imported?
   - Is it called?
   - Can it be reached from application entry points?
4. Document reachability with evidence.
5. Identify the remediation path: version bump, configuration change, code change, or acceptance.

## Output

A patch advisory:
- **Component and version**: what is affected
- **Reachability**: is the vulnerable code actually used? Evidence.
- **Proposed remediation**: specific action
- **Risk if deferred**: business impact
- **Effort**: rough estimate

The vuln-analyst agent runs this routine. You delegate to it when the question is whether
a vulnerability matters to this application.
