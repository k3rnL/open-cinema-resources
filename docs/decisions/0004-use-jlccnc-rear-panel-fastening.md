# Decision: Use JLCCNC-installed self-clinching nuts for the rear panel

- Status: Accepted for the next mechanical revision; fabrication unverified
- Date: 2026-11-03
- Owner: `@k3rnL`
- Related: [rear-panel reference](../reference/topics/rear-panel-interface.md),
  [fabrication guidance](../../manufacturing/rear-panel-fastening.md),
  [session record](../worklog/2026-11-03-jlccnc-rear-panel-fastening.md)

## Context

The removable rear panel must attach to bent tongues in the bottom chassis. The
joint should be serviceable and present flush screw heads on the exterior. The
owner chose to have JLCCNC supply and install the captive hardware instead of
pressing self-clinching nuts after delivery.

Native enclosure CAD is not yet in the repository, so this decision establishes
the fastening baseline rather than releasing a fabrication drawing.

## Decision

- Use **JLCCNC `S-M3-2` carbon-steel self-clinching nuts**, M3 x 0.5, supplied
  and installed by JLCCNC in the bent chassis tongues.
- Use **3.0 mm aluminium 5052** for the bottom chassis/tongues and the removable
  rear panel.
- Model each nut mounting hole at **diameter 4.25 mm**, following JLCCNC's
  fastener chart. Keep the hole centre at least **4.8 mm** from an edge; use a
  design target of at least **6 mm**, giving a tongue width of at least 12 mm
  and preferably 15 mm.
- Install each nut from the enclosure interior so that the tongue face contacting
  the rear panel remains flat and flush and the nut body is inside the enclosure.
- Fasten the panel with **M3 x 8 countersunk machine screws** conforming to
  ISO 10642 or DIN 7991. Use nominal **diameter 3.8 mm through holes** in the
  rear panel and a **90-degree countersink fitted to the actual screw head**.
- Use six fixing positions for an unsupported, flat, full-width rear panel: two
  near each side and two near the centre. Four positions are acceptable only if
  the cover captures the panel, a return flange stiffens it, or a prototype
  verifies adequate stiffness under connector insertion and removal loads.
- Submit the chassis, rear panel and installed hardware as one STEP assembly,
  with a separate 2D fastening drawing in JLCCNC's `Thread or Riveting File`
  field. Require confirmation of stock, orientation, fit and countersink before
  production.

The screw length is deliberately **M3 x 8**, not the earlier provisional
M3 x 6. The complete nominal stack contains a 3 mm rear panel and a 3 mm tongue;
M3 x 6 leaves insufficient margin for reliable thread engagement. Final tip
protrusion and internal clearance still require a CAD check.

This decision covers only the mechanical rear-panel joint. It does not select
connectors, electronics, mains components, protective-earth hardware or wiring.

## Alternatives considered

- **Owner-installed PEM hardware:** technically feasible with parallel press
  tooling, but rejected because JLCCNC can supply and install its stocked
  fasteners and control the mounting-hole/installation process.
- **PEM `S-M3-2ZI`:** used to establish the self-clinching approach. The released
  design will use JLCCNC's stocked `S-M3-2` geometry rather than assuming that an
  externally sourced PEM part will be accepted.
- **JLCCNC `CLA-M3-2` aluminium or `CLS-M3-2` stainless nuts:** available
  alternatives, but not selected. Carbon steel gives durable threads for a
  repeatedly removable panel; finish and corrosion compatibility remain part of
  the fabrication review.
- **Button-head screws:** simpler holes, but do not meet the preferred flush
  exterior. They remain a fallback if countersink quality or panel thickness is
  unsatisfactory.
- **Four fixings:** the owner's initial concept. It remains conditional on
  additional panel support or physical stiffness verification.

## Evidence

- [JLCCNC sheet-metal fastener chart](https://jlccnc.com/help/article/sheet-metal-fasteners-chart)
  lists `S-M3-2`, a 4.25 mm mounting hole and the available alternative material
  families.
- [JLCCNC sheet-metal fabrication guidelines](https://jlccnc.com/help/article/sheet-metal-fabrication-guidelines)
  describe the separate thread/riveting drawing upload and manual order review.
- [Fabrication baseline and inspection points](../../manufacturing/rear-panel-fastening.md)

No CAD fit check, fabricated sample, stiffness test or repeated-assembly test has
yet been performed.

## Consequences

- The tab geometry and rear-panel drawing now have concrete hole, material and
  hardware targets.
- The rear face can remain flush and the panel can be removed without access to a
  loose nut.
- The design depends on JLCCNC's current stocked fastener and successful manual
  DFM review. A supplier or fastener change requires rechecking the mounting hole
  and installation data.
- Six fixings add two tabs and two screws relative to the initial four-point idea,
  unless the enclosure supplies equivalent panel support.

## Follow-up

- Import the native enclosure CAD and apply this baseline to a named revision.
- Check bend access, nut press access, actual tongue edge/bend distances,
  countersink geometry, screw-tip clearance and assembly tolerances in CAD.
- Obtain JLCCNC DFM confirmation before payment.
- Inspect the first article for nut seating, flushness, rotation, panel fit and
  screw engagement; verify stiffness during representative connector handling.
- Coordinate any finish with the installed fasteners and validate corrosion and
  cosmetic behavior on the first article.
