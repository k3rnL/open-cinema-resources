# Straight speaker terminals and A3 fit study

2026-11-03.

The owner rejected A2's downward speaker tails near the PSU and supplied a 220 × 35 R5 opening. [Decision 0008](../decisions/0008-require-straight-speaker-terminals.md). Read-only Fusion measurement confirms z34…69 and reference fixings x−115,z44/59. The original screenshot and measured snapshot have one canonical home in [hardware evidence](https://github.com/k3rnL/open-cinema-hardware/tree/d5228f5392d0190ffe00a72066b3816928dcd31a/mechanical/reference). No owner CAD was modified.

A3 uses **two Dragon City PT-603B** six-contact blocks, straight rear-facing pins through a **228 × 32 × 1.6 vertical PCB**. The drawing shows 30 mm body height, 13 mm contact-column pitch, 19.5 mm row spacing and 3.4 mm pin projection behind the seating plane. The project reconstructs STEP geometry and a provisional footprint. Signal drill size, pin thickness, ear envelope and numbering include explicit project assumptions. Manufacturer current rating and small-quantity supply are unconfirmed; no purchase or supplier enquiry was made.

Optical inputs retain their two horizontal daughterboards; RCA and HDMI are unchanged. No nets, tracks, schematic, decoder, LVDS or speaker distribution were added. Owner frame points remain graphics; four component NPTH holes are separate provisional speaker fixings. Supports, plate setback/apertures, harness and thermal/electrical clearance remain unfinished.

Native KiCad 10.0.5 DRC returns zero violations with recorded defaults; no nets exist, so this is not circuit validation. Closed outline/windows, 41 electrical pads plus four component NPTH, model paths and nominal front-envelope fit were checked. The STEP reimported into an unsaved Fusion document as 102 solid-body instances; native front/oblique renders were inspected. The original frame document was restored unchanged. This is not a full enclosure collision test.

The owner opening top69 is 3.75 mm below the upper frame-hole edges72.75, resolving A2's assumed opening intersection. The main PCB bottom37 remains only 4 mm above the old PSU-top line33 in projection; actual depth and insulation are unresolved.

Implementation: [A3 selection and assumptions](https://github.com/k3rnL/open-cinema-hardware/blob/d5228f5392d0190ffe00a72066b3816928dcd31a/docs/connector-selection-A3.md), [mechanical geometry](https://github.com/k3rnL/open-cinema-hardware/blob/d5228f5392d0190ffe00a72066b3816928dcd31a/docs/rear-io-mechanical.md), [verification](https://github.com/k3rnL/open-cinema-hardware/blob/d5228f5392d0190ffe00a72066b3816928dcd31a/docs/verification-A3.md). Hardware revision: [A3](https://github.com/k3rnL/open-cinema-hardware/commit/d5228f5392d0190ffe00a72066b3816928dcd31a).

A2 sources/exports and [rejected approach](2026-11-03-speaker-clip-correction.md) remain historical. Current procurement and fabrication qualification are still open.
