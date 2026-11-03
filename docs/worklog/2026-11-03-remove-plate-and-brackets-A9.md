# 2026-11-03 — Remove backplate and L brackets from the PCB model

The owner explicitly took responsibility for the backplate and L brackets and requested their removal from the PCB model. This supersedes the assistant-proposed supports in the A8 fit study; it does not change the horizontal PCB/direct-solder requirement in decision 0011.

A9 exports contain only the PCB and connectors: one component, 67 solid bodies. Exactly three enclosure solids were removed. The four Ø3 PCB holes at x±110 mm, inward depths 12/30 mm remain; the former vertical holes were in the removed plate/brackets and are now owner-side mechanical references only. No KiCad board or connector placement change was made.

STEP and F3D were reimported and all retained solid volumes/bounding boxes matched the previous board-only export. The native source component had only the three identified solids removed; remaining body volumes were unchanged. Source cloud save remains pending at v2, while the standalone exports are verified. Pre-removal and updated-source private archives were retained without closing or discarding the modified source.

Hardware revision: **cca850974a5c3060e4bc8d971570bd204b7b031f**. [A9 implementation and evidence](https://github.com/k3rnL/open-cinema-hardware/blob/cca850974a5c3060e4bc8d971570bd204b7b031f/docs/pcb-only-assembly-A9.md). Prior [A8 experiment](2026-11-03-horizontal-rear-io-A8.md) is historical for support geometry. Speaker current qualification and sourcing remain unresolved.
