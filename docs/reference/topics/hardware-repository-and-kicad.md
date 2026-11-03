---
title: Hardware repository and KiCad connector assembly
summary: A6 adds a bolted optical cradle prototype and rigid Fusion files; all four alignment holes retained, speaker sourcing/qualification open.
status: active
updated: 2026-11-03
tags: [hardware, repository, kicad, pcb, connectors, mechanical]
aliases: [open-cinema-hardware, kikad, connector-board, connection-plate, rear-io, a0, a1, a2, a3, daughterboard, pt-603b, straight-pins, surface-mount, fcr684205r, rcj-021, 10078837-001lf]
sources:
  - docs/worklog/2026-11-03-rigid-fusion-and-optical-support.md
  - docs/worklog/2026-11-03-restore-alignment-holes.md
  - docs/decisions/0008-require-straight-speaker-terminals.md
  - docs/worklog/2026-11-03-straight-speaker-terminals.md
  - docs/decisions/0007-use-conventional-speaker-clips.md
  - docs/decisions/0005-use-separate-hardware-repository-and-kicad.md
  - docs/decisions/0006-vertical-carrier-and-optical-daughterboards.md
  - docs/worklog/2026-11-03-rear-connector-selection.md
---

# Hardware repository and KiCad connector assembly

[open-cinema-hardware](https://github.com/k3rnL/open-cinema-hardware) owns editable PCB sources and integration exports. Resources owns research, reference book and history. Both checkouts live in `Documents/Open Cinema`; the memory skill remains here. [Decision 0005](../../decisions/0005-use-separate-hardware-repository-and-kicad.md).

## Current A6 fit study

The owner requires conventional red/black finger-operated clips and rejects downward speaker pins near the PSU. A3 evaluates **two Dragon City PT-603B six-contact blocks**, with straight pins extending behind the **228 × 32 × 1.6 mm vertical PCB**. Surface-mount construction is not necessary for that direction. This is an unqualified mechanical candidate: current rating, small-quantity supply, sample dimensions and final drills remain open.

The updated owner opening is **220 × 35 R5, z34…69**, measured read-only from Fusion. The owner requested real holes for model alignment: **HREF1–HREF4 are Ø3 NPTH at x±115,z44/59**, two per side in small R4 tabs (overall PCB width238). They remain provisional mounting geometry. [A4/A5 correction](../../worklog/2026-11-03-restore-alignment-holes.md). A3 includes four provisional component-fixing NPTH holes for the speaker blocks; these do not define frame mounting. A2's upper-frame-hole collision no longer applies to the actual opening. Full enclosure clearance and mounting remain unverified.

Sources: [decision 0008](../../decisions/0008-require-straight-speaker-terminals.md), [A3 session with exact revision/evidence](../../worklog/2026-11-03-straight-speaker-terminals.md).

| Qty | Interface | Reference / state |
| --- | --- | --- |
| 2 | Six-contact red/black speaker block | Dragon City **PT-603B**, mechanical candidate |
| 2 | Optical receiver, one per horizontal daughterboard | Cliff **FCR684205R / ORJ5**, retained from A1 |
| 1 | Vertical RCA for coaxial S/PDIF | Same Sky **RCJ-021**, retained |
| 1 | Vertical HDMI Type A | Amphenol FCI **10078837-001LF**, retained |

Main J7/J8 are assembly instances; optical receiver pads are on separate 16 × 24 × 1.6 mm boards. A6 adds a shared bolted cradle prototype, two mounting holes per daughterboard and bolts through the receiver lugs. Electrical interconnects remain unselected; physical fit, temperature and load qualification are open. [A6 session](../../worklog/2026-11-03-rigid-fusion-and-optical-support.md). The optical part's 16 Mbit/s limit does not support 192 kHz stereo PCM; the HDMI socket alone does not establish eARC compatibility. No nets, schematic, tracks, decoding, LVDS or speaker-current distribution exist.

Sources: [A1 audio-input evidence](../../worklog/2026-11-03-rear-connector-selection.md), [A3 model assumptions](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/connector-selection-A3.md).

## Fusion integration and sourcing

Use the A6 **rigid STEP/F3D**: one component with123 solid bodies. The raw KiCad assembly contains separate components. Disable Ground to Parent on the inserted unit before making a rigid joint. A temporary joint from one alignment hole moved all123 solids together. Owner CAD was not modified.

JLCPCB is preferred, with Global Sourcing/pre-order and outside suppliers allowed. HDMI stock was verified at JLC; optical/RCA distributor stock was found; exact speaker supply/current capability remains unresolved. [Sourcing topic](component-sourcing.md).

## Retrieve and verify

- [Main KiCad project](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/rear-io)
- [Optical daughterboard](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/optical-input)
- [A6 exports](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/rear-io/exports)
- [Mechanical coordinates](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/rear-io-mechanical.md)
- [A6 verification and exact source hashes](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/verification-A6.md)
- [Original evidence](https://github.com/k3rnL/open-cinema-hardware/tree/main/mechanical/reference)

Native KiCad10.0.5 main/child DRC returns zero violations under recorded settings. A6 has41 electrical pads and12 main-board NPTH holes, including four unchanged alignment holes and four new cradle holes. Fusion found no positive-volume cradle/connector collision, measured all four alignment holes and verified rigid movement. No full enclosure, load, thermal or electrical test is claimed. With no nets, zero unconnected items is not functional completeness. [A6 exact evidence](../../worklog/2026-11-03-rigid-fusion-and-optical-support.md).

## History

[A0](../../worklog/2026-11-03-kicad-rear-io-mechanical.md) used generic envelopes. [A1](../../worklog/2026-11-03-rear-connector-selection.md) introduced real input parts and rejected industrial speaker terminals. [A2](../../worklog/2026-11-03-speaker-clip-correction.md) tried KLS downward-tail clips with a shortened input PCB and assumed upward opening growth; both packaging assumptions are superseded by A3. Historical exports and decisions remain available.

Related: [rear panel](rear-panel-interface.md), [digital audio/LVDS](digital-audio-input.md).
