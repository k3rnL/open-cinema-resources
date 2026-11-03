# Work log: JLCCNC rear-panel fastening selection

- Date: 2026-11-03
- Contributors: `@k3rnL` (fabrication preference and acceptance), Codex
  (supplier-document review and mechanical recommendation)
- Related revision: enclosure discussed as Home Cinema v5; native CAD not imported
- Type: design discussion and supplier-document review; no physical experiment
- Related: [decision 0004](../decisions/0004-use-jlccnc-rear-panel-fastening.md),
  [fabrication baseline](../../manufacturing/rear-panel-fastening.md)

## Objective

Choose a rear-panel fastening method that can be fabricated entirely by JLCCNC,
without owner-installed self-clinching hardware. Retain only the mechanical
rear-panel joint from the discussion.

## Setup

- Proposed host material: 3.0 mm aluminium 5052 sheet.
- Joint: removable flat rear panel against bent tongues in the bottom chassis.
- Supplier sources: JLCCNC sheet-metal fastener chart, fabrication guidelines and
  supported-process documentation as available on 2026-11-03.
- No native CAD, physical parts or measured connector loads were available.

## Actions

- Confirmed that JLCCNC advertises riveting/self-clinching processing and a
  dedicated `Thread or Riveting File` upload.
- Read the JLCCNC fastener chart and selected its stocked `S-M3-2` M3 x 0.5
  carbon-steel nut with a 4.25 mm mounting hole.
- Defined a flush countersunk panel joint and reviewed the screw length against
  the complete nominal panel-and-tongue stack.
- Separated fastening information from the rear-panel electronics discussion.

## Observations

- JLCCNC's chart lists `S-M3-2`, `CLS-M3-2` and `CLA-M3-2` families with a
  nominal 4.25 mm mounting hole; final stock remains subject to factory review.
- The `S-M3-2` table gives a 4.8 mm minimum hole-centre-to-edge distance and a
  minimum host-sheet thickness below the proposed 3.0 mm sheet.
- A nominal M3 x 6 countersunk screw spans only the combined 3 mm rear panel and
  3 mm tongue thickness. It does not provide comfortable engagement margin in
  the installed nut.
- A flat, full-width panel has no confirmed central support in the available
  screenshots.

## Interpretation

- JLCCNC should control the mounting hole and nut installation rather than the
  owner attempting a post-delivery press operation.
- `S-M3-2` provides the preferred durable steel thread for a serviceable panel.
- M3 x 8 is the appropriate baseline screw length, subject to CAD confirmation of
  thread engagement, tip protrusion and internal clearance.
- Six fixing positions are preferred for a flat unsupported panel. Four remain
  conditional on a captured edge, a stiffening return or physical verification.

## Evidence

- [JLCCNC sheet-metal fastener chart](https://jlccnc.com/help/article/sheet-metal-fasteners-chart)
- [JLCCNC sheet-metal fabrication guidelines](https://jlccnc.com/help/article/sheet-metal-fabrication-guidelines)

## Next steps

- Apply the fastening baseline to imported native CAD and a named revision.
- Submit the STEP assembly and 2D riveting drawing for JLCCNC manual DFM review.
- Inspect and handling-test the first fabricated article before releasing the
  joint as verified manufacturing guidance.
