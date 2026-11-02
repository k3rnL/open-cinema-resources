# Decision: Initial enclosure main components

- Status: Accepted
- Date: 2026-11-02
- Owners: `@k3rnL`
- Related: [enclosure reference](../reference/topics/enclosure-appliance.md),
  [preliminary component register](../../bom/preliminary-components.csv)

## Context

The Open Cinema software is largely implemented and has an accepted Raspberry Pi
appliance release. Physical enclosure work has started, so the major component
choices need a durable, traceable home before detailed layout and integration.

## Decision

Use the following initial main component set:

- Raspberry Pi 5 as the appliance computer. The currently accepted software
  fixture is the 8 GB Model B.
- Wolfson/Cirrus Logic WM8804 for the S/PDIF digital-audio interface.
- WONDOM/Sure Electronics KAB9 (AA-KA32473) for the configurable eight-channel
  power-amplifier output.
- MEAN WELL UHP-500 family for the main low-profile AC/DC power supply.

This decision records component selection, not a completed electrical, mechanical,
thermal, or safety design.

## Alternatives considered

No rejected alternatives or comparative evaluation were supplied with this
decision. Add them in a superseding decision if the selection changes.

## Evidence

- [Open Cinema software system](../reference/topics/open-cinema-software.md)
- [Raspberry Pi 5](../reference/topics/raspberry-pi-5.md)
- [WM8804](../reference/topics/wm8804.md)
- [WONDOM KAB9](../reference/topics/wondom-kab9.md)
- [MEAN WELL UHP-500](../reference/topics/mean-well-uhp-500.md)
- [Imported third-party datasheets](../../hardware/electronics/datasheets/README.md)

## Consequences

- Enclosure layout must accommodate a Pi 5 with active cooling, the KAB9 board and
  its heatsink/input module clearance, and the UHP-500 thermal mounting boundary.
- The power design needs at least a high-current amplifier rail and a protected,
  regulated 5 V Raspberry Pi rail.
- WM8804 lifecycle status and KAB9 availability introduce sourcing risk.
- Detailed connectors, wiring, speaker configuration, carrier electronics, cooling,
  mains safety, and compliance remain separate design work.

## Follow-up

- Confirm exact Raspberry Pi memory/board revision and cooler.
- Confirm UHP-500 voltage and `R`/non-`R` suffix.
- Record the WM8804 carrier/module and its Pi interface.
- Define KAB9 channel configuration, load, connectors, and cooling target.
- Produce the enclosure CAD, power tree, wiring diagram, thermal plan, and safety
  review before freezing the design.
