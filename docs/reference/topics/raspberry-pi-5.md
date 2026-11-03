---
title: Raspberry Pi 5
summary: Selected appliance computer and current supported Open Cinema deployment target.
status: active
updated: 2026-11-03
tags: [compute, raspberry-pi, enclosure, thermal, power]
aliases: [rpi5, pi-5, raspberry-pi-5-model-b]
sources:
  - docs/decisions/0013-pi-source-control-and-future-hat.md
  - https://www.raspberrypi.com/products/raspberry-pi-5/
  - https://pip.raspberrypi.com/categories/892-raspberry-pi-5
  - https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf
  - https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-mechanical-drawing.pdf
  - https://github.com/k3rnL/open-cinema/blob/master/deployment/SUPPORTED_PLATFORMS.md
  - docs/worklog/2026-11-02-enclosure-requirements-update.md
  - docs/decisions/0003-prefer-earc-and-lvds-input-architecture.md
  - hardware/electronics/notes/rear-input-evidence.md
---

# Raspberry Pi 5

## Summary

Raspberry Pi 5 is the selected Open Cinema appliance computer. The current
software production boundary is the 8 GB Model B fixture on Debian 13 Trixie.

## Confirmed facts

- The Open Cinema deployment matrix currently accepts Raspberry Pi 5 Model B
  8 GB with at least 7,500 MB reported RAM, AArch64, and active cooling.
- Raspberry Pi documents an approximately 85 mm x 56 mm board footprint. Final
  enclosure production dimensions must use the current mechanical drawing and a
  physical board because connector/component tolerances apply.
- The board uses 5 V/5 A USB-C Power Delivery for full peripheral allowance.
- Raspberry Pi recommends active cooling for best sustained performance.
- A basic Raspberry Pi cooling fan has already been purchased for the enclosure.
  Its manufacturer, part number, mounting, and inclusion of a heatsink have not
  been recorded.
- Relevant interfaces include two USB 3.0 ports, two USB 2.0 ports, Gigabit
  Ethernet, Wi-Fi, Bluetooth 5/BLE, PCIe 2.0 x1, the 40-pin header, and a dedicated
  four-pin fan connector.

## Interface direction

The owner plans a custom HAT to simplify connections and will use Pi GPIO-header signals plus later custom software to control rear-board source selection. Integrating the LVDS receiver adapter into that HAT is proposed; its mechanical design, pin allocation and control bus are not selected. Processed audio goes from the Pi to the amplifier over USB. See [decision 0013](../../decisions/0013-pi-source-control-and-future-hat.md).

## Constraints

- Provide a regulated 5 V rail with adequate current and transient behavior.
- Maintain access to required I/O and the microSD card, or explicitly document
  which interfaces become internal-only.
- Do not use approximate product-brief dimensions as production CAD authority;
  use the current mechanical drawing/STEP model and verify the physical board.
- The proposed multichannel capture uses the Pi's I2S clock-consumer interface.
  The [digital audio input topic](digital-audio-input.md) records candidate GPIO
  assignments and clocking constraints. This is not yet a tested Linux capture
  configuration, and it must be checked against other GPIO users.

## Evidence

- [Raspberry Pi 5 product page](https://www.raspberrypi.com/products/raspberry-pi-5/)
- [Official product-information portal](https://pip.raspberrypi.com/categories/892-raspberry-pi-5)
- [Product brief](https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf)
- [Mechanical drawing](https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-mechanical-drawing.pdf)
- [Open Cinema supported platforms](https://github.com/k3rnL/open-cinema/blob/master/deployment/SUPPORTED_PLATFORMS.md)

## Open questions

- Confirm that the enclosure unit is the same 8 GB board revision as the accepted
  software fixture.
- Which connectors must remain externally accessible?
- Identify the purchased fan and determine its mounting, airflow direction,
  heatsink requirements, and thermal acceptance test.
- How will the 5 V rail be generated from the enclosure's main DC bus?

## Related

- [Open Cinema software system](open-cinema-software.md)
- [Enclosure and appliance system](enclosure-appliance.md)
- [Front-panel interface](front-panel-interface.md)
- [Digital audio input and LVDS transport](digital-audio-input.md)
