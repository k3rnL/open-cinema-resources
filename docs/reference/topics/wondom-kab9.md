---
title: WONDOM KAB9 eight-channel amplifier
summary: Selected configurable eight-channel Class-D output board, part AA-KA32473.
status: active
updated: 2026-11-03
tags: [electronics, amplifier, audio-output, power, thermal]
aliases: [kab9, aa-ka32473, sure-electronics-kab9]
sources:
  - docs/decisions/0013-pi-source-control-and-future-hat.md
  - hardware/electronics/datasheets/wondom-kab9-aa-ka32473.pdf
  - https://store.sure-electronics.com/product/AA-KA32473
---

# WONDOM KAB9 eight-channel amplifier

## Summary

KAB9 (AA-KA32473) is the selected main-output amplifier. Four amplifier sections
can be configured independently for BTL stereo or PBTL mono operation.

## Confirmed facts

- The board supports eight 50 W channels at 4 ohm and can combine channel pairs
  into 100 W mono outputs for 6.1, 4.2, 4.0, and related configurations.
- Operating input is 12-30 V DC, with 24 V nominal and a stated nominal power
  requirement of 400 W for the eight-channel configuration.
- The documented board footprint is 152.4 mm x 114.3 mm, with mounting spans of
  142.24 mm x 104.14 mm. The product overview states 152.4 mm x 114.3 mm x
  45.7 mm overall; the USB codec daughter board height is documented as 27.6 mm.
- The default input is differential through a 16-pin header. A 7.1/5.1 USB codec
  daughter board is documented as an alternative/default module.
- Gain is switch-selectable at five levels. Shutdown, mute, amplifier switching-
  frequency synchronization, fault, power-enable, and half-power signals are
  exposed on headers.
- The vendor recommends adding a fan for continuous higher-power operation.
- The official WONDOM listing currently marks AA-KA32473 out of stock; procurement
  status should be rechecked when ordering.

## Selected input path

The owner confirmed USB audio from the Raspberry Pi to the amplifier, after Pi-side decoding and processing. The alternative external differential-input path is no longer an open architecture choice. Validate the actual USB codec module, channel mapping and amplifier configuration for 5.1 initially and optional 7.1. See [decision 0013](../../decisions/0013-pi-source-control-and-future-hat.md).

## Constraints

- Provide a DC supply, wiring, connectors, fusing, and conductor sizing suitable
  for the actual load and fault current.
- Maintain heatsink airflow and clearance for the chosen input daughter board.
- Validate channel mapping, output mode switches, gain, noise, mute/shutdown
  sequencing, and speaker impedance on the actual board revision.

## Evidence

- [Local product document](../../../hardware/electronics/datasheets/wondom-kab9-aa-ka32473.pdf)
- [Official WONDOM product page](https://store.sure-electronics.com/product/AA-KA32473)

## Open questions

- Confirm the actual USB codec module revision, supported USB modes and working
  capture-to-playback integration with the Pi.
- What exact channel-to-speaker mapping and BTL/PBTL configuration is required?
- What continuous programme power and cooling target should the enclosure support?
- Which mating connectors and cable kit are selected?

## Related

- [MEAN WELL UHP-500](mean-well-uhp-500.md)
- [Enclosure and appliance system](enclosure-appliance.md)
- [Open Cinema software system](open-cinema-software.md)
