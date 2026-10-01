# Hooks — Quick Reference

These files define **lifecycle automation scripts** that run at specific Claude Code events.

**For detailed guidance on authoring and wiring hooks**, see `../../docs/guides/hooks/README.md`.

## Hook Types

| Hook | When it Runs | Purpose | Example |
|------|---|---------|---------|
| `session-start.sh` | When Claude Code starts a session | Setup checks, environment validation | Verify required tools are installed |
| `pre-tool-use.sh` | Before any tool is invoked | Permission gates, credential validation | Check user authorization before running commands |
| `*-approved.sh` | After a gated action is approved | Post-approval automation | Deploy after human approval |

## Files in This Directory

Currently configured:
- `session-start.sh` — Runs on session start (example: checks build tools, verifies env vars)

Optional:
- Add `pre-tool-use.sh` for permission gates (managed policy may block additions)
- Add `*-approved.sh` for post-approval workflows

## Getting Started

1. **Understand the lifecycle?** Read `../../docs/guides/hooks/README.md`
2. **Wire a hook?** 
   - Create the script (e.g., `my-hook.sh`)
   - Add entry to `.claude/settings.json` under `hooks:`
   - Test with `/doctor`

## Hook Constraints

- Managed hooks (from enterprise) always run — cannot be disabled
- Pod hooks (app-specific) require enterprise permission (`allowManagedHooksOnly: false`)
- Hooks run in the order they appear in `settings.json`
- Output is captured and logged; long-running hooks will timeout

## Verification

Run these commands to verify hooks:

```
/hooks          # List all active hooks
/doctor         # Diagnose hook loading issues
/status         # Confirm enterprise + app hooks registered
```

## Examples

See `../../docs/guides/hooks/README.md` for:
- Credential validation hooks
- Build environment checkers
- Permission gates
- Post-approval deployment scripts
