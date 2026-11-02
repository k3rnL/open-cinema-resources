# Repository guidance

## Purpose

Maintain the public hardware resources and durable project memory for Open Cinema.

## Working agreements

- Prefer editable source files over exports. Keep exports alongside their sources
  only when they are useful for review or fabrication.
- Do not commit credentials, private contact details, personal addresses, vendor
  account data, or confidential quotations.
- Keep generated binaries and large transient files out of Git unless they are a
  deliberate release artifact.
- For material design choices, add or update a decision record in
  `docs/decisions/`.
- For experiments and build sessions, add a dated entry in `docs/worklog/` with
  observations and evidence.
- Update `ROADMAP.md` when milestone state, priorities, or major unknowns change.
- Use the `open-cinema-memory` repository skill to organize incoming project
  information and maintain `docs/reference/INDEX.md` plus its topic pages.
- Never rewrite historical records to hide a change of direction. Supersede them
  with a new record and link both directions.

## Context retrieval

- Start with `docs/reference/INDEX.md` instead of scanning the whole repository.
- Search the reference book, decisions, work logs, and roadmap before assuming
  project context is missing.
- Follow topic-page links to original evidence when accuracy matters.
- Distinguish confirmed facts, decisions, observations, interpretations, and open
  questions in summaries.

## Hardware documentation

- State units and tolerances explicitly.
- Record tool and software versions when they affect reproducibility.
- Include part numbers and supplier-independent specifications where possible.
- Connect verification results to the exact design revision tested.

## Completion check

Before calling a change complete, verify that source files open, exports match the
source revision, relevant memory records are current, and no sensitive information
is included.

