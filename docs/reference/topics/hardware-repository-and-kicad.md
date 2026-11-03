---
title: Hardware repository and KiCad connector assembly
summary: A1 vertical rear carrier with selected connectors and two optical daughterboards.
status: active
updated: 2026-11-03
tags: [hardware, repository, kicad, pcb, connectors, mechanical]
aliases: [open-cinema-hardware, kikad, connector-board, connection-plate, rear-io, a0, a1, daughterboard, 1732496, fcr684205r, rcj-021, 10078837-001lf]
sources:
  - docs/decisions/0005-use-separate-hardware-repository-and-kicad.md
  - docs/decisions/0006-vertical-carrier-and-optical-daughterboards.md
  - docs/worklog/2026-11-03-rear-connector-selection.md
  - docs/worklog/2026-11-03-kicad-rear-io-mechanical.md
---

# Hardware repository and KiCad connector assembly

[open-cinema-hardware](https://github.com/k3rnL/open-cinema-hardware) owns editable PCB sources and integration exports. Resources owns research, reference book and history. Both checkouts live in `Documents/Open Cinema`; the memory skill remains here. [Decision 0005](../../decisions/0005-use-separate-hardware-repository-and-kicad.md).

## Current A1 study

The owner chose a **vertical main PCB and small optical daughterboards**. Main PCB is 228 × 32 × 1.6 mm, with two clearance windows; two horizontal optical boards are each 16 × 24 × 1.6. KiCad 10.0.5 sources contain actual connector pads and models but no circuit nets, schematic or tracks. Logic/LVDS remain deferred. This is not fabrication-ready.

| Qty | Interface | Reference |
| --- | --- | --- |
| 6 | Two-pole industrial speaker spring terminal | Phoenix Contact **1732496** |
| 2 | Optical receiver, each on a daughterboard | Cliff **FCR684205R / ORJ5** |
| 1 | Vertical RCA for coax S/PDIF | Same Sky **RCJ-021** |
| 1 | Vertical HDMI Type A | Amphenol FCI **10078837-001LF** |

Sources: [decision 0006](../../decisions/0006-vertical-carrier-and-optical-daughterboards.md), [manufacturer drawings, supplier links and model provenance](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/connector-selection-A1.md).

Phoenix CAD comes from KiCad; other 3D models are drawing-derived project models with cosmetic simplifications. Main J7/J8 are assembly instances, not solder footprints. Actual optical receiver pads are child-board J1. No daughterboard support or interconnect is chosen. Optical part's 16 Mbit/s limit does not support 192 kHz stereo PCM. The HDMI socket does not establish eARC compatibility.

The opening is 210 × 25 R5 at z39…64. Updated Sketch3 adds two Ø3 reference locations at x−110,z44/59, explicitly without a chosen mounting method. They are only graphics in KiCad; A0's four proposed PCB holes are removed. Optical tab-to-opening top margin is only 0.5 mm nominal. Final plate cutouts, setback, retention, sample fit, current/wire access and full enclosure checks remain open. Frame model thickness 2 mm versus 3 mm baseline, and Ø4.5 frame holes versus Ø3.8 baseline, remain unresolved.

Source: [A1 work log](../../worklog/2026-11-03-rear-connector-selection.md).

## Retrieve and verify

- [Main KiCad project](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/rear-io)
- [Optical daughterboard](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/optical-input)
- [A1 STEP and drawing exports](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/rear-io/exports)
- [Mechanical coordinates and integration](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/rear-io-mechanical.md)
- [A1 verification, exact PCB hashes and limits](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/verification-A1.md)
- [Original evidence](https://github.com/k3rnL/open-cinema-hardware/tree/main/mechanical/reference)

Both native boards pass current DRC; the full STEP imports as 88 solid-body instances. No full enclosure interference or electrical/thermal test is claimed. With no circuit nets, zero unconnected items is not proof of functional completeness.

## History

[A0 session](../../worklog/2026-11-03-kicad-rear-io-mechanical.md) introduced padless generic envelopes and four proposed holes. Those assumptions are superseded by A1; old exports remain explicitly marked A0.

Related: [rear panel](rear-panel-interface.md), [digital audio/LVDS](digital-audio-input.md).
