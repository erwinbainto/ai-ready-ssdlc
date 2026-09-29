---
description: The required shape of any finding, recommendation or analysis.
---

# Advisory format

Loads in every session. Applies to anything presented as a finding.

Use the five-part shape: observation, evidence, proposal, risk, effort. Keep each part to what is true.

## Rules

- One finding per item. Do not bundle three problems into one paragraph.
- Evidence is a file and line, command output, or a ticket reference. "It appears that" is
  not evidence.
- Effort is rough and labelled rough. Do not imply precision you do not have.
- If you are uncertain whether something is a finding, say so and present it anyway with
  the uncertainty stated.

## Not this

> The error handling could be improved in several places and there may be some risk around
> the payment flow.

## This

> **Observation.** `PaymentClient.retry()` swallows all exceptions.
> **Evidence.** `<path>:88-94`, bare except with `pass`.
> **Proposal.** Catch the transport exception explicitly, re-raise anything else.
> **Risk.** Medium. A failed settlement currently logs nothing.
> **Effort.** Small, roughly.
