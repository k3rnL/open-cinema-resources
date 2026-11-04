# 2026-11-04 — Adopt ARC for the first version

The owner accepted ARC after reviewing eARC receiver documentation gaps and ARC format limits. [Decision 0014](../decisions/0014-use-arc-for-first-version.md) is the canonical scope and target matrix. Initial lossless-over-TV input is deferred; DD+ Atmos payload preservation remains required.

## Receiver lead, not a selection

TI's [PCM9211 datasheet](https://www.ti.com/lit/ds/symlink/pcm9211.pdf), SBAS495D, provides public pin definitions, electrical requirements, register descriptions and application circuits. Its overview includes ARC and non-PCM detection. It is a candidate, not a complete HDMI/CEC solution or an approved replacement for A10's CS8416K. DD+ bit preservation, ARC electrical front end, control and procurement remain unqualified. Revision C removed an older eARC-compatibility claim; that old claim must not be used to infer full eARC support.

## Changes and verification boundary

Added decision 0014, partial supersession notices on 0003/0012, updated reference topics/index/roadmap, and added an ARC implementation contract in hardware. Receiver status is separate from audio; codec/Atmos metadata must remain inside the encoded payload.

This session changes requirements and memory only. KiCad schematic/PCB, STEP/F3D, Fusion assembly and firmware remain unchanged. A10's previous static reviews still apply only to A10. No new physical capture/CEC/EMI test, order or supplier contact occurred.

Documentation checks: no whitespace errors; changed Markdown links resolve locally in both repositories; the memory search for “ARC first” returns the current digital-input topic and decision 0014 first. The existing manual KiCad project-file edit is excluded from this update.
