# Verification routine

Run after any deployment or change. Every row is evidence for the deployment records.

| Check | Command | What good looks like |
|---|---|---|
| Enterprise policy is active | `/status` | Managed or enterprise appears under setting sources |
| Permission mode | `/status` | The mode set by policy, not a developer default |
| Instructions loaded | `/context` | Both the enterprise and the application `CLAUDE.md` |
| Path-scoped rules gate correctly | `/context` | A rule appears with a matching file open, absent without |
| Admitted servers only | `/mcp` | Exactly the catalogue. An unadmitted server does not appear |
| Server actually works | ask a real question | A real answer from the real system, logged once per server |
| Agent roles present and scoped | `/agents` | The five roles, each restricted to its declared tools |
| Skills available | `/skills` | Seed skills plus bundled skills |
| Hooks registered | `/hooks` | The enterprise hooks. Note managed-only policy may suppress pod hooks |
| Setup problems | `/doctor` | No unresolved findings |
| Telemetry and adoption | `/usage`, `/insights` | Usage and cost visible |
| Write is refused | attempt an edit | Refusal, captured with a trace reference |

The last row is the one that proves the deliverable. Everything else proves configuration.
