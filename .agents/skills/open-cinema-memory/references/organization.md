# Organization rules

Use this guide when ingesting or relocating project information.

## Classification map

| Material | Canonical location | Memory action |
| --- | --- | --- |
| CAD sources, drawings, dimensions, exports | `hardware/mechanical/` | Update the relevant reference topic and link the exact revision |
| Schematics, PCB sources, wiring, datasheets | `hardware/electronics/` | Update the relevant component, interface, or subsystem topic |
| Embedded code and device configuration | `firmware/` | Update the relevant subsystem or interface topic |
| Parts lists and sourcing information | `bom/` | Link the supported design revision and component topics |
| Fabrication and assembly guidance | `manufacturing/` | Update process, material, or assembly topics |
| Test procedures, measurements, photos, results | `verification/` | Link the tested revision, setup, and related decision |
| Stable project knowledge or terminology | `docs/reference/topics/` | Create or update one canonical topic page |
| An actual choice with rationale and consequences | `docs/decisions/` | Create a numbered decision record and link it from topic pages |
| A dated session, experiment, or observation | `docs/worklog/` | Create a dated log and promote only durable conclusions to topic pages |
| Priorities, milestones, or future work | `ROADMAP.md` | Update only the affected section |
| Material that cannot yet be classified safely | `docs/inbox/` | Preserve it temporarily, mark the owner/question, and list it under Triage in the index |

## Placement principles

- Keep an original artifact in one canonical location. Link to it elsewhere.
- Prefer editable sources. Keep exports when they materially help review,
  interoperability, fabrication, or verification.
- A topic page represents a concept, component, subsystem, interface, process, or
  constraint—not an individual upload.
- Split a topic when it becomes difficult to scan or has clearly independent
  ownership and lifecycle. Merge pages that merely repeat the same facts.
- Use lowercase kebab-case filenames for new Markdown records. Preserve tool-
  required or established source filenames.
- Include dates as `YYYY-MM-DD` and state units explicitly.
- If an input contradicts existing knowledge, retain both claims with their
  provenance and mark the conflict unresolved until evidence or an authorized
  decision resolves it.

## Public-repository check

Before filing material, inspect it for credentials, tokens, private addresses,
personal contact details, unreleased vendor terms, confidential pricing, embedded
document metadata, and accidental backups. Do not assume that a file is safe
because the user supplied it. Ask before publishing when sensitivity is unclear.

## Ingestion outcomes

An ingestion is complete when the original evidence has a stable home, durable
knowledge has been promoted into the reference book, the index points to new or
changed topics, and unresolved questions remain visible.

