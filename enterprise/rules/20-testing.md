---
description: Testing and quality standards across applications.
paths: ["<STACK_GLOBS>"]
---

# Testing standards

Applies to all tests and quality gates.

## Coverage expectations

- Unit tests: <minimum_coverage_percent>% of new code
- Integration tests: happy path and error paths
- Security tests: where OWASP or regulatory scope applies

## Test isolation

- Tests do not depend on external services unless explicitly integration tests
- Each test is independent and can run in any order
- Database tests use transactions or fixtures; they never leave state behind

## Mocking and fakes

- Mock external APIs; do not make real calls during test runs
- Distinguish unit tests (everything mocked) from integration tests (real databases allowed)
- Document what is mocked and why

## Test commands

The verifier role runs only these commands. Nothing else counts as a receipt.

| Command | Purpose | Environment |
|---|---|---|
| `<command>` | <purpose> | <local / CI / staging> |

## Baseline

Record pre-existing test failures here, if any.
