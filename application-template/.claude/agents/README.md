# Agent roles

This directory optionally contains agent role definitions for this application. It is empty
by default; the five agent roles (explorer, reviewer, verifier, vuln-analyst, container-assessor)
are defined in the enterprise harness and available globally.

Use this directory only to override or extend the enterprise roles for this specific application.
In most cases, you do not need to.

## Verify with

```
/agents
```

The five roles from the enterprise set should be listed. Any application-specific overrides
will also appear.
