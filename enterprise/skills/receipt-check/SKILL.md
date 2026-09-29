---
name: receipt-check
description: Verify that a claimed receipt is genuine. Check the evidence against the command contract.
argument-hint: "[receipt text]"
disable-model-invocation: true
---

# Receipt check

Verify that $ARGUMENTS is a genuine receipt.

## Steps

1. Read the claimed receipt. Identify the command claimed to have been run.
2. Check the command contract in `.claude/context/commands.md`.
3. Confirm the command declared in the contract is what appears in the receipt.
4. Confirm the exit status and output match the command's expected behavior.
5. If the baseline records pre-existing failures, ensure this receipt does not introduce new ones.

## Output

- **Valid**: the receipt is genuine. The command ran, the result is real.
- **Invalid**: the command does not appear in the contract, or the output is inconsistent.
- **Inconclusive**: the receipt is incomplete or the contract is ambiguous.

This is a user-only skill. Invoke it manually when verifying the verifier's work.
