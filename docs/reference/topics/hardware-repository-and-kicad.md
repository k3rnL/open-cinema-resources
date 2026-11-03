---
title: Hardware repository and KiCad connector assembly
summary: A10 adds an unrouted optical/coax, selection and LVDS draft with a rigid model; eARC remains incomplete. A9 is the mechanical baseline.
status: active
updated: 2026-11-03
tags: [hardware, repository, kicad, pcb, connectors, mechanical]
aliases: [open-cinema-hardware, kikad, connector-board, connection-plate, rear-io, a0, a1, a2, a3, a7, a8, a9, a10, cs8416, horizontal, inverted, kls, fe6930, spare-pairs, daughterboard, pt-603b, straight-pins, surface-mount, fcr684205r, rcj-021, 10078837-001lf]
sources:
  - docs/worklog/2026-11-03-a10-electrical-draft.md
  - docs/worklog/2026-11-03-remove-plate-and-brackets-A9.md
  - docs/decisions/0011-horizontal-pcb-with-all-connectors.md
  - docs/worklog/2026-11-03-horizontal-rear-io-A8.md
  - docs/decisions/0010-select-cliff-fe6930-and-two-spare-pairs.md
  - docs/worklog/2026-11-03-fe6930-speaker-connectors.md
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

[open-cinema-hardware](https://github.com/k3rnL/open-cinema-hardware) owns editable PCB sources; resources owns memory. Both repositories live in `Documents/Open Cinema`.

## A9 mechanical baseline / A8 PCB layout

The owner requested a **horizontal PCB with all connectors soldered directly to it**, including conventional speaker clips. This supersedes the vertical carrier and optical daughterboards. Six working pairs remain required; two spares are allowed but are not required. [Decision 0011](../../decisions/0011-horizontal-pcb-with-all-connectors.md).

The A8 fit experiment places the component side downward at z67 mm, with solder tails upward. A nominal 228 ×39.8 ×1.6 mm PCB holds two three-pair KLS blocks, both Cliff FCR684205R optical receivers, Same Sky RCJ-011 coaxial RCA and Amphenol10029449-001RLF HDMI. There are no optical daughterboards or cradle in the current assembly.

**The KLS L-KLS1-WP-6P-03B-B/R blocks are mechanical candidates only.** Operating-current rating and exact retail supply remain unverified. They must not inherit the FE6930's 7 A rating; the prior 3 A alternative remains rejected for 4 ohm/mixed loads. This is not an order-ready BOM. [Sourcing](component-sourcing.md).

The owner designs the backplate and L brackets. A9 removes those three solids and retains all four horizontal Ø3 PCB holes at x±110 mm, inward depths 12/30 mm. Previous vertical plate holes remain owner-side mechanical references; the PCB model does not contain them. The opening remains 220 × 35 R5. [Owner request and A9 evidence](../../worklog/2026-11-03-remove-plate-and-brackets-A9.md).

## Integration and evidence

The A9 rigid STEP/F3D contains one component with 67 solids: PCB and connectors only. Both formats reimported with unchanged geometry and no child occurrences. The native PCB layout is unchanged. The open linked Fusion source has been updated, but its cloud save remains unresolved at v2. [A9 record](../../worklog/2026-11-03-remove-plate-and-brackets-A9.md).

KiCad10.0.5 DRC reports zero violations;45 electrical pads and10 NPTH holes are present, all pad centers lie on the board and model paths resolve. There are no nets, tracks, schematic, decoding or LVDS circuitry. Zero unconnected items does not establish electrical completeness.

Historical A8 verification: read-only copies of the current frame and PSU in Home Cinema v7 show no modeled collision with the new assembly/supports. PSU top is z35 mm; minimum assembly/PSU distance is2 mm; maximum assembly height72.5 mm. Thermal behavior, airflow, EMI, mains separation, tolerances, cable bodies and support loads remain unqualified.

Sources: [A8 session with exact implementation revision](../../worklog/2026-11-03-horizontal-rear-io-A8.md), [current hardware record](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/horizontal-assembly-A8.md), [editable project and exports](https://github.com/k3rnL/open-cinema-hardware/tree/main/boards/rear-io).

## History

A7 used two7 A FE6930 blocks on a vertical board with supported optical daughterboards. Its exact source revision and verification remain in the [A7 log](../../worklog/2026-11-03-fe6930-speaker-connectors.md). The [A6 cradle](../../worklog/2026-11-03-rigid-fusion-and-optical-support.md), [A3 straight-pin correction](../../worklog/2026-11-03-straight-speaker-terminals.md), [A2 clip experiment](../../worklog/2026-11-03-speaker-clip-correction.md) and [A1 selection](../../worklog/2026-11-03-rear-connector-selection.md) remain historical evidence. Current orientation is governed by0011.

Related: [rear panel](rear-panel-interface.md), [digital audio/LVDS](digital-audio-input.md).

## A10 electrical draft update

See the [A10 work log](../../worklog/2026-11-03-a10-electrical-draft.md). A separate KiCad schematic and rigid integration model now exist. CS8416K is the draft optical/coax choice, with documented source selection and LVDS circuitry. eARC remains unresolved; no order-ready BOM or manufacturing release exists. Prior WM8804 and connector records remain historical evidence.
