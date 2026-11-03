---
title: Digital audio input and LVDS transport
summary: Working eARC/ARC and optical/coax input architecture, with multichannel I2S over LVDS to the Raspberry Pi.
status: active
updated: 2026-11-03
tags: [electronics, audio, inputs, earc, arc, spdif, i2s, lvds]
aliases: [input-board, hdmi-audio-extraction, differential-i2s, rear-to-pi, ds90lv047a, ds90lv048a]
sources:
  - docs/decisions/0012-require-lossless-audio-and-atmos.md
  - docs/worklog/2026-11-03-enlarged-enclosure-and-input-architecture.md
  - docs/worklog/2026-11-03-rear-connector-selection.md
  - docs/decisions/0006-vertical-carrier-and-optical-daughterboards.md
  - docs/worklog/2026-11-03-kicad-rear-io-mechanical.md
  - docs/decisions/0003-prefer-earc-and-lvds-input-architecture.md
  - docs/worklog/2026-11-03-rear-panel-and-audio-architecture.md
  - hardware/electronics/notes/rear-input-evidence.md
---

# Digital audio input and LVDS transport

## Summary

The working direction is a rear input board feeding a small adapter beside the
Raspberry Pi through an LVDS cable link. All audio decoding, Atmos processing
and DSP stay on the Pi, as explicitly reaffirmed by the owner.
eARC plus explicit legacy ARC support is the compatibility target. This is an
architecture to validate, not a completed circuit or demonstrated capture path.

## First-version compatibility requirement

The owner requires broad TV compatibility and lossless TrueHD/DTS-HD plus Atmos in the initial version, with 5.1 initially and an option for 7.1. [Decision 0012](../../decisions/0012-require-lossless-audio-and-atmos.md) confirms the responsibility boundary: the rear board extracts/selects/transports audio; all audio processing runs on the Pi. Preserve PCM and encoded payloads, including the necessary HBR/MAT transport cases, with documented packing and clocks. The current decoder gap is separate Pi software work, not a reason to add a hardware decoder or renderer.

## Project direction

[Decision 0003](../../decisions/0003-prefer-earc-and-lvds-input-architecture.md)
records the rationale and scope. Physical input requirements and placement are
canonical in the [rear-panel topic](rear-panel-interface.md).

| Location | Proposed responsibility |
| --- | --- |
| Rear input board | Optical and coaxial reception/conditioning; HDMI eARC/ARC reception and negotiation; input selection; audio clock/data output and LVDS drivers |
| Internal harness | Audio and its clocks over differential pairs; ground reference, power and control connections also required |
| Adapter beside Pi | LVDS receivers and short logic-level I2S connection to the 40-pin header |
| Raspberry Pi | Capture, supported compressed-audio decoding, routing, volume, EQ and other DSP |

Assume one selected physical input at a time. The HDMI receiver/controller,
source-selection circuit, rails, control protocol and complete firmware are open.
Input extraction is not Dolby/DTS decoding. A receiver such as EP92H1 illustrates
the relevant interface functions, but is not a selected or validated part.

## Candidate transport implementation

I2S defines audio timing/data; LVDS carries those signals electrically over a
cable. The proposed parallel link uses one differential pair per signal. It does
not compress, resample or serialize all channels into one pair. The cited Analog
Devices serialized example is evidence of the broader technique, not this exact
circuit. See the [manufacturer evidence](../../../hardware/electronics/notes/rear-input-evidence.md).

For up to eight-channel PCM, the candidate Pi 5 connection is:

| I2S signal | Differential pairs | BCM GPIO at the Pi |
| --- | --- | --- |
| BCLK/SCK | 1 | 18 |
| WS/LRCLK | 1 | 19 |
| DATA0 | 1 | 20 |
| DATA1 | 1 | 22 |
| DATA2 | 1 | 24 |
| DATA3 | 1 | 26 |

Each data lane carries two PCM channels. Six pairs mean twelve signal conductors,
plus a ground reference. Power and control are additional connections. These are
GPIO numbers, not physical header-pin numbers; allocation against other project
functions is not checked.

