# Enterprise harness set

Tier 0 and tier 1. Authored once, distributed as a plugin, inherited by every application.

```
enterprise/
├── .claude-plugin/        plugin manifest and marketplace catalogue
├── managed/               tier 0 policy, deployed to the machine, not the repo
├── CLAUDE.md              enterprise instruction set
├── rules/                 topic guidance, path-scoped where not universal
├── agents/                the five agent roles, tool-scoped
├── skills/                seed skills, each a folder with SKILL.md
├── hooks/                 lifecycle scripts referenced by settings
└── evals/                 eval case templates, the gate before publication
```

## What lives where, and why

`managed/` is **not** part of the plugin. Policy has to reach the machine through a
privileged path or the admin console; a plugin cannot enforce itself. Everything else
ships in the plugin.

## Publishing

```
claude plugin validate .
/plugin marketplace add <YOUR_MARKETPLACE_URL>
/plugin install ai-ready-ssdlc-harness@<YOUR_MARKETPLACE_NAME>
```

Pin the marketplace and restrict sources with `strictKnownMarketplaces` in managed settings,
or any pod can install from anywhere.

## Versioning

Bump `version` in `.claude-plugin/plugin.json` on every change. Application records cite
that version. An application citing a version that no longer exists is a finding.
