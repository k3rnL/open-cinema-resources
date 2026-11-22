# Compact A13 rear I/O fit study

On 2026-11-22 the owner selected two panel-mounted Cliff FE6930 speaker blocks and requested a compact input PCB for Fusion integration. [Decision 0016](../decisions/0016-panel-mounted-cliff-speaker-blocks.md)

A13 reduces PCB width from 228 to 115 mm at the original 39.8 mm depth. The four input sockets retain their coordinates. The speaker-side mounting holes move inward, giving a 97 × 18 mm pattern of four Ø3 mm holes. The hardware repository carries native Fusion and STEP files for one speaker block, the proposed pair and the populated PCB. The pair uses 68 mm centre spacing and leaves 5.658 mm to the closest modelled PCB solid. These dimensions are fit-study choices pending enclosure and sample approval. [A13 integration record](https://github.com/k3rnL/open-cinema-hardware/tree/499283356c8b014503ae0398ba6dab9f6dd46854/boards/rear-io-A13)

KiCad checked 399 retained pad connections and 1,512 tracks and vias. ERC, DRC, schematic parity and unrouted counts were zero. The physical harness, its fastening and the insert plate still need assembly review. The owner designs the plate and brackets.

With the plate datum on the current frame’s inner face, Fusion measured 19.70 mm from the bare clip pair to the PSU reference and 4.50 mm to the frame. The PCB-to-frame gap was 0.452 mm. Review this tight clearance when assigning plate and bracket tolerances. [Enclosure check](https://github.com/k3rnL/open-cinema-hardware/blob/499283356c8b014503ae0398ba6dab9f6dd46854/boards/rear-io-A13/exports/enclosure-fit.json)
