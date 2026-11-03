# Rear connector selection and KiCad A1

Date: 2026-11-03. Hardware implementation: [open-cinema-hardware A1, commit 1572164](https://github.com/k3rnL/open-cinema-hardware/commit/1572164741b85f3490ec4d7c0763b48538fe5d90).

## Owner input

Requested actual obtainable connectors, footprints and 3D models in the existing rear-panel opening. Supplied an updated fixing sketch and stated mounting points are references only. Explicitly answered: "Keep the vertical PCB; use small optical daughterboards."

The screenshot and read-only `Rear Panel v4 / Sketch3` extraction are archived once in hardware's [mechanical/reference](https://github.com/k3rnL/open-cinema-hardware/tree/main/mechanical/reference). The opening remains 210 × 25 R5, z39…64. The new reference holes are Ø3 at x−110,z44/59. Sketch3's x basis is direct world x, unlike the older Sketch2 basis. The current frame model reads 2 mm thick, while the accepted fabrication baseline says 3 mm: unresolved. Existing frame-hole Ø4.5 versus nominal Ø3.8 baseline also remains unresolved.

## Implementation and findings

- Chosen references: six Phoenix 1732496, two Cliff FCR684205R, one Same Sky RCJ-021, one Amphenol FCI 10078837-001LF. [Source register and sourcing](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/connector-selection-A1.md).
- Main board remains vertical 228 × 32 × 1.6. It receives two clearance windows for the two 16 × 24 × 1.6 horizontal optical boards. Receiver footprints are in a separate KiCad project. No interboard connector or retention design was invented.
- Replaced generic main-board connector envelopes with actual electrical footprints for speaker/RCA/HDMI and mechanical instances of the complete optical assemblies. Removed the four proposed A0 mounting holes; added only the owner's two reference graphics.
- Copied the KiCad Phoenix model and derived its footprint with Ø1.2 manufacturer drill sizes. Built the other models from manufacturer drawings, recording simplifications. No vendor CAD download or vendor model certification is claimed.
- KiCad 10.0.5 loads both boards; native DRC reports zero violations. An independent check confirms pad counts, positions, models and nominal projected fit. No nets or tracks exist, so DRC is not electrical validation.
- Full STEP imports into temporary Fusion as 88 solid-body instances. The owner's original document was restored unchanged. No full enclosure interference or physical test was performed.
- Optical module top tab has only 0.5 mm nominal opening margin. The receiver is 16 Mbit/s, sufficient by rate budget for 96 kHz stereo PCM, not 192 kHz. Speaker terminals are industrial green spring types, not red/black consumer clips.

## Remaining work

Choose plate thickness/setback, fastening and daughterboard supports/interconnect; check full enclosure, plugs and tool access, tolerances and board stiffness. Review HDMI pad stack/pin-in-paste stencil before fabrication. Implement/validate input reception, eARC/ARC, supply/protection, source switching, LVDS and Pi capture later. No purchases, prototype, electrical test or fabrication release occurred.

Decision: [0006](../decisions/0006-vertical-carrier-and-optical-daughterboards.md). Verification: [hardware A1 report](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/verification-A1.md).
