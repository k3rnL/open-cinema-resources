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
- [x] Record the working eARC/ARC and I2S-over-LVDS input architecture direction
- [ ] Import the current enclosure CAD and mechanical constraints
- [ ] Confirm exact component variants, power tree, wiring, and cooling design
- [ ] Design the front panel and select its display, encoder, and power button
- [ ] Design the back panel and select its connectors and controls
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

- Which CAD and electronics tools are authoritative?
- Which exports are required for collaborators without the source tools?
- Which components have acceptable substitutes?
- How many input boards are required, and which functions and interfaces belong
  on the input and power/control boards?
- Which exact eARC/ARC receiver, controller and audio formats can be supported
  end to end by the existing software? Does it absorb the WM8804's S/PDIF role?
- What are the internal height datum, rear gap, connector service volumes and
  meaning of the requested six speaker connections?
- How does manufacturer adjacent-heat-source guidance apply to the proposed
  compact PSU/input-board/amplifier arrangement?
- How should the local touch interface relate to the existing Open Cinema UI?
- What safety, regulatory, thermal, acoustic, and reliability constraints apply?

