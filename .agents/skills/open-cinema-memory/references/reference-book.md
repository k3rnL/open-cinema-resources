# Reference book format

Use this guide when creating or maintaining `docs/reference/`.

## Structure

```text
docs/reference/
├── INDEX.md
├── 0000-template.md
└── topics/
    └── descriptive-topic-name.md
```

`INDEX.md` is the fast orientation layer. Topic pages are the durable knowledge
layer. Decisions, work logs, and source artifacts remain authoritative for their
own evidence and history.

## Topic metadata

Start each topic page with YAML frontmatter:

```yaml
---
title: Human-readable title
summary: One-sentence description of the topic
status: active
updated: YYYY-MM-DD
tags: [domain, subsystem]
aliases: [alternate term]
sources:
  - path/to/source
---
```

Allowed status values are `draft`, `active`, and `superseded`. Keep tags short and
stable. Include search terms and previous names in `aliases`. Repository paths in
`sources` are provenance, not proof that every statement in the page is current.

## Topic body

Use only sections that add value:

- `Summary` — compact orientation.
- `Confirmed facts` — supported statements with inline repository links.
- `Constraints` — boundaries, tolerances, requirements, and assumptions.
- `Decisions` — links to decision records, including superseded choices.
- `Evidence` — tests, measurements, drawings, photos, and source artifacts.
- `Open questions` — unknowns, contradictions, owners, and next evidence needed.
- `Related` — links to adjacent topic pages.

Do not paste entire source documents into a topic page. Summarize and link.

## Index maintenance

Keep the index concise and navigational:

- Add each active topic once under its primary domain.
- Use a one-sentence description that helps a human choose what to open.
- List aliases only when they materially improve discovery.
- Keep a visible Triage section for unclassified material and a visible Known
  gaps section for missing or contradictory information.
- Remove stale index text when updating it, but preserve historical facts in the
  topic, decision, or work-log record where they belong.

## Retrieval quality

Good answers cite the topic page and, when the conclusion matters, the underlying
decision or evidence. State whether an answer is confirmed, decided, observed,
interpreted, superseded, or unresolved.

