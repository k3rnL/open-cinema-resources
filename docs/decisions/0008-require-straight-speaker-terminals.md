# 0008: Avoid downward speaker terminals; use the 220 mm opening

- Date: 2026-11-03
- Status: Accepted owner geometry/terminal-direction constraint; PT-603B is an unqualified mechanical candidate
- Owner: @k3rnL
- Implementation update: [A4](../worklog/2026-11-03-restore-alignment-holes.md) restores actual alignment holes at the owner's request; earlier graphics-only treatment below is superseded.
- Supersedes: A2 downward-tail packaging and upward-opening assumption associated with [0007](0007-use-conventional-speaker-clips.md); preserves conventional red/black clips and six pairs

The owner rejected A2's speaker blocks because their pins descend toward the PSU. The owner suggested surface-mounted parts and supplied a new **220 × 35 mm R5** opening. Read-only Fusion Sketch3 measurement confirms x−110…110,z34…69, with Ø3 reference fixing points at x−115,z44/59. The assistant did not edit the frame.

The functional constraint is **no downward speaker pins near the PSU**. Surface-mount technology is not itself a finalized owner requirement: straight through-hole pins can run behind the vertical PCB. The main PCB remains vertical, with separate small horizontal optical boards.

A3 evaluates **two Dragon City PT-603B six-contact blocks**, with straight rear-facing pins and twelve independent contacts, on a restored 228 × 32 × 1.6 mm main PCB. This is the assistant's drawing-backed mechanical proposal, not owner approval of an order-ready part. Manufacturer current rating, supply, sample geometry, final drills and support remain unqualified. No speaker-current routing or harness is designed.

The measured opening top69 clears the original upper Ø4.5 holes at z75; A2's top-hole conflict was a consequence of its superseded z74 assumption. Actual enclosure depth, solder/PSU clearance and thermal behavior still need verification. Reference frame fixing points remain graphics only; the new component-fixing holes belong to the speaker footprints.

Evidence: [A3 session and source links](../worklog/2026-11-03-straight-speaker-terminals.md), [manufacturer catalogue](https://www.dragoncity.com.hk/st6p.html), [PT-603B drawing](https://www.dragoncity.com.hk/dwpt603b.pdf). Do not substitute similar-looking downward-tail variants.
