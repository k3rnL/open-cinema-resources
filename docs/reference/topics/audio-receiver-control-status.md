---
title: Audio receiver control and status
summary: Meaning of lock, carrier rate and transport format; Pi source switching and unchanged payload boundary.
status: active
updated: 2026-11-03
tags: [audio, control, status, clock, capture, spdif, earc]
aliases: [signal-lock, rate, format, carrier-rate, word-packing, pcm-auto-decoder]
sources:
  - docs/decisions/0013-pi-source-control-and-future-hat.md
  - docs/worklog/2026-11-03-a10-electrical-draft.md
---

# Audio receiver control and status

The owner explicitly asked to preserve these definitions before starting hardware design. They refine [decision 0013](../../decisions/0013-pi-source-control-and-future-hat.md), without moving audio processing off the Raspberry Pi.

| Status | Meaning | What it does not establish |
|---|---|---|
| Signal lock | Receiver is synchronized to the incoming digital transport | Audible sound, supported codec, or successful Pi decoding; valid silence can be locked |
| Rate | Transport/carrier rate delivered to capture, with the relevant clocks | Decoded programme sample rate in every encoded format |
| Format | PCM/non-audio indication when available; I2S/other mode, lane count, slot/word width, alignment and clock edges | Universal Dolby/DTS identification or decoding by the rear board |

The Pi commands the source, waits for stable reception, reads supported status, configures/restarts capture where necessary, then sends the unchanged payload to pcm-auto-decoder. Coordinate output muting and decoder boundaries during source changes or errors; ordinary logic clock muxes must not be switched during active capture. Never silently resample, truncate, apply de-emphasis or substitute samples on the valid encoded-payload path.

Extracting framing and repacking words is allowed only with an explicit, tested mapping that preserves the payload bits. Metadata belongs in status/control; it is not inserted into the audio data. Processed output goes from Pi to amplifier over USB. The future HAT and Pi GPIO allocation remain separate work.

## Current evidence and limits

The [A10 work log](../../worklog/2026-11-03-a10-electrical-draft.md) links a drafted CS8416K receiver/mux/LVDS schematic. Its CS8416K control interface is 100 kHz I2C, with reset/interrupt/error/selection connections. OMCK is unused, so its clock-ratio register cannot establish rate; clock measurement/validation at the Pi/HAT remains required. eARC status fields and raw HBR/MAT packing cannot be finalized until the actual receiver documentation is available.

These definitions are accepted project knowledge. A10 component and connector choices are draft implementation proposals, not a claim that the end-to-end stream has been captured or tested.
