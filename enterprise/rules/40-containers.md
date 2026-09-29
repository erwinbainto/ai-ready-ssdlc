---
description: Containerization standards for applications.
paths: ["**/Dockerfile*", "**/docker-compose*", "**/*.yaml", "**/*.yml"]
---

# Container standards

Applies to all containerized workloads.

## Image security

- Use minimal base images (Alpine, distroless, scratch where applicable)
- Do not run as root; create a non-root user
- Scan images for vulnerabilities: `<SCAN_COMMAND>`
- Remove build tools from runtime images (use multi-stage builds)
- Never embed secrets in images

## Dockerfile best practices

- Each layer should reduce image size or add functionality; avoid unnecessary layers
- Copy only what is needed (use `.dockerignore`)
- Combine commands where it reduces layers without sacrificing clarity
- Use specific version tags; never `latest`

## Runtime configuration

- Configuration must be read from environment variables or files at runtime, not baked in
- Secrets must come from secrets management, never environment variables in images
- Health checks must be defined
- Resource limits must be set (CPU, memory)

## Orchestration

- Manifests use the organization's approved format (Docker Compose, Kubernetes, etc.)
- All services are defined in source control
- Images are tagged with commit hash or version number

## Verification

- Images can start and reach readiness within <timeout>
- Health check passes consistently
- Logs do not contain secrets or credentials
