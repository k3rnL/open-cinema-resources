# 0015 — Retain ADV7511 with the owner’s LCSC sourcing choice

- Date: 2026-11-04
- Status: accepted component choice; electrical validation pending
- Source: owner’s project chat following the A12 remaining-work review.
- Related: [ARC scope](0014-use-arc-for-first-version.md), [A12 evidence](../worklog/2026-11-04-a12-routing-and-manufacturing-review.md).

## Decision and rationale

The owner stated: “The ADV7511 is ok for me. Available on LCSC.” Retain **ADV7511KSTZ**, the exact A12 BOM part, and record LCSC as the owner-accepted sourcing route. A replacement search is not required solely because of the previously raised sourcing concern. This records owner-reported availability, not an independently checked stock count, completed purchase or supplier acceptance.

The existing manufacturer purchasing-condition evidence is retained in the historical sourcing records. Component acceptance does not demonstrate ARC-only startup, CEC operation or untouched DD+ payload delivery; those tests remain open.

## Pending owner review

The owner requested the speaker-clip references before confirming them. A12 SP1 and SP2 each use **KLS L-KLS1-WP-6P-03B-B/R**, six contacts / three pairs per block, two blocks total. The manufacturer’s [product page](https://klsele.com/products/Audio-Video-Connectors/Loudspeaker-Terminals/12425.html) confirms the ordering reference. Operating-current rating, exact purchase route and sample qualification remain unresolved; no speaker approval was given in this exchange.

The owner will inspect the A12 model in Fusion to confirm mechanics. No mechanical approval has been received. Use [A12 rigid F3D](https://github.com/k3rnL/open-cinema-hardware/blob/7ab8b660ab667bbf1e1aee3b9737be17c1d84e11/boards/rear-io-A12/exports/rear-io-A12-rigid.f3d); earlier Fusion cloud links may still contain older geometry.

No PCB, model, manufacturing release or order is changed by this decision.
