# Vulnerability patch triage eval

## Input

Ticket: [SECURITY-1234] Vulnerability in <AFFECTED_PACKAGE> <VERSION>

**Component**: <PACKAGE_NAME>
**Version**: <AFFECTED_VERSION_RANGE>
**CVE**: CVE-XXXX-XXXXX
**Severity**: <HIGH | CRITICAL>
**Description**: <VULNERABILITY_DESCRIPTION>

**Affected Code Path**: <vulnerability_path_in_affected_library>
**Remediation**: Update to <FIXED_VERSION> or apply patch <PATCH_ID>

## Expected output

A patch advisory covering:

1. **Component and version**: confirmed from ticket
2. **Reachability analysis**: determine whether <AFFECTED_PACKAGE> is used in this codebase
   - Is it imported? Evidence (file and import statement)
   - Is the vulnerable function called? Evidence
   - Can it be reached from entry points? Evidence
3. **Proposed remediation**: specific action (version bump, config change, code change)
4. **Risk if deferred**: business impact
5. **Effort**: rough estimate

The grader checks:
- Did the analysis correctly identify reachability (or lack thereof)?
- Is the evidence concrete (files and lines)?
- Is the remediation specific and actionable?
