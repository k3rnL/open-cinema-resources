# Roadmap

## Current milestone: resource inventory

- [ ] Inventory existing mechanical resources
- [ ] Inventory existing electronics resources
- [ ] Inventory existing firmware and device configuration
- [x] Import the initial main-component datasheets and create a preliminary
  component register
- [x] Capture the existing Open Cinema software and supported-appliance context
- [x] Select the 24 V UHP-500 output variant for the amplifier rail
- [x] Obtain a basic Raspberry Pi cooling fan
- [x] Archive enclosure layout screenshots and capture rear interface requirements
- [x] Select the JLCCNC-installed rear-panel fastening baseline
- [x] Record the original eARC/ARC and I2S-over-LVDS architecture direction
- [x] Adopt ARC first, retain DD+ Atmos transport and defer eARC/lossless HDMI; [decision 0014](docs/decisions/0014-use-arc-for-first-version.md)
- [x] Create a separate hardware repo and KiCad rear connector mechanical study,
  with the measured rear-frame opening and STEP review exports
- [ ] Import the current enclosure CAD and mechanical constraints
- [ ] Confirm exact component variants, power tree, wiring, and cooling design
- [ ] Design the front panel and select its display, encoder, and power button
- [x] Build A1 part-specific audio-input footprints/models and optical daughterboards
- [x] Replace A1 industrial terminals in the mechanical model with red/black clip candidates (A2)
- [x] Replace rejected downward speaker tails with straight rear-facing pins in the A3 fit study; record measured 220 × 35 opening
- [x] Select 7 A Cliff FE6930 blocks, accept two spare pairs and verify the revised A7 nominal layout
- [x] Build A8 horizontal fit study with all connectors directly soldered and upward tails
- [ ] Qualify a horizontal conventional speaker block: current rating, exact supply, samples, lands and mounting
- [x] Add A6 rigid Fusion integration files and a bolted optical-cradle prototype
- [x] Audit connector sourcing and record permission to use outside suppliers
- [ ] Owner to design backplate and L brackets; then verify plate cutouts, cable insertion, tolerances, loads and temperatures
- [ ] Integrate the recommended DC11 mains inlet: resolve panel thickness, reserve its mounting/wiring volume, and design protection/earth bonding; [selection evidence](docs/worklog/2026-11-03-compact-mains-inlet.md)
- [x] Draft and statically review optical/coax selection and LVDS electronics in separate A10; [scope and limitations](docs/worklog/2026-11-03-a10-electrical-draft.md)
- [x] Draft A11 ADV7511 ARC support circuit into CS8416 selection and three-pair LVDS; two static reviews and rigid exports; [evidence](docs/worklog/2026-11-04-a11-arc-electrical-study.md)
- [ ] Resolve ADV7511 procurement eligibility and ARC-only/DD+ operation; implement CEC, finish routing/protection and qualify the HAT/capture path
- [ ] Define delegated power/control electronics
- [ ] Reserve rear-board control/status connections; later design the Pi connection HAT and implement GPIO-header source control; [decision 0013](docs/decisions/0013-pi-source-control-and-future-hat.md)
- [ ] Qualify ARC PCM/AC-3/DTS/DD+ extraction, including DD+ Atmos metadata, source selection and LVDS-to-Pi capture; [current scope 0014](docs/decisions/0014-use-arc-for-first-version.md)
- [ ] Separately validate Pi processing for ARC formats, DD+ Atmos behavior and 5.1→7.1 output mapping; no decoder/renderer is planned on the rear PCB
- [ ] Future upgrade: documented eARC reception, HBR/MAT/TrueHD/DTS-HD transport and corresponding Pi software; deferred from the ARC prototype
- [ ] Resolve above-PSU placement against manufacturer thermal guidance, airflow,
  mains separation and loaded-enclosure temperature/interference measurements
- [ ] Design and implement the local touch-screen software
- [ ] Establish the first bill of materials
- [ ] Select a hardware license
- [ ] Define the first reproducible verification baseline

## Next milestone: reproducible prototype

- [ ] Freeze a named prototype revision
- [ ] Publish assembly and manufacturing guidance
- [ ] Link the prototype revision to a complete BOM
- [ ] Publish verification results and known limitations

## Open questions

- KiCad is selected for PCB work and Fusion is used for the enclosure. STEP is
  the mechanical exchange format; A8 uses horizontal input parts and an unqualified KLS speaker candidate; nominal frame/PSU fit passes, production qualification remains open.
- Which components have acceptable substitutes?
- How many input boards are required, and which functions and interfaces belong
  on the input and power/control boards?
- Can the A11 ADV7511 candidate be obtained through an eligible route and preserve DD+ carrier/JOC payload during ARC-only operation? If not, a different documented front end or module is required before fabrication.
- What are the internal height datum, rear gap and connector service volumes?
  How will the A8 supports and recessed RCA perform in sample-fit/load/temperature checks? How should the current Ø4.5 frame holes
  be reconciled with the nominal Ø3.8 fastening baseline, and 2 mm frame CAD with the 3 mm material baseline?
- How does manufacturer adjacent-heat-source guidance apply to the proposed
  compact PSU/input-board/amplifier arrangement?
- How should the local touch interface relate to the existing Open Cinema UI?
- What safety, regulatory, thermal, acoustic, and reliability constraints apply?

