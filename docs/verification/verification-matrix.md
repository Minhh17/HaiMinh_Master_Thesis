# Verification matrix — 2026-10-23

Source of truth cho trạng thái kiểm chứng, tách khỏi task [backlog](../../planning/backlog.md).
PASS cần evidence phù hợp đúng scope. BLOCKED = prerequisite ngăn chạy; NOT RUN = chưa thực thi.
Template: [test case](test-case-template.md). Board hiện TBD. Vivado trên server của người dùng.

| Test ID / task | Hạng mục | Acceptance evidence | Trạng thái hiện tại |
|---|---|---|---|
| WS-01 / P0-01 | Structure, docs/config, hygiene | `make check`, local links/config/required fields/ignore cases + tests | PASS, [validation report](../reports/workspace-validation-2026-10-23.md) |
| WS-02 / P1-02 | Tool inventory | `make doctor` và version report | PASS inventory; individual missing tools BLOCKED, [inventory](../../tools/tool-versions.md) |
| WS-03 / P0-01 | Utility regression | guard failures/relative links/ignore assertions | PASS, số test và output trong [report](../reports/workspace-validation-2026-10-23.md) |
| ENV-01 / P1-02 | Vivado executable | `vivado -version` trên đúng server | BLOCKED cho agent; USER-AVAILABLE / AGENT-NOT-VERIFIED |
| ENV-02 / P1-02 | RV32 isolated compiler probe | ELF32 object đúng ISA/ABI | PASS isolated compile; upstream link NOT RUN, [inventory](../../tools/tool-versions.md) |
| SIM-01 / P1-04 | RTL simulator build | pinned FuseSoC/Verilator command exits 0 | BLOCKED: checkout/FuseSoC/compiler prefix chưa có |
| SIM-02 / P1-04 | C firmware execution | UART output/oracle + source, command, time boundary | NOT RUN; build alone không chứng minh execution |
| SIM-03 / P1-07 | RTL waveform/load-store/branch | trace và expected transaction comparison | NOT RUN |
| FPGA-01 / P1-09 | Synthesis | pinned target, part/constraints, synthesis log | BLOCKED: board TBD; server config chưa ghi |
| FPGA-02 / P1-09 | Implementation | placed/routed design + DRC review | NOT RUN |
| FPGA-03 / P1-09 | Timing closure | constraints reviewed, setup/hold slack và unconstrained paths reviewed | NOT RUN |
| FPGA-04 / P1-09 | Bitstream | tool exit, output hash, matched source/target | NOT RUN |
| FPGA-05 / P1-10 | Physical bring-up | program/reset/boot/UART log trên đúng board | BLOCKED: board chưa chọn |
| PER-01 / P1-11 | GPIO output/input | stimulus/readback, pin mapping và polarity | NOT RUN |
| PER-02 / P1-11 | UART TX/RX | expected bytes, baud/framing và round-trip | NOT RUN |
| PER-03 / P1-12 | Timer/interrupt | controlled timer event, handler/count/ack evidence | NOT RUN |
| DBG-01 / P1-13 | OpenOCD/GDB | halt, register read, step, breakpoint on actual transport | BLOCKED: tool/probe/board chưa sẵn sàng |
| REP-01 / P1-15 | Reproducible rebuild | clean locked tree + commands/tool versions + output comparison | NOT RUN |
| REP-02 / P1-15 | Resource characterization | utilization report with config/clock/part and units | NOT RUN |
| BASE-01 / P1-16 | Tagged baseline v1 | approved matrix, limitations, linked run artifacts and Git tag | NOT RUN |
| CI-01 / P0-01 | GitHub Actions hosted run | successful remote workflow URL | NOT RUN — local-only repository |

Workspace tool PASS không chứng minh CPU correctness, timing hoặc novelty. Khi chạy test,
lưu record theo [experiment protocol](../../experiments/README.md), link artifact có hash và
cập nhật riêng từng hàng. Không thay số liệu thiếu bằng zero.
