# Rigid Fusion integration, optical support and sourcing — A6

Date:2026-11-03. Hardware implementation commit: [`66f69f2`](https://github.com/k3rnL/open-cinema-hardware/commit/66f69f2acba4282ec5b1e67392752482bb2918ad).

## Owner feedback and constraints

The owner reported that a joint to one alignment hole moved only one part of the imported assembly. They also rejected unsupported/floating optical daughterboards and asked for JLCPCB availability. Follow-up answers allow pre-order/Global Sourcing and then AliExpress/other outside suppliers for hard-to-find parts. [Decision0009](../decisions/0009-prefer-jlcpcb-allow-external-parts.md).

The vertical carrier and two horizontal optical boards,220×35 opening, and four alignment holes on both sides remain required. No logic/LVDS circuitry was requested in this revision.

## Implementation and observations

- The original imported STEP contained separate unconstrained components. A6 provides a single-component STEP and native F3D with123 solid bodies. The raw hierarchical KiCad STEP remains available for inspection.
- Temporary Fusion joint verification used a circular edge of HREF1. After disabling Ground to Parent, all123 bodies moved and every checked body vertex matched the single occurrence transform. Both rigid file formats reimport with no child occurrences. The owner's working document was inspected/restored, not edited or saved.
- HREF1–HREF4 remain real Ø3 holes at x±115,z44/59.
- A6 introduces a **prototype support proposal**, not an owner-approved production part: one insulating cradle bolted to the carrier in four places, two screws per optical board, and one bolt through each receiver's existing mounting lug. The load path no longer relies only on electrical leads.
- Native KiCad main/child DRC returned zero violations under recorded settings; no circuit/nets exist. Fusion found no positive-volume collision between the modeled cradle and connector assembly. Full enclosure/PSU fit, actual parts, temperature, cable-load strength, process acceptance and tolerance checks remain open. The nominal RCA-tail gap is only about0.4mm.

## Sourcing evidence

The live JLC public catalogue showed Amphenol10078837-001LF as **C7159430**,2400 in stock. RCJ-021 is **C4992555**, zero public stock, with distributor stock available. CliffFCR684205R is stocked at DigiKey; JLC Global Sourcing acceptance was not obtained. A JLC consignment/virtual entry was not counted as purchasable stock.

Exact PT-603B public stock and current rating remain unverified. Harfington item1058833 / UxcellWP6-03 SKU a19012500ux0044 was in stock and its photos show rear-normal pins. It is **not confirmed equivalent** to the modeled Dragon City part; row pitch/depth and production footprint remain unqualified. Seller3A rating is below the illustrative3.54A RMS needed for50W into4Ω. No production substitution or order was made.

## Artifacts and next evidence

- [Rigid Fusion file](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/boards/rear-io/exports/rear-io-A6-rigid.f3d)
- [Assembly/cradle instructions and dimensions](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/assembly-and-optical-support-A6.md)
- [Verification and source hashes](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/verification-A6.md)
- [Sourcing audit and exact links](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/sourcing-A6.md)

Next: qualify the exact speaker choice against load/current requirements and physical samples, validate cradle fit/temperature/load and full plate/PSU stack, then finish the circuit and assembly procurement. Do not describe the whole BOM or the cradle as manufacturing-ready.
