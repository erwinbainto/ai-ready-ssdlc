# Application Verification Checklist

Run this after deploying an application harness instance. Every row is evidence for deployment records.

**Prerequisite:** Enterprise harness must be deployed and verified first (enterprise `VERIFY.md`).

## Configuration verification

| Check | Command/Action | What good looks like |
|---|---|---|
| Enterprise policy active | `/status` | Managed or enterprise appears under setting sources (inherited from fleet) |
| Application instructions loaded | `/context` | Both enterprise `CLAUDE.md` and this application's `CLAUDE.md` appear |
| Application context files present | `/context` | Knowledge connection loaded: commands, architecture, glossary, hazards from `.claude/context/*` |
| Path-scoped rules gate correctly | `/context` with relevant file open | Application rules appear when `.claude/` files are open; disappear elsewhere |
| Admitted MCP servers | `/mcp` | Exactly the servers listed in `D4_Application_Harness_Form.md` section 4 |
| MCP servers actually work | Ask a question requiring each server | Real answer from the real system; log the server name and query once per server |
| Agents available | `/agents` | Five enterprise roles available; check that permissions match form section 1 (role → tool mapping) |
| Application skills | `/skills` | Enterprise seed skills plus any app-bundled skills from `.claude/skills/` |
| Enterprise hooks active | `/hooks` | Pre-tool-use, session-start hooks from enterprise are registered |
| Build/run environment | `<BUILD_COMMAND>` from form section 5 | Build succeeds; environment matches deployment target (dev/staging/prod per form) |
| Setup diagnostics | `/doctor` | No unresolved findings; any warnings match known constraints from form section 0 |

## Boundary verification (proves read-only harness)

| Check | Action | What good looks like |
|---|---|---|
| Write boundary holds | Attempt to edit a source file (e.g., `git add; git commit`) | Claude refuses with a trace reference; no file is modified |
| Test write-attempt | Run the write-attempt test defined in form section 5 | Refusal logged; evidence captures the trace reference and tool rejection reason |

## Deployment completion checklist

- [ ] All form fields in `D4_Application_Harness_Form.md` filled (no `<LIKE_THIS>` placeholders remain)
- [ ] `.claude/` directory structure complete:
  - [ ] `.claude/settings.json` (narrowed permissions, hooks wired)
  - [ ] `.claude/context/` files present (commands, architecture, glossary, hazards)
  - [ ] `.claude/rules/` rules scoped correctly (if app-specific rules exist)
- [ ] Context files reviewed and approved by dev lead (section 2 of form)
- [ ] MCP servers tested and working (section 4 of form)
- [ ] Configuration verification table above: all rows green
- [ ] Boundary verification table above: all rows green
- [ ] Write-attempt test evidence captured (trace reference)
- [ ] Deployment records filed (form, verification evidence, trace references)

## If verification fails

**Permission denied on `/context`, `/agents`, `/mcp`:**
- Check `.claude/settings.json` is not missing
- Verify enterprise settings are inherited (run `/status`)
- Confirm Claude Code has reloaded (restart the session)

**MCP server connection fails:**
- Verify server is in the admitted catalogue (enterprise managed settings)
- Check network connectivity to server endpoints
- Confirm credentials/auth (if applicable) are configured
- Re-run the test query to verify transient vs. persistent failure

**Write-attempt succeeded (boundary breach):**
- **Critical:** Do not proceed. Escalate to enterprise team.
- Verify enterprise hooks are active (`/hooks`)
- Check that `.claude/settings.json` has the correct permission mode
- Confirm read-only core is not bypassed (review `enterprise/rules/`)

## Reference

- **Enterprise VERIFY.md:** `VERIFY.md` (root)
- **Application form:** `D4_Application_Harness_Form.md`
- **Enterprise CLAUDE.md:** `enterprise/CLAUDE.md`
- **Application CLAUDE.md:** `.claude/CLAUDE.md` (this repository)
