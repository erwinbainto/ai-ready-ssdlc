---
description: API and interface standards for the organization.
paths: ["<STACK_GLOBS>"]
---

# Interface standards

Applies to all external and internal interfaces: REST, gRPC, queues, events.

## API design

- Use semantic HTTP verbs (GET for read, POST for create, PUT/PATCH for update, DELETE for delete)
- Version APIs explicitly in URL or Accept header
- Use standard status codes (200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Internal Server Error)
- Return errors in a consistent format

## Authentication and authorization

- APIs require authentication except where explicitly public
- Use tokens (JWT, OAuth 2.0, API keys); never embed passwords in requests
- Encode tokens in Authorization header; never in query parameters or body
- Validate scopes and permissions on every request

## Documentation

- Every interface must have a specification: OpenAPI, gRPC descriptor, AsyncAPI, or equivalent
- Specifications are versioned and live alongside code
- Breaking changes require a version bump and migration period

## Breaking changes

- Provide a migration period before removing an old interface
- Document the path forward for clients
- Notify consumers in advance

## <STACK> specific

Replace this with framework-specific guidance (e.g., Flask, Express, FastAPI, Go net/http).
