---
title: Rear-panel interface and enclosure layout
summary: Rear layout and connector context, with an accepted JLCCNC-installed self-clinching fastening baseline and provisional above-PSU board placement.
status: active
updated: 2026-11-04
tags: [mechanical, enclosure, rear-panel, fasteners, connectors, thermal, electronics]
aliases: [back-panel, rear-input-board, tongues, self-clinching-nuts, pem, jlccnc, s-m3-2, s-m3-2zi]
sources:
  - docs/decisions/0014-use-arc-for-first-version.md
  - docs/worklog/2026-11-03-enlarged-enclosure-and-input-architecture.md
  - docs/worklog/2026-11-03-compact-mains-inlet.md
  - docs/worklog/2026-11-03-remove-plate-and-brackets-A9.md
  - docs/decisions/0011-horizontal-pcb-with-all-connectors.md
  - docs/worklog/2026-11-03-horizontal-rear-io-A8.md
  - docs/worklog/2026-11-03-restore-alignment-holes.md
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

The PSU spans the rear; the Pi/electronics and amplifier are at the front. The owner now requires one horizontal PCB with every connector directly soldered, including speaker clips. A8 is a fit experiment with component side downward and solder tails upward. See [current hardware context](hardware-repository-and-kicad.md) and [decision0011](../../decisions/0011-horizontal-pcb-with-all-connectors.md).

The owner has enlarged the enclosure. Current live CAD shows a **250 × 51 mm opening**, X±125, Z18…69, in a 290 × 80 mm rear frame. The PSU-to-inner-rear-wall gap is about 32.7 mm. A9's PCB is unchanged and its current assembled setback needs correction before assessing airflow. Its older 220 × 35 fit result does not validate this new placement. See the [new geometry and architecture discussion](../../worklog/2026-11-03-enlarged-enclosure-and-input-architecture.md). The owner still designs the backplate and brackets.

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
| Mains cord inlet with power switch (described as 220 V) | DC11 snap-in C14/two-pole module recommended; panel-thickness variant and placement/protection need finalization; see current mains note below |
| Two optical inputs | Two TOSLINK/S/PDIF receive inputs |
| One coaxial input | Coaxial S/PDIF input; A8 uses horizontal Same Sky RCJ-011 |
| One HDMI ARC input | Standard ARC first under [decision 0014](../../decisions/0014-use-arc-for-first-version.md); DD+ Atmos transport targeted, eARC deferred |
| Speaker spring clips | Owner confirmed six speaker pairs/twelve contacts on 2026-11-03 |

The owner confirmed speaker pairs and audio inputs on the same connector strip
for A0, evolving the earlier suggestion of separate speaker/input assemblies.
The mains module remains separate. A8 places all connectors directly on one horizontal PCB. Speaker wiring must preserve the
amplifier topology; do not assume common speaker-negative terminals.

## Historical A3–A5 alignment update

The owner rejected downward speaker pins near the PSU and supplied the **220 × 35 R5** opening. Read-only measurement gives x−110…110,z34…69. A3 evaluates two Dragon City PT-603B six-contact blocks with straight pins through a **228 × 32 × 1.6 vertical PCB**; current rating, supply, final drills and support are unqualified. The owner's surface-mount suggestion is a possible means, not a finalized technology constraint. [Decision 0008](../../decisions/0008-require-straight-speaker-terminals.md).

At the owner's request, A5 includes **four real Ø3 alignment holes at x±115,z44/59**, two per side, carried by matching R4 PCB tabs. These appear in both STEP exports; mounting hardware remains undecided. [A4/A5 correction](../../worklog/2026-11-03-restore-alignment-holes.md). The upper actual Ø4.5 holes at x±40,z75 clear the opening by 3.75 mm in projection. A2's upward-enlargement conflict is superseded. Speaker pins point behind the PCB, not below the body. The PCB bottom remains 4 mm above the old PSU-top line in projection; actual depth, solder insulation, plate setback and full enclosure fit remain open. [A3 evidence/session](../../worklog/2026-11-03-straight-speaker-terminals.md).

[A2's KLS downward-tail arrangement](../../worklog/2026-11-03-speaker-clip-correction.md) is retained as rejected history.

## Historical A1 frame and mechanical PCB study

The A1 opening was **210 × 25 mm, R5**, z39…64, in a 260 × 80 frame. A1 keeps a **228 × 32 mm** nominal 1.6 mm vertical main PCB, selected connector footprints/models and two optical daughterboards. [Current parts and implementation](hardware-repository-and-kicad.md).

Updated Sketch3 provides two **Ø3 reference points at x−110,z44/59**; the owner has not selected the mounting method. They are drawing graphics only; A0's four proposed PCB drills were removed. The optical module tabs have only 0.5 mm nominal clearance below the opening top.

Frame CAD currently reads **2 mm thick**, conflicting with the 3 mm fabrication baseline. Its six Ø4.5 holes also differ from the nominal Ø3.8 through-hole baseline. Both remain unresolved; the original frame was unchanged. PCB bottom remains 4 mm above the old sketch's PSU-top line in projection, which does not validate clearance.

Source: [A1 connector session](../../worklog/2026-11-03-rear-connector-selection.md), [decision 0006](../../decisions/0006-vertical-carrier-and-optical-daughterboards.md).

## Placement constraints

- Current A8 uses a narrow horizontal board, component side down. Check its effect on PSU ventilation; the former vertical-board recommendation is superseded.
- From outside the rear, the A8 preview has speakers on the right and audio inputs on the left; port order remains a fit-study choice. Locate the mains
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
- Six pairs use conventional red/black clips directly soldered to the horizontal board. A8 KLS candidate current rating, supply and physical qualification remain open. Pins point upward in the proposed installation. See [decision0011](../../decisions/0011-horizontal-pcb-with-all-connectors.md).
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

## A9 model scope correction

The owner will design the connection backplate and L brackets. The current PCB export contains only PCB and connectors, retaining its four PCB mounting holes. Earlier plate/support solids and their vertical alignment holes are historical. [A9 record](../../worklog/2026-11-03-remove-plate-and-brackets-A9.md).

## Compact mains inlet recommendation

The [mains selection record](../../worklog/2026-11-03-compact-mains-inlet.md) recommends SCHURTER DC11.0001.301 for the current 2 mm panel, with thickness-specific alternatives. This is a component recommendation, not a validated placement or owner-approved layout change. The read-only current model confirms the PSU reaches the rear frame below z35; the existing upper connector region needs a dedicated mains bay and a fresh fit/separation check. Mains remains separate from the audio PCB. Fuse selection, insulated wiring and protective-earth bonding remain open.
