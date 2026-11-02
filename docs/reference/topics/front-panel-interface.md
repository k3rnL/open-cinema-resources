---
title: Front-panel interface
summary: Unbuilt local interface requiring a touch screen, encoder, power button, and new screen software.
status: active
updated: 2026-11-02
tags: [enclosure, front-panel, display, controls, software]
aliases: [local-ui, touch-screen, touchscreen, display-ui]
sources:
  - docs/worklog/2026-11-02-enclosure-requirements-update.md
  - https://www.waveshare.com/7.9inch-dsi-lcd.htm
  - https://www.waveshare.com/wiki/7.9inch_DSI_LCD
---

# Front-panel interface

## Summary

The front panel has not been designed. It is intended to provide a touch display,
a rotary encoder, and a power button. The Waveshare 7.9inch DSI LCD is the current
display candidate, but no front-panel component has been selected and the local
screen software has not started.

## Confirmed facts

- A touch screen, an encoder, and a power button are required on the front panel.
- The Waveshare 7.9inch DSI LCD is under consideration, not accepted.
- Waveshare identifies the candidate as SKU 22293 with a 7.9-inch, 400 x 1280 IPS
  panel, five-point capacitive touch over I2C, and DSI display connection.
- Waveshare documents Raspberry Pi 5 support, software-controlled brightness, and
  5 V power with 0.6 A listed as the standard input-current value.
- The panel is portrait by default; a landscape front-panel layout requires
  coordinated display and touch rotation.
- No local screen application has been started.

## Constraints

- Keep the display classified as a candidate until its mechanical drawing,
  landscape usability, software support, availability, viewing geometry, and
  integration with the enclosure are accepted.
- Verify the display and touch behavior on the exact Open Cinema Debian 13 Trixie
  Lite image and selected local UI stack; general Raspberry Pi support is not the
  same as an appliance-level compatibility result.
- Reserve Raspberry Pi DSI/I2C resources and include the display in the 5 V power
  budget if it is selected.
- Define the encoder and power-button electrical interfaces before assigning GPIO
  or auxiliary-controller responsibilities.

## Evidence

- [Waveshare product page](https://www.waveshare.com/7.9inch-dsi-lcd.htm)
- [Waveshare integration wiki](https://www.waveshare.com/wiki/7.9inch_DSI_LCD)
- [Enclosure requirements update](../../worklog/2026-11-02-enclosure-requirements-update.md)

## Open questions

- Is the Waveshare 7.9inch DSI LCD accepted after mechanical and software review?
- Does it work reliably on the exact Open Cinema appliance image without an
  unsupported kernel or display-stack divergence?
- What are the required front-panel dimensions, orientation, bezel, visible area,
  cutout, mounting points, and service method?
- Which encoder, knob, power button, illumination, and tactile behavior are
  required?
- Does the encoder connect to the Raspberry Pi or an auxiliary controller?
- Is the local screen software a dedicated client, a kiosk presentation of the
  existing Open Cinema UI, or another architecture?
- What must remain operable when the main screen application is unavailable?

## Related

- [Enclosure and appliance system](enclosure-appliance.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [Auxiliary control electronics](auxiliary-control-electronics.md)
- [Open Cinema software system](open-cinema-software.md)
