# D4 Enterprise Harness Form

> **What this is.** A fill-in form. You complete the fields, then follow the GENERATE steps
> at the end of each section, and the result is the enterprise Claude Code artefacts for
> D4 — tiers 0 and 1. Completed **once**, by the technical lead. Every application form
> inherits what you set here.
>
> **How to use it.** Replace every `<...>` with a real value. Where a section says
> GENERATE, create the file it describes using the values you just entered. Where it says
> VERIFY, run the command and confirm the output before moving on. Where it says ESCALATE,
> stop until the item is agreed in writing.
>
> **Ground truth.** Claude Code keys and behaviour change between versions. Before relying
> on any generated file, run `claude plugin validate` on the enterprise plugin and `/doctor`
> in a session. A file that loads silently and does nothing is the failure to watch for.

---

## 0. Decisions that gate everything

Answer these before generating anything. Each one changes how later files are written.

| # | Decision | Your answer | Why it gates |
|---|---|---|---|
| 0.1 | Is Claude Code inference routed through a client-controlled LLM gateway? | `<yes / no>` | If yes, admin-console settings are not fetched; policy must ship as the managed file. |
| 0.2 | Is device management (MDM/GPO) reliable across the fleet? | `<yes / no>` | Decides MCP route A vs B in section 2. |
| 0.3 | Transcript retention period agreed with security? | `<N days>` | Sets `cleanupPeriodDays`. Transcripts hold whatever a tool read. |
| 0.4 | May application-authored hooks run, or managed only? | `<managed only / pod allowed>` | Sets `allowManagedHooksOnly` and whether app forms may add hooks. |
| 0.5 | Marketplace sources permitted? | `<list>` | Sets `strictKnownMarketplaces` + `extraKnownMarketplaces`. |
| 0.6 | KPI definitions frozen in D3? | `<yes / no>` | **ESCALATE if no.** Nothing runs until baselines are frozen. |
| 0.7 | Memory tier definitions agreed with RRD? | `<yes / no>` | **ESCALATE if no.** Section 7. |

> **ESCALATE now** on any of 0.6, 0.7, and on 0.1 if unknown. These block the enterprise
> layer and cannot be closed by Accenture alone.

---

## 1. Identity of the enterprise set

| Field | Value |
|---|---|
| Plugin name | `<rrd-harness>` |
| Version | `<0.1.0>` |
| Technical lead (author) | `<name>` `<email>` |
| Internal docs URL | `<url>` |
| Marketplace name | `<YOUR_MARKETPLACE_NAME>` |
| Marketplace URL | `<YOUR_MARKETPLACE_URL>` |

**GENERATE** `enterprise/.claude-plugin/plugin.json` and `marketplace.json` from these.

---

## 2. Tool access policy (primitive 4)

From 0.2, choose the route and complete only that block.

### Route A — exclusive control (device management is reliable)

Deploy `managed-mcp.json` to the OS system path.

| Category | Admitted server URL |
|---|---|
| Source control | `<url>` |
| Work management | `<url>` |
| Build and test | `<url>` |
| Documentation | `<url>` |
| Security findings | `<url>` |
| Observability | `<url>` |

### Route B — enforced catalogue without device management

Merge a `managedMcpServers` block into managed settings. Entries must be `https` remote
servers and may not name a program to run. Set `allowManagedMcpServersOnly: true`.

| Category | Admitted server URL (https only) |
|---|---|
| Source control | `<url>` |
| Work management | `<url>` |
| Build and test | `<url>` |
| Documentation | `<url>` |
| Security findings | `<url>` |
| Observability | `<url>` |

Servers to block everywhere: `<list or none>`

**GENERATE** the matching MCP file (`managed-mcp.json` for A, or the `managedMcpServers`
block for B).
**VERIFY** later with `/mcp`: exactly this catalogue appears, nothing else.

> No built-in registry exists for users to browse, so this catalogue is the whole control.
> A server *name* is a user label, not a security control; matching is by URL or exact
> command.

---

## 3. Execution boundary (primitives 5, 7) — the read-only core

This is what makes D4 read-only. Complete every row.

| Control | Value |
|---|---|
| Build command (allowed) | `Bash(<build>:*)` |
| Test command (allowed) | `Bash(<test>:*)` |
| Lint command (allowed) | `Bash(<lint>:*)` |
| Commands needing approval | `Bash(<cmd>:*)` in `ask` |
| Default permission mode | `<default / plan>` |
| Bypass mode | `disable` |

Write-class tools to deny: `Write`, `Edit`, `NotebookEdit`, `Bash(git commit:*)`,
`Bash(git push:*)`, `Bash(git merge:*)`, `Bash(gh pr create:*)`, `Bash(gh pr merge:*)`,
`Bash(rm:*)` — plus `<any others for this estate>`.

Credential reads to deny: `Read(./.env)`, `Read(./.env.*)`, `Read(**/*secret*)`,
`Read(**/*credential*)`, `Read(**/id_rsa)` — plus `<any others>`.

**GENERATE** the `permissions` block of `enterprise/managed/managed-settings.json`.

> **Enforcement caution.** There are field reports of `Read(...)` deny rules being ignored.
> Do **not** rely on the deny list alone for credential protection. Pair it with the
> PreToolUse hook in section 8, which blocks the call before it executes. Treat the deny
> list as the declaration and the hook as the guard.

**VERIFY** with `/status` (mode and setting source) and by attempting a write, which must be
refused.

---

## 4. Enterprise instructions (primitive 1)

