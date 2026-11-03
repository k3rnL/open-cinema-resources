# Open Cinema Resources

Public hardware resources for the Open Cinema project.

This repository holds reference resources, bills of materials, manufacturing
guidance, evidence and the durable project memory. New editable PCB implementation
lives in [open-cinema-hardware](https://github.com/k3rnL/open-cinema-hardware).
Both checkouts live beside each other in `Documents/Open Cinema`; existing
resource artifacts stay here and are linked from hardware.

## Repository map

- `hardware/mechanical/` — CAD sources, drawings, dimensions, and exported models
- `hardware/electronics/` — schematics, PCB sources, wiring, and component notes
- `firmware/` — embedded software and device configuration
- `bom/` — bills of materials and sourcing notes
- `manufacturing/` — fabrication, assembly, and finishing guidance
- `verification/` — test plans, results, photos, and measurements
- `docs/decisions/` — durable architecture and design decision records
- `docs/worklog/` — dated experiment and development logs
- `docs/reference/` — searchable project reference book and topic index
- `docs/inbox/` — temporary triage for material that cannot yet be classified
- `ROADMAP.md` — current priorities, milestones, and open questions

## Working memory

Use the project memory for concise, reviewable reasoning rather than private
chain-of-thought:

1. Record important choices in `docs/decisions/`.
2. Record experiments and sessions in `docs/worklog/`.
3. Update `ROADMAP.md` when priorities or milestone status change.
4. Maintain `docs/reference/INDEX.md` and its topic pages as the current knowledge
   map.
5. Link records to commits, issues, pull requests, CAD files, measurements, and
   photos whenever possible.

Templates are provided in both memory folders.

## Status

Main-component resources, software context, enclosure requirements and decisions
are recorded. A KiCad rear I/O mechanical study and STEP exports are available in
hardware; exact connectors, circuitry and enclosure fit remain open.

## License

No license has been selected yet. Until one is added, copyright remains with the
respective contributors and reuse rights are not granted automatically.

