---
title: Rear-panel interface and enclosure layout
summary: Confirmed rear connector needs and enclosure orientation, with provisional mounting and above-PSU input-board placement.
status: active
updated: 2026-11-03
tags: [mechanical, enclosure, rear-panel, connectors, thermal, electronics]
aliases: [back-panel, rear-input-board, tongues, self-clinching-nuts, pem, s-m3-2zi]
sources:
  - docs/worklog/2026-11-03-rear-panel-and-audio-architecture.md
  - hardware/mechanical/enclosure-layout/README.md
  - hardware/electronics/notes/rear-input-evidence.md
  - docs/decisions/0003-prefer-earc-and-lvds-input-architecture.md
---

# Rear-panel interface and enclosure layout

## Summary

The PSU spans the rear of the enclosure; the Pi/electronics stack and amplifier
are at the front. A compact input board high on the rear panel is proposed within
the space above the PSU. Its position, dimensions and cutouts are not frozen.

## Confirmed owner-supplied context

- Looking from the front: Pi/electronics are at front left, amplifier at front
  right, PSU across the rear. Looking at the exterior rear reverses left/right.
- The owner stated **80 mm total height**, estimating about **50 mm above the
  PSU for connectors**. Whether 80 mm is an outside or internal dimension is
  unresolved. No manufacturing tolerance was supplied. The gross band is not all
  available for PCB height: panels, mounting, bodies, wiring and clearances count.
- A **2 or 3 mm bottom sheet** is under consideration to help spread PSU heat.
  Final material/alloy, thickness and thermal contact are not selected.
- The rear panel is envisaged as laser-cut metal sheet, fastened to the bent
  mounting tabs/tongues. Its thickness and support geometry remain open.

Sources: [session record](../../worklog/2026-11-03-rear-panel-and-audio-architecture.md),
[original enclosure views](../../../hardware/mechanical/enclosure-layout/README.md).

## Required interfaces

| Owner request | Current interpretation/status |
| --- | --- |
| Mains cord inlet with power switch (described as 220 V) | 230 V AC nominal application; inlet, fuse, switch and wiring design still open |
| Two optical inputs | Two TOSLINK/S/PDIF receive inputs |
| One coaxial input | Coaxial S/PDIF input; exact connector not selected |
| One HDMI ARC input; later priority "most compatible" | eARC plus explicit legacy ARC support is the working architecture target |
| "spring clips for speaker, 6" | Provisionally interpreted as six speaker pairs/twelve contacts; owner confirmation still needed |

The mains module, low-voltage input PCB and speaker terminals should be separate
assemblies in the proposed layout. This is not a request to put mains circuitry on
the digital-audio PCB. Speaker wiring must preserve the selected amplifier's
output topology; do not assume common speaker-negative terminals.

## Proposed placement and constraints

- Place a narrow vertical input PCB high on the rear panel, supported by panel
  mounts or dedicated brackets. Avoid using a broad horizontal PCB as a shelf
  covering the PSU's ventilation.
- The discussed **30-35 mm PCB height** is an initial packaging target only. The
  receiver/module and connectors may change it; no fit analysis has been done.
- From outside the rear, the proposed speaker group is toward the amplifier side
  on the left and audio inputs toward the Pi side on the right. Locate the mains
  assembly near the PSU's actual AC-terminal end; that end has not been verified
  from the supplied images. Final port order is undecided.
- Preserve space for connector bodies, solder joints, insulated terminals,
  strain relief, cable bends, assembly tools and removal. The PSU-to-rear-panel
  gap has not been measured.
- LVDS helps the cable segment, not every EMI path. Local supply filtering,
  decoupling, a continuous PCB ground plane, short single-ended traces, suitable
  bonding and cable routing away from mains and amplifier outputs remain design
  work. No interference performance has been measured.
- Resolve [PSU thermal/mounting guidance](mean-well-uhp-500.md), airflow and
  mains-terminal separation before approving the above-PSU location. Gross
  available height is not a validated thermal or electrical clearance.

Sources: [working architecture decision](../../decisions/0003-prefer-earc-and-lvds-input-architecture.md),
[manufacturer evidence](../../../hardware/electronics/notes/rear-input-evidence.md).

## Fastening candidates retained from the discussion

Self-clinching nuts are under consideration; they are not selected for fabrication.
The manufacturer reference discussed was **PEM S-M3-2ZI**, an M3 x 0.5 zinc-plated
steel nut for suitable steel/aluminium sheet. PEM specifies minimum sheet
thickness 1.4 mm, mounting hole diameter **4.22 +0.08/-0 mm**, minimum hole-centre
to edge distance **4.8 mm**, and sheet hardness at most HRB 80 / HB 150. The `2`
is a shank code, not a statement that the sheet must be 2 mm thick.

Confirm the actual tab alloy/hardness, edge and bend distances, press access,
installation process and panel loads with the fabricator. Four fixing points were
the owner's initial idea; additional supports/fixings were discussed but not
selected. [PEM specification](https://catalog.pemnet.com/item/nuts-types-s-ss-cls-clss-cla-sp/self-clinching-nuts-types-s-ss-cls-clss-sp-metric/s-m3-2zi).

M3 button-head screws (ISO 7380-1) and countersunk screws (ISO 10642) were discussed.
Screw length is **not selected**: calculate the complete panel/tab/nut stack and
thread engagement, including washers or gaskets. The earlier M3 x 6 suggestion
was not a verified fit. A flush countersunk head requires a matching countersink
operation and suitable sheet thickness; a laser-cut hole alone does not provide
it. Generic marketplace listings have not been qualified as equivalent parts.

## Open questions

- Internal height datum, overall width/depth, actual PSU-to-panel gap and native
  CAD revision/export; screenshots are not dimensional authority.
- Receiver/module footprint, connector parts and full insertion/service volumes.
- Exact speaker count, terminal current/wire ratings and amplifier configuration.
- Final sheet material, thickness, finish, mounting tabs, fixings and earth bonds.
- Applicability of the manufacturer's adjacent-heat-source guidance, thermal
  derating, closed-enclosure temperatures and EMI behavior under load.

## Related

- [Enclosure and appliance system](enclosure-appliance.md)
- [Digital audio input and LVDS transport](digital-audio-input.md)
- [Front-panel interface](front-panel-interface.md)
- [WONDOM KAB9](wondom-kab9.md)
