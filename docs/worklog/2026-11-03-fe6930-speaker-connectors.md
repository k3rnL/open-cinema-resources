# A7 — FE6930 speaker connectors and two spare pairs

2026-11-03. Owner authorized two spare speaker pairs after confirming 4 Ω or mixed/unknown speaker loads. [Decision 0010](../decisions/0010-select-cliff-fe6930-and-two-spare-pairs.md).

## Implementation

Hardware revision **eae54aa79c94255bdad5aaae5bf087d2b4166b0e** replaces both PT-603B blocks with Cliff FE6930. The native KiCad main PCB uses part-specific drawing-derived footprints and a project-reconstructed STEP model. There are sixteen speaker contacts: six proposed working pairs and two spares, all electrically independent. Production pad/slot qualification is still pending.

SP1/SP2 centres: x−77/−11,z52. Optics: x32/52,z50.5; RCA/HDMI: x69/91,z51.5. The A6 bolted optical cradle and daughterboards are retained, translated 4 mm right. Main outline and four Ø3 holes at x±115,z44/59 remain unchanged. Owner enclosure CAD was not edited.

## Observed evidence

- [Cliff product specification](https://www.cliffusa.com/products/springterminals/multi.htm) and visually inspected [issue2 drawing](https://www.cliffuk.co.uk/products/springterminals/FE6930.pdf): 7 A at 60 V AC, 65 mm overall width including ears,30 mm flange height, straight rear tags. Drawing is linked rather than republished.
- [DigiKey 4654-FE6930-ND](https://www.digikey.com/en/products/detail/cliff-electronic-components-ltd/FE6930/25552004) retrieved page showed active and151 in stock, minimum1; web page may be cached. This is not a reservation or JLC stock claim.
- KiCad10.0.5 native main/child DRC: zero violations within a mechanical design with no nets/routes. Main has 45 electrical pads and 12 NPTH holes. Child source unchanged from A6.
- Fusion exact-solid projection checks fit connector bodies inside220×35 R5. No new speaker/neighbour or cradle/assembly intersection was found.
- Rigid STEP and F3D contain135 solid root bodies with no child occurrences. F3D reimport passed; a temporary joint using HREF1 moved all 135 bodies with one transform. All four alignment holes were measured.
- Left speaker ear has only 0.5 mm nominal aperture clearance; inter-block ear gap1 mm; approximately 0.4 mm inherited RCA/cradle gap remains. Real tolerances and plug/finger access were not tested.

## Exact implementation evidence

- [A7 selection, footprint assumptions and pair mapping](https://github.com/k3rnL/open-cinema-hardware/blob/eae54aa79c94255bdad5aaae5bf087d2b4166b0e/docs/connector-selection-A7.md)
- [A7 sourcing](https://github.com/k3rnL/open-cinema-hardware/blob/eae54aa79c94255bdad5aaae5bf087d2b4166b0e/docs/sourcing-A7.md)
- [A7 verification and source hashes](https://github.com/k3rnL/open-cinema-hardware/blob/eae54aa79c94255bdad5aaae5bf087d2b4166b0e/docs/verification-A7.md)
- [A7 rigid integration file](https://github.com/k3rnL/open-cinema-hardware/blob/eae54aa79c94255bdad5aaae5bf087d2b4166b0e/boards/rear-io/exports/rear-io-A7-rigid.f3d)

No purchase, supplier request, sample, complete-enclosure/PSU check, solder-process qualification, thermal test, circuit design or manufacturing release occurred. The optical cradle remains a prototype proposal. Next work is physical sample/tolerance and plate/mounting validation before final cutouts and production lands.
