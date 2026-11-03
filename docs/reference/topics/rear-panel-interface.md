---
title: Rear-panel interface and enclosure layout
summary: Rear layout and connector context, with an accepted JLCCNC-installed self-clinching fastening baseline and provisional above-PSU board placement.
status: active
updated: 2026-11-03
tags: [mechanical, enclosure, rear-panel, fasteners, connectors, thermal, electronics]
aliases: [back-panel, rear-input-board, tongues, self-clinching-nuts, pem, jlccnc, s-m3-2, s-m3-2zi]
sources:
  - docs/worklog/2026-11-03-rear-panel-and-audio-architecture.md
  - docs/worklog/2026-11-03-jlccnc-rear-panel-fastening.md
  - hardware/mechanical/enclosure-layout/README.md
  - hardware/electronics/notes/rear-input-evidence.md
  - docs/decisions/0003-prefer-earc-and-lvds-input-architecture.md
  - docs/decisions/0004-use-jlccnc-rear-panel-fastening.md
  - manufacturing/rear-panel-fastening.md
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
- The fastening baseline selects **3.0 mm aluminium 5052** for both the bottom
  chassis/tongues and removable rear panel. This does not verify PSU thermal
  spreading or thermal contact.
- The rear panel remains a laser-cut sheet fastened to bent mounting tongues.
  The native geometry and support arrangement are not yet in the repository.

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

## Rear-panel fastening decision

[Decision 0004](../../decisions/0004-use-jlccnc-rear-panel-fastening.md) selects
JLCCNC supply and installation of **`S-M3-2` carbon-steel self-clinching nuts**,
M3 x 0.5, in the 3 mm aluminium 5052 chassis tongues. The JLCCNC mounting-hole
diameter is **4.25 mm**. Its 4.8 mm minimum hole-centre-to-edge distance is raised
to a 6 mm design target, with 12 mm minimum and 15 mm preferred tongue width.

Install each nut from inside so the rear-facing tongue surface remains flat and
flush against the panel. The 3 mm rear panel uses nominal 3.8 mm through holes,
a 90-degree countersink fitted to the selected screw, and **M3 x 8 ISO 10642 or
DIN 7991 countersunk screws**. M3 x 6 is not retained: it is too marginal across
the nominal 3 mm panel plus 3 mm tongue stack.

Use six fixings for a flat unsupported full-width panel. Four are acceptable only
with equivalent support from a captured cover edge, a stiffening return or a
representative stiffness test. See the
[fabrication baseline](../../../manufacturing/rear-panel-fastening.md) for order
callouts and first-article checks.

This is an accepted but unverified design baseline. JLCCNC stock, bend and press
access, countersink fit, screw protrusion and assembly tolerance require manual
DFM review and first-article inspection.

## Open questions

- Internal height datum, overall width/depth, actual PSU-to-panel gap and native
  CAD revision/export; screenshots are not dimensional authority.
- Receiver/module footprint, connector parts and full insertion/service volumes.
- Exact speaker count, terminal current/wire ratings and amplifier configuration.
- Native tab/support geometry, final finish, JLCCNC DFM confirmation and
  first-article verification of the selected fastening system. Protective-earth
  hardware remains a separate design question.
- Applicability of the manufacturer's adjacent-heat-source guidance, thermal
  derating, closed-enclosure temperatures and EMI behavior under load.

## Related

- [Enclosure and appliance system](enclosure-appliance.md)
- [Digital audio input and LVDS transport](digital-audio-input.md)
- [Front-panel interface](front-panel-interface.md)
- [WONDOM KAB9](wondom-kab9.md)
