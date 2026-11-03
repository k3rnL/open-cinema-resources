# 0011 — Use a horizontal PCB with every connector soldered to it

- Date: 2026-11-03
- Status: Owner-accepted orientation and mounting requirement; A8 implementation is an unqualified fit study
- Source: owner requested “Let's try horizontal”, then answered “I want the speaker clips soldered to the horizontal PCB too”
- Supersedes: vertical carrier and optical daughterboards in [0006](0006-vertical-carrier-and-optical-daughterboards.md); the straight-rear-pin implementation in [0008](0008-require-straight-speaker-terminals.md); FE6930 as the current fit-model part in [0010](0010-select-cliff-fe6930-and-two-spare-pairs.md)

## Choice

Use one horizontal rear-I/O PCB carrying six speaker pairs, two optical receivers, coaxial RCA and HDMI. All connectors, including the conventional red/black speaker clips, must solder directly to that PCB. A proposed wired, panel-only speaker arrangement was explicitly declined. Keep mains separate and retain real alignment holes on both sides.

The motivation is the unequal connector projections and mechanical burden of the vertical arrangement. The requirement to avoid speaker pins descending toward the PSU remains relevant. Two spare pairs are allowed, not mandatory; the A8 candidate returns to exactly six pairs.

## Working implementation, not an additional owner decision

A8 places the component side downward at z 67 mm so solder tails point upward. It replaces the vertical speaker/RCA/HDMI parts with horizontal candidates and puts the optical receivers directly on the main PCB. Two provisional support brackets preserve vertical Ø3 reference holes at x±115,z 44/59, while separate horizontal holes support the board.

The compact KLS L-KLS1-WP-6P-03B-B/R speaker block is only a mechanical candidate: its operating-current rating and exact small-quantity purchase route remain unverified. This is not acceptance of a lower current rating. The prior 3 A part remains rejected for 4 Ω/mixed loads, and FE6930's 7 A rating must not be attributed to KLS.

Nominal geometry, rigid Fusion movement and KiCad checks pass in the scope recorded in the [A8 work log](../worklog/2026-11-03-horizontal-rear-io-A8.md). Electrical qualification, tolerances, bracket hardware, cable insertion, tight plate clearance and above-PSU thermal behavior remain open. No manufacturing or purchase release exists.
