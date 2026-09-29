# Evals

Test case templates for pre-publication gates. Before shipping a skill or agent instruction, 
measure its contribution with an eval suite.

Each subdirectory represents one eval case or suite:

| Case | Purpose | Inputs | Expected output |
|---|---|---|---|
| `vuln-patch-triage` | Patch advisory accuracy | vulnerability ticket | reachability determination |

## Running evals

```bash
claude eval run ./evals/<case>/
```

Document results before and after any change to the skill or agent. A skill without
measured contribution is not published.

## Authoring new evals

1. Create a subdirectory: `evals/<case>/`
2. Write `prompt.md` with the test input (the user prompt)
3. Write `graders.md` with the evaluation criteria
4. Optional: add example files to `cases/` if the prompt references them

See individual case READMEs for specifics.
