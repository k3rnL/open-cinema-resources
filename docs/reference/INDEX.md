# Open Cinema reference book

Last reviewed: 2026-11-02

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
- [Auxiliary control electronics](topics/auxiliary-control-electronics.md) — input
  front-end and delegated power, shutdown, and IR-control functions still to be
  designed.

### Mechanical

- [Enclosure and appliance system](topics/enclosure-appliance.md) — current layout,
  thermal, safety, and serviceability context.
- [Front-panel interface](topics/front-panel-interface.md) — candidate touch screen,
  encoder and power-button requirements, and unstarted local UI.

### Electronics

- [Raspberry Pi 5](topics/raspberry-pi-5.md) — selected computer and supported
  appliance target.
- [WM8804 S/PDIF transceiver](topics/wm8804.md) — selected digital-audio interface
  and lifecycle constraints.
- [WONDOM KAB9](topics/wondom-kab9.md) — selected configurable eight-channel
  amplifier.
- [MEAN WELL UHP-500](topics/mean-well-uhp-500.md) — selected power-supply family;
  24 V output selected and redundancy suffix still open.
- [Front-panel interface](topics/front-panel-interface.md) — Waveshare display
  candidate and unresolved controls/integration.
- [Auxiliary control electronics](topics/auxiliary-control-electronics.md) —
  unimplemented input and power/control board functions.

### Firmware

- [Front-panel interface](topics/front-panel-interface.md) — local display software
  has not started.
- [Auxiliary control electronics](topics/auxiliary-control-electronics.md) —
  delegated controller firmware and host protocol remain undefined.

### Manufacturing and assembly

### Verification and testing

### Operations and maintenance

## Triage

No unclassified material.

## Known gaps

- Enclosure CAD, target dimensions, materials, mounting, and service clearances are
  not yet imported.
- The UHP-500 is confirmed as 24 V, but its `R`/non-`R` suffix, the Raspberry Pi
  board revision, and supporting 5 V conversion are not yet confirmed.
- The purchased Raspberry Pi fan has not been identified by model, mounting, or
  verified thermal performance.
- The WM8804 carrier/interface implementation and KAB9 input/channel configuration
  are not yet recorded.
- The front panel, encoder, power button, rear panel, connectors, auxiliary boards,
  and local-screen software are not yet designed.
- Wiring, connectors, mains safety, thermal validation, and regulatory constraints
  remain to be defined.
- The hardware license has not yet been selected.

## Retrieval notes

Search aliases and older terminology when the preferred name is unknown. Treat
topic summaries as orientation; follow their evidence and decision links for
conclusions that matter.

