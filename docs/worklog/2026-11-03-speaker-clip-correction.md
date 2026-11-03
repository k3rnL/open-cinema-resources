# Speaker clip correction and A2 fit study

2026-11-03.

**Historical A2:** subsequently rejected for downward pins near the PSU. See [A3 correction](2026-11-03-straight-speaker-terminals.md); the actual updated opening also supersedes the upper-hole conflict below.

The owner rejected A1's industrial speaker terminals and supplied a [photo of conventional red/black clips](../../hardware/electronics/notes/speaker-clips-owner-reference.png). The owner then allowed increasing the opening from 210 × 25 to about 210 × 35 mm upward. [Decision 0007](../decisions/0007-use-conventional-speaker-clips.md).

A2 uses two KLS **L-KLS1-WP-6P-03B-B/R** blocks as mechanical candidates: 52 × 30 front size each, six contacts each, twelve independent contacts total. They are panel-supported mechanical instances in KiCad with project-authored models derived from the manufacturer's V1 drawing. No fake main-PCB solder pads were added for the right-angle tails. Direct insulated wiring to the amplifier is proposed; support, strain relief and termination remain open.

The vertical input board is shortened to **99 × 32 × 1.6 mm** beside the clips. Optical assemblies, RCA, HDMI and optical child boards remain unchanged. No decoding or LVDS circuitry was added. The original frame CAD was not edited.

Validation: native KiCad 10.0.5 DRC reports zero violations; closed outline/windows and nominal front-envelope fit checked. The A2 STEP imports into Fusion as 96 solid-body instances. Full-width native renders inspected. These checks do not establish electrical function or full enclosure fit.

Open: KLS drawing lacks an operating current rating; confirm before purchase. Enlarging the opening to z74 intersects original Ø4.5 upper frame fixings at x±40,z75. Speaker tails reach z36 below the opening bottom39, requiring frame/PSU depth and insulation checks. Frame changes, attachment and panel cutouts remain unfinished.

Implementation: [A2 mechanical notes](https://github.com/k3rnL/open-cinema-hardware/blob/779d95c3889d94193dccc8718139f433efac4941/docs/rear-io-mechanical.md), [verification and source hashes](https://github.com/k3rnL/open-cinema-hardware/blob/779d95c3889d94193dccc8718139f433efac4941/docs/verification-A2.md), [source drawings and part research](https://github.com/k3rnL/open-cinema-hardware/blob/779d95c3889d94193dccc8718139f433efac4941/docs/speaker-clips-correction.md). Historical A1 exports and rejection rationale are retained.

Hardware revision: [`779d95c`](https://github.com/k3rnL/open-cinema-hardware/commit/779d95c3889d94193dccc8718139f433efac4941).
