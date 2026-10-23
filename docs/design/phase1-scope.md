# Phạm vi Phase 1

Mục tiêu: tái lập một baseline Ibex Demo System, chạy C bare-metal trên FPGA đã
được lựa chọn, kiểm chứng UART/GPIO/timer/interrupt/debug và ghi tài nguyên/timing.
Hiện chỉ workspace và nguồn tham chiếu được chuẩn bị; không có baseline phần cứng đã xác nhận.

| ID | Yêu cầu | Bằng chứng hoàn thành |
| --- | --- | --- |
| P1-ENV | Môi trường/tool versions và source pins rõ | Doctor, version log, lock, lệnh tái lập |
| P1-SIM | Build RTL + firmware, quan sát chạy | Build log, ELF hash, output/waveform có kiểm tra |
| P1-FPGA | Build cho board được duyệt | ADR board, constraints provenance, timing/DRC, bitstream hash |
| P1-IO | UART TX/RX, GPIO input/output | Test case và log/ảnh đúng board, không suy từ simulation |
| P1-IRQ | Timer/interrupt hoạt động | Firmware revision, số lần/timestamp, expected vs observed |
| P1-DBG | OpenOCD/GDB halt/step/registers | Phiên debug có transcript |
| P1-BASE | Rebuild và baseline được review | Run manifest, source revision, report, tag sau khi đạt gate |

Giữ cấu hình demo mặc định trước khi tối ưu. Mọi thay đổi ISA, firmware flags,
clock, memory hoặc peripherals phải được ghi vào run manifest. UART print trong
vùng đo sẽ làm sai thời gian benchmark; Phase 1 chưa tuyên bố performance.

Ngoài phạm vi: custom instruction, MMIO accelerator, radar application, ADC/RF,
DMA thiết kế mới, Linux port, so sánh novelty/energy chưa có thí nghiệm.
PWM/SPI hiện diện ở upstream nhưng không tự thêm vào tiêu chí bắt buộc.

Traceability: ID trên → backlog/work package → ADR → commit → test trong
[verification matrix](../verification/verification-matrix.md) → run metadata → report.
Quyết định hiện tại: [ADR-0001](../decisions/ADR-0001-workspace-architecture.md),
[ADR-0002](../decisions/ADR-0002-ibex-preferred-board-tbd.md).
