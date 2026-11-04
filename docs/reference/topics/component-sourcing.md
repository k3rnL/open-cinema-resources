---
title: Component sourcing and JLCPCB
summary: A11 has exact chip catalogue references, but ADV7511 purchase eligibility, DD+ validation and horizontal speaker qualification remain open.
status: active
updated: 2026-11-04
tags: [manufacturing, procurement, connectors, jlcpcb]
aliases: [aliexpress, global-sourcing, pre-order, stock, bom, c7159430, c4992555, wp6-03, fe6930, spare-pairs, adv7511, c179459, tlv75518, tps2553, bas116]
sources:
  - docs/worklog/2026-11-04-a11-arc-electrical-study.md
  - docs/decisions/0014-use-arc-for-first-version.md
  - docs/worklog/2026-11-03-a10-electrical-draft.md
  - docs/decisions/0011-horizontal-pcb-with-all-connectors.md
  - docs/worklog/2026-11-03-horizontal-rear-io-A8.md
  - docs/decisions/0010-select-cliff-fe6930-and-two-spare-pairs.md
  - docs/worklog/2026-11-03-fe6930-speaker-connectors.md
  - docs/decisions/0009-prefer-jlcpcb-allow-external-parts.md
  - docs/worklog/2026-11-03-rigid-fusion-and-optical-support.md
---

# Component sourcing and JLCPCB

The owner prefers JLCPCB, accepts its pre-order/Global Sourcing service, and allows AliExpress or other websites when parts are hard to source. This is procurement policy, not authorization to purchase. [Decision0009](../../decisions/0009-prefer-jlcpcb-allow-external-parts.md).

## Current A8 horizontal study

The owner now requires every connector soldered to one horizontal PCB. KLS L-KLS1-WP-6P-03B-B/R is a drawing-backed mechanical candidate, **not electrically qualified or source-confirmed**. Its published drawing lacks an operating-current rating. FE6930 straight tags do not directly suit the new board orientation; the7 A rating cannot be transferred to KLS.

RCJ-011 replaces RCJ-021; JLC C4992678 showed21 units at lookup. Horizontal HDMI10029449-001RLF has JLC listing C428493, but purchasable stock was not established. FCR684205R retains its external-source route. Exact dated links and evidence are in the [A8 work log](../../worklog/2026-11-03-horizontal-rear-io-A8.md) and its pinned hardware record. No sourcing requests, orders or reservations were made.

## Historical A6/A7 supply evidence

On 2026-11-03, JLC's public catalogue had stocked Amphenol 10078837-001LF (**C7159430**). Same Sky RCJ-021 (**C4992555**) had zero JLC stock but outside distributor stock. Cliff FCR684205R had outside distributor stock; a purchasable JLC listing/Global Sourcing acceptance was not verified. Stock counts and exact supplier links live in the [dated A6 audit](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/sourcing-A6.md), not as timeless guarantees in this topic.

The owner accepted **two Cliff FE6930 eight-contact blocks**, giving six working pairs plus two spares. The published rating is 7 A at 60V AC and DigiKey 4654-FE6930-ND is an identified distributor source; exact dated evidence is in the [A7 session](../../worklog/2026-11-03-fe6930-speaker-connectors.md). Physical samples, production lands and JLC acceptance remain unqualified. [Decision 0010](../../decisions/0010-select-cliff-fe6930-and-two-spare-pairs.md).

This supersedes the PT-603B mechanical candidate with unresolved current rating/retail supply. The 3 A Uxcell WP6-03 alternative remains rejected for the owner's 4 Ω or mixed/unknown loads. No production order is ready merely because a connector source is identified.

Do not equate distributor stock with confirmed JLC availability, or count a **Consign Parts**/virtual catalogue entry as stock. JLC sourcing is for subsequent PCBA, not loose-part delivery. A6/A7 proposed a separate JLC3DP/custom optical cradle; A8 no longer uses it. No sourcing requests, orders or reservations have been placed.

Related: [hardware implementation](hardware-repository-and-kicad.md), [rear panel](rear-panel-interface.md).

## A10 electrical draft update

See the [A10 work log](../../worklog/2026-11-03-a10-electrical-draft.md). A separate KiCad schematic and rigid integration model now exist. CS8416K is the draft optical/coax choice, with documented source selection and LVDS circuitry. HDMI remains unwired in A10. [Decision 0014](../../decisions/0014-use-arc-for-first-version.md) now targets ARC first and defers eARC; at that scope-record stage no ARC implementation existed. A11 below adds a candidate; no order-ready BOM or manufacturing release exists. Prior WM8804 and connector records remain historical evidence.

## Current A11 sourcing

The [A11 work log](../../worklog/2026-11-04-a11-arc-electrical-study.md) pins the detailed sourcing table. ADV7511KSTZ has JLC C179459, but ADI explicitly requires HDMI-adopter status to purchase; the listing does not confirm eligibility or accepted supply. Exact regulator, LVDS, protection, oscillator and inductor candidates are recorded. Some need pre-order/Global Sourcing or external procurement; no complete order-ready BOM exists. KLS current rating/supply remains open. Stock is a dated observation, not a durable promise. No order, reservation or supplier contact was made.
