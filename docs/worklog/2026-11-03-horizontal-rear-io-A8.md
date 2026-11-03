# 2026-11-03 — Horizontal rear I/O fit experiment A8

The owner observed different connector projection depths in A7, requested a horizontal layout and explicitly required the speaker clips to solder to the horizontal PCB as well. [Decision 0011](../decisions/0011-horizontal-pcb-with-all-connectors.md) supersedes the vertical direction while retaining conventional clips, six active pairs, the 220 × 35 R5 opening, separate mains and four actual reference holes.

## Work and evidence

- Hardware revision: **f9e1e6c13e3d4213cc60600bce4dc70ce0d63df1**. [A8 design/source/verification record](https://github.com/k3rnL/open-cinema-hardware/blob/f9e1e6c13e3d4213cc60600bce4dc70ce0d63df1/docs/horizontal-assembly-A8.md).
- Main PCB becomes 228 × 39.8 × 1.6 mm, installed component side down at z 67 mm. All connectors directly solder to it; solder tails point upward. A7 and the optical daughterboard/cradle artifacts remain historical.
- Speaker candidate: two KLS L-KLS1-WP-6P-03B-B/R six-contact blocks, based on the manufacturer's right-angle drawing. **Current rating and exact retail supply unresolved.** RCA becomes RCJ-011; HDMI becomes10029449-001RLF. FCR684205R optical receivers are retained without daughterboards.
- Provisional 1.5 mm connection plate and two side supports preserve Ø3 reference holes at x±115,z 44/59. Four independent horizontal PCB holes are at x±110, depths 12/30. Hardware and tolerances are not selected.
- KiCad 10.0.5: zero DRC violations; 45 electrical pads, 10 NPTH holes; all pad centers on the board and model paths resolved; no nets or tracks.
- Rigid STEP/F3D each reimport as one component with 70 solids. A rigid joint using one reference hole moved all 70 together. All four reference-hole centers were checked.
- Read-only copies of the current Home Cinema v 7 rear frame and PSU show no modeled interference with the new plate/supports/assembly. Actual PSU top is z 35, correcting an older 33 mm assumption. Minimum nominal assembly/PSU distance is 2 mm; maximum assembly height 72.5 mm leaves 7.5 mm below an assumed 80 mm lid. No thermal/tolerance/safety qualification is implied. That temporary verification did not change user CAD; the subsequent authorized integration is described below.
- JLC RCJ-011 C4992678 was shown with 21 units in the public RCA catalogue at lookup. HDMI C428493 has an exact listing, but purchasable stock was not established. Other sourcing remains as stated in the A8 record. No supplier contact or purchase occurred.

## Remaining limits

The 0.2 mm board-front/plate gap and 0.4 mm nominal board/frame upper margin need tolerance review; nearby connector geometry is also close to the opening. The RCA shoulder is recessed 3 mm and the provisional 14 × 14 mm aperture must be checked with actual cable plugs. The KLS rating cannot be inferred from contact resistance or dielectric withstand specifications. Board current distribution, supports, samples, heat/airflow/EMI and all electronics remain unqualified.

Source screenshots are retained in hardware `mechanical/reference/2026-11-03-owner-A7-depth-side.png` and `2026-11-03-owner-A7-depth-top.png`. Manufacturer drawings, dated sourcing links, model provenance and check hashes are recorded in the pinned hardware revision. The inverted orientation and brackets are assistant-proposed fit details; only the horizontal/direct-solder direction was explicitly owner-selected.


## Authorized Fusion update — incomplete source save

The owner authorized updating the existing `rear-io-A5-assembly` cloud file and its linked assembly. The open source now contains 70 A8 bodies in its original coordinate frame. `Rear Panel Assembly` v 3 and `Home Cinema` v 8 finished saving; the parent uses a rigid as-built joint that does not depend on replaced connector faces.

The source itself remains modified at cloud v 2: Save calls produced no new version and the native Save confirmation was disabled. The open enclosure displays A8, but persistence after reopening is not verified. Original/current source backups reimported successfully with 135/70 bodies. Automatic approval review rejected closing the modified source without saving, even with those backups. It remains open; a same-file cloud revision is still pending. No ambiguous upload by name was attempted. See the pinned hardware record for coordinate conventions and recovery status.
