# 2026-11-04 — A11 ARC schematic, two reviews and rigid model

## Authorization and scope

The owner accepted standard ARC for now, then authorized continuing the hardware work. Earlier instructions cover chip sourcing, requirements, schematic creation, two verification passes, model export and memory upkeep. [Decision 0014](../decisions/0014-use-arc-for-first-version.md) defines the accepted format scope; it does not itself select a particular chip. All decoding/DSP remains on the Pi, with processed output to the amplifier by USB. No supplier contact or purchase was requested.

## Implementation observation

A separate A11 project now contains an **ADV7511KSTZ ARC test candidate → CS8416K-CZZR input selector → DS90LV047A LVDS link**. Optical 1/2 and coax use CS8416 RXP0/1/2; ARC uses RXP3. A11 adds ARC coupling/HPD, CEC oscillator/pull-up, DDC, HDMI current-limited 5 V/protection, 1.8 V regulator/filter domains and upgraded 3.3 V regulator package. Full requirements, parts and sources are in the hardware repository.

A10 muxes, its second LVDS driver and external eARC placeholder header are removed. ARC uses only BCLK, LRCLK and DATA0: three differential pairs. J22 keeps the former positions for those pairs, with unused lanes NC. **J20 pin 7 is now ADV_INT; pin 8 is HDMI_5V_EN**, replacing A10 AUDIO_SEL/MUX_DISABLE. Source selection now uses the CS8416 I2C interface. Preserve the [lock/carrier-rate/format definitions](../reference/topics/audio-receiver-control-status.md) and stop/reconfigure capture across source changes.

This is an assistant implementation candidate within the authorized work, **not owner acceptance of ADV7511 procurement or a demonstrated ARC product**. ADI's public guides establish pin/control information, but do not explicitly establish DD+ carrier-rate support. Its product page also requires HDMI-adopter status to purchase; JLC C179459 is a listing, not evidence that the owner is eligible or JLC has accepted sourcing. ARC-only startup/EDID without video-clock input needs qualification. No codec/Atmos capability is claimed merely from the transmitter's separate forward-audio specifications.

## Mechanical observation

97 footprints fit nominally on the retained 228 × 39.8 × 1.6 mm board. This is placement-space evidence, not routing completion. All connector positions and four Ø3 PCB holes remain unchanged. New rigid STEP/F3D exports have one component and 161 solid bodies; backplate, L brackets and mains are excluded. The latest 250 × 51 mm window and enlarged enclosure still need an assembly/airflow/EMI review.

The open linked `rear-io-A5-assembly v2` had unsaved edits. A11 was exported and reimported in temporary documents; no user Fusion document was overwritten or saved. Git publication does not update that cloud component automatically. The existing modified A9 KiCad project was preserved and excluded from this commit.

## Verification evidence

Two static passes by the same assistant, not two independent engineers:

1. Datasheet and exported-schematic review: complete ADV 100-pin map/support circuit, receiver/PLL/straps, power and protection pinouts, LVDS polarities, control-header changes and isolated BTL returns. KiCad 10.0.5 ERC: 0 violations. All nine sheets visually reviewed, with a PDF export.
2. PCB/netlist/model review: 421 electrical pad keys, 97 footprints, 91 resolved model links, retained geometry/holes. Geometry DRC: 0 violations; **318 unrouted connections, zero tracks**. STEP and F3D each reimport with 161 solids, no child components, matching body volumes/bounds.

Corrected the inherited 10 µF capacitor MPN typo in A11 to CL10A106KP8NNNC; A10 historical files remain unchanged. Confirmed the exposed-pad regulator package and separately tracked supply/filter thermal assumptions. No physical prototype, payload comparison, firmware, EMC or temperature test was performed.

## Remaining work

Resolve ADV procurement eligibility and prove ARC-only startup/CEC plus DD+ carrier/JOC preservation before committing fabrication. Optimize/route the board, qualify power/ground/protection, build the Pi HAT/control firmware and run clock-consumer capture tests. The KLS horizontal speaker block still lacks a qualified current rating/supply route. Header/passive selection and JLC acceptance remain incomplete. eARC remains deferred; it is not a drop-in promise.

## Evidence

Hardware revision: `41bfb5a8019e18576301200c7c10d39e4678c63f`. Published files:

- [A11 overview](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/README.md)
- [Circuit/interface requirements](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/requirements.md)
- [Sourcing and ADI purchase condition](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/sourcing.md)
- [Primary source register](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/source-register.json)
- [Verification and exact source hashes](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/verification.md)
- [Schematic PDF](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/exports/rear-io-A11-schematic.pdf)
- [Rigid STEP](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/exports/rear-io-A11-rigid.step) / [Fusion archive](https://github.com/k3rnL/open-cinema-hardware/blob/41bfb5a8019e18576301200c7c10d39e4678c63f/boards/rear-io-A11/exports/rear-io-A11-rigid.f3d)

Related: [A10 history](2026-11-03-a10-electrical-draft.md), [accepted ARC scope](2026-11-04-arc-first-version.md).
