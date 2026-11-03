# Enlarged enclosure and input-board architecture discussion

Date: 2026-11-03. Status: new owner geometry and read-only observations; electronics arrangement remains a proposal. No PCB or Fusion geometry was edited.

## Owner update

The owner enlarged the enclosure by approximately 30 mm in both horizontal directions to avoid covering the PSU with the input PCB, widened the rear opening, and asked whether extraction, selection and LVDS fit on the existing board or require stacked boards. A board-to-board connection is acceptable in principle. No stack, receiver, connector pinout or detailed electronic circuit was selected.

## Read-only live CAD observations

Inspected the modified open Home Cinema v10, with Rear Panel Assembly v5 / Rear Panel v8 and the existing A9 67-body input assembly. These observations describe live unsaved state, not a verified cloud release.

| Feature | Observed nominal geometry, mm |
| --- | --- |
| Rear frame | 290 wide × 80 high; inner Y120, outer Y122 |
| Window | 250 × 51, X−125…125, Z18…69; owner sketch calls R5 |
| Four panel reference holes | Ø3; X±130, Z26 and 61 |
| PSU gross envelope | X−90…142, Y6.3…87.3, Z2…35 |
| Gap behind PSU to inner rear wall | 32.7 |
| Existing PCB | 228 × 39.8 × 1.6, unchanged A9 |

The current assembled PCB sits partly outside the rear frame: its rearward edge is near Y141.8 while the rear-frame outer face is Y122. Its apparent separation from the PSU is therefore not evidence of final clearance. Restoring approximately the previous connector seating relative to the frame would move it inward about 20 mm and put its inner edge near Y82, overlapping the PSU projection by about 5 mm. These are placement estimates; the owner-designed connection plate datum and component mating positions must be established before correcting the model.

For the next fit study, investigate a shallower board (approximately 25–30 mm is a starting envelope, not a released dimension), using the extra lateral room while preserving a mains bay, fasteners, cables and actual airflow. The larger window is not itself a PCB outline or proof of thermal/mains clearance. Existing four PCB mounting holes remain unchanged until a new mechanical design is agreed. The prior 220 × 35 window describes A9's historical fit, not the current enclosure.

## Working electronics proposal

Start with one four-layer rear PCB containing the connectors, input protection, eARC/ARC reception, optical/coax reception and selection, control, local supply filtering and LVDS transmitters. Keep the Pi-side LVDS receiver adapter already envisaged in decision 0003. Existing PCB gross area is about 91 cm²; a complete custom front end appears plausible, but no placement/routing proves fit yet. Usable space depends on the selected receiver, support circuits and high-current speaker routing.

A small mezzanine is an acceptable fallback when a documented receiver module or the final placement justifies it. Prefer the HDMI receptacle and its receiver on the same PCB; cross a short, supported board-to-board connector with recovered I2S data/clocks, controls, supply and adequate grounds. A raw eARC link across a connector is possible only with an appropriate signal-integrity design. Do not use ordinary small signal contacts for speaker currents. A second board must remain in the clear rear volume rather than recreating an airflow obstruction over the PSU.

[EP92H1 manufacturer overview](https://www.epmi.com.tw/hdmi-arc-earc/ep92h1/) demonstrates that eARC/ARC reception, a single S/PDIF input receiver and internal audio routing can share one IC. It remains an illustrative candidate: complete documentation, firmware/control access, supply and exact output modes are unqualified. Two optical and one coax input would still need selection ahead of a single S/PDIF receiver. Do not assume WM8804 is necessary alongside an integrated receiver.

## Requirements to settle before layout

- Actual TV/source models, return-audio-only versus a full HDMI video receiver, required formats/sample rates and acceptable latency. TV models and whether lossless/Atmos are essential initially were asked; answers pending when this record was written. eARC transport is not a Dolby/DTS decoder or Atmos renderer.
- Receiver documentation, obtainable parts, controller firmware, CEC/ARC fallback and capability advertisement.
- Validate receiver-to-Pi capture on the supported OS: four stereo I2S data lanes with common BCLK/LRCLK for eight PCM channels, not an assumed single-wire TDM path. [Official Pi guide](https://pip-assets.raspberrypi.com/categories/1259-audio-camera-and-display/documents/RP-009699-WP-1-Using%20the%20I2S%20peripherals%20on%20Raspberry%20Pi%20SBCs.pdf).
- Source changes must coordinate data and clocks, mute, lock detection and capture restart. If amplifier output uses an independently clocked USB device, validate drift correction after decoding; encoded payloads must stay unmodified until decoded. [PipeWire clock/resampling behavior](https://docs.pipewire.org/devel/page_man_pipewire-props_7.html).
- Standby behavior, TV-remote volume/wake, always-powered controller/receiver rails, and Pi shutdown sequencing.
- Final board setback/depth, inlet and insulated wiring volume, support loads, and unresolved horizontal speaker-clip current rating/supply.

## EMI and thermal approach

PSU proximity is a manageable design concern, not demonstrated immunity. Include Class-D speaker wiring and local converters as interference sources. Proposed measures: continuous reference planes, compact clock routes, local decoupling/filtering, specified differential impedance and termination, deliberate connector-shell/chassis bonding, and separation of mains/high-current speaker paths from input/clock circuits. LVDS neither isolates grounds nor protects receiver power/clock circuits from every interference path. [TI layout guidance](https://www.ti.com/lit/an/snla302/snla302.pdf).

Validate with the assembled enclosure under amplifier load and during power/source transitions: receiver lock/errors, capture stability, audible artifacts and temperatures. Preserve unobstructed PSU vents; the manufacturer's installation and thermal conditions still apply. [MEAN WELL installation manual](https://www.meanwell.com/Upload/PDF/Enclosed_Type_EN.pdf).
