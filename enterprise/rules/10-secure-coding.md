---
description: Secure coding standards and practices for the organization.
paths: ["<STACK_GLOBS>"]
---

# Secure coding standards

Applies to all code at this engagement.

## Mandatory practices

- Input validation: all untrusted input must be validated before use
- Output encoding: encode output appropriately for its context
- Authentication and authorization: verify identity and permissions explicitly
- Cryptography: use approved algorithms and libraries; never roll your own
- Error handling: never leak sensitive information in error messages
- Logging: log security events with sufficient context; never log secrets

## OWASP top 10 — what applies here

| Vulnerability | Policy | Evidence |
|---|---|---|
| <vulnerability> | <what we do / do not do> | <where this is verified> |

## <STACK> specific standards

Replace this section with language-specific secure coding guidance.

Examples:
- Go: use standard library `crypto` packages; use `encoding/base64` not custom encoding
- Node.js: use parameterized queries with `pg` or similar; use `bcrypt` for password hashing
- Python: use `secrets` module for tokens; validate with `marshmallow` or `pydantic`

## Dependencies and supply chain

- Dependency updates are tracked in `<path>` and reviewed for security advisories
- Locked versions: `<lock_file>`
- Audit command: `<command>`
