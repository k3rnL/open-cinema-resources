# Decision: Prefer eARC/ARC reception and an LVDS audio link

> **2026-11-04 scope update:** [Decision 0014](0014-use-arc-for-first-version.md) supersedes the initial eARC/lossless HDMI requirement with standard ARC, including DD+ Atmos transport. Pi processing and the LVDS direction remain. The original decision below is retained as history.

- Status: Accepted as a working architecture direction; implementation unvalidated
- Date: 2026-11-03
- Owner: `@k3rnL`
- Related: [session evidence](../worklog/2026-11-03-rear-panel-and-audio-architecture.md),
  [digital audio input](../reference/topics/digital-audio-input.md),
  [rear panel](../reference/topics/rear-panel-interface.md)

## Context

The power supply spans the rear of the enclosure; the Raspberry Pi and amplifier
are at the front. The input board therefore needs an internal audio connection to
the Pi. The owner requested broad HDMI compatibility and responded positively to
the proposed I2S-over-LVDS approach, then asked to retain this discussion.

## Decision

Use the following direction for further design and prototyping:

- Target an HDMI audio-return receiver with both eARC and legacy ARC support.
  This is the interpretation of the owner's "most compatible" priority; an exact
  receiver and an interoperability/codec matrix have not been selected.
- Put input reception, extraction and source-selection functions on a rear input
  board. Keep the main audio decoding and DSP on the Raspberry Pi.
- Prefer a multichannel I2S connection transported electrically over LVDS to a
  small adapter beside the Pi. Restore ordinary logic-level I2S only near the
  GPIO header.
- Preserve an eight-channel PCM design target. The specific six-pair parallel
  LVDS implementation and TI parts discussed are candidates, not frozen parts or
  a released wiring specification.

This decision does not approve the board's position above the PSU, mains design,
PCB dimensions, connector selection, Linux capture integration, or fabrication.
The intended division assumes one selected physical source at a time; concurrent
capture has not been requested or validated.

## Rationale and alternatives considered

- A selected S/PDIF stream over coax to a receiver beside the Pi was the earlier
  recommendation for standard ARC/optical/coax. It remains an option for a
  deliberately limited version, but cannot preserve uncompressed multichannel
  PCM from eARC. It was a discussion proposal, not an earlier accepted decision.
- Ordinary single-ended I2S over the enclosure cable would use fewer parts, but
  its timing, return paths and interference exposure require careful design.
  LVDS is preferred for the cable section; it does not make the complete board
  immune to noise or remove timing validation.
- A narrow vertical board high on the rear panel is the current placement
  proposal. Heat, airflow, AC-terminal separation and mechanical access remain
  unresolved, so placement is not frozen by this decision.

## Consequences

- The eARC multichannel path must not be forced through the WM8804/S/PDIF path.
  The WM8804 remains selected for an S/PDIF role under
  [decision 0001](0001-initial-enclosure-components.md); its necessity and exact
  role may be revisited when the HDMI receiver is selected.
- A custom cable/connector pinout, LVDS drivers and receivers, power/control
  wiring, and a Pi-side adapter are additional hardware work.
- Receiver clocks, source switching and Pi capture configuration must agree.
- eARC transport support does not establish Dolby/DTS codec support or Atmos
  object rendering. Advertised capabilities must match verified end-to-end
  playback.

## Evidence and follow-up

- [Manufacturer evidence register](../../hardware/electronics/notes/rear-input-evidence.md)
- [Candidate interface and integration questions](../reference/topics/digital-audio-input.md)
- [Placement and mechanical constraints](../reference/topics/rear-panel-interface.md)
- [PSU thermal constraints](../reference/topics/mean-well-uhp-500.md)

Prototype receiver-to-Pi capture, source transitions, PCM and supported compressed
payload handling before freezing the PCB and cutouts. Validate timing, powered
states, temperatures and interference in the closed enclosure under representative
sustained load. Resolve applicable manufacturer clearance guidance before treating
the arrangement as acceptable.

## Later requirement refinement

[Decision 0012](0012-require-lossless-audio-and-atmos.md) makes lossless TrueHD/DTS-HD and Atmos first-version requirements and confirms that all audio decoding/rendering/DSP stays on the Raspberry Pi. The rear electronics only extract, select and transport audio. Qualify receiver output packing, clocks and bit-preserving capture before finalizing the interconnect; Pi codec implementation remains separate work.
