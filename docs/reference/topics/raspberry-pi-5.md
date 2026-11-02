---
title: Raspberry Pi 5
summary: Selected appliance computer and current supported Open Cinema deployment target.
status: active
updated: 2026-11-02
tags: [compute, raspberry-pi, enclosure, thermal, power]
aliases: [rpi5, pi-5, raspberry-pi-5-model-b]
sources:
  - https://www.raspberrypi.com/products/raspberry-pi-5/
  - https://pip.raspberrypi.com/categories/892-raspberry-pi-5
  - https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf
  - https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-mechanical-drawing.pdf
  - https://github.com/k3rnL/open-cinema/blob/master/deployment/SUPPORTED_PLATFORMS.md
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
- Relevant interfaces include two USB 3.0 ports, two USB 2.0 ports, Gigabit
  Ethernet, Wi-Fi, Bluetooth 5/BLE, PCIe 2.0 x1, the 40-pin header, and a dedicated
  four-pin fan connector.

## Constraints

- Provide a regulated 5 V rail with adequate current and transient behavior.
- Maintain access to required I/O and the microSD card, or explicitly document
  which interfaces become internal-only.
- Do not use approximate product-brief dimensions as production CAD authority;
  use the current mechanical drawing/STEP model and verify the physical board.

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
- Which active cooler and airflow direction will be used?
- How will the 5 V rail be generated from the enclosure's main DC bus?

## Related

- [Open Cinema software system](open-cinema-software.md)
- [Enclosure and appliance system](enclosure-appliance.md)
