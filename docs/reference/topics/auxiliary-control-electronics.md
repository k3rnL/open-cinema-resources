---
title: Auxiliary control electronics
summary: Required input front-end and delegated power, shutdown, IR, and housekeeping electronics that have not yet been designed.
status: active
updated: 2026-11-02
tags: [electronics, control, inputs, power, infrared]
aliases: [logic-board, input-board, power-control-board, housekeeping-controller]
sources:
  - docs/worklog/2026-11-02-enclosure-requirements-update.md
---

# Auxiliary control electronics

## Summary

The appliance requires at least one input board between external inputs and the
Raspberry Pi, plus a power/control board for delegated low-level functions. No
components, interfaces, schematic, or firmware have been selected.

## Confirmed facts

- At least one input logic board is required to handle input-side functions before
  passing signals to the Raspberry Pi.
- The Raspberry Pi remains responsible for the main/full processing after the
  input front end.
- A power/control board is also required for power management and basic delegated
  electronics. Examples supplied so far are main-power shutdown and infrared
  control.
- The number of input boards and the detailed function split remain open.

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

- Which physical inputs and signal formats must the input board accept, condition,
  switch, detect, or convert?
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
