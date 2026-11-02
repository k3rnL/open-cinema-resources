---
name: open-cinema-memory
description: Organize incoming Open Cinema files, notes, decisions, and evidence into the repository knowledge system, or retrieve project context from it. Use for project librarianship and memory, not implementation planning.
---

# Open Cinema Memory

Maintain a trustworthy, searchable project memory for both humans and agents.
Preserve source evidence, keep one canonical home for each fact, and make derived
knowledge easy to trace back to its origin.

This is an information-management workflow. Do not start implementation, turn
ideas into specifications, or invoke OpenSpec unless the user separately asks for
that work.

## Choose the mode

- **Ingest** when the user supplies files, thoughts, observations, decisions,
  links, or corrections and asks to retain or organize them.
- **Retrieve** when the user asks what the project knows, why a choice was made,
  where a resource lives, or what remains uncertain.
- Use both when new material must be organized before answering a question.

## Start with the map

Work from the repository root. Read `AGENTS.md` and
`docs/reference/INDEX.md` first. Then load only the topic pages, decisions, work
logs, and source artifacts relevant to the request.

For classification and placement rules, read
[references/organization.md](references/organization.md). For reference-page and
index formats, read [references/reference-book.md](references/reference-book.md).

## Ingest

1. Inspect the supplied material and identify its provenance. Treat claims as
   unverified unless the material or existing project evidence supports them.
2. Separate source artifacts, durable facts, constraints, decisions, experiments,
   interpretations, open questions, and future work. One input may update several
   records, but keep one canonical copy of the original artifact.
3. Check that the material is appropriate for a public repository. Do not commit
   credentials, private contact details, personal addresses, confidential quotes,
   or other sensitive information. Stop and ask before publishing uncertain
   material.
4. Place source files in the domain folder defined by the organization guide.
   Never overwrite a different file silently; preserve the original name when it
   is meaningful and use a clear revision or date suffix for collisions.
5. Update or create the smallest useful reference topic page. Cite repository
   paths under `Sources` for every synthesized group of claims. Record uncertainty
   and contradictions explicitly instead of resolving them by guesswork.
6. Create or update a decision record only for an actual choice and its stated
   rationale. Use a work log for experiments, sessions, and observations. Update
   `ROADMAP.md` only when priorities, milestones, or open questions truly change.
7. Update `docs/reference/INDEX.md` whenever a topic is added, renamed,
   superseded, or materially reframed. Keep summaries compact enough to scan.
8. Report what was filed, what knowledge records changed, the provenance kept,
   and any unresolved classification or factual conflict.

Do not store private model chain-of-thought. Preserve useful project reasoning as
concise rationale, alternatives, evidence, assumptions, and consequences.

## Retrieve

1. Read `docs/reference/INDEX.md` to identify likely topics and terminology.
2. Search before opening broad folders. Run:

   `python3 .agents/skills/open-cinema-memory/scripts/search_reference.py "<query>" --root .`

   Use `--json` when structured results help. Search again with aliases or a
   narrower term only when the first pass does not resolve the question.
3. Open the highest-ranked topic pages, then follow their links to decisions,
   work logs, and original artifacts as needed. Do not load the entire memory by
   default.
4. Answer with repository links and distinguish:
   - confirmed project facts;
   - accepted decisions and their rationale;
   - observations or interpretations;
   - superseded information;
   - unresolved questions or missing evidence.
5. If the reference book is incomplete or inconsistent, say so and propose the
   smallest maintenance update. Do not invent context to fill a gap.

## Invariants

- Original evidence remains traceable and historical decisions remain visible.
- Topic pages summarize; they do not duplicate whole source documents.
- A new decision supersedes an old one rather than rewriting history.
- Links are repository-relative and useful in GitHub and a local checkout.
- Retrieval is read-only unless the user also asks to capture or correct memory.
- External publication, commits, and pushes remain separately authorized actions.

