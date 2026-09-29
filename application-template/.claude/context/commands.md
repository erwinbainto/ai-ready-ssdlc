# Command contract — <APPLICATION_NAME>

The declared commands. The `verifier` role uses these and nothing else. An agent that
improvises a command is producing an unreliable receipt.

| Purpose | Command | Expected | Typical duration | Passes today? |
|---|---|---|---|---|
| Build | `<command>` | exit 0 | <time> | <yes / no> |
| Test | `<command>` | exit 0 | <time> | <yes / no> |
| Lint | `<command>` | exit 0 | <time> | <yes / no> |
| Type check | `<command>` | exit 0 | <time> | <yes / no> |

## Baseline

**Currently failing:** <list, or "none">

Record this honestly. A suite with pre-existing failures is common and fine, but if the
baseline is not stated, the first agent-assisted change appears to have broken something it
did not, and comparisons are contaminated.

## Reduced receipt set

Where a command is unavailable, state the reduced set here and who performs the manual
verification instead.
