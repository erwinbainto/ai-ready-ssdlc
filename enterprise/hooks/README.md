# Hooks

Unlike instructions, a hook runs. It can execute a command, an HTTP request, a tool call, a
prompt or a subagent.

Register in settings, referencing scripts via `$CLAUDE_PROJECT_DIR` so resolution does not
depend on the working directory:

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/hooks/session-start.sh" } ] }
    ],
    "PreToolUse": [
      { "matcher": "*", "hooks": [ { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/hooks/pre-tool-use.sh" } ] }
    ]
  }
}
```

## Two cautions

**These scripts do not enforce anything.** The permission deny list is the control. These
produce the audit trail that evidences it. Do not present a logging hook as a boundary.

**Managed-only policy suppresses pod hooks.** If `allowManagedHooksOnly` is set, hooks
authored in an application will not run. Confirm the position before authoring any. Verify
with `/hooks`.

Make them executable: `chmod +x hooks/*.sh`.
