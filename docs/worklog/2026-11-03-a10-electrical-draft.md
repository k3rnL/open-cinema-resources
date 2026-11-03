# 2026-11-03 — A10 electrical draft and receiver-status memory

## Owner instruction

Preserve the lock/rate/format explanation in durable memory; source chips and requirements, create the electronic schematic, verify it twice and export a model for integration. Existing accepted boundary: rear extraction/selection/transport only, Raspberry Pi decoding/DSP, USB output to the amplifier. No supplier message or purchase was requested.

## Implemented draft

Created a separate [A10 project](https://github.com/k3rnL/open-cinema-hardware/tree/d2c430eea1eaef925cf6f22560fbf2d665d4ba8f/boards/rear-io-A10), preserving A9 and the existing modified KiCad project. It contains CS8416K optical/coax reception, two LVC157 muxes, two DS90LV047 transmitters, 3.3 V power, control headers and six independent speaker-pair connections. CS8416K is a documented working alternative to WM8804, not a released substitution. No extra decoding chip is introduced.

Saved canonical [receiver-status definitions](../reference/topics/audio-receiver-control-status.md). Hardware requirements record startup, 100 kHz control, unchanged encoded payload, lock-loss handling, optical bandwidth, LVDS termination/skew and regulator thermal budget.

## Verification and export

Two static reviews by the same assistant: datasheet/netlist review and PCB/interface/model consistency. KiCad 10.0.5 reported 0 ERC issues and 0 geometry/clearance/courtyard DRC issues; 186 connections remain unrouted. The PCB has 62 footprints and no tracks. Both rigid exports reimport as 114 solids with zero child components and matching geometry. No powered prototype, fidelity/EMI/thermal test or new enclosure collision check was performed. Existing Fusion user documents were left untouched.

## Unresolved

SiI9437 and EP92H1 are eARC/ARC candidates. Exact catalogue/distributor leads exist, but available public documentation does not establish full pinout, rails, firmware/control and HBR/MAT output mapping. Therefore the HDMI socket is explicitly unwired in A10; the test header is not a module specification. A full schematic and manufacturing release remain blocked on that design package plus routing/protection/harness/bench qualification.

KLS speaker-block current rating/supply remains unverified. Current board outline and four Ø3 holes are retained, not a freeze of the enlarged enclosure fit. The new 250 × 51 opening is recorded; prior nominal z 67 and plate datum are retained for comparison. Do not infer PSU airflow clearance or a final eARC space claim from the export. Backplate, L brackets and mains assembly remain owner/separate work.

## Evidence

Hardware revision: `d2c430eea1eaef925cf6f22560fbf2d665d4ba8f`, pushed to `main`.

- [Sourcing and prepared document request](https://github.com/k3rnL/open-cinema-hardware/blob/d2c430eea1eaef925cf6f22560fbf2d665d4ba8f/boards/rear-io-A10/sourcing.md)
- [Circuit/control requirements](https://github.com/k3rnL/open-cinema-hardware/blob/d2c430eea1eaef925cf6f22560fbf2d665d4ba8f/boards/rear-io-A10/requirements.md)
- [Verification scope and reports](https://github.com/k3rnL/open-cinema-hardware/blob/d2c430eea1eaef925cf6f22560fbf2d665d4ba8f/boards/rear-io-A10/verification.md)
- [Decision 0013](../decisions/0013-pi-source-control-and-future-hat.md)
