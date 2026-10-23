# Báo cáo FPGA gọn, có nguồn

Chưa có kết quả. Khi có run thực, tạo `<run-id>.md` với các trường sau:

| Trường | Giá trị phải ghi |
| --- | --- |
| Status | NOT RUN / BLOCKED / FAIL / PASS với tiêu chí rõ |
| Source | Workspace commit, demo pin, patch/config digest |
| Hardware | Board/revision, device part, target, clock constraints |
| Tools | Vivado version/edition, FuseSoC/Edalize, host OS |
| Firmware | Commit, ELF/VMEM SHA-256, ISA/ABI/optimization |
| Commands | Cwd và command line đầy đủ, return code |
| Reports | Post-synth/post-route, WNS/TNS/hold, unconstrained paths, DRC, utilization có units |
| Artifacts | Raw log/report/bitstream paths và SHA-256; không nhúng binary |
| Hardware tests | Tách kết quả UART/GPIO/timer/JTAG và observation thực |
| Limits | Phần chưa chạy, điều kiện lỗi, hành động tiếp |

Lưu reports ngắn đã review vào Git; raw logs, DCP, .bit và output nặng ở ignored
build hoặc kho ngoài. Không có số đo thì ghi NOT RUN/unknown, không điền 0.
