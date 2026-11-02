# Contributing

Contributions should be small enough to review and should preserve the connection
between a design, why it changed, and how it was verified.

## Suggested flow

1. Open an issue or describe the intended outcome.
2. Create or update a decision record when the change involves a meaningful
   trade-off.
3. Make the design change in editable source files.
4. Add or update verification evidence.
5. Add a concise work-log entry for experiments or discoveries worth retaining.
6. Submit a pull request that links the relevant records and evidence.

## File hygiene

- Use descriptive, stable filenames.
- Avoid spaces when a toolchain handles them poorly.
- Keep machine-generated caches and backups out of Git.
- Do not commit secrets or personal information to this public repository.

## Commit messages

Use an imperative summary, for example: `Document enclosure ventilation test`.
Explain the reason and evidence in the commit body when the change is not obvious.

