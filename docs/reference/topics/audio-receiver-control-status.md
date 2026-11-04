---
title: Audio receiver control and status
summary: Lock, carrier rate and transport format definitions; A11 I2C source selection and unchanged payload boundary.
status: active
updated: 2026-11-04
tags: [audio, control, status, clock, capture, spdif, earc]
aliases: [signal-lock, rate, format, carrier-rate, word-packing, pcm-auto-decoder, adv-int, hdmi-5v-en, j20, a11]
sources:
  - docs/worklog/2026-11-04-a11-arc-electrical-study.md
  - docs/decisions/0014-use-arc-for-first-version.md
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

Extracting framing and repacking words is allowed only with an explicit, tested mapping that preserves the payload bits. Receiver status (lock, carrier rate, channel-status readback and errors) travels separately. Codec metadata, including DD+ Atmos/JOC, remains inside the unchanged encoded payload; do not strip it or move it to a side channel. Processed output goes from Pi to amplifier over USB. The future HAT and Pi GPIO allocation remain separate work.

## Current evidence and limits

The [A10 work log](../../worklog/2026-11-03-a10-electrical-draft.md) links a drafted CS8416K receiver/mux/LVDS schematic. Its CS8416K control interface is 100 kHz I2C, with reset/interrupt/error/selection connections. OMCK is unused, so its clock-ratio register cannot establish rate; clock measurement/validation at the Pi/HAT remains required. [Decision 0014](../../decisions/0014-use-arc-for-first-version.md) now targets ARC first. ARC/CEC status, DD+ carrier packing and bit preservation still need validation; eARC status and HBR/MAT packing are deferred.

These definitions are accepted project knowledge. A10 component and connector choices are draft implementation proposals, not a claim that the end-to-end stream has been captured or tested.

## A11 interface update

The [A11 work log](../../worklog/2026-11-04-a11-arc-electrical-study.md) records CS8416 selection of all four inputs. A11 removes the external muxes. J20 pin7 changes to ADV_INT and pin8 to HDMI_5V_EN; the remainder and full J22 assignment are in the pinned hardware interface contract. Do not use A10 GPIO semantics on A11. Stop capture and disable the link before selecting; re-lock, read supported status, restart capture and decoder, then unmute output. These are requirements; firmware and capture validation are not complete.
