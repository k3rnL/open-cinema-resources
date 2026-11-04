---
title: Digital audio input and LVDS transport
summary: A11 drafts ADV7511 ARC into CS8416 source selection and a three-pair LVDS link; DD+ capture and procurement remain unqualified.
status: active
updated: 2026-11-04
tags: [electronics, audio, inputs, earc, arc, spdif, i2s, lvds]
aliases: [input-board, hdmi-audio-extraction, differential-i2s, rear-to-pi, ds90lv047a, ds90lv048a, a11, adv7511, c179459]
sources:
  - docs/worklog/2026-11-04-a11-arc-electrical-study.md
  - docs/decisions/0014-use-arc-for-first-version.md
  - docs/worklog/2026-11-03-a10-electrical-draft.md
  - docs/decisions/0013-pi-source-control-and-future-hat.md
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
**Standard ARC is the first-version HDMI target** under [decision 0014](../../decisions/0014-use-arc-for-first-version.md). eARC is deferred. This is an architecture to validate, not a demonstrated capture path.

## First-version compatibility requirement

Target stereo PCM, AC-3, conventional DTS and DD+, including unchanged DD+ Atmos/JOC metadata. TV passthrough and receiver/capture implementation must be validated. TrueHD, DTS-HD MA, MAT and multichannel PCM over HDMI are deferred with eARC. [Decision 0014](../../decisions/0014-use-arc-for-first-version.md) supersedes the initial lossless requirement in 0012 while retaining 5.1 output with an option for 7.1, unchanged payload and all processing on the Pi. Direct files/network audio are not restricted by ARC.

## Project direction

[Decision 0003](../../decisions/0003-prefer-earc-and-lvds-input-architecture.md)
records the original rationale; [decision 0014](../../decisions/0014-use-arc-for-first-version.md) now defines HDMI scope. Physical input requirements and placement are
canonical in the [rear-panel topic](rear-panel-interface.md).

| Location | Proposed responsibility |
| --- | --- |
| Rear input board | Optical and coaxial reception/conditioning; HDMI ARC reception and CEC negotiation; input selection; audio clock/data output and LVDS drivers |
| Internal harness | Audio and its clocks over differential pairs; ground reference, power and control connections also required |
| Adapter beside Pi | LVDS receivers and short logic-level I2S connection to the 40-pin header |
| Raspberry Pi | Capture, supported compressed-audio decoding, routing, volume, EQ and other DSP |

One selected input at a time. **Current A11:** ADV7511KSTZ is the ARC test candidate; CS8416K-CZZR selects optical1/2/coax/ARC internally, and one DS90LV047 drives three LVDS pairs. No external mux or stacked receiver board is used. These are prototype implementation choices, not qualified purchasing or format guarantees. See the [A11 evidence](../../worklog/2026-11-04-a11-arc-electrical-study.md). PCM9211 research and the original unimplemented ARC scope remain [historical](../../worklog/2026-11-04-arc-first-version.md).

## Pi control and future HAT

[Decision 0013](../../decisions/0013-pi-source-control-and-future-hat.md) confirms Pi-controlled source selection through the GPIO header and a future custom connection HAT. Custom control software is deferred. The proposed HAT would incorporate the LVDS receiver adapter; exact bus, pins, circuitry and harness remain open. Reserve a control/status connection alongside the audio link, with readback and source-change handling to be defined from the selected receiver.

The unchanged captured payload feeds pcm-auto-decoder on the Pi, followed by the Pi audio processing pipeline. Processed audio leaves the Pi over USB to the amplifier. Source selection/control is separate from audio payload transport.

## Historical A10 implementation draft

The [A10 work log](../../worklog/2026-11-03-a10-electrical-draft.md) records the first separate electrical schematic: CS8416K optical/coax receiver, logic muxes, LVDS drivers and Pi control. **HDMI remains unwired and the PCB is unrouted.** A10 predates the ARC-only decision and has not been electrically revised for ARC. The two static review passes do not qualify the full audio path. Canonical [lock/rate/format definitions](audio-receiver-control-status.md) are now saved.

## Candidate transport implementation

I2S defines audio timing/data; LVDS carries those signals electrically over a
cable. The proposed parallel link uses one differential pair per signal. It does
not compress, resample or serialize all channels into one pair. The cited Analog
Devices serialized example is evidence of the broader technique, not this exact
circuit. See the [manufacturer evidence](../../../hardware/electronics/notes/rear-input-evidence.md).

**ARC A11:** one data lane plus BCLK and LRCLK, over three LVDS pairs; one DS90LV047 transmitter and one future DS90LV048 HAT receiver. A two-slot carrier may contain encoded multichannel audio.

**Historical A10 / possible future eARC provision:** the following six-pair proposal is not the populated A11 link. DATA1–3 are NC in A11; eARC is not a drop-in upgrade. For future eight-channel PCM, the candidate Pi 5 connection is:

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

- Historical six-pair driver quantity: **2 x TI DS90LV047A**; A11 uses one.
- Historical six-pair receiver quantity: **2 x TI DS90LV048A**; ARC HAT needs one.
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
  future HDMI receiver may absorb some of that function; A10 uses CS8416K as a draft alternative, not a released replacement.
- Preserve encoded payloads unchanged before software decoding. PCM capture,
  IEC 61937 handling and DD+ Atmos are separate first-version validation cases; HBR/MAT is deferred with eARC. Do not advertise formats merely because the HDMI chip can
  transport them.

Sources: [manufacturer evidence register](../../../hardware/electronics/notes/rear-input-evidence.md),
[existing software boundary](open-cinema-software.md).

## Open questions

- Which obtainable ARC front end/controller has adequate documentation, CEC behavior and verified stereo/encoded-surround output, including DD+ Atmos?
- Which carrier rates and format capabilities can be advertised after the accepted ARC targets pass capture/interoperability tests?
- How is the CS8416 internal source change coordinated with mute, capture stop,
  re-lock and restart, including ARC CEC startup/shutdown?
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
  now provides A1 selected connectors, real pads and optical daughterboards. A10 later adds draft logic/LVDS circuitry; physical electrical validation remains deferred.

## Related

- [Rear-panel interface](rear-panel-interface.md)
- [Auxiliary power/control electronics](auxiliary-control-electronics.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [MEAN WELL UHP-500](mean-well-uhp-500.md)

## Enlarged-enclosure discussion

The [2026-11-03 review](../../worklog/2026-11-03-enlarged-enclosure-and-input-architecture.md) proposes evaluating a single four-layer rear front end before adding a mezzanine. Stacking is acceptable to the owner in principle. A11 subsequently drafts a single-board ARC candidate; no mezzanine is needed for the nominal placement. Complete receiver documentation, TV/format requirements, clock/capture behavior and standby control precede layout. Current mechanical geometry is 250 × 51 at the window; see the rear-panel topic.

## A11 implementation evidence and remaining gates

The [A11 work log](../../worklog/2026-11-04-a11-arc-electrical-study.md) records public-source research, the complete candidate support circuit and two static reviews. This supports proceeding with a one-board prototype study, not a claim that ARC works. ADI purchase eligibility, DD+ carrier/JOC preservation and ARC-only startup without a video clock remain unresolved. Pi CEC/source-control firmware, HAT/driver capture, routing, grounding and powered EMI/thermal tests are still required. All accepted formats remain targets until measured.