- Candidate driver: **2 x TI DS90LV047A** on the rear board.
- Candidate receiver: **2 x TI DS90LV048A** on the Pi adapter.
- Each IC has four signal paths, so two provide eight paths, six used here.
- Candidate harness: nominal **100 ohm differential impedance**, preferably
  shielded, with suitable connectors and defined pair assignments. Two short
  Cat5e/Cat6 lengths were discussed as a prototype source of eight twisted pairs;
  neither a harness nor a connector pinout is approved.
- Terminate each used pair at the receiving end with a resistor matched to the
  line, nominally **100 ohm**. Include local power decoupling and verify layout,
  propagation delay and clock-to-data skew across chips and cable pairs.
- These candidate ICs use 3.3 V supplies. Check the selected audio receiver's I/O
  voltage; 1.8 V outputs cannot simply be assumed compatible. LVDS must be
  converted before connecting to Pi GPIO. This link is not galvanic isolation.

Component quantities are architecture-derived candidates in the
[preliminary register](../../../bom/preliminary-components.csv), not purchased or
released BOM items. The physical drivers/receivers need no firmware themselves;
the input controller and Linux integration do.

## Compatibility and clocking constraints

- Pi 5 has four usable I2S data lanes and a clock-consumer interface, I2S1. The
  source should provide the audio clocks in this proposed arrangement. The
  producer and consumer interfaces share header pins. Native multichannel TDM
  on one data wire is not supported by the cited Pi guide.
- Hardware capability alone does not prove eight-channel ALSA capture. Device
  tree, driver/channel configuration, GPIO conflicts, sample rates and source
  lock/loss behavior need validation on the actual supported Pi OS fixture.
- S/PDIF can serve stereo PCM and compatible compressed surround streams, but
  cannot be the common link for uncompressed eARC 5.1/7.1 PCM.
- The [WM8804](wm8804.md) is an S/PDIF interface, not an eARC or Dolby/DTS decoder.
  Its single receiver input requires selection for multiple S/PDIF sources. A
  future HDMI receiver may absorb some of that function; no replacement decision
  has been made.
- Preserve encoded payloads unchanged before software decoding. PCM capture,
  IEC 61937 handling and higher-bit-rate compressed formats are separate
  validation cases. Do not advertise formats merely because the HDMI chip can
  transport them.

Sources: [manufacturer evidence register](../../../hardware/electronics/notes/rear-input-evidence.md),
[existing software boundary](open-cinema-software.md).

## Open questions

- Which obtainable eARC/ARC receiver has adequate documentation, control firmware,
  CEC/fallback behavior and Pi-compatible multichannel output?
- Which source formats and sample rates should actually be advertised and tested?
- Where are clocks and all data lanes switched together, and how are mute,
  re-lock, source changes and startup/shutdown handled?
- Does the chosen capture path preserve required compressed payloads without
  resampling or other modification before decoding?
- What are the exact cable length, skew budget, connector, ground/shield strategy,
  supply rails, signal voltages and controller interface?
- Does the proposed rear placement pass the
  [thermal, EMI and mains constraints](rear-panel-interface.md)?

## Evidence

- [Discussion provenance and evolution](../../worklog/2026-11-03-rear-panel-and-audio-architecture.md)
- [Manufacturer sources](../../../hardware/electronics/notes/rear-input-evidence.md)
- The original architecture discussion produced no schematic, PCB, physical prototype, timing measurement or new capture test.
- A later [KiCad mechanical PCB study](hardware-repository-and-kicad.md)
  now provides A1 selected connectors, real pads and optical daughterboards. Logic/LVDS circuitry and
  electrical validation remain deferred; it does not validate this architecture.

## Related

- [Rear-panel interface](rear-panel-interface.md)
- [Auxiliary power/control electronics](auxiliary-control-electronics.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [MEAN WELL UHP-500](mean-well-uhp-500.md)

## Enlarged-enclosure discussion

The [2026-11-03 review](../../worklog/2026-11-03-enlarged-enclosure-and-input-architecture.md) proposes evaluating a single four-layer rear front end before adding a mezzanine. Stacking is acceptable to the owner in principle; no split or receiver is selected. Complete receiver documentation, TV/format requirements, clock/capture behavior and standby control precede layout. Current mechanical geometry is 250 × 51 at the window; see the rear-panel topic.
