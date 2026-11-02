# Work log: Rear panel and digital-audio architecture

- Recorded: 2026-11-03
- Contributors: `@k3rnL` (requirements, CAD screenshots, preferences), Codex
  (research and architecture recommendations)
- Related revision: enclosure discussed as Home Cinema v5; screenshots only,
  native CAD/source revision not imported
- Type: design discussion and source review; no hardware experiment
- Related: [rear panel](../reference/topics/rear-panel-interface.md),
  [audio input](../reference/topics/digital-audio-input.md),
  [decision 0003](../decisions/0003-prefer-earc-and-lvds-input-architecture.md)

## Objective and provenance

Retain the rear-panel discussion and its evolution as searchable project memory.
The evidence is the owner's conversation, the two supplied enclosure views and
the manufacturer sources linked below. This log summarizes requirements and
useful rationale; it is not a verbatim transcript or a measured test report.

## Owner-supplied observations and preferences

- The PSU spans the rear; the Pi/electronics stack and amplifier are at the front.
  The owner explicitly corrected the earlier interpretation of their placement.
- The second supplied screenshot is a view from the front. The top view therefore
  has rear at the top, Pi at lower left and amplifier at lower right.
- The owner stated: "80mm height total. That let 50mm for connectors". The internal
  versus external datum and the PSU-to-panel gap remain unspecified.
- The bottom sheet is contemplated at 2 or 3 mm to help dissipate PSU heat; the
  rear is expected to be laser-cut sheet with fixing tabs. Self-clinching nuts
  were requested as a fastening option.
- Requested rear interfaces: mains inlet/switch, two optical inputs, one coaxial
  input, one HDMI ARC input and "spring clips for speaker, 6".
- Asked whether to perform input reception/conversion on the rear board and carry
  signals to the Pi, given proximity to the PSU.
- When asked ARC versus eARC, answered "most compatible".
- After the LVDS explanation, stated that the approach "looks great" and confirmed
  understanding of the input board delivering I2S through LVDS.
- Requested that this knowledge be organized into the project resources using
  the memory skill.

## Evolution and classification

1. Rear connector positioning was reframed after the orientation correction.
   The upper space above the PSU is a placement candidate, not verified clearance.
2. For standard ARC/optical/coax, the initial recommendation was rear source
   selection followed by S/PDIF over coax to a WM8804 beside the Pi and short I2S.
3. The broad-compatibility preference led to an eARC-plus-ARC target. A common
   S/PDIF-only link would constrain uncompressed multichannel PCM, so the working
   recommendation changed to multichannel I2S transported over LVDS.
4. Rear reception/selection, LVDS transport and a Pi-side adapter became the
   accepted working direction in [decision 0003](../decisions/0003-prefer-earc-and-lvds-input-architecture.md).
   The specific ICs, cable, GPIO allocation and board dimensions are candidates.
5. The discussion separated cable interference immunity from power/ground noise,
   heat, airflow and mains separation. None was tested. Above-PSU placement remains
   conditional on resolving those constraints and manufacturer guidance.

This does not supersede the original major-component or 24 V decisions. The
WM8804's continued role is an open integration question, not a silent replacement.

## Corrections and limits retained

- Rear exterior left/right is reversed relative to the owner's front view.
- The estimated 50 mm band is gross packaging space, not usable PCB height or a
  certified safety/thermal clearance. The suggested 30-35 mm PCB is provisional.
- The LVDS link uses a custom internal pinout. Commercial "I2S over HDMI" examples
  are not HDMI ARC/eARC receivers or universally compatible eight-channel links.
- The parallel six-pair proposal differs from the serialized LVDS application-note
  example; both demonstrate the same broad electrical transport idea.
- eARC reception does not guarantee decoding of every compressed codec or
  object-audio format. The existing software fixture is not evidence of this new
  eight-channel capture implementation.
- Earlier M3 x 6 screw suggestions were not checked against the complete joint.
  Retain the screw families and PEM reference as candidates; derive length after
  the panel/tab/nut stack is known. Marketplace variants were not qualified.

## Evidence

- [Original top and front-perspective screenshots, names and checksums](../../hardware/mechanical/enclosure-layout/README.md)
- [Manufacturer evidence register](../../hardware/electronics/notes/rear-input-evidence.md)
- [Existing software boundary](../reference/topics/open-cinema-software.md)

No CAD was edited and no schematic, PCB, purchasing, new firmware, physical
measurement, EMI test or thermal test was performed in this session.

## Next evidence needed

- Native CAD and actual packaging/clearance measurements, final connector choices
  and confirmation of six speaker pairs.
- An obtainable and documented eARC/ARC receiver, its output/clock/voltage details,
  controller requirements and supported-format declarations.
- Demonstrated Pi capture, source switching, PCM channel mapping and preservation
  of supported encoded payloads with the proposed link.
- Harness/PCB timing checks and representative closed-enclosure load, thermal,
  interference and mains-integration review; resolution of manufacturer guidance.
