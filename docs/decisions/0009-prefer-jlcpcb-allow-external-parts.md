# 0009 — Prefer JLCPCB, allow outside sourcing for difficult parts

- Date: 2026-11-03
- Status: Accepted owner sourcing policy
- Scope: Rear-I/O component procurement; not an order or production release

## Decision and provenance

The owner initially asked to order everything through JLCPCB. During the sourcing review, the owner explicitly allowed JLCPCB pre-order/Global Sourcing. The subsequent instruction permits AliExpress or another website when a component is difficult to find.

**JLCPCB is preferred, not exclusive.** Use its stocked parts where suitable; use pre-order/Global Sourcing or external suppliers for awkward connectors. Do not redesign around a poorly matched connector merely to claim every item is in one catalogue.

## Consequences

Record exact manufacturer/part and supplier SKU, dated availability, and whether a source is public JLC stock, distributor stock, pre-order, consignment or an unconfirmed sourcing request. A look-alike retail part is not a qualified substitute without matching geometry and electrical requirements.

No purchase quantity, budget or permission to place an order was supplied. External components can be assembled manually, or consigned only if JLC accepts them. Final mechanical assembly is separate from PCBA. The PCB remains a mechanical prototype without circuitry.

The A6 audit finds stocked HDMI at JLC and outside stock for the selected RCA and Cliff optical receivers. Exact PT-603B speaker supply/current qualification remains unresolved. The owner subsequently confirmed4Ω or mixed/unknown loads. The stocked3A Uxcell alternative is rejected for the intended full-power use. A7A Cliff alternative would change the pair count/layout and has not been accepted.

Sources: owner instructions in the 2026-11-03 session; [work log](../worklog/2026-11-03-rigid-fusion-and-optical-support.md); [dated hardware sourcing audit](https://github.com/k3rnL/open-cinema-hardware/blob/66f69f2acba4282ec5b1e67392752482bb2918ad/docs/sourcing-A6.md).
