# 0012 — Require lossless/Atmos transport; keep processing on the Raspberry Pi

- Date: 2026-11-03
- Status: Owner-accepted requirements and processing allocation; extraction hardware and interoperability unvalidated
- Source: owner requested broad TV compatibility, lossless formats and Atmos initially, then specified 5.1 with an option for 7.1 and clarified that all audio processing belongs on the Raspberry Pi.
- Refines [0003](0003-prefer-earc-and-lvds-input-architecture.md).

## Requirements and responsibility boundary

Target broad TV/source compatibility rather than tailoring the hardware to one TV. Lossless Dolby TrueHD, DTS-HD and Atmos are required in the initial working system. Keep eARC and explicit legacy ARC support. Broad compatibility does not promise unavailable formats from every TV: lossless return audio requires eARC and appropriate source/TV passthrough. Older ARC and optical/coax sources still need a usable fallback.

The owner explicitly clarified: **the rear electronics only extract/select/transport audio; all decoding, Atmos processing and DSP run on the Raspberry Pi.** Do not add a hardware Dolby/DTS decoder or renderer, or make choosing such a module a prerequisite for this PCB. The preceding question about rendering versus compatible channel playback does not change this allocation; its software behavior is outside the current extraction-board task. The full lossless/Atmos requirement has not been downgraded.

The owner selected **5.1 initially, with the option for 7.1**. Preserve an eight-channel system target. No height-speaker layout has been requested. Eight rear speaker pairs are a proposed use of the previously allowed two spare pairs; actual amplifier mode, channel mapping and output/subwoofer wiring still need qualification.

## Extraction-board design consequences

The proposed rear board receives HDMI eARC/ARC and the two optical plus one coaxial inputs, selects one source, and carries its audio and clocks to a small LVDS receiver adapter beside the Pi. Input protection, receiver control/negotiation, status reporting and local power conditioning belong to this hardware scope. DSP and audio decoding do not.

Preserve both multichannel PCM and encoded audio payloads without downmixing, volume changes, sample-rate conversion or truncation. Treat Atmos carried by Dolby Digital Plus, TrueHD and Dolby MAT as separate transport cases to validate; MAT must not be assumed identical to ordinary PCM capture. Do not funnel the eARC lossless path through an S/PDIF-only stage. A source selector may be shared logically while the different reception paths retain their required bandwidth and packing.

The earlier six-pair parallel LVDS proposal established an eight-channel PCM target, not proven HBR/MAT capture support. Before finalizing the receiver, connector pinout or routing, document its output lane mapping, audio clocks, maximum carrier rate, word widths/packing and status/control interface. Verify that the electrical link and Pi capture interface preserve the required payload. Pi-side codec implementation can progress separately; it is not a prerequisite to exploring board placement or extraction circuitry.

One four-layer rear PCB remains the preferred fit hypothesis, with a small LVDS receiver adapter beside the Pi. A mezzanine may be justified by mechanical fit or availability of a documented extraction module. Neither size nor a receiver/module is selected by this requirement. No separate decoder/renderer board is planned.

## Verified current software limitation — separate Pi work

Open Cinema's checked-in release manifest identifies pcm-auto-decoder v0.2.2, commit 5856a5ef035618a7284a91f80bdd4ac24afe3427. Read-only inspection of the pinned IEC61937 parser and decoder dispatch found PCM handling plus AC-3, E-AC-3 and DTS types I–III. The inspected code does not implement the complete TrueHD/DTS-HD transport and Atmos rendering path. This is a Pi software integration gap, not a reason to move decoding onto the rear board or a claim that every FFmpeg version or possible Pi implementation is incapable of these functions. No software changes were made during this hardware discussion.

Evidence:

- [Open Cinema manifest](https://github.com/k3rnL/open-cinema/blob/master/deployment/release-manifest.yml)
- [Pinned transport parser](https://github.com/k3rnL/pcm-auto-decoder/blob/5856a5ef035618a7284a91f80bdd4ac24afe3427/src/iec61937_detector.rs)
- [Pinned decoding implementation](https://github.com/k3rnL/pcm-auto-decoder/blob/5856a5ef035618a7284a91f80bdd4ac24afe3427/src/decoders.rs)

## Primary technical references

- [HDMI LA eARC overview](https://www.hdmi.org/spec2sub/enhancedaudioreturnchannel): multichannel PCM and lossless/Atmos transport capabilities.
- [Explore EP92H1](https://www.epmi.com.tw/hdmi-arc-earc/ep92h1/): example receiver supporting eARC/ARC, eight-channel LPCM, IEC61937 and HBR outputs. This is a capability example, not a qualified part; full output/register documentation and procurement remain to be checked.
- [Dolby Atmos soundbar architecture](https://professional.dolby.com/siteassets/tv/home/dolby-atmos/dolby-atmos-for-sound-bar-applications.pdf): distinct DD+, TrueHD and MAT decoding followed by rendering; those functions are allocated to the Pi in this project.
