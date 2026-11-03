---
title: Component sourcing and JLCPCB
summary: JLCPCB is preferred; Global Sourcing/pre-order and outside suppliers are allowed; FE6930 is selected, with physical and production qualification open.
status: active
updated: 2026-11-03
tags: [manufacturing, procurement, connectors, jlcpcb]
aliases: [aliexpress, global-sourcing, pre-order, stock, bom, c7159430, c4992555, wp6-03, fe6930, spare-pairs]
sources:
  - docs/decisions/0010-select-cliff-fe6930-and-two-spare-pairs.md
  - docs/worklog/2026-11-03-fe6930-speaker-connectors.md
  - docs/decisions/0009-prefer-jlcpcb-allow-external-parts.md
  - docs/worklog/2026-11-03-rigid-fusion-and-optical-support.md
---

# Component sourcing and JLCPCB

The owner prefers JLCPCB, accepts its pre-order/Global Sourcing service, and allows AliExpress or other websites when parts are hard to source. This is procurement policy, not authorization to purchase. [Decision0009](../../decisions/0009-prefer-jlcpcb-allow-external-parts.md).

On 2026-11-03, JLC's public catalogue had stocked Amphenol 10078837-001LF (**C7159430**). Same Sky RCJ-021 (**C4992555**) had zero JLC stock but outside distributor stock. Cliff FCR684205R had outside distributor stock; a purchasable JLC listing/Global Sourcing acceptance was not verified. Stock counts and exact supplier links live in the [dated A6 audit](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/sourcing-A6.md), not as timeless guarantees in this topic.

The owner accepted **two Cliff FE6930 eight-contact blocks**, giving six working pairs plus two spares. The published rating is 7 A at 60V AC and DigiKey 4654-FE6930-ND is an identified distributor source; exact dated evidence is in the [A7 session](../../worklog/2026-11-03-fe6930-speaker-connectors.md). Physical samples, production lands and JLC acceptance remain unqualified. [Decision 0010](../../decisions/0010-select-cliff-fe6930-and-two-spare-pairs.md).

This supersedes the PT-603B mechanical candidate with unresolved current rating/retail supply. The 3 A Uxcell WP6-03 alternative remains rejected for the owner's 4 Ω or mixed/unknown loads. No production order is ready merely because a connector source is identified.

Do not equate distributor stock with confirmed JLC availability, or count a **Consign Parts**/virtual catalogue entry as stock. JLC sourcing is for subsequent PCBA, not loose-part delivery. A separate JLC3DP/custom mechanical order and final screw assembly would be needed for the proposed optical cradle. No sourcing requests, orders or reservations have been placed.

Related: [hardware implementation](hardware-repository-and-kicad.md), [rear panel](rear-panel-interface.md).
