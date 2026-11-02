---
title: Open Cinema software system
summary: Control plane that turns versioned desired audio graphs into a reconciled PipeWire/WirePlumber appliance runtime.
status: active
updated: 2026-11-02
tags: [architecture, software, audio, raspberry-pi]
aliases: [open-cinema, control-plane, audio-orchestrator]
sources:
  - https://github.com/k3rnL/open-cinema
  - https://github.com/k3rnL/open-cinema/commit/e52008996dd35fe645e2bd682e9c1d2a5277a0f1
  - https://github.com/k3rnL/open-cinema/blob/master/README.md
  - https://github.com/k3rnL/open-cinema/blob/master/docs/audio-orchestration/AUTHORING_AND_STATE.md
  - https://github.com/k3rnL/open-cinema/blob/master/docs/audio-orchestration/ORCHESTRATOR.md
  - https://github.com/k3rnL/open-cinema/blob/master/deployment/SUPPORTED_PLATFORMS.md
  - https://github.com/k3rnL/open-cinema/blob/master/docs/release-readiness/2026-08-27-open-cinema-v0.3.2-closure.md
---

# Open Cinema software system

## Summary

Open Cinema is the management and orchestration layer for a configurable home-
cinema audio appliance. It stores durable desired audio behavior, resolves that
intent against the devices and signal formats currently available, and safely
reconciles the result with the native Linux audio runtime.

## Confirmed facts

- The backend's authoritative version is `0.3.2`. This page was reviewed against
  `master` commit
  [`e5200899`](https://github.com/k3rnL/open-cinema/commit/e52008996dd35fe645e2bd682e9c1d2a5277a0f1)
  on 2026-11-02.
- Django owns the database-backed management API and the desired, resolved-history,
  and applied state. Redis carries bounded projections and wake-ups, not the
  authoritative audio state.
- The dedicated `open-cinema-orchestrator` process is the single owner of live
  reconciliation. PipeWire carries media and WirePlumber 0.5 remains the session
  manager; Open Cinema does not replace either one.
- WyrePlumber is the single runtime binding. CamillaDSP is a managed DSP processor,
  and PCM Auto Decoder exposes one stable adaptive PCM output for encoded or PCM
  inputs.
- Desired behavior progresses through distinct draft, immutable published,
  resolved-plan, and applied/runtime representations. Saving a draft does not
  change live audio.
- The management and on-box UI are maintained in the separate
  [`open-cinema-ui`](https://github.com/k3rnL/open-cinema-ui) repository.
- The currently supported appliance is a Raspberry Pi 5 Model B 8 GB running
  Raspberry Pi OS Lite/Debian 13 Trixie on AArch64. The accepted fixture uses
  PipeWire 1.4, WirePlumber 0.5, one decoder, and one CamillaDSP instance.
- The `v0.3.2` appliance closure functionally accepted TV S/PDIF/I2S input,
  adaptive decode, CamillaDSP, an eight-channel main output, Bluetooth programme
  input, and Bluetooth headset takeover/return on the provisioned fixture.

## Constraints

- The supported production boundary is the exercised Pi 5 8 GB Trixie fixture;
  other boards, memory tiers, distributions, and 32-bit systems remain outside the
  claim.
- Fresh-image installation, arbitrary upgrade paths, and full quantitative
  latency, thermal, resource, transition-gap, and soak campaigns remain open.
- Saved endpoint intent must use stable evidence rather than transient PipeWire
  numeric object IDs.

## Evidence

- [Main software repository](https://github.com/k3rnL/open-cinema)
- [Software overview](https://github.com/k3rnL/open-cinema/blob/master/README.md)
- [Desired-state model](https://github.com/k3rnL/open-cinema/blob/master/docs/audio-orchestration/AUTHORING_AND_STATE.md)
- [Orchestrator lifecycle](https://github.com/k3rnL/open-cinema/blob/master/docs/audio-orchestration/ORCHESTRATOR.md)
- [Supported platform matrix](https://github.com/k3rnL/open-cinema/blob/master/deployment/SUPPORTED_PLATFORMS.md)
- [Open Cinema 0.3.2 appliance closure](https://github.com/k3rnL/open-cinema/blob/master/docs/release-readiness/2026-08-27-open-cinema-v0.3.2-closure.md)

## Open questions

- Which software repository documents should be mirrored or summarized here as
  the hardware design evolves?
- Which hardware identifiers and connector definitions should become stable
  endpoint evidence in the production enclosure?

## Related

- [Enclosure and appliance system](enclosure-appliance.md)
- [Raspberry Pi 5](raspberry-pi-5.md)
- [WM8804 S/PDIF transceiver](wm8804.md)
- [WONDOM KAB9 amplifier](wondom-kab9.md)
