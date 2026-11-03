---
title: Hardware repository and KiCad mechanical PCB
summary: Separate implementation checkout and the A0 rear connector fit study.
status: active
updated: 2026-11-03
tags: [hardware, repository, kicad, pcb, mechanical]
aliases: [open-cinema-hardware, kikad, connector-board, connection-plate, rear-io, a0]
sources:
  - docs/decisions/0005-use-separate-hardware-repository-and-kicad.md
  - docs/worklog/2026-11-03-kicad-rear-io-mechanical.md
---

# Hardware repository and KiCad mechanical PCB

[open-cinema-hardware](https://github.com/k3rnL/open-cinema-hardware) owns new
editable PCB implementation and mechanical integration exports. Resources keeps
the reference book, research and history. Both checkouts are now beside each
other in `Documents/Open Cinema`. The memory skill stays under this repository's
`.agents/skills/open-cinema-memory/`; hardware guidance links to it.

Source: [decision 0005](../../decisions/0005-use-separate-hardware-repository-and-kicad.md).

## Current study

The owner requested KiCad for board shape and connector placement first. A0 uses
KiCad 10.0.5 with a proposed 228 × 32 mm board, nominal 1.6 thickness, four Ø3.2
mounting holes and ten padless connector envelopes: six speaker pairs, optical
×2, coax and HDMI. Connector parts and electronic design remain deferred. This
is not a fabrication-ready board.

The opening was read from `Rear Panel v4 / Sketch2`: 210 × 25 mm, R5, centred
51.5 mm above its bottom datum. Board dimensions and holes are proposals. Source
screenshots and geometry are archived in hardware. Frame circles currently
measure Ø4.5, conflicting with the fastening baseline's nominal Ø3.8 through
holes. Preserve both pending review.

## Retrieve

- [KiCad sources](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/rear-io)
- [STEP and drawing exports](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/rear-io/exports)
- [Fit assumptions and coordinates](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/rear-io-mechanical.md)
- [Verification scope](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/verification-A0.md)
- [Original evidence](https://github.com/k3rnL/open-cinema-hardware/tree/main/mechanical/reference)
- [Session evidence](../../worklog/2026-11-03-kicad-rear-io-mechanical.md)

Native KiCad and STEP import checks passed. Actual connector fit, enclosure
interference and electrical/thermal behavior remain untested.

Related: [rear panel](rear-panel-interface.md), [digital audio/LVDS](digital-audio-input.md).