These become `enterprise/CLAUDE.md`. Keep under ~200 lines; longer still loads but adherence
drops. The mandate, verification duty, output contract, security rules and extension rules
are standard — edit the placeholders, do not rewrite the structure.

| Field | Value |
|---|---|
| Engagement name confirmed | `<RRD Autonomous Development>` |
| Advisory output owner | `<who consolidates findings>` |
| Stack standards live in rules? | `<yes — section 5>` |

**GENERATE** `enterprise/CLAUDE.md` (start from the version in the artefact tree; adjust the
mandate and output-contract lines only).

---

## 5. Rules library (primitives 1, 3) — **stack-dependent**

One file per topic under `enterprise/rules/`. Fill the globs and stack specifics.

| Rule file | Path glob(s) | Stack specifics to fill |
|---|---|---|
| `00-advisory-format.md` | none (always) | — |
| `10-secure-coding.md` | `<source globs>` | injection classes for `<stack>` |
| `20-testing.md` | `<test globs>` | mocking policy: `<...>` |
| `30-interfaces.md` | `<interface globs>` | contract style: `<...>` |
| `40-containers.md` | manifest globs | base image policy: `<...>` |

**GENERATE** each rule file with its `paths:` frontmatter set.
**VERIFY** with `/context`: a rule appears with a matching file open, absent without.

---

## 6. Agent roles (primitive 8)

Five roles ship as-is; you only confirm enablement and isolation.

| Role | Tools | `isolation: worktree`? |
|---|---|---|
| explorer | Read, Grep, Glob | n/a |
| reviewer | Read, Grep, Glob | n/a |
| verifier | Read, Grep, Glob, Bash | `<yes / no>` |
| vuln-analyst | Read, Grep, Glob | n/a |
| container-assessor | Read, Grep, Glob | n/a |

**GENERATE** `enterprise/agents/*.md` (bodies are system prompts — use as provided).
**VERIFY** with `/agents`.

> Use these names unchanged in every application; renaming breaks reuse and the D11 harvest.
> `tools` is enforced; an instruction telling a role not to use a tool is not.

---

## 7. Memory tiers (primitive 6)

**Do not complete until 0.7 is agreed in writing.**

| Tier | What it holds | Where |
|---|---|---|
| Enterprise | standards, cross-app patterns | committed files + knowledge server |
| Application | repo knowledge, corrections | committed files (see app form) |
| Session | plans, checkpoints, transcripts | per run, retention = 0.3 |

> Auto memory is per-user and uncommitted, so it is **not** a shared application tier. Where
> a shared tier is expected, realise it through committed files, not auto memory.

**GENERATE** the memory layout note in `enterprise/CLAUDE.md` and set `cleanupPeriodDays`.

---

## 8. Hooks (primitive 7)

| Hook | Purpose | Included |
|---|---|---|
| SessionStart | stamp app + version into the trace | yes |
| PreToolUse | log calls; **block credential reads and write-class calls** | yes |

**GENERATE** `enterprise/hooks/*.sh` and the `hooks` block in managed settings. `chmod +x`.
**VERIFY** with `/hooks`.

> The PreToolUse hook is not just audit — given the deny-rule caution in section 3, it is
> the reliable guard on sensitive reads. If 0.4 is "managed only", confirm these enterprise
> hooks are registered at the managed tier so they actually run.

---

## 9. Skills + eval gate (primitives 9, 10)

Five seed skills ship as folders with `SKILL.md`. Nothing is published at P1 without an eval
suite showing a positive delta against a no-plugin baseline. Evals are **publication gates**:
they validate skill contribution before release. Applications do not run evals in D4 (skills
are not published until WP2/D11); see `application-template/evals/README.md`.

| Skill | Invocation | Ship at P1 |
|---|---|---|
| repo-onboarding-brief | model / slash | yes |
| vuln-patch-triage | model / slash | yes |
| containerization-assessment | model / slash | yes |
| receipt-check | user-only | yes |
| advisory-writeup | model / slash | yes |

| Eval setting | Value |
|---|---|
| Threshold | `<0.8>` |
| Judge model | `<small model>` |
| Cost cap (USD) | `<cap>` |
| Gated in CI on | `<release branch>` |

**GENERATE** `enterprise/skills/*/SKILL.md` and `enterprise/evals/` templates.
**VERIFY** `/skills`, then `claude plugin eval` on one skill before publishing anything.

---

## 10. Observability (primitive 10)

| Field | Value |
|---|---|
| OTLP endpoint | `<url>` |
| Telemetry enabled | `CLAUDE_CODE_ENABLE_TELEMETRY=1` |
| Analytics dashboard | `<url>` |
| KPI schema aligned to D3 | `<yes — reference>` |

**GENERATE** the `env` block in managed settings.
**VERIFY** `/usage` and `/insights` report data; confirm a trace reaches the endpoint.

---

## 11. Publish and hand off

1. `claude plugin validate .` on `enterprise/` — must pass.
2. Deploy `enterprise/managed/` to one machine; `/status` shows the enterprise source.
3. Publish the plugin to your marketplace; pin sources with `strictKnownMarketplaces`.
4. Record the published **version** — every application form cites it.
5. Run the full `VERIFY.md` routine once end to end.

**Completed by** `<technical lead>`  **date** `<...>`
**Plugin version published** `<...>`
**Open items still outstanding** `<list, or none>`

> This form, completed, is the evidence for the **D4 Enterprise Layer Record**. Attach it,
> or transcribe the values into that record.
