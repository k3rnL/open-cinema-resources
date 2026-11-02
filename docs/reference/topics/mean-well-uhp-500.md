---
title: MEAN WELL UHP-500 power supply
summary: Selected low-profile 24 V AC/DC supply; redundancy suffix remains to be confirmed.
status: active
updated: 2026-11-03
tags: [electronics, power-supply, mains, thermal, enclosure]
aliases: [uhp-500, uhp-500r, mean-well-uhp-500]
sources:
  - hardware/electronics/datasheets/mean-well-uhp-500-series-2019.pdf
  - docs/decisions/0002-select-24v-main-supply.md
  - docs/worklog/2026-11-03-rear-panel-and-audio-architecture.md
  - hardware/electronics/notes/rear-input-evidence.md
  - https://www.meanwell.com/Upload/PDF/UHP-500%28R%29/UHP-500-spec.pdf
  - https://www.meanwell.com/Upload/PDF/Enclosed_Type_EN.pdf
---

# MEAN WELL UHP-500 power supply

## Summary

The 24 V MEAN WELL UHP-500 output version is selected as the main low-profile
AC/DC supply because it is compatible with the KAB9 amplifier. The `R` redundancy
suffix has not yet been selected.

## Confirmed facts

- The family accepts 90-264 V AC or 127-370 V DC and includes active PFC.
- The 24 V variant is rated 20.9 A / 501.6 W in the supplied 2019 datasheet, with a
  22.8-25.2 V adjustment range and 94.5% typical efficiency at full load.
- The project owner selected the 24 V output version for compatibility with the
  amplifier rail.
- The enclosure is approximately 232 mm x 81 mm x 31 mm.
- The supply is fanless, but output capability is subject to input-voltage,
  ambient/case-temperature, orientation, and mounting derating.
- The vendor installation drawing specifies mounting the supply to an additional
  aluminum plate or equivalent cabinet surface to meet the published thermal
  curves; its illustrated reference plate is 450 mm x 450 mm x 3 mm.
- The `R` type adds DC-OK and redundant/parallel functionality and is a distinct
  requested configuration.

## Constraints

- The local PDF is dated 2019-12-20. Use the current manufacturer revision for
  procurement, compliance, derating, and terminal details.
- Mains input, protective earth, enclosure bonding, fusing, switchgear, insulation,
  wiring, and touch protection require a competent safety design and applicable
  regulatory review.
- Confirm actual thermal performance in the final enclosure rather than assuming
  the 500 W headline rating applies under every mounting condition.

## Rear-board placement and thermal interpretation

The current online specification reviewed on 2026-11-03 is dated **2025-08-01**;
the local 2019 document remains preserved as the original supplied evidence.
The [rear-panel proposal](rear-panel-interface.md) places a narrow vertical input
PCB above the PSU. That placement has not been approved or physically tested.

- At rated output, using the listed 94.5% typical efficiency gives estimated loss
  `501.6 W x (1 / 0.945 - 1) = 29.2 W`. This is a calculation, not a measurement
  or a prediction of normal programme load; variant, input voltage and loading
  affect efficiency.
- The illustrated thermal reference plate's area, mounting/contact and external
  heat rejection matter as well as its 3 mm thickness. A smaller 3 mm enclosure
  bottom is not automatically thermally equivalent.
- The generic enclosed-type installation manual includes the UHP family, requires
  unobstructed ventilation and specifies **10-15 cm clearance when an adjacent
  device is a heat source**. Resolve how that guidance applies to this compact
  PSU/input-board/amplifier assembly with manufacturer guidance or an appropriate
  design change; an arbitrary smaller PCB gap is not established as equivalent.
- Closed-enclosure temperature and interference testing under representative
  sustained load is still needed. A successful temperature test alone does not
  waive an applicable manufacturer installation requirement.

Sources: [current specification](https://www.meanwell.com/Upload/PDF/UHP-500%28R%29/UHP-500-spec.pdf),
[installation manual](https://www.meanwell.com/Upload/PDF/Enclosed_Type_EN.pdf),
[discussion/evidence register](../../../hardware/electronics/notes/rear-input-evidence.md).

## Evidence

- [Local 2019 datasheet](../../../hardware/electronics/datasheets/mean-well-uhp-500-series-2019.pdf)
- [Current manufacturer datasheet](https://www.meanwell.com/Upload/PDF/UHP-500%28R%29/UHP-500-spec.pdf)
- [Enclosed-type installation manual](https://www.meanwell.com/Upload/PDF/Enclosed_Type_EN.pdf)

## Decisions

- [Select the 24 V main supply](../../decisions/0002-select-24v-main-supply.md)

## Open questions

- Confirm `UHP-500-24` versus `UHP-500R-24`.
- Is the enclosure itself intended to serve as the specified heat-spreading plate?
- What load, headroom, inrush, fuse, wiring, and thermal acceptance criteria apply?
- What protected converter provides the Raspberry Pi 5 V rail?
- How will the rear input PCB preserve ventilation, mains separation and service
  access, and what manufacturer guidance resolves the compact thermal layout?

## Related

- [WONDOM KAB9](wondom-kab9.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [Enclosure and appliance system](enclosure-appliance.md)
- [Auxiliary control electronics](auxiliary-control-electronics.md)
- [Rear-panel interface](rear-panel-interface.md)
