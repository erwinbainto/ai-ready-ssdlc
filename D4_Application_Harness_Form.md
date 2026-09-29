# D4 Application Harness Form

> **What this is.** A fill-in form, completed **once per application** by the FDE with the
> RRD Dev Lead. Completing it produces the tier-3 Claude Code artefacts for that application
> and the evidence for its **D4 Application Instance Record**.
>
> **Prerequisite.** The enterprise form is done and the plugin is published. You will cite
> its version. Do not start until you can.
>
> **Legend.** `<...>` = replace. **GENERATE** = create the file. **VERIFY** = run the
> command, confirm output. **ESCALATE** = stop until agreed.

---

## 0. Application identity and prerequisites

| Field | Value |
|---|---|
| Application name | `<name>` |
| Enterprise plugin version inherited | `<from enterprise form §11>` |
| RRD Dev Lead (co-author) | `<name>` |
| RRD application owner (signs autonomy) | `<name>` |
| Autonomy target from D2 (current → target) | `<L0→L1 / L1→L2>` |
| D1 readiness summary + open blockers | `<...>` |
| D3 frozen KPIs for this app | `<count + reference>` **ESCALATE if not frozen** |
| Repository set, primary marked | `<repos>` |
| Languages / frameworks in scope | `<stack>` |

**Install the plugin first** (do not copy its files):
```
/plugin marketplace add <YOUR_MARKETPLACE_URL>
/plugin install rrd-harness@<YOUR_MARKETPLACE_NAME>
```

---

## 1. Application instructions (primitive 1) → `CLAUDE.md`

| Field | Value |
|---|---|
| One-line business purpose | `<...>` |
| Entry points (area / path / role) | `<...>` |
| Generated paths — never hand-edit | `<...>` |
| Named RRD approver for gated actions | `<...>` |
| Local conventions (each with reason) | `<...>` |
| Rules narrowed from enterprise | `<...>` |

**GENERATE** `<app>/CLAUDE.md` — must reference the enterprise set, never copy it. Keep short.
**VERIFY** `/context` shows both enterprise and app instructions loaded.

> If a rule appears in both files, one is wrong. If the app rule is *broader* than the
> enterprise rule it extends, the app file is wrong.

---

## 2. The knowledge connection (primitives 2, 3) → `.claude/context/`

This is the part that cannot be templated. Draft with the `explorer` role, then the Dev Lead
corrects it. A draft nobody corrected is worse than nothing.

### 2a. `architecture.md`
| Field | Value |
|---|---|
| What it is / how it fits | `<...>` |
| Key components + responsibilities | `<...>` |
| Interfaces (name / type / consumers / contract) | `<...>` |
| Data and state ownership | `<...>` |
| **Unowned or unclear components** | `<name them — this is a real finding>` |

### 2b. `commands.md` — the command contract
| Purpose | Command | Passes today? |
|---|---|---|
| Build | `<...>` | `<yes/no>` |
| Test | `<...>` | `<yes/no>` |
| Lint | `<...>` | `<yes/no>` |
| Type check | `<...>` | `<yes/no>` |

Baseline — currently failing: `<list or none>`

> State this honestly. An unstated failing baseline makes the first agent-assisted change
> look like it broke something, and contaminates the D10 comparison.

### 2c. `hazards.md` — do-not-touch, incidents, surprising behaviour: `<...>`
### 2d. `glossary.md` — only terms whose local meaning differs from the obvious: `<...>`

**GENERATE** the four context files.
**VERIFY** `/context`; ask one real question per source and record the answer.

---

## 3. Sources indexed (primitive 2)

| Source | Location | Index method | Owner | Verification Q + answer |
|---|---|---|---|---|
| Source code | `<...>` | `<...>` | `<...>` | `<...>` |
| Specs / contracts | `<...>` | `<...>` | `<...>` | `<...>` |
| Tests | `<...>` | `<...>` | `<...>` | `<...>` |
| ADRs / decisions | `<...>` | `<...>` | `<...>` | `<...>` |
| Docs | `<...>` | `<...>` | `<...>` | `<...>` |
| Manifests | `<...>` | `<...>` | `<...>` | `<...>` |
| Incidents | `<...>` | `<...>` | `<...>` | `<...>` |
| Metrics / logs | `<...>` | `<...>` | `<...>` | `<...>` |
| Tickets | `<...>` | `<...>` | `<...>` | `<...>` |
| Vulnerability data | `<...>` | `<...>` | `<...>` | `<...>` |

> "Indexed" is not "delivered". The verification answer is the evidence indexing worked.

---

## 4. Server bindings (primitive 4) → `.mcp.json`

Bind only from the admitted catalogue. An unadmitted server will not load.

