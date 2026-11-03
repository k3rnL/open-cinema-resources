# 0006: Keep the vertical rear PCB and use optical daughterboards

> Later direction: [0011](0011-horizontal-pcb-with-all-connectors.md) supersedes the vertical/straight-pin implementation with a horizontal board carrying all connectors directly. The conventional-clip style, six working pairs, current requirement and alignment-hole requirements remain. Text below is historical.


- Date: 2026-11-03
- Later correction: [0007](0007-use-conventional-speaker-clips.md) rejects the Phoenix speaker terminals; the vertical PCB / optical daughterboard decision remains active.
- Status: Owner-accepted orientation; A1 connector selection for mechanical integration
- Owner: @k3rnL
- Evolves: [0005](0005-use-separate-hardware-repository-and-kicad.md)

The owner explicitly chose **keep the vertical PCB; use small optical daughterboards** after the receiver drawings showed that readily available TOSLINK parts need a horizontal board to face the rear. Preserve the six speaker pairs plus two optical, coax and HDMI inputs in the same visible connector strip. Mains remains a separate panel assembly.

A1 in hardware replaces A0 generic envelopes with Phoenix Contact 1732496 (six two-pole speaker terminals), Cliff FCR684205R (two optical receivers), Same Sky RCJ-021 (coax RCA) and Amphenol FCI 10078837-001LF (vertical HDMI). These were selected under the owner's request to choose fitting parts; they are not purchased or production-qualified. Part-specific pads are in KiCad. The Phoenix model is from KiCad; the other STEP models are project reconstructions of manufacturer drawings with simplified cosmetic details.

Two 16 × 24 mm horizontal optical boards pass through clearance windows in the 228 × 32 mm vertical main PCB. Main J7/J8 represent complete optical assemblies; receiver solder pads are on child-board J1. Wiring and mechanical support are deferred. This preserves the requested main-board orientation without pretending right-angle receivers mount directly on it.

The owner supplied two Ø3 fixing locations at rear x−110, z44/59 and explicitly stated they are references only, because the mounting method is undecided. A1 keeps them as drawing graphics, removes the four proposed A0 PCB mounting holes, and adds no mirrored fixing points.

Consequences: optical modules need support/interconnect design; connector projection depths differ; the optical mounting tab has only 0.5 mm nominal clearance below the opening top. The 16 Mbit/s optical receiver is not a 192 kHz stereo PCM choice. Final fit, tolerance, mating access, fabrication footprint/stencil review, HDMI receiver/ARC compatibility and all logic/LVDS circuitry remain open.

Sources: [A1 work log](../worklog/2026-11-03-rear-connector-selection.md), [parts and source drawings](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/connector-selection-A1.md), [mechanical notes](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/rear-io-mechanical.md).
