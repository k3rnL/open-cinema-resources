# Rear-input architecture: manufacturer evidence

- Reviewed in the design discussion and recorded: 2026-11-03
- Scope: technical references supporting the
  [audio-input topic](../../../docs/reference/topics/digital-audio-input.md) and
  [rear-panel topic](../../../docs/reference/topics/rear-panel-interface.md).
- These are linked manufacturer documents, not locally archived revisions or
  proof that the assembled Open Cinema design works. Download URLs may change.

| Source | Supported point and boundary |
| --- | --- |
| [HDMI Licensing Administrator: eARC](https://www.hdmi.org/spec2sub/enhancedaudioreturnchannel) | eARC supports uncompressed multichannel and higher-bandwidth audio. Require both eARC and ARC support explicitly in the selected receiver; do not infer every codec is implemented by the Pi. |
| [Explore Microelectronics EP92H1](https://www.epmi.com.tw/hdmi-arc-earc/ep92h1/) | Example of a receiver offering eARC/ARC and digital I2S/S/PDIF output functions, including eight-channel LPCM capability. Illustrative candidate only; availability, detailed documentation, firmware and integration have not been qualified. |
| [NXP UM11732, I2S bus specification, Rev. 3.0 (2022-02-17)](https://www.nxp.com/docs/en/user-manual/UM11732.pdf) | I2S carries data, bit clock and word select between ICs. It does not define this project's cable, connector or LVDS pinout. |
| [Raspberry Pi: Using the I2S peripherals on Raspberry Pi SBCs, Release 1](https://pip-assets.raspberrypi.com/categories/1259-audio-camera-and-display/documents/RP-009699-WP-1-Using%20the%20I2S%20peripherals%20on%20Raspberry%20Pi%20SBCs.pdf) | Pi 5 exposes four data lanes and producer/consumer choices on shared GPIO pins. The guide states TDM is unsupported. Custom capture still needs appropriate device-tree/driver configuration and testing. |
| [TI DS90LV047A, SNLS044D (July 2016)](https://www.ti.com/lit/ds/symlink/ds90lv047a.pdf) | Quad logic-to-LVDS driver with a 3.3 V supply. Candidate, not selected BOM authority. |
| [TI DS90LV048A, SNLS045C (July 2016)](https://www.ti.com/lit/ds/symlink/ds90lv048a.pdf) | Quad LVDS-to-logic receiver; balanced interconnect, matched nominal 100 ohm termination, layout, common-mode range and skew need attention. Differential signalling does not provide galvanic isolation. |
| [Analog Devices: transmitting I2S using MAX9205/MAX9206](https://www.analog.com/en/resources/design-notes/transmitting-i178s-audio-streams-in-automotive-applications-using-the-max9205max9206-lvds-serdes.html) | Established example transporting up to four I2S streams through an LVDS serializer/deserializer. Its single-pair serialization circuit is different from the proposed parallel six-pair link. |
| [Audial S5b manual, revision 0](https://www.audialonline.com/static-files/s5/s5b_user-manual_rev0.pdf) | Commercial example of LVDS I2S using an HDMI-shaped connector. The manual distinguishes it from HDMI protocol; it is not an eARC extractor or evidence of our eight-channel compatibility. |
| [Cirrus WM8804 datasheet, Rev. 4.5](https://statics.cirrus.com/pubs/proDatasheet/WM8804_v4.5.pdf) | One received S/PDIF stream, clock recovery and serial audio interface; non-audio detection is not Dolby/DTS decoding. [Lifecycle page](https://www.cirrus.com/products/wm8804) lists the part as discontinued. |
| [MEAN WELL UHP-500(R) specification, 2025-08-01](https://www.meanwell.com/Upload/PDF/UHP-500%28R%29/UHP-500-spec.pdf) | Dimensions, thermal mounting/derating and typical efficiency. See the [PSU topic](../../../docs/reference/topics/mean-well-uhp-500.md) for the reference plate and calculated heat estimate. This is newer than the local 2019 PDF. |
| [MEAN WELL enclosed-type installation manual](https://www.meanwell.com/Upload/PDF/Enclosed_Type_EN.pdf) | Includes the UHP family; ventilation openings must remain unobstructed. Its 10-15 cm adjacent-heat-source guidance needs resolving for this compact assembly, not treating as a universal measured clearance for our input PCB. |

## Evidence still absent

No selected receiver module documentation package, complete schematic, defined
cable assembly, PCB layout, validated GPIO allocation, capture configuration,
measured signal integrity, closed-enclosure thermal result or compliance result
is available for this proposed input architecture.