| Category | Bound? | Read scope | First successful call logged |
|---|---|---|---|
| Source control | `<y/n>` | `<...>` | `<...>` |
| Work management | `<y/n>` | `<...>` | `<...>` |
| Build and test | `<y/n>` | `<...>` | `<...>` |
| Documentation | `<y/n>` | `<...>` | `<...>` |
| Security findings | `<y/n>` | `<...>` | `<...>` |
| Observability | `<y/n>` | `<...>` | `<...>` |

**GENERATE** `<app>/.mcp.json`.
**VERIFY** `/mcp`; log one real call per bound server.

---

## 5. Execution environment (primitive 5) → `.claude/settings.json` + the write test

| Field | Value |
|---|---|
| Repository mount / mode | `read-only. <...>` |
| Worktree isolation | `<y/n>` |
| Service identity + scope (non-human) | `<...>` |
| Network egress permitted | `<...>` |
| Permissions narrowed for this app | `<...>` (narrow only, never widen) |
| Untracked build deps → `.worktreeinclude` | `<...>` |

### The write-attempt test — the one row that proves the deliverable
| Field | Value |
|---|---|
| What you attempted | `<e.g. edit src/…>` |
| How it was refused | `<deny rule / hook>` |
| Trace reference + date | `<...>` |
| Verified with Dev Lead | `<date>` |

**GENERATE** `<app>/.claude/settings.json` and `.worktreeinclude`.
**VERIFY** `/status`; run the write attempt; capture the refusal.

---

## 6. Roles, memory, hooks (primitives 8, 6, 7)

| Role | Enabled | Why not, if disabled |
|---|---|---|
| explorer / reviewer | `<y/n>` | |
| verifier | `<y/n>` | needs a usable command contract |
| vuln-analyst | `<y/n>` | needs work-management binding |
| container-assessor | `<y/n>` | |

Memory: app tier location `<...>`; session retention `<per enterprise>`; evidence vault `<...>`.
Hooks: only if the enterprise policy permits pod hooks (enterprise form 0.4). Enabled: `<y/n>`.

**VERIFY** `/agents`; attempt a tool outside a role's scope and confirm refusal.

---

## 7. Capability candidates (primitive 9)

Log as real patterns appear. Nothing is published here — publication is WP2 / D11.

| Candidate | Observed need | Invocation | Owner | Logged |
|---|---|---|---|---|
| `<...>` | `<the repeated situation>` | `<model / user-only>` | `<...>` | `<date>` |

---

## 8. Verification + evidence (primitive 10)

| Field | Value |
|---|---|
| Declared commands runnable by harness | `<y/n>` |
| Receipt sample reference | `<...>` |
| Full trace export reference | `<...>` |
| Cost + latency captured | `<y/n>` |
| D3 KPIs instrumented + verified vs definitions | `<date>` |

**VERIFY** `/usage`, `/insights`; export one full session trace.

---

## 9. Extension register

Every difference from the inherited harness, against the five mechanisms.

| Mechanism | What this app did | Reason | Approved by |
|---|---|---|---|
| Add | `<...>` | `<...>` | FDE |
| Narrow | `<...>` | `<...>` | FDE |
| Bind | `<...>` | `<...>` | FDE |
| Implement (a contract) | `<...>` | `<...>` | FDE |
| Change request (widens/shared) | `<...>` | `<...>` | tech lead |

> Narrow yes, widen no. A local allowlist cannot defeat a managed deny. Anything that would
> widen is a change request, applied to all apps.

---

## 10. D7 enablement environment (primitives 5, 9)

| Field | Value |
|---|---|
| Read-only sandbox prepared | `<ref>` |
| Practitioners from this pod for D7 | `<count>` |
| Lab exercises drafted + verified end to end | `<y/n>` |
| Facilitator (FDE) | `<name>` |

> Labs run against *this* application, not a demo repo.

---

## 11. Close-out

Exit checklist — all must be true:
- [ ] Enterprise plugin installed, version cited
- [ ] Context pack complete and Dev-Lead-corrected
- [ ] `CLAUDE.md` references enterprise, duplicates nothing
- [ ] Servers bound from catalogue, each with a logged call
- [ ] Write-attempt test run, refusal + trace captured
- [ ] Every indexed source has a verification answer
- [ ] D3 KPIs instrumented and verified before first run
- [ ] Extension register complete, change requests approved
- [ ] D7 lab prepared

**FDE** `<name>`  **Tech lead (extensions)** `<name>`  **Dev Lead** `<name>`  **App owner** `<name>`
**Date** `<...>`  **Enterprise version inherited** `<...>`

> This form, completed, is the evidence for this application's **D4 Application Instance
> Record**, and the artefacts it generated are the D4 deliverable for this application.
