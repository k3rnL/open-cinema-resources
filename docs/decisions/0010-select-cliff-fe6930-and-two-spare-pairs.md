# 0010 — Select Cliff FE6930 and allow two spare pairs

> Later direction: [0011](0011-horizontal-pcb-with-all-connectors.md) supersedes the vertical/straight-pin implementation with a horizontal board carrying all connectors directly. The conventional-clip style, six working pairs, current requirement and alignment-hole requirements remain. Text below is historical.


- Date: 2026-11-03
- Status: Accepted for the mechanical fit model; production qualification pending
- Source: owner answer “Allow two spare pairs” to the proposed two-block FE6930 layout
- Related: [conventional clips](0007-use-conventional-speaker-clips.md), [straight rear terminals](0008-require-straight-speaker-terminals.md), [external sourcing policy](0009-prefer-jlcpcb-allow-external-parts.md)

## Choice

Use two **Cliff FE6930 eight-contact blocks**, providing six working speaker pairs and two spare pairs. This supersedes the PT-603B mechanical candidate while retaining conventional red/black clips, straight rear pins, the vertical carrier and the 220 ×35 mm rear opening.

## Rationale and evidence

The owner confirmed 4 Ω or mixed/unknown loads. The stocked 3 A WP6-03 alternative is unsuitable for the intended full 50 W/4 Ω basis (approximately 3.54 A RMS before margin). Cliff publishes 7 A at 60 V AC for FE6930 and an exact distributor reference is available. This removes the PT-603B's unresolved rating/retail-source problem. [Dated implementation and sources](../worklog/2026-11-03-fe6930-speaker-connectors.md).

## Consequences and limits

- A7 changes speaker footprints/models and shifts the optical group, cradle and RCA 4 mm right, HDMI 3 mm right. All four owner alignment holes remain unchanged.
- Six active pairs plus two spares require sixteen independent contacts; no negatives are commoned. The FE6930 colour layout pairs contacts horizontally. No circuitry or harness has been designed.
- Outside purchase is permitted if JLC sourcing or assembly is unavailable. This is not authorization to purchase, nor confirmed JLC inventory/acceptance.
- Nominal fit and rigid Fusion movement pass. Physical sample dimensions, project-derived plated slots, mounting loads, plate depth, real tolerances, PSU clearance and production qualification remain open. The cradle remains an assistant-proposed prototype, not an owner-approved production part.
