# Evals (Future phase)

This directory is reserved for application-specific skill evaluation suites.

**Current phase (D4):** Applications do not publish skills. See `.claude/skills/README.md` and `D4_Application_Harness_Form.md` § 7 ("Capability candidates").

**Future phases (WP2 / D11):** When application-authored skills are ready to publish, follow the enterprise eval pattern:

1. Create a subdirectory: `evals/<skill-name>/`
2. Write `prompt.md` with test inputs
3. Write `graders.md` with evaluation criteria
4. Run: `claude eval run ./evals/<skill-name>/`
5. Verify positive delta against baseline before publishing

See `enterprise/evals/README.md` for the full pattern and example cases.

## Why evals live here (not in `.claude/`)

Evals are **validation artifacts**, not **runtime configuration**. They are:
- Used at publication time, not session load time
- Separate from agents/skills/rules that run in Claude Code
- Tests that prove skill quality before shipping

See the architecture guidance in the root `CLAUDE.md` for the tier separation model.
