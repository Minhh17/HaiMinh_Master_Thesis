# Năm việc kế tiếp

Ngày 2026-10-23. Trạng thái task chính thức: [backlog](../planning/backlog.md).

1. **P1-02 — Khi cần build, ghi cấu hình Vivado trên server.** Hiện để TBD theo yêu cầu người dùng;
   chưa cần truy cập server để dùng khung workspace. Sau này ghi version/edition/device support,
   chạy `make vivado-check` theo [Vivado runbook](../docs/guides/vivado-workflow.md).
   DoD: report không chứa license/host IDs, version PASS hoặc blocker chính xác.
2. **P1-01/P1-08 — So sánh/chọn board với người dùng.** Dùng [board candidates](../fpga/boards/candidates.json)
   và ADR template, cân nhắc giá/khả dụng, tài nguyên, JTAG/UART, support và Vivado edition.
   DoD: quyết định được người dùng xác nhận, `selected-board.json` cùng target/ADR; không tự mua.
3. **P1-03 — Lấy checkout và tạo môi trường build.** Sau khi được duyệt tải nguồn/package,
   chạy `make upstream`, cài theo [local setup](../docs/guides/local-setup.md), xác minh compiler
   RV32 đúng prefix. DoD: remote/HEAD đúng lock, tool inventory và dependency freeze có provenance.
4. **P1-04 — Build rồi thực thi firmware trong simulator.** Sau bước 3: `make sim`, chạy theo
   [simulation guide](../docs/guides/simulation.md), lưu UART output và lệnh/timeout. DoD:
   phân biệt build PASS và firmware behavior PASS; timeout đơn thuần không đủ bằng chứng.
5. **CA01–CA02 — Học và tự giải thích core/SoC, RV32I.** Đọc [knowledge index](../knowledge/README.md),
   vẽ đường đi một lệnh và một MMIO store; đối chiếu source pin. DoD: ghi giải thích bằng lời mình,
   giải bài tập, đánh dấu riêng nội dung đã tự xác nhận và còn chưa hiểu.
