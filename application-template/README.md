# Application template

Copy the contents of this directory into an application repository root and complete it.
One copy per application.

```
<app-repo>/
├── CLAUDE.md                  app instructions; references the enterprise set
├── .mcp.json                  bindings selected from the admitted catalogue
├── .worktreeinclude           untracked files the build actually needs
└── .claude/
    ├── settings.json          permissions narrowed, hooks wired
    ├── rules/                 app-specific, path-scoped
    ├── context/               the knowledge connection
    ├── agents/                roles enabled for this app
    └── skills/                app capability candidates
```

## Order

1. Install the enterprise plugin. Do not copy its contents here.
2. Complete `.claude/context/` with the team that owns the application. This is the part
   that cannot be templated.
3. Complete `CLAUDE.md`, keeping it short.
4. Bind servers in `.mcp.json`, from the admitted catalogue only.
5. Narrow `settings.json` where this application needs it stricter. Never looser.
6. Run the verification routine in `../VERIFY.md`.
7. Run a write attempt and capture the refusal. That is the deliverable evidence.

## The rule that matters

Reference the enterprise set. Never copy from it. A duplicated instruction drifts within
weeks and an upstream correction reaches nobody.
