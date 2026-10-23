# Firmware bare-metal

Baseline hiện dùng `sw/c` trong demo checkout. Workspace chưa có application
riêng; không viết một chương trình giả rồi gọi là firmware Ibex đã chạy.

Compiler upstream dùng `riscv32-unknown-elf-gcc`, ISA `rv32imc`, ABI `ilp32`.
CMake build vào `sw/c/build`; xem [simulation guide](../docs/guides/simulation.md).
Không đổi optimization/ISA/clock giữa các lần đo mà thiếu manifest.

`apps/` dành cho chương trình thử riêng; `drivers/` chỉ dành cho driver bổ sung;
`tests/` cho self-checking test; `common/` cho startup/linker/support do ta sở hữu
khi thật sự cần. Dùng driver upstream trước khi viết lại.
