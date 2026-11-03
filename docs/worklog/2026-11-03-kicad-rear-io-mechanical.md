# Work log: hardware repository and rear I/O mechanical draft

- Date: 2026-11-03
- Owner: @k3rnL; implementation and checks: Codex
- Source: Fusion `Rear Panel v4 / Sketch2`, two owner screenshots
- Hardware revision: A0-mechanical; KiCad 10.0.5
- Hardware source commit: [`3c61a7d`](https://github.com/k3rnL/open-cinema-hardware/commit/3c61a7dcd9b1f909dcdbf003cf7d56254bf6f54b)

## Owner request and evidence

The owner supplied a rear frame and free-space sketch. A separate connection
plate plus PCB will attach to that frame. The requested scope was a new hardware
repo, both checkouts in `Documents/Open Cinema`, and KiCad board shape and
connector placement only. Logic and LVDS are for later. The owner explicitly
confirmed six speaker pairs (12 contacts) plus the four audio inputs.

Retrieved the latest resources memory at `c36193f`, including the 3 mm aluminium
and JLCCNC fastening baseline. Read the active Fusion sketch without changes:
opening 210 × 25, R5; limits ±105 horizontally and 39…64 vertically, centre
height 51.5. Frame outer limits are ±130 and 0…80. The PSU-top reference is 33.
Units are mm. The sketch x direction is opposite the exterior rear-view x axis.

The six frame circles are Ø4.5, differing from the earlier nominal Ø3.8
through-hole baseline. Both are retained pending review; no sketch was altered.
The screenshots and geometry extraction are archived in the hardware repo.

## Work and result

Moved the complete resources checkout, including Git history, to the requested
folder. Created the sibling hardware repository with KiCad sources, local
libraries, placement data, STEP/DXF/SVG exports and a rendered preview.

A0 proposes a vertical 228 × 32 × 1.6 nominal board, R2 corners and four Ø3.2
holes outside the opening. Six speaker pairs are on the exterior rear left,
followed by optical 1, optical 2, coax and HDMI. Speaker channel roles remain open.
Because connector parts are unselected, their footprints are padless mechanical
envelopes. Body dimensions and the common 20 mm depth are allowances, not supplier
measurements. There are no electrical pads, schematic, routing, logic or LVDS.
The mains module remains separate and unplaced.

Native KiCad checks passed: closed outline, specified holes/placements, all
connector face envelopes inside the opening, no overlapping bodies, zero DRC
violations. A padless layout passing DRC is not electrical verification. STEP
imported into a temporary Fusion document as solid geometry; that document was
closed unsaved and the owner's original restored.

No full enclosure interference, actual connector fit, mating access, thermal or
electrical testing was done. The PCB bottom is only 4 mm above the sketch's PSU
top in projection; this is not approved clearance. Vertical PCB placement needs
appropriate normal-entry parts or a panel/daughterboard arrangement. Actual parts
may require revising the board, plate or number of PCBs.

## Links and next work

- [Hardware sources](https://github.com/k3rnL/open-cinema-hardware/tree/3c61a7dcd9b1f909dcdbf003cf7d56254bf6f54b/boards/rear-io)
- [Geometry and assumptions](https://github.com/k3rnL/open-cinema-hardware/blob/3c61a7dcd9b1f909dcdbf003cf7d56254bf6f54b/docs/rear-io-mechanical.md)
- [Verification scope](https://github.com/k3rnL/open-cinema-hardware/blob/3c61a7dcd9b1f909dcdbf003cf7d56254bf6f54b/docs/verification-A0.md)
- Choose parts before final footprints/cutouts/standoff lengths; reconcile the
  frame-hole discrepancy and check the full assembly before ordering.
