# Current state — 2026-10-23 (Asia/Phnom_Penh)

Active phase: Phase 1 preparation; khung Phase 0 đã kiểm tra. Không có engineering baseline.
Nguồn yêu cầu: spec v1.1. Repository local `riscv-ibex-thesis`, branch `workspace/bootstrap`;
Revision của bản đang dùng: `git rev-parse HEAD`; validation được chạy trên working tree
bootstrap trước initial commit. Không tạo tag hardware baseline.

Đã có infrastructure, planning WP1–6/CA01–08, templates, official-source guides và upstream
immutable pins. Đã chạy `make help`, `make doctor`, `make check` PASS cho phạm vi workspace.
Xem [report](../docs/reports/workspace-validation-2026-10-23.md) và
[verification matrix](../docs/verification/verification-matrix.md) cho phạm vi chính xác.

Vivado **CONFIRMED BY USER — trên server**, không phải máy local agent; chưa có server access,
version/edition/license/device-support/path. Người dùng yêu cầu chỉ tạo khung,
để phần server ở trạng thái chuẩn bị; chưa yêu cầu cài toolchain/chạy build.
Board TBD; không tự chọn/mua. Local có Verilator 4.028 và GCC 9.3.0 RV64 multilib;
isolated RV32 compile PASS, upstream build chưa chạy. Xem [tool inventory](../tools/tool-versions.md).

Blockers: chưa clone upstream (cần quyền tải), thiếu FuseSoC và prefix compiler upstream,
chưa chọn board/record Vivado server, chưa có OpenOCD/GDB/probe. Simulation/FPGA/hardware NOT RUN.
Không dataset download, không remote repo/push, không tự chọn license hoặc tạo citation giả.

ADRs: [repository design](../docs/decisions/ADR-0001-workspace-architecture.md),
[Ibex preferred, board TBD](../docs/decisions/ADR-0002-ibex-preferred-board-tbd.md).
Trạng thái task: [backlog](../planning/backlog.md). Tiếp tục: [five actions](next-actions.md).
