# Open Cinema reference book

Last reviewed: 2026-11-04

This is the fast map of durable project knowledge. Topic pages summarize what the
project knows and link back to decisions, work logs, and original evidence.

## Start here

- [Project roadmap](../../ROADMAP.md)
- [Current HDMI decision: ARC first, eARC deferred](../decisions/0014-use-arc-for-first-version.md)
- [Decision records](../decisions/README.md)
- [Work logs](../worklog/README.md)
- [Reference topic template](0000-template.md)

## Topics by domain

### Architecture and systems

- [Open Cinema software system](topics/open-cinema-software.md) — desired-state
  audio control plane, runtime ownership, supported platform, and current release
  boundary.
- [Enclosure and appliance system](topics/enclosure-appliance.md) — selected major
  components, system-level constraints, and unresolved integration work.

### Mechanical

- [Front-panel interface](topics/front-panel-interface.md) — candidate touch screen,
  encoder and power-button requirements, and unstarted local UI.
- [Rear-panel interface](topics/rear-panel-interface.md) — owner-supplied layout,
  connector needs, enlarged 250 × 51 mm opening, current rear clearance, fastening baseline and compact mains-inlet recommendation.

### Electronics

- [Audio receiver control and status](topics/audio-receiver-control-status.md) — accepted lock/carrier-rate/format meanings, source switching and unchanged-payload boundary.

- [Hardware repository and KiCad mechanical PCB](topics/hardware-repository-and-kicad.md)
  — A12 routing passes ERC/DRC with no unrouted items and provides rigid models/manufacturing review files; procurement and live operation remain unqualified. A9 is the mechanical baseline.

- [Raspberry Pi 5](topics/raspberry-pi-5.md) — selected computer and supported
  appliance target.
- [WM8804 S/PDIF transceiver](topics/wm8804.md) — original digital-audio choice and lifecycle constraints; CS8416 is the A11 draft alternative.
- [WONDOM KAB9](topics/wondom-kab9.md) — selected configurable eight-channel
  amplifier.
- [MEAN WELL UHP-500](topics/mean-well-uhp-500.md) — selected power-supply family;
  24 V output selected and redundancy suffix still open.
- [Digital audio input and LVDS transport](topics/digital-audio-input.md) — ARC first, unchanged stereo/encoded surround including DD+ Atmos, eARC deferred; Pi-controlled selection and future HAT.
- [Auxiliary control electronics](topics/auxiliary-control-electronics.md) —
  delegated power, shutdown, IR and housekeeping functions; controller and firmware
  still undefined.

### Manufacturing and assembly

- [Component sourcing and JLCPCB](topics/component-sourcing.md) — JLCPCB preferred; Global Sourcing/pre-order and outside suppliers allowed; horizontal speaker candidate current rating and supply unresolved.

### Verification and testing

- [A12 routed prototype](../worklog/2026-11-04-a12-routing-and-manufacturing-review.md) — zero ERC/DRC/unrouted items; review package and rigid exports, manufacturing qualification still open.
- [Historical A11 ARC electrical study](../worklog/2026-11-04-a11-arc-electrical-study.md) — schematic/PCB static reviews, rigid-model exports and explicitly untested functions.

### Operations and maintenance

## Triage

No unclassified material.

## Known gaps

- Enclosure screenshots and orientation are recorded; a measured rear-frame sketch
  snapshot and KiCad placement study are now in hardware. Full assembly CAD,
  internal height datum and service clearances remain missing. The rear-panel
  fastening material/hardware baseline is selected but not CAD- or
  first-article-verified.
- The UHP-500 is confirmed as 24 V, but its `R`/non-`R` suffix, the Raspberry Pi
  board revision, and supporting 5 V conversion are not yet confirmed.
- The purchased Raspberry Pi fan has not been identified by model, mounting, or
  verified thermal performance.
- A12 ADV7511 procurement eligibility, ARC/CEC operation, DD+ Atmos payload preservation, Pi capture and the LVDS harness are not validated. eARC/HBR/MAT is deferred and no longer a first-version gate.
- A12 routes ADV7511 ARC into CS8416 four-input selection, with three active LVDS pairs; WM8804/A10 history is retained. CEC firmware, physical protection testing and KAB9 channel configuration remain unresolved. USB is the
  selected Pi-to-amplifier interface; its actual module/mapping still needs validation.
  Six working pairs now solder to one horizontal board along with the audio inputs. A8's KLS speaker candidate has unverified current rating/supply. Tails point upward; optical daughterboards/cradle are historical.
- A9 keeps the PCB holes but removes the provisional plate and supports; the owner designs those parts. The owner enlarged the opening to 250 × 51 mm; A9 PCB geometry remains unchanged. Current assembled setback needs correction before rechecking clearance; tight plate/PCB gaps, cable mating, hardware, tolerances and production qualification remain open. Frame CAD reads2 mm versus the3 mm fabrication baseline; Ø4.5 frame holes differ from nominal Ø3.8.
- Above-PSU board placement needs thermal, airflow, EMI and mains-separation
  validation, including resolution of manufacturer adjacent-heat-source guidance.
- The hardware license has not yet been selected.

## Retrieval notes

Search aliases and older terminology when the preferred name is unknown. Treat
topic summaries as orientation; follow their evidence and decision links for
conclusions that matter.


- Fusion A9 cloud integration is partial: source save pending; see [A8 work log](../worklog/2026-11-03-horizontal-rear-io-A8.md#authorized-fusion-update--incomplete-source-save).

- [A9 scope change: owner-designed plate and brackets](../worklog/2026-11-03-remove-plate-and-brackets-A9.md).
