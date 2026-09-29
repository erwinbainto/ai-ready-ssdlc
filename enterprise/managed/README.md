# Tier 0 policy

Deployed to the machine, not committed to an application repository. This is where the
security and governance boundaries actually live. Everything else in this set is guidance the model reads.

## Choose the delivery route first

**Route A — exclusive control.** `managed-settings.json` and `managed-mcp.json` placed at
a system path. Needs administrator privileges, so in practice device management tooling.

| Platform | Path |
|---|---|
| macOS | `/Library/Application Support/ClaudeCode/` |
| Linux and WSL | `/etc/claude-code/` |
| Windows | `C:\Program Files\ClaudeCode\` |

**Route B — enforced catalogue without device management.** Deliver the same settings
through server-managed settings from the admin console. `managed-mcp.json` is a standalone
file and cannot travel this way, so use the `managedMcpServers` and `allowedMcpServers`
block inside managed settings instead.

Route B is the pragmatic choice where fleet management is inconsistent. It reaches machines
without device management infrastructure.

## The question that decides it

If Claude Code traffic is routed through a client-controlled gateway, settings from the
admin console are not fetched and policy must arrive by the managed file. Answer this
before authoring anything.

## Verify before fleet rollout

Deploy to one machine, open a session, run `/status`. The enterprise source must appear.
A policy that is silently not loading looks identical to no policy at all.
