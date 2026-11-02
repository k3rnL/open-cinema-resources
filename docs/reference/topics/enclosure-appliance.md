---
title: Enclosure and appliance system
summary: Current system-level enclosure context, selected major components, and unresolved integration constraints.
status: active
updated: 2026-11-02
tags: [architecture, enclosure, mechanical, electronics, thermal]
aliases: [case, chassis, appliance-enclosure]
sources:
  - docs/decisions/0001-initial-enclosure-components.md
  - docs/decisions/0002-select-24v-main-supply.md
  - docs/worklog/2026-11-02-initial-resource-import.md
  - docs/worklog/2026-11-02-enclosure-requirements-update.md
  - bom/preliminary-components.csv
---

# Enclosure and appliance system

## Summary

The physical enclosure effort has started. The initial major component set is
selected. The front and back panels, auxiliary electronics, detailed mechanical
layout, power distribution, cooling validation, connectors, and safety
implementation remain to be designed.

## Confirmed facts

- The project software is largely implemented and has a functionally accepted
  `v0.3.2` appliance release on a Raspberry Pi 5 8 GB fixture.
- The initial selected component set includes a Raspberry Pi 5, a WM8804 S/PDIF
  transceiver, a WONDOM KAB9 eight-channel amplifier, and a MEAN WELL UHP-500
  power-supply family member.
- The accepted software fixture uses active cooling on the Raspberry Pi 5.
- A basic Raspberry Pi cooling fan has been purchased. Its exact model, mounting,
  and thermal performance have not been recorded.
- KAB9 is a nominal 24 V, eight-channel Class-D amplifier board. Its vendor
  recommends forced air when it is run continuously at higher power.
- The UHP-500 series is a low-profile, fanless AC/DC supply whose permitted load
  depends on input voltage, ambient/case temperature, mounting, and derating.
- The 24 V UHP-500 output version is selected to match the KAB9 amplifier rail;
  the `R`/non-`R` suffix is still open.
- The intended front panel needs a touch screen, an encoder, and a power button.
  The Waveshare 7.9inch DSI LCD is a candidate, not a selected part.
- The back panel still needs to be designed and its components have not been
  selected.
- The appliance needs at least one input front-end board and a power/control board
  for delegated functions. Their components and interfaces are not yet decided.

## Constraints

- Provide isolation and safe mechanical segregation between mains wiring and
  extra-low-voltage electronics. Final mains design requires competent electrical
  and regulatory review.
- Preserve airflow and service access for the Pi 5, KAB9, and power supply.
- Do not treat headline wattage as enclosure thermal design evidence. Validate the
  actual programme load, losses, temperatures, and airflow.
- The Raspberry Pi 5 and candidate display require regulated 5 V power; the
  conversion path from the selected 24 V rail has not yet been recorded.

## Decisions

- [Initial enclosure main components](../../decisions/0001-initial-enclosure-components.md)
- [Select the 24 V main supply](../../decisions/0002-select-24v-main-supply.md)

## Evidence

- [Preliminary component register](../../../bom/preliminary-components.csv)
- [Initial resource import work log](../../worklog/2026-11-02-initial-resource-import.md)
- [Enclosure requirements update](../../worklog/2026-11-02-enclosure-requirements-update.md)
- Component topic pages and linked manufacturer datasheets.

## Open questions

- What are the enclosure's target outside dimensions, orientation, materials,
  acoustic limits, mounting method, and service-clearance requirements?
- Is the non-redundant `UHP-500-24` or the `UHP-500R-24` required?
- What protected DC/DC stage will provide the Raspberry Pi's 5 V rail?
- What are the AC inlet, fuse, switch, protective-earth, creepage/clearance, and
  strain-relief requirements?
- Is the purchased basic Pi fan sufficient, and what heatsink, vents, filters,
  temperature sensors, and control policy are required?
- What carrier board or module implements the WM8804, and how does it connect to
  the Raspberry Pi and the accepted software audio path?
- Which front-panel display, encoder, and power button will be selected, and what
  cutouts, mounting, and service access do they require?
- Which rear-panel connectors, controls, and labels are required?
- How many input boards are needed, which input functions belong on them, and
  which power, shutdown, IR, and housekeeping functions belong on the delegated
  controller?

## Related

- [Open Cinema software system](open-cinema-software.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [MEAN WELL UHP-500](mean-well-uhp-500.md)
- [WONDOM KAB9](wondom-kab9.md)
- [WM8804](wm8804.md)
- [Front-panel interface](front-panel-interface.md)
- [Auxiliary control electronics](auxiliary-control-electronics.md)
