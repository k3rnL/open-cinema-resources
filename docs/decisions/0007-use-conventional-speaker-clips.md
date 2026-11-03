# 0007: Require conventional red/black speaker clips

- Date: 2026-11-03
- Status: Accepted style correction and taller-opening allowance; replacement mechanically evaluated, not electrically qualified
- Owner: @k3rnL
- Partially superseded by: [0008](0008-require-straight-speaker-terminals.md), which rejects A2 downward tails and records the actual 220 × 35 opening. The red/black clip style remains accepted.
- Supersedes: speaker-terminal selection only in [0006](0006-vertical-carrier-and-optical-daughterboards.md)

The owner rejected the Phoenix Contact 1732496 terminals chosen for A1 and supplied a [reference photograph](../../hardware/electronics/notes/speaker-clips-owner-reference.png). The required interface is conventional **red/black finger-operated speaker spring clips**, like the panel strips shown. Industrial screwdriver-operated spring terminals do not meet this requirement.

Retain six speaker pairs / twelve independent contacts. The vertical main carrier, small optical daughterboards, separate mains assembly and undecided mounting method remain unchanged. This correction selects the interaction/style, **not an exact manufacturer part**.

The 210 × 25 mm opening constrains conventional clip packaging. A wider single row or a taller double row requires a revised fit study. The owner subsequently answered **"Yes, allow a taller opening"** to the proposed 210 × 35 mm opening grown upward. That dimensional allowance is accepted. A2 evaluates two KLS six-contact blocks with a shortened 99 × 32 mm vertical input PCB beside them. Panel-supported clips with independent amplifier wiring are the proposed implementation, not a qualified attachment/wiring design. Historical A1 speaker choices remain rejected.

See [research and implementation status](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/speaker-clips-correction.md). Candidate KLS L-KLS1-WP-6P-03B-B/R is compact but its operating current rating and termination remain unresolved. The taller opening intersects original top frame fixings; speaker tails extend below the opening. These require mechanical resolution before cutting or ordering. Do not confuse a candidate with a qualified part.

Evidence: owner message and photograph supplied in this session. Original image manufacturer/model is unknown; it establishes requested style only.
