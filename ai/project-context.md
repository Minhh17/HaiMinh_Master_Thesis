# Project context

Nguồn yêu cầu: [spec v1.1](../IBEX_THESIS_WORKSPACE_SPEC_v1.1.md), ngày 2026-10-22.
Luận văn thạc sĩ Kỹ thuật máy tính, hướng RISC-V/FPGA và khả năng tối ưu data movement cho
workload DSP/radar về sau. Phase 1 chỉ xây baseline Ibex SoC trên FPGA với C firmware,
UART/GPIO/timer/interrupt và debug. Chưa chọn board, chưa kết luận Ibex tối ưu.

Người dùng có thể sử dụng Vivado trên server; version/edition/license/path để TBD theo
xác nhận 2026-10-23. Yêu cầu hiện tại chỉ tạo khung workspace, chưa cài toolchain/chạy build.
Không suy ra FPGA đã chạy từ việc Vivado được cài. Phase 1 dự kiến 2026-10-21–2026-12-15;
ngày lịch không tự hoàn thành milestone. Phase 2–5 chỉ được tổ chức để mở rộng.

Ngôn ngữ: tiếng Việt cho học tập/kế hoạch; identifiers và thuật ngữ kỹ thuật dùng tiếng Anh.
Monorepo local-first, remote private khi được duyệt. Không có Zotero/remote storage bắt buộc.
License phần tự viết còn chưa chọn. Build outputs, vendor tooling và raw data nằm ngoài Git.

Đọc [system context](../docs/architecture/system-context.md) và
[verification matrix](../docs/verification/verification-matrix.md) trước khi tuyên bố behavior.
