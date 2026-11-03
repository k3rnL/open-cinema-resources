# Compact switched mains inlet recommendation

Date: 2026-11-03. Status: component recommendation for mechanical integration; mounting position and complete mains design remain unvalidated. No purchase, PCB change or enclosure CAD edit was made.

## Request and recommendation

The owner requested the most compact 230 V cord inlet satisfying the enclosure and electrical needs. The earlier integrated power-switch requirement and separate mains assembly remain applicable.

Recommend **SCHURTER DC11.0001.301**, the snap-in C14/earth, non-illuminated two-pole switch version for a **2.0 ±0.1 mm mounting panel**. This matches the current rear-frame CAD thickness, not the unresolved 3 mm fabrication baseline. If the actual mounting sheet is 3 mm, use **DC11.0001.501**; for 1.5 mm use **DC11.0001.201**. Do not substitute the single-pole .303 version. The screw-mounted .001 has a wider flange. DC11 is the most compact suitable integrated candidate among those checked, not a proven global minimum.

## Manufacturer evidence

[Current DC11 datasheet](https://www.schurter.com/en/datasheet/typ_DC11.pdf), dated 2025-09-15: IEC rating 10 A/250 VAC; 4.8 × 0.8 mm quick-connect tabs; no fuse or filter. Snap-in face 30 × 34 mm; cutout 27.6 × 31.6 mm, dimensions ±0.10 mm, R2.4 ±0.10. Rear extent from flange seating face to longest terminal is 32.3 mm; insulated receptacles and wire bends need additional room. Rotate 90° for a 34 mm wide / 30 mm tall face. The manufacturer drawing on page 3 was visually checked using its [DigiKey-hosted copy](https://media.digikey.com/pdf/Data%20Sheets/Schurter%20PDFs/DC11_.pdf); dimensional values agree with the current official sheet.

[MEAN WELL UHP-500 specification](https://www.meanwell.com/Upload/PDF/UHP-500%28R%29/UHP-500-spec.pdf), dated 2025-08-01: typical AC draw 2.6 A at 230 VAC; cold-start inrush 60 A with 10% tolerance. [SCHURTER switch data](https://www.schurter.com/en/knowledge/line-switch) specifies the DC11 family's capacitive switching test at 100 A for 3–4 ms, 5 A continuous, 10,000 operations. These are a sound selection basis; pulse shape, restart conditions, wiring/protection and operating temperature still need application validation.

## Actual CAD observations and fit limitation

Read-only inspection of the open Home Cinema v8 with the live A9 source found nominal bounds in mm:

| Item | X | Y | Z |
| --- | --- | --- | --- |
| Rear frame | −130…130 | 100…102 | 0…80 |
| PSU gross reference | −116…116 | 19…100 | 2…35 |
| PCB plus connectors | −114…114 | 62…113.4 | 37…72.5 |

PCB underside/connector seating plane is z 67; its upper face is 68.6. The PSU effectively reaches the rear frame, preventing a lower-rear inlet without moving the supply. The side strips beside the PSU are only 14 mm wide each. Existing connectors occupy the upper rear region. A 35 mm-high opening alone does **not** prove fit: the inlet's inward body, terminal insulation, cable bends and mains separation occupy volume behind it.

Preferred next fit study: reserve a dedicated end bay in the rear panel, revising the audio layout/PCB as required. Do not declare a drop-in fit or remove mounting holes without a fresh integration check. A side-panel position above the PSU is an alternative, not an accepted change. Keep the module separate from the audio PCB. The owner continues to design the backplate and brackets; none were reintroduced.

## Sourcing and remaining design

[TME exact part listing](https://www.tme.com/us/en-us/details/dc11.0001.301/iec-60320-connectors/schurter/) showed 85 units, MOQ 1, at lookup. This is an external sourcing route, not JLC assembly availability. Other panel-thickness versions need their own stock check. Use a suitable earthed C13 cord. Protective earth must bond the PSU and exposed metalwork and remain unswitched; fuse protection, insulated terminations and separation are still to be designed. No fuse value has been selected from the nominal running current alone.

Current implementation remains [A9, hardware commit cca8509](https://github.com/k3rnL/open-cinema-hardware/tree/cca850974a5c3060e4bc8d971570bd204b7b031f). This recommendation does not alter the unresolved Fusion source-save state.
