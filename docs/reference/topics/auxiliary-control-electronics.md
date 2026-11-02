---
title: Auxiliary control electronics
summary: Delegated power, shutdown, IR and housekeeping functions, with the input-audio architecture tracked separately.
status: active
updated: 2026-11-03
tags: [electronics, control, inputs, power, infrared]
aliases: [logic-board, input-board, power-control-board, housekeeping-controller]
sources:
  - docs/worklog/2026-11-02-enclosure-requirements-update.md
  - docs/worklog/2026-11-03-rear-panel-and-audio-architecture.md
  - docs/decisions/0003-prefer-earc-and-lvds-input-architecture.md
---

# Auxiliary control electronics

## Summary

The appliance requires at least one input board between external inputs and the
Raspberry Pi, plus a power/control board for delegated low-level functions. The
[digital input architecture](digital-audio-input.md) now has a working eARC/ARC
and LVDS direction. The power/controller components, host protocol, schematic and
firmware remain unselected.

## Confirmed facts

- At least one input logic board is required to handle input-side functions before
  passing signals to the Raspberry Pi.
- The Raspberry Pi remains responsible for the main/full processing after the
  input front end.
- A power/control board is also required for power management and basic delegated
  electronics. Examples supplied so far are main-power shutdown and infrared
  control.
- The proposed audio split is a rear input PCB and a small adapter beside the Pi.
  The controller partition, exact board count and detailed circuits remain open;
  [decision 0003](../../decisions/0003-prefer-earc-and-lvds-input-architecture.md)
  establishes direction only.

## Constraints

- Define responsibilities and failure behavior before selecting a controller or
  communication protocol.
- Main-power shutdown must distinguish user intent, orderly Raspberry Pi shutdown,
  amplifier mute/sequencing, low-voltage removal, and mains isolation. These are
  separate functions with different safety implications.
- Input-side processing must not silently move the main audio-processing boundary
  away from the Raspberry Pi without a new decision.
- IR, encoder, power-button, wake, fault, and temperature functions should be
  considered together before assigning pins and board boundaries.

## Open questions

- How will the [captured rear interfaces](rear-panel-interface.md) and
  [audio-input architecture](digital-audio-input.md) be implemented, controlled and
  coordinated with mute, shutdown and fault handling?
- Which functions must continue while the Raspberry Pi is off or unresponsive?
- Which controller, power domains, isolation, watchdogs, nonvolatile state, and
  Raspberry Pi communication interface are required?
- How are amplifier mute, startup, shutdown, fault reporting, and rail sequencing
  coordinated?
- Which IR protocols and front/rear sensor locations are required?
- How many input boards are required, and how are responsibilities divided between
  them and the power/control board?

## Related

- [Enclosure and appliance system](enclosure-appliance.md)
- [Front-panel interface](front-panel-interface.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [WM8804 S/PDIF transceiver](wm8804.md)
- [WONDOM KAB9 amplifier](wondom-kab9.md)
- [Digital audio input and LVDS transport](digital-audio-input.md)
- [Rear-panel interface](rear-panel-interface.md)
