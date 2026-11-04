---
title: Enclosure and appliance system
summary: Current system-level enclosure context, selected major components, and unresolved integration constraints.
status: active
updated: 2026-11-04
tags: [architecture, enclosure, mechanical, electronics, thermal]
aliases: [case, chassis, appliance-enclosure]
sources:
  - docs/decisions/0014-use-arc-for-first-version.md
  - docs/worklog/2026-11-03-rear-connector-selection.md
  - docs/decisions/0006-vertical-carrier-and-optical-daughterboards.md
  - docs/worklog/2026-11-03-kicad-rear-io-mechanical.md
  - docs/decisions/0001-initial-enclosure-components.md
  - docs/decisions/0002-select-24v-main-supply.md
  - docs/worklog/2026-11-02-initial-resource-import.md
  - docs/worklog/2026-11-02-enclosure-requirements-update.md
  - docs/worklog/2026-11-03-rear-panel-and-audio-architecture.md
  - docs/decisions/0003-prefer-earc-and-lvds-input-architecture.md
  - hardware/mechanical/enclosure-layout/README.md
  - bom/preliminary-components.csv
---

# Enclosure and appliance system

## Summary

The physical enclosure effort has started. The initial major component set is
selected. Owner-supplied enclosure views and rear interface requirements are now
recorded. A rear input board and LVDS link are the working audio architecture;
a measured rear-frame sketch and KiCad mechanical PCB study are available in
hardware with A1 selected connectors and optical daughterboards. Full assembly integration, circuitry, power distribution,
cooling and safety implementation remain open.

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
- The back-panel interface requirements and enclosure orientation are captured in
  the [rear-panel topic](rear-panel-interface.md), with original screenshots.
  The PSU spans the rear; the Pi and amplifier are at the front. A1 connector references are selected for integration; final manufacturing dimensions remain open.
- The appliance needs at least one input front-end board and a power/control board
  for delegated functions. The [digital-input working direction](digital-audio-input.md)
  targets ARC first with I2S over LVDS and eARC deferred; power/control electronics and
  detailed implementations remain open.

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
- [Prefer eARC/ARC and LVDS input architecture](../../decisions/0003-prefer-earc-and-lvds-input-architecture.md)

## Evidence

- [Preliminary component register](../../../bom/preliminary-components.csv)
- [Initial resource import work log](../../worklog/2026-11-02-initial-resource-import.md)
- [Enclosure requirements update](../../worklog/2026-11-02-enclosure-requirements-update.md)
- [Rear-panel and audio discussion](../../worklog/2026-11-03-rear-panel-and-audio-architecture.md)
- [Owner-supplied enclosure views](../../../hardware/mechanical/enclosure-layout/README.md)
- Component topic pages and linked manufacturer datasheets.

## Open questions

- What is the precise internal/outside height datum for the owner's 80 mm total
  height, and what are the width/depth, materials, acoustic limits, mounting and
  service-clearance requirements? Orientation is now recorded.
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
- Which cutouts, labels, support and mounting details qualify the A1 connector selection? Six speaker pairs are confirmed; channel roles remain open.
- Can the above-PSU input-board location satisfy manufacturer guidance and actual
  thermal, EMI, mains-separation and maintenance requirements?
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
- [Rear-panel interface](rear-panel-interface.md)
- [Digital audio input and LVDS transport](digital-audio-input.md)
- [Hardware repository and KiCad study](hardware-repository-and-kicad.md)
