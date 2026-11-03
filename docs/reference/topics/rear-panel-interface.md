---
title: Rear-panel interface and enclosure layout
summary: Rear layout and connector context, with an accepted JLCCNC-installed self-clinching fastening baseline and provisional above-PSU board placement.
status: active
updated: 2026-11-03
tags: [mechanical, enclosure, rear-panel, fasteners, connectors, thermal, electronics]
aliases: [back-panel, rear-input-board, tongues, self-clinching-nuts, pem, jlccnc, s-m3-2, s-m3-2zi]
sources:
  - docs/decisions/0008-require-straight-speaker-terminals.md
  - docs/worklog/2026-11-03-straight-speaker-terminals.md
  - docs/decisions/0007-use-conventional-speaker-clips.md
  - docs/worklog/2026-11-03-rear-connector-selection.md
  - docs/decisions/0006-vertical-carrier-and-optical-daughterboards.md
  - docs/worklog/2026-11-03-kicad-rear-io-mechanical.md
  - docs/decisions/0005-use-separate-hardware-repository-and-kicad.md
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
the space above the PSU. The owner has drawn a frame for a separate connection
plate and PCB; a first [KiCad mechanical study](hardware-repository-and-kicad.md)
now has an A3 straight-pin red/black speaker-clip fit study in the measured 220 × 35 opening, with optical daughterboards. Mounting depth, cutouts and final qualification remain open.

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
  A read-only `Rear Panel v4 / Sketch2` geometry snapshot is now archived in
  hardware; the full enclosure assembly and support verification remain missing.

Sources: [session record](../../worklog/2026-11-03-rear-panel-and-audio-architecture.md),
[original enclosure views](../../../hardware/mechanical/enclosure-layout/README.md).

## Required interfaces

| Owner request | Current interpretation/status |
| --- | --- |
| Mains cord inlet with power switch (described as 220 V) | 230 V AC nominal application; inlet, fuse, switch and wiring design still open |
| Two optical inputs | Two TOSLINK/S/PDIF receive inputs |
| One coaxial input | Coaxial S/PDIF input; A1 uses Same Sky RCJ-021 |
| One HDMI ARC input; later priority "most compatible" | eARC plus explicit legacy ARC support is the working architecture target |
| Speaker spring clips | Owner confirmed six speaker pairs/twelve contacts on 2026-11-03 |

The owner confirmed speaker pairs and audio inputs on the same connector strip
for A0, evolving the earlier suggestion of separate speaker/input assemblies.
The mains module remains separate. A1 keeps a vertical main PCB and adds two small horizontal optical daughterboards, by owner decision. Speaker wiring must preserve the
amplifier topology; do not assume common speaker-negative terminals.

## Current A3 correction

The owner rejected downward speaker pins near the PSU and supplied the **220 × 35 R5** opening. Read-only measurement gives x−110…110,z34…69. A3 evaluates two Dragon City PT-603B six-contact blocks with straight pins through a **228 × 32 × 1.6 vertical PCB**; current rating, supply, final drills and support are unqualified. The owner's surface-mount suggestion is a possible means, not a finalized technology constraint. [Decision 0008](../../decisions/0008-require-straight-speaker-terminals.md).

Reference frame fixing points are now x−115,z44/59, Ø3, still graphics only. The upper actual Ø4.5 holes at x±40,z75 clear the opening by 3.75 mm in projection. A2's upward-enlargement conflict is superseded. Speaker pins point behind the PCB, not below the body. The PCB bottom remains 4 mm above the old PSU-top line in projection; actual depth, solder insulation, plate setback and full enclosure fit remain open. [A3 evidence/session](../../worklog/2026-11-03-straight-speaker-terminals.md).

[A2's KLS downward-tail arrangement](../../worklog/2026-11-03-speaker-clip-correction.md) is retained as rejected history.

## Historical A1 frame and mechanical PCB study

The A1 opening was **210 × 25 mm, R5**, z39…64, in a 260 × 80 frame. A1 keeps a **228 × 32 mm** nominal 1.6 mm vertical main PCB, selected connector footprints/models and two optical daughterboards. [Current parts and implementation](hardware-repository-and-kicad.md).

Updated Sketch3 provides two **Ø3 reference points at x−110,z44/59**; the owner has not selected the mounting method. They are drawing graphics only; A0's four proposed PCB drills were removed. The optical module tabs have only 0.5 mm nominal clearance below the opening top.

Frame CAD currently reads **2 mm thick**, conflicting with the 3 mm fabrication baseline. Its six Ø4.5 holes also differ from the nominal Ø3.8 through-hole baseline. Both remain unresolved; the original frame was unchanged. PCB bottom remains 4 mm above the old sketch's PSU-top line in projection, which does not validate clearance.

Source: [A1 connector session](../../worklog/2026-11-03-rear-connector-selection.md), [decision 0006](../../decisions/0006-vertical-carrier-and-optical-daughterboards.md).

## Proposed placement and constraints

- Place a narrow vertical input PCB high on the rear panel, supported by panel
  mounts or dedicated brackets. Avoid using a broad horizontal PCB as a shelf
  covering the PSU's ventilation.
- The discussed **30-35 mm PCB height** is an initial packaging target only. The
  receiver electronics may change it; A1 checks nominal connector projection only.
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
- Receiver/module circuitry, final footprint qualification and full insertion/service volumes.
- Six pairs use conventional red/black finger-operated clips. A3 evaluates PT-603B straight terminals; current rating, supply, production footprint and mounting remain unqualified. A1 industrial terminals and A2 downward tails are rejected. See [decision 0008](../../decisions/0008-require-straight-speaker-terminals.md).
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
