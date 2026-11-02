# Work log: Initial software and enclosure resource import

- Date: 2026-11-02
- Contributors: `@k3rnL`, Codex
- Related revision: Open Cinema `master` at `e52008996dd35fe645e2bd682e9c1d2a5277a0f1`
- Related: [component decision](../decisions/0001-initial-enclosure-components.md),
  [reference index](../reference/INDEX.md)

## Objective

Capture the existing Open Cinema software context, record that enclosure work has
started, and import the supplied main-component documents into the project memory.

## Setup

- Inspected the public [`k3rnL/open-cinema`](https://github.com/k3rnL/open-cinema)
  repository, including its overview, desired-state model, orchestrator, supported
  platform matrix, and `v0.3.2` appliance closure.
- Inspected the supplied WM8804, UHP-500 series, and KAB9 PDF documents through
  text extraction, metadata, checksums, and representative rendered pages.
- Checked current manufacturer pages for lifecycle/specification provenance.

## Actions

- Filed the three supplied PDFs under `hardware/electronics/datasheets/` with
  stable filenames, SHA-256 hashes, attribution, and authoritative links.
- Added a preliminary component register.
- Added topic pages for the software system, enclosure, Raspberry Pi 5, WM8804,
  KAB9, and UHP-500.
- Recorded the initial component selection as decision `0001`.

## Observations

- Open Cinema `0.3.2` is a coordinated, functionally accepted control-plane and
  appliance release on a provisioned Pi 5 8 GB Trixie fixture; quantitative and
  generalized-installation claims remain explicitly open.
- WM8804 is listed as discontinued by Cirrus Logic.
- WONDOM's official listing currently marks KAB9 AA-KA32473 out of stock.
- The UHP-500 local PDF is a 2019 snapshot; the manufacturer currently publishes a
  newer revision.
- Enclosure thermal and power-distribution details are not yet captured.

## Interpretation

The selected components are coherent with the existing eight-channel Open Cinema
appliance direction, but selection alone does not close integration. The most
important next records are the exact power variant/tree, physical CAD/layout,
WM8804 carrier/interface, KAB9 channel mapping, and cooling/safety plan.

## Evidence

- [Imported datasheets](../../hardware/electronics/datasheets/README.md)
- [Open Cinema software reference](../reference/topics/open-cinema-software.md)
- [Preliminary component register](../../bom/preliminary-components.csv)

## Next steps

- Import or create the current enclosure CAD and mechanical constraints.
- Resolve the open component variants and supporting electronics.
- Add wiring, connector, thermal, and safety records as they become available.
