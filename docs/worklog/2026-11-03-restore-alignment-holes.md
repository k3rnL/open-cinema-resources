# Restore the plate alignment holes — A4

2026-11-03.

The owner clarified that the reference holes are needed to align the PCB model to the connection plate. Earlier A1–A3 choices to retain only drawing circles did not satisfy that workflow. The two latest owner centres remain **x−115,z44/59, Ø3 mm**, 15 mm apart. This supersedes only the graphics-only implementation in [the A3 record](2026-11-03-straight-speaker-terminals.md); final mounting hardware is still undecided.

A4 adds two real non-plated holes, HREF1/HREF2. Their centres were just outside the A3 board edge, so small R4 left tabs now support them. The main body stays228 ×32 ×1.6; overall width including tabs is233 mm. No mirrored right-hand holes were invented. All six connector footprints, positions, pads and models are unchanged from A3.

Native KiCad 10.0.5 DRC passes with zero violations. Board-only and assembly STEP imports both expose the two Ø3 cylindrical faces/circular edges at the exact coordinates for Fusion alignment. Source footprint hashes match A3. The assembly still imports as102 solid-body instances. No original frame CAD was modified and no mounting-strength or full enclosure test is claimed.

Hardware revision: [A4](https://github.com/k3rnL/open-cinema-hardware/commit/75377e706d041911d0f8f0661f29c19c44987acb). [Mechanical notes](https://github.com/k3rnL/open-cinema-hardware/blob/75377e706d041911d0f8f0661f29c19c44987acb/docs/rear-io-mechanical.md), [verification](https://github.com/k3rnL/open-cinema-hardware/blob/75377e706d041911d0f8f0661f29c19c44987acb/docs/verification-A4.md), [assembly STEP](https://github.com/k3rnL/open-cinema-hardware/blob/75377e706d041911d0f8f0661f29c19c44987acb/boards/rear-io/exports/rear-io-A4-assembly.step).

## A5 correction: both sides

The owner clarified: the alignment holes must be on **both sides**. A5 adds HREF3/HREF4 at x+115,z44/59, matching the existing left pair. There are now four Ø3 mm holes, 230 mm between left/right centres and 15 mm vertically. Four R4 tabs bring overall PCB width to238 mm; the main body and connector placements are unchanged. This supersedes A4's left-only interpretation, not the provisional status of the mounting hardware.

Native KiCad DRC passes with zero violations; all connector footprint hashes remain unchanged. Fusion imports of both assembly and board-only STEP expose four Ø3 cylindrical hole faces at the exact positions. Owner frame CAD was not changed.

[A5 hardware revision](https://github.com/k3rnL/open-cinema-hardware/commit/35a1c20e7d1ee435424c3fd0a4161c47114329d6), [STEP](https://github.com/k3rnL/open-cinema-hardware/blob/35a1c20e7d1ee435424c3fd0a4161c47114329d6/boards/rear-io/exports/rear-io-A5-assembly.step), [verification](https://github.com/k3rnL/open-cinema-hardware/blob/35a1c20e7d1ee435424c3fd0a4161c47114329d6/docs/verification-A5.md).
