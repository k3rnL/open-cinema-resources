---
title: Enclosure and appliance system
summary: Current system-level enclosure context, selected major components, and unresolved integration constraints.
status: active
updated: 2026-11-02
tags: [architecture, enclosure, mechanical, electronics, thermal]
aliases: [case, chassis, appliance-enclosure]
sources:
  - docs/decisions/0001-initial-enclosure-components.md
  - docs/worklog/2026-11-02-initial-resource-import.md
  - bom/preliminary-components.csv
---

# Enclosure and appliance system

## Summary

The physical enclosure effort has started. The initial major component set is
selected, while the detailed mechanical layout, power distribution, cooling,
connectors, and safety implementation remain to be captured.

## Confirmed facts

- The project software is largely implemented and has a functionally accepted
  `v0.3.2` appliance release on a Raspberry Pi 5 8 GB fixture.
- The initial selected component set includes a Raspberry Pi 5, a WM8804 S/PDIF
  transceiver, a WONDOM KAB9 eight-channel amplifier, and a MEAN WELL UHP-500
  power-supply family member.
- The accepted software fixture uses active cooling on the Raspberry Pi 5.
- KAB9 is a nominal 24 V, eight-channel Class-D amplifier board. Its vendor
  recommends forced air when it is run continuously at higher power.
- The UHP-500 series is a low-profile, fanless AC/DC supply whose permitted load
  depends on input voltage, ambient/case temperature, mounting, and derating.

## Constraints

- Provide isolation and safe mechanical segregation between mains wiring and
  extra-low-voltage electronics. Final mains design requires competent electrical
  and regulatory review.
- Preserve airflow and service access for the Pi 5, KAB9, and power supply.
- Do not treat headline wattage as enclosure thermal design evidence. Validate the
  actual programme load, losses, temperatures, and airflow.
- The Raspberry Pi 5 requires a regulated 5 V supply; the selected UHP-500 family
  output and the required conversion path have not yet been recorded.

## Decisions

- [Initial enclosure main components](../../decisions/0001-initial-enclosure-components.md)

## Evidence

- [Preliminary component register](../../../bom/preliminary-components.csv)
- [Initial resource import work log](../../worklog/2026-11-02-initial-resource-import.md)
- Component topic pages and linked manufacturer datasheets.

## Open questions

- What are the enclosure's target outside dimensions, orientation, materials,
  acoustic limits, mounting method, and service-clearance requirements?
- Which exact UHP-500 voltage and `R`/non-`R` suffix is selected?
- What protected DC/DC stage will provide the Raspberry Pi's 5 V rail?
- What are the AC inlet, fuse, switch, protective-earth, creepage/clearance, and
  strain-relief requirements?
- What fans, vents, filters, temperature sensors, and control policy are required?
- What carrier board or module implements the WM8804, and how does it connect to
  the Raspberry Pi and the accepted software audio path?
- Which connectors, harnesses, speakers, storage, display, and user controls must
  fit inside or on the enclosure?

## Related

- [Open Cinema software system](open-cinema-software.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [MEAN WELL UHP-500](mean-well-uhp-500.md)
- [WONDOM KAB9](wondom-kab9.md)
- [WM8804](wm8804.md)
