# Work log: Enclosure requirements update

- Date: 2026-11-02
- Contributor: `@k3rnL`
- Related: [enclosure reference](../reference/topics/enclosure-appliance.md),
  [24 V supply decision](../decisions/0002-select-24v-main-supply.md)

## Source observations

- The 24 V UHP-500 output version is chosen for compatibility with the amplifier.
- A basic Raspberry Pi cooling fan has already been purchased.
- The front panel is not designed. It needs a touch screen, encoder, and power
  button. The Waveshare 7.9inch DSI LCD is a probable display candidate.
- The back panel is not designed and its components are not selected.
- Input-side logic is needed before the Raspberry Pi performs the main processing.
- A power/control board is also needed for delegated functions, including main
  power shutdown and infrared control.
- Local screen software has not started.

## Classification

- The 24 V selection is recorded as an accepted decision.
- The purchased fan is recorded as inventory with incomplete identification.
- The Waveshare display is recorded as a candidate, not a selected component.
- Front/rear panel work, controls, auxiliary boards, and local UI are recorded as
  open requirements and roadmap work.

## Next evidence needed

- Fan photographs, markings, invoice/SKU, dimensions, and mounting arrangement.
- Waveshare display mechanical drawing and a landscape Pi 5/Trixie integration
  check.
- Front and rear panel requirements and preliminary layouts.
- Input list, power/control functional breakdown, power tree, and board-boundary
  decision.
- Local screen-software requirements and relationship to `open-cinema-ui`.
