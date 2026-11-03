# 0005: Separate hardware repository and KiCad

- Date: 2026-11-03
- Status: Accepted organization and mechanical-study scope
- Owner: @k3rnL

Create `k3rnL/open-cinema-hardware` for editable hardware implementation,
beginning with a KiCad rear connector board. Both checkouts live in
`Documents/Open Cinema`; the existing resources checkout is relocated there.
Resources retains the reference book, research, decisions and historical evidence.
Link new hardware sources instead of duplicating them in resources.

The owner has drawn a rear frame accepting a separate connection plate and PCB.
The first PCB task covers shape and connector placement only; input logic and
LVDS electronics are deferred. The owner confirmed six speaker pairs (12 spring
contacts), plus optical ×2, coax and HDMI on the connector strip. The mains
inlet/switch remains a separate panel assembly.

KiCad supplies editable PCB sources and STEP supplies exchange with Fusion.
The A0 board size, hole pattern and connector envelopes are proposals, not a
selection of commercial connectors or approval of final plate cutouts, mounting
depth, circuitry or fabrication. Existing resource artifacts remain in place.

Evidence: [session](../worklog/2026-11-03-kicad-rear-io-mechanical.md),
[hardware repository](https://github.com/k3rnL/open-cinema-hardware).
