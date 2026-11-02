# Decision: Select the 24 V main supply

- Status: Accepted
- Date: 2026-11-02
- Owners: `@k3rnL`
- Related: [initial enclosure components](0001-initial-enclosure-components.md),
  [UHP-500 reference](../reference/topics/mean-well-uhp-500.md)

## Context

The KAB9 amplifier uses a nominal 24 V input. The initial component decision named
the MEAN WELL UHP-500 family but left its output voltage open.

## Decision

Use the 24 V output version of the MEAN WELL UHP-500 family for compatibility with
the amplifier rail.

This fixes the output voltage but does not yet choose between `UHP-500-24` and the
redundant-function `UHP-500R-24`.

## Rationale

A shared 24 V main rail directly matches the selected amplifier's nominal supply.

## Consequences

- Amplifier power distribution can be designed around a 24 V main rail.
- The Raspberry Pi, candidate touch display, and any lower-voltage logic still
  require protected, regulated conversion from 24 V.
- Load, fuse, conductor, connector, sequencing, grounding, thermal, and safety
  requirements remain to be designed and verified.

## Follow-up

- Decide whether the `R` functions are required.
- Define the complete power tree and current budget.
- Select and verify the 24 V-to-5 V conversion and shutdown architecture.
