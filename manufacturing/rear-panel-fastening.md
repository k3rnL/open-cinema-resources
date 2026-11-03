# Rear-panel fastening fabrication baseline

- Status: design baseline; not released for fabrication
- Date: 2026-11-03
- Related decision:
  [0004: Use JLCCNC-installed self-clinching nuts](../docs/decisions/0004-use-jlccnc-rear-panel-fastening.md)
- Scope: removable rear-panel mechanical attachment only

## Joint definition

| Element | Baseline |
| --- | --- |
| Bottom chassis and bent tongues | Aluminium 5052, 3.0 mm |
| Rear panel | Aluminium 5052, 3.0 mm |
| Captive fastener | JLCCNC `S-M3-2`, carbon steel, M3 x 0.5 |
| Quantity | Six for a flat, unsupported full-width panel |
| Nut mounting hole | Diameter 4.25 mm |
| Minimum nut-hole centre to edge | 4.8 mm supplier minimum; 6 mm design target |
| Tongue width | 12 mm minimum at the hole; 15 mm preferred |
| Panel clearance hole | Nominal diameter 3.8 mm through |
| Panel countersink | 90 degrees, fitted to the actual screw head and made flush |
| Removable screw | ISO 10642 or DIN 7991, M3 x 8, countersunk |

M3 x 8 is the baseline for the nominal 3 mm panel plus 3 mm tongue stack. Check
the exact selected screw, nut thread location, finish thickness and free volume
behind every fixing in CAD. A shorter screw may not provide adequate engagement;
a longer screw must not contact internal parts or wiring.

## Installation orientation

- JLCCNC supplies and installs the self-clinching nuts.
- Install from the enclosure interior.
- Keep the rear-facing surface of every tongue flat and flush for direct contact
  with the rear panel.
- Keep the protruding nut body inside the enclosure.
- Do not substitute a rivet nut/nutsert that leaves a rear-facing flange or gap.

## Fixing layout

For a flat panel spanning the enclosure width, use two fixings near each side and
two near the centre. Four fixings may be used only when the top cover captures the
panel, a return flange provides equivalent stiffness, or a representative
prototype passes the handling check.

Keep holes clear of bend-distorted regions. The 6 mm edge-distance design target
does not replace JLCCNC's bend-distance and tooling-access review.

## JLCCNC drawing callout

```text
REAR-PANEL FASTENING ONLY

SUPPLY AND INSTALL:
6x S-M3-2 SELF-CLINCHING NUT, M3 x 0.5
MOUNTING HOLE DIA 4.25 mm
INSTALL FROM ENCLOSURE INTERIOR
REAR-FACING TONGUE SURFACE MUST REMAIN FLAT AND FLUSH

REAR PANEL:
6x DIA 3.8 mm THRU
90 DEG COUNTERSINK TO SUIT ISO 10642 / DIN 7991 M3 SCREW
SCREW HEAD FLUSH WITH EXTERIOR PANEL SURFACE

ASSEMBLY SCREW BASELINE: M3 x 8

CONFIRM FASTENER STOCK, INSTALLATION ORIENTATION,
COUNTERSINK FIT AND ASSEMBLY ALIGNMENT BEFORE PRODUCTION
```

Submit one STEP assembly containing the chassis, rear panel and captive nuts.
Upload a separate 2D drawing with the callouts above in the order's
`Thread or Riveting File` field. JLCCNC's published fastener dimensions are
reference values and final availability is subject to its manual review.

## First-article checks

- All nuts are fully seated and do not rotate under normal screw installation.
- Rear-facing tongue surfaces remain flat; no nut or displaced material holds the
  panel away from a tongue.
- The panel fits without forcing all six screws into alignment.
- Screw heads sit flush without an oversized, sharp or visibly off-centre
  countersink.
- Each screw achieves useful thread engagement without bottoming or contacting an
  internal item.
- Repeated removal and refitting does not loosen a nut or visibly deform the
  panel.
- The assembled panel remains acceptably stiff during representative connector
  insertion and removal. This is a mechanical handling check only; connector
  selection is outside this document.

## Exclusions and unresolved inputs

This baseline does not cover connector cutouts, electronic boards, mains
components, protective-earth hardware, wiring, shielding or electrical safety.
Native CAD, final finish and measured connector loads are still missing. Do not
release a fabrication package until those mechanical fit inputs and JLCCNC DFM
feedback have been reconciled.

## Supplier references

- [JLCCNC sheet-metal fastener chart](https://jlccnc.com/help/article/sheet-metal-fasteners-chart)
- [JLCCNC sheet-metal fabrication guidelines](https://jlccnc.com/help/article/sheet-metal-fabrication-guidelines)
