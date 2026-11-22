# 0016 — Mount the two Cliff FE6930 blocks on the rear plate

Accepted by the owner on 2026-11-22.

Two Cliff FE6930 blocks mount to the removable rear plate. The amplifier feeds six independent speaker pairs directly. Two more pairs are available. The horizontal A13 input PCB measures 115 × 39.8 × 1.6 mm.

Each eight-contact block provides four speaker pairs. Use a separate positive and negative conductor from each amplified channel. The rear I/O schematic and copper carry the digital inputs, source selection, power/control and LVDS. USB remains the Pi-to-amplifier connection. The plate and its brackets belong to the enclosure design.

This updates the speaker mounting in [decision 0011](0011-horizontal-pcb-with-all-connectors.md) and confirms the part and spare capacity from [decision 0010](0010-select-cliff-fe6930-and-two-spare-pairs.md). It resolves the selection left open in [decision 0015](0015-retain-adv7511-lcsc-source.md).

Cliff specifies 7 A at 60 V AC. Each housing spans 65 × 30 mm including the ears, with two nominal Ø2.5 mm bores on 58 mm centres. The rear contacts are straight pins. Harness support, physical sample fit and panel machining clearance need review. [Cliff drawing, issue 2](https://www.cliffuk.co.uk/products/springterminals/FE6930.pdf)

The pair model uses 68 mm centre spacing as a proposed fit. The hardware repository provides a single block for independent positioning, the positioned pair and the populated input board. [A13 models and drawings](https://github.com/k3rnL/open-cinema-hardware/tree/499283356c8b014503ae0398ba6dab9f6dd46854/boards/rear-io-A13)
