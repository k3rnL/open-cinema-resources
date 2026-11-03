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
- [x] Record the working eARC/ARC and I2S-over-LVDS input architecture direction
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
- [ ] Complete A8 back-panel supports, plate cutouts, cable insertion, tolerance, load and temperature qualification
- [ ] Define the input front-end and delegated power/control electronics
- [ ] Select/document an eARC/ARC receiver and validate multichannel Pi capture,
  supported encoded formats, source switching and the LVDS interconnect
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
- Which exact eARC/ARC receiver, controller and audio formats can be supported
  end to end by the existing software? Does it absorb the WM8804's S/PDIF role?
- What are the internal height datum, rear gap and connector service volumes?
  How will the A8 supports and recessed RCA perform in sample-fit/load/temperature checks? How should the current Ø4.5 frame holes
  be reconciled with the nominal Ø3.8 fastening baseline, and 2 mm frame CAD with the 3 mm material baseline?
- How does manufacturer adjacent-heat-source guidance apply to the proposed
  compact PSU/input-board/amplifier arrangement?
- How should the local touch interface relate to the existing Open Cinema UI?
- What safety, regulatory, thermal, acoustic, and reliability constraints apply?

