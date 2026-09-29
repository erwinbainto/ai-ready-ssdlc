# Graders for vulnerability patch triage

Evaluation criteria for the vuln-patch-triage skill output.

## Correctness (must pass)

- [ ] Reachability determination is correct: if the output says reachable, the package is actually used and the function is actually called
- [ ] If unreachable, the reasoning is sound: the package is not imported, OR the vulnerable function is not called
- [ ] Evidence supports the claim: file paths and line numbers, or import statements

## Specificity (should pass)

- [ ] Remediation is specific, not vague: "update to 2.5.0" not "update the package"
- [ ] Risk is quantified: "High — production outage possible if X is triggered" not "could be risky"
- [ ] Effort is rough but reasonable: "1-2 hours" not "effort varies"

## Completeness

- [ ] All five parts are present: component, reachability, remediation, risk, effort
- [ ] No made-up information: if the analysis cannot be completed, that is stated

## Failure cases (fail immediately)

- [ ] Hallucinates reachability without evidence
- [ ] Confuses "the package is installed" with "the vulnerable code is executed"
- [ ] Proposes a remediation that would not fix the vulnerability
- [ ] Leaves the finding in advisory format incomplete
