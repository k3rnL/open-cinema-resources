# 0013 — Pi-controlled source selection and a future connection HAT

- Date: 2026-11-03
- Status: Owner-accepted allocation and future HAT direction; bus, pins and implementation open
- Source: owner reaffirmed pcm-auto-decoder as the Pi-side adaptive decoder, requested an unaltered input stream, Pi-controlled source selection, and a future custom HAT to simplify connections. Custom control software will be developed later. The preceding owner clarification confirmed USB output to the amplifier.
- Refines [0012](0012-require-lossless-audio-and-atmos.md); preserves the extraction-only rear electronics boundary.

## Accepted direction

1. The rear board extracts the selected input and delivers its audio payload unchanged to the Raspberry Pi. The working audio link remains I2S-compatible data/clocks carried electrically over LVDS and converted beside the Pi.
2. pcm-auto-decoder is the intended Pi-side adaptive decoding component. Main audio processing remains on the Pi. This records the software responsibility; it does not replace the version-specific verification evidence in decision 0012 or certify every format.
3. The Raspberry Pi commands source selection on the rear board. Provide a control connection through the Pi GPIO header and suitable rear-board circuitry; the custom control software is deferred.
4. Plan a custom Pi HAT to simplify the appliance connections. HAT design is future work, not a completed board or a frozen pin assignment.
5. The Raspberry Pi sends processed audio to the amplifier over USB. The input I2S link does not also need to carry amplifier playback.

## Proposed implementation details — not yet selected

- Integrate the already-envisaged Pi-side LVDS receivers into the future HAT, with a short logic-level connection to the Pi capture pins and connectors for control/status.
- Use an appropriate GPIO-header control interface, such as I2C or SPI, selected from the eventual receiver/selector documentation. Reserve provision for reset and a status-change interrupt if useful. No particular bus, register map, pin count or microcontroller is selected.
- Keep control/status signals separate from the audio data signals. They may share a suitably designed physical harness, but do not encode source-selection commands into the audio payload.
- Include readback/status in the interface proposal: active source, signal lock, rate, transport mode and faults as supported by the selected receiver. The Pi needs enough information to coordinate capture when the input changes.
- Source switching should coordinate output muting, receiver re-lock, capture restart/reconfiguration and decoder reset when required. These are future integration requirements; no state machine or software has been implemented.
- Reserve connector/PCB space for control now, even though software and final pin assignments come later. Check the complete GPIO allocation against audio, front-panel controls, IR, power management and HAT identification before wiring.

The proposed HAT does not settle which power/wake functions must operate while the Pi is off. That remains part of the separate auxiliary control design. The next rear-board iteration must provide the interface, without moving audio decoding onto that board.

## Evidence and related records

- [Digital audio input](../reference/topics/digital-audio-input.md)
- [Raspberry Pi 5](../reference/topics/raspberry-pi-5.md)
- [WONDOM KAB9](../reference/topics/wondom-kab9.md)
- [Pi GPIO documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio): GPIO alternate functions include I2C/SPI; pin assignment and voltage compatibility need checking.
