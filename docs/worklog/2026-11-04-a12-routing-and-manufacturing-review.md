# A12 routing and manufacturing review

2026-11-04. The owner authorized routing and the work needed toward a final PCB. Implementation is preserved in hardware commit [`7ab8b66`](https://github.com/k3rnL/open-cinema-hardware/commit/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11). This record supersedes A11's **unrouted** status; it does not supersede the ARC-first decision or declare a manufacturing release.

## Delivered implementation

[A12 sources and exports](https://github.com/k3rnL/open-cinema-hardware/tree/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12) contain the routed four-layer PCB, schematic, BOM, Gerbers/drills, SMT placement data, stackup and pending bring-up/release criteria. The signal path remains ADV7511 ARC candidate → CS8416 optical1/optical2/coax/ARC selection → DS90LV047 three-pair link → future Pi HAT. The Pi owns capture/decoding/DSP and USB output to the amplifier.

A12 adds TPD1E10B06DYAR coax ESD clamping and selects the remaining passive MPNs and Samtec prototype headers. It adds continuous inner ground in the electronics region, outer fills, thermal/return vias and twelve independent 2.5 mm speaker conductors on both outer layers. No speaker negative is commoned. The exact stackup/impedance assumptions are in the hardware record; nominal LVDS geometry is a design calculation, not measured impedance/timing.

## Observed verification

- KiCad 10.0.5: **0 ERC violations, 0 DRC violations, 0 unrouted connections**.
- Two static passes by the same assistant: 423 electrical pad keys agree between exported schematic and PCB; 98 footprints and 92 model links checked. No independent engineer approval or powered test is claimed.
- The 228 × 39.8 × 1.6 mm outline, external connector positions and four Ø3 holes match A9. Current owner window remains 250 × 51 mm; no new assembled-enclosure test was performed.
- STEP/F3D each reimport as one component, 162 solids, zero child components, with matching geometry. They retain component-down installation coordinates, nominal seating z 67 mm, and contain no owner plate/L brackets or mains circuit.
- Native and review SMT position exports agree for 80 populated SMT references. Manufacturing package source hashes match the PCB used for the 3D export.
- The original manual KiCad project change was preserved outside the A12 commit. Existing owner Fusion documents and the linked cloud assembly were not saved/overwritten.

Canonical evidence: [verification](https://github.com/k3rnL/open-cinema-hardware/blob/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12/verification.md), [machine-readable checks](https://github.com/k3rnL/open-cinema-hardware/blob/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12/exports/review-two-passes.json), [Fusion checks](https://github.com/k3rnL/open-cinema-hardware/blob/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12/exports/fusion-check.json), [review package](https://github.com/k3rnL/open-cinema-hardware/blob/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12/manufacturing-review/README.md).

## Remaining gates

**Manufacturing release remains on hold.** ADV7511 eligible procurement and ARC-only/DD+ operation, CEC/TV compatibility, future HAT/capture timing and unchanged-payload tests, horizontal KLS clip current rating/supply, actual impedance, thermal/current/EMI/ESD and assembled tolerances are unresolved. The review package is not order approval. No supplier was contacted and no purchase made.

Header references: J20 TSW-106-07-G-D, J22 TSW-110-07-G-D, J21/J24 TSW-102-07-G-S. They are unkeyed prototype headers with generic KiCad envelope models; a retained/locking LVDS harness remains a separate task. Exact references do not imply live stock or JLC acceptance. [Sourcing](https://github.com/k3rnL/open-cinema-hardware/blob/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12/sourcing.md), [pending bring-up](https://github.com/k3rnL/open-cinema-hardware/blob/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12/bring-up.md).

A11 and earlier source files remain historical. The saved A12 PCB owns routing; do not run the old placement generator over it. Git publication does not automatically replace a Fusion cloud component.
