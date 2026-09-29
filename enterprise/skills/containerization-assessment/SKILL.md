---
name: containerization-assessment
description: Assess this application's readiness for containerization. Identify gaps, blockers, effort and sequence.
---

# Containerization assessment

Assess how ready this application is for containerization.

## Steps

1. Establish the current runtime: build process, startup, configuration, runtime assumptions.
2. Identify state management: files, in-process caches, affinity, anything assuming one instance.
3. Identify configuration and secrets: what is baked at build time, what should be runtime.
4. Identify undocumented build dependencies: tools, services, environment variables needed to build.
5. Check existing containerization artifacts (Dockerfile, docker-compose, K8s manifests) against enterprise rules.

## Output

Target state, gap list with each gap classified as:
- **Small**: cosmetic or convenience (< 1 day)
- **Medium**: functional gap, requires work (1-3 days)
- **Structural**: architectural blocker (> 1 week or needs design)

Also provide:
- Proposed sequence (what to do first)
- Rough effort estimate
- Which gaps must be closed before containerization (blockers)
- Which gaps make it untidy but are not blockers

The container-assessor agent runs this routine. You delegate to it when the question is
whether and how this application can containerize.
