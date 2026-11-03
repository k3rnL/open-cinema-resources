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
  connector needs, 80 mm height context, accepted JLCCNC fastening baseline and
  provisional above-PSU board placement.

### Electronics

- [Hardware repository and KiCad mechanical PCB](topics/hardware-repository-and-kicad.md)
  — implementation checkout, rear connector fit study, STEP exports and unselected parts.

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

- Enclosure screenshots and orientation are recorded; a measured rear-frame sketch
  snapshot and KiCad placement study are now in hardware. Full assembly CAD,
  internal height datum and service clearances remain missing. The rear-panel
  fastening material/hardware baseline is selected but not CAD- or
  first-article-verified.
- The UHP-500 is confirmed as 24 V, but its `R`/non-`R` suffix, the Raspberry Pi
  board revision, and supporting 5 V conversion are not yet confirmed.
- The purchased Raspberry Pi fan has not been identified by model, mounting, or
  verified thermal performance.
- eARC/ARC receiver selection, documented control/CEC behavior, eight-channel Pi
  capture, supported encoded formats and the LVDS harness are not validated.
- WM8804 integration and KAB9 input/channel configuration remain unresolved.
  Six speaker pairs are confirmed; roles and terminal parts remain open.
- A0 rear PCB shape/placements are a mechanical study with connector envelopes.
  Actual parts, final plate cutouts, circuitry, front panel and local-screen
  software remain open. Frame holes (Ø4.5) differ from the nominal Ø3.8 fastening
  baseline and require reconciliation.
- Above-PSU board placement needs thermal, airflow, EMI and mains-separation
  validation, including resolution of manufacturer adjacent-heat-source guidance.
- The hardware license has not yet been selected.

## Retrieval notes

Search aliases and older terminology when the preferred name is unknown. Treat
topic summaries as orientation; follow their evidence and decision links for
conclusions that matter.

