# Restore the plate alignment holes — A4

2026-11-03.

The owner clarified that the reference holes are needed to align the PCB model to the connection plate. Earlier A1–A3 choices to retain only drawing circles did not satisfy that workflow. The two latest owner centres remain **x−115,z44/59, Ø3 mm**, 15 mm apart. This supersedes only the graphics-only implementation in [the A3 record](2026-11-03-straight-speaker-terminals.md); final mounting hardware is still undecided.

A4 adds two real non-plated holes, HREF1/HREF2. Their centres were just outside the A3 board edge, so small R4 left tabs now support them. The main body stays228 ×32 ×1.6; overall width including tabs is233 mm. No mirrored right-hand holes were invented. All six connector footprints, positions, pads and models are unchanged from A3.

Native KiCad 10.0.5 DRC passes with zero violations. Board-only and assembly STEP imports both expose the two Ø3 cylindrical faces/circular edges at the exact coordinates for Fusion alignment. Source footprint hashes match A3. The assembly still imports as102 solid-body instances. No original frame CAD was modified and no mounting-strength or full enclosure test is claimed.

Hardware revision: [A4](https://github.com/k3rnL/open-cinema-hardware/commit/75377e706d041911d0f8f0661f29c19c44987acb). [Mechanical notes](https://github.com/k3rnL/open-cinema-hardware/blob/75377e706d041911d0f8f0661f29c19c44987acb/docs/rear-io-mechanical.md), [verification](https://github.com/k3rnL/open-cinema-hardware/blob/75377e706d041911d0f8f0661f29c19c44987acb/docs/verification-A4.md), [assembly STEP](https://github.com/k3rnL/open-cinema-hardware/blob/75377e706d041911d0f8f0661f29c19c44987acb/boards/rear-io/exports/rear-io-A4-assembly.step).
