# Nguồn kỹ thuật chính thức

Kiểm tra ngày 2026-10-23. Các liên kết revision cố định phục vụ baseline; các
manual latest có thể thay đổi, phải đối chiếu với pin và tool version thực.

| Nguồn | Dùng để xác nhận |
| --- | --- |
| [Demo README tại pin](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/README.md) | Build commands, prerequisites, phân loại board, debug |
| [Demo core file](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/ibex_demo_system.core) | Từng target, top, XDC, part và SRAMInitFile |
| [Demo RTL](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/rtl/system/ibex_demo_system.sv) | Memory map, wiring interrupt và module parameters |
| [Ibex vendor lock](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/vendor/lowrisc_ibex.lock.hjson) | Core nguồn revision 594ea976… |
| [Ibex manual](https://ibex-core.readthedocs.io/) | Đọc kiến trúc; xác nhận lại ở doc của pin khi mô tả implementation |
| [Labs tại pin](https://github.com/lowRISC/ibex-demo-system-labs/tree/5a2eec7ebd567a4ac763f4c1b971d191414ebe79) | Lab 1/2 cho bring-up, Verilator/waves; đường dẫn sw/build đã cũ |
| [lowRISC toolchain releases](https://github.com/lowRISC/lowrisc-toolchains/releases) | Toolchain RV32; chọn artifact/checksum có ghi revision |
| [AMD Vivado downloads](https://www.xilinx.com/support/download.html) | Installer hợp lệ; không đưa bộ cài/license vào Git |
| [AMD UG904 reports](https://docs.amd.com/r/en-US/ug904-vivado-implementation/Step-8-Run-Required-Reports) | report_timing_summary, report_utilization |
| [AMD UG904 open_checkpoint](https://docs.amd.com/r/en-US/ug904-vivado-implementation/open_checkpoint) | Mở DCP để phân tích |
| [AMD UG906 timing summary](https://docs.amd.com/r/en-US/ug906-vivado-design-analysis/Report-Timing-Summary) | Đọc báo cáo và kiểm tra timing sau route |

Lab 4 có custom instruction nhưng **deferred**: không thuộc Phase 1.
Không nhập số performance từ README upstream thành kết quả của luận văn.
Tài liệu tool phải khớp version được ghi trong [tool-versions](../../tools/tool-versions.md).
