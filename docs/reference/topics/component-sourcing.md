---
title: Component sourcing and JLCPCB
summary: JLCPCB is preferred; Global Sourcing/pre-order and outside suppliers are allowed; speaker qualification remains open.
status: active
updated: 2026-11-03
tags: [manufacturing, procurement, connectors, jlcpcb]
aliases: [aliexpress, global-sourcing, pre-order, stock, bom, c7159430, c4992555, wp6-03]
sources:
  - docs/decisions/0009-prefer-jlcpcb-allow-external-parts.md
  - docs/worklog/2026-11-03-rigid-fusion-and-optical-support.md
---

# Component sourcing and JLCPCB

The owner prefers JLCPCB, accepts its pre-order/Global Sourcing service, and allows AliExpress or other websites when parts are hard to source. This is procurement policy, not authorization to purchase. [Decision0009](../../decisions/0009-prefer-jlcpcb-allow-external-parts.md).

On2026-11-03, JLC's public catalogue had stocked Amphenol10078837-001LF (**C7159430**). Same Sky RCJ-021 (**C4992555**) had zero JLC stock but outside distributor stock. CliffFCR684205R had outside distributor stock; a purchasable JLC listing/Global Sourcing acceptance was not verified. Stock counts and exact supplier links live in the [dated A6 audit](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/sourcing-A6.md), not as timeless guarantees in this topic.

Dragon CityPT-603B remains an unqualified mechanical candidate: exact small-quantity retail supply and current rating unresolved. A stocked UxcellWP6-03 SKU a19012500ux0044 has similar packaging and straight pins but is **not a proven drop-in replacement**. Its advertised3A limit does not qualify full50W into4Ω. [Session evidence](../../worklog/2026-11-03-rigid-fusion-and-optical-support.md).

Do not equate distributor stock with confirmed JLC availability, or count a **Consign Parts**/virtual catalogue entry as stock. JLC sourcing is for subsequent PCBA, not loose-part delivery. A separate JLC3DP/custom mechanical order and final screw assembly would be needed for the proposed optical cradle. No sourcing requests, orders or reservations have been placed.

Related: [hardware implementation](hardware-repository-and-kicad.md), [rear panel](rear-panel-interface.md).
