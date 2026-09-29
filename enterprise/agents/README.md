# Agent roles

Five roles, all read-only at the governed plateau. The body of each file is the **system prompt** for
that role, not a user prompt. This is the most common authoring mistake.

| Role | Tools | Use it for |
|---|---|---|
| `explorer` | read and search | where something lives, what depends on it |
| `reviewer` | read and search | whether something is sound |
| `verifier` | read, search, restricted shell | producing receipts |
| `vuln-analyst` | read and search | vulnerability and patch analysis |
| `container-assessor` | read and search | containerization readiness |

## Rules

- Use these names unchanged in every application. Renaming locally breaks reuse and cross-application analysis.
- `tools` is enforced. An instruction telling a role not to use a tool is not.
- `verifier` is the only role with shell access, and the permission deny list still bounds
  it. It runs declared commands, nothing else.
- Set `isolation: worktree` on any role that runs commands, if your policy permits it.

Verify with `/agents`.
