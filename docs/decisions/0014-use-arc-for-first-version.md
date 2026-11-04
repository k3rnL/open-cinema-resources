# 0014 — Use standard ARC for the first version

- Date: 2026-11-04
- Status: Accepted by owner; implementation and interoperability unvalidated
- Source: owner accepted the ARC format trade-off and said, “Let's do with ARC for now.”
- Partially supersedes [0003](0003-prefer-earc-and-lvds-input-architecture.md) and [0012](0012-require-lossless-audio-and-atmos.md): HDMI transport scope and initial lossless requirement only.
- Preserves [0013](0013-pi-source-control-and-future-hat.md): Pi source control, unchanged payload, Pi processing and USB amplifier output.

## Decision and rationale

Target **standard HDMI ARC** for the first working rear input board. Defer eARC because obtaining implementation-ready receiver documentation and validating lossless output/capture proved too burdensome for this iteration.

Keep two optical inputs, one coaxial input and one selected source at a time. The HDMI port receives audio returned by a TV; this does not add a conventional HDMI source input or video passthrough.

Rear electronics receive, select and transport. All audio decoding, Atmos processing and DSP remain on Raspberry Pi 5, using the intended pcm-auto-decoder pipeline. Processed output reaches the amplifier over USB. No rear-board decoder/renderer is planned.

## First-version transport targets

| Incoming format over HDMI ARC | Target |
|---|---|
| Stereo PCM | Preserve unchanged |
| Dolby Digital / AC-3 | Preserve encoded payload unchanged |
| Conventional DTS core | Preserve unchanged, subject to TV passthrough |
| Dolby Digital Plus / E-AC-3 | Preserve unchanged, subject to source/TV capability |
| Atmos carried by DD+ / JOC | Preserve full DD+ payload including Atmos metadata; required qualification case |
| Multichannel PCM 5.1 / 7.1 | Deferred with eARC |
| Dolby TrueHD, including TrueHD Atmos | Deferred with eARC |
| DTS-HD Master Audio and lossless DTS:X | Deferred with eARC |
| Dolby MAT, including MAT Atmos | Deferred with eARC |

This is an accepted target matrix, not tested compatibility. It does not promise DD+/DTS passthrough from every TV, nor prove Atmos rendering on the Pi. It does not restrict files/network audio received directly by the Pi or reduce the owner's 5.1 output with optional 7.1 system direction.

An unsupported source may provide a compatible alternative; the receiver cannot reconstruct information lost upstream. Never advertise unsupported formats or describe a converted fallback as the original lossless stream.

## Implementation consequences

- Qualify an ARC physical receiver, HDMI/CEC control, source selection and status reporting. No chip/module is selected by this decision.
- The first-version audio link can use one data lane plus bit/frame clocks over three LVDS pairs. Encoded surround in a two-slot carrier is not a two-speaker limit after decoding.
- Keep A10's additional-lane provision until the next electrical revision is settled. No footprint/harness reduction is authorized by this scope note alone. Future eARC is not guaranteed to be a drop-in or firmware-only upgrade.
- Preserve lock/carrier-rate/transport-format distinctions and source-change handling. Test DD+ at its actual carrier rate and packing, not just the decoded programme rate.
- Retain the horizontal board, connector/mounting datums and owner-designed backplate/brackets.
- eARC/HBR/MAT qualification no longer blocks the ARC prototype. ARC circuitry, CEC, protection, routing, capture and physical testing still do.

## Implementation boundary

A10 remains an unrouted optical/coax + mux + LVDS draft with an unwired HDMI socket. The requirement change does not implement ARC. See the [ARC implementation contract](https://github.com/k3rnL/open-cinema-hardware/blob/main/docs/arc-v1-requirements.md).

## Evidence

- Owner discussion in this chat, 2026-11-04: explicit ARC acceptance after reviewing exclusions.
- [Sony format table](https://helpguide.sony.net/ht/2089/v1/en/contents/119_Supported_Audio_Formats_2089.html): published ARC/eARC format distinction.
- [Dolby DD+ Atmos delivery](https://ott.dolby.com/OnDelKits/DDP/Dolby_Digital_Plus_Online_Delivery_Kit_v1.5/Documentation/Playback/Interactive_test_procedure_help/help_files/topics/c_joc.html): DD+ Atmos transmission via ARC.
- [Sonos format/container explanation](https://support.sonos.com/en-gb/article/supported-home-theater-audio-formats): MAT/high-bandwidth formats require eARC on the TV-return path.
- [Transition work log](../worklog/2026-11-04-arc-first-version.md).
