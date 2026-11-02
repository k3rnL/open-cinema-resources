# Open Cinema reference book

Last reviewed: 2026-11-03

This is the fast map of durable project knowledge. Topic pages summarize what the
project knows and link back to decisions, work logs, and original evidence.

## Start here

- [Project roadmap](../../ROADMAP.md)
- [Decision records](../decisions/README.md)
- [Work logs](../worklog/README.md)
- [Reference topic template](0000-template.md)

## Topics by domain

### Architecture and systems

- [Open Cinema software system](topics/open-cinema-software.md) — desired-state
  audio control plane, runtime ownership, supported platform, and current release
  boundary.
- [Enclosure and appliance system](topics/enclosure-appliance.md) — selected major
  components, system-level constraints, and unresolved integration work.

### Mechanical

- [Front-panel interface](topics/front-panel-interface.md) — candidate touch screen,
  encoder and power-button requirements, and unstarted local UI.
- [Rear-panel interface](topics/rear-panel-interface.md) — owner-supplied layout,
  connector needs, 80 mm height context, fastening candidates and provisional
  above-PSU board placement.

### Electronics

- [Raspberry Pi 5](topics/raspberry-pi-5.md) — selected computer and supported
  appliance target.
- [WM8804 S/PDIF transceiver](topics/wm8804.md) — selected digital-audio interface
  and lifecycle constraints.
- [WONDOM KAB9](topics/wondom-kab9.md) — selected configurable eight-channel
  amplifier.
- [MEAN WELL UHP-500](topics/mean-well-uhp-500.md) — selected power-supply family;
  24 V output selected and redundancy suffix still open.
- [Digital audio input and LVDS transport](topics/digital-audio-input.md) — eARC/ARC
  working direction, rear-to-Pi multichannel link, candidate parts and unvalidated
  capture/clocking details.
- [Auxiliary control electronics](topics/auxiliary-control-electronics.md) —
  delegated power, shutdown, IR and housekeeping functions; controller and firmware
  still undefined.

### Manufacturing and assembly

### Verification and testing

### Operations and maintenance

## Triage

No unclassified material.

## Known gaps

- Enclosure screenshots and orientation are recorded; native CAD, internal height
  datum, full dimensions, final materials and service clearances remain missing.
- The UHP-500 is confirmed as 24 V, but its `R`/non-`R` suffix, the Raspberry Pi
  board revision, and supporting 5 V conversion are not yet confirmed.
- The purchased Raspberry Pi fan has not been identified by model, mounting, or
  verified thermal performance.
- eARC/ARC receiver selection, documented control/CEC behavior, eight-channel Pi
  capture, supported encoded formats and the LVDS harness are not validated.
- WM8804 integration and KAB9 input/channel configuration remain unresolved; confirm
  whether the requested six speaker connections mean six pairs.
- Front/rear panel cutouts, connectors, auxiliary PCBs and local-screen software
  remain undesigned despite the captured requirements and working architecture.
- Above-PSU board placement needs thermal, airflow, EMI and mains-separation
  validation, including resolution of manufacturer adjacent-heat-source guidance.
- The hardware license has not yet been selected.

## Retrieval notes

Search aliases and older terminology when the preferred name is unknown. Treat
topic summaries as orientation; follow their evidence and decision links for
conclusions that matter.

