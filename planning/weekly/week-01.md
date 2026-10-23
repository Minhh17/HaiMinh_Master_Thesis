# W1 — 2026-10-21 đến 2026-10-27

Ghi nhận phiên đầu: **2026-10-23**. Đây là nhật ký/checklist tuần, không thay trạng thái trong [backlog](../backlog.md). Dấu tick chỉ nói hành động cụ thể đã làm; chưa xác nhận học viên đã hoàn tất CA01 hay hardware đã chạy.

Mục tiêu tuần: có nơi làm việc tái lập, biết core/SoC khác nhau thế nào, phát hiện tool blockers, chuẩn bị upstream và lần chạy simulator đầu. Ước lượng dưới đây là thời gian tập trung tham khảo, không bảo đảm thời hạn.

| Việc cụ thể | Task | Ước lượng | Đầu ra/checkpoint |
| --- | --- | --- | --- |
| Đọc README workspace, scope và flow dữ liệu | P0-01 | 30–45 phút | Biết đường dẫn code, planning, knowledge, experiment |
| Đọc nguồn Ibex + Demo System, ghi core vs SoC | P1-01/05 | 1–2 giờ | Sơ đồ tự vẽ, 3 câu hỏi chưa hiểu |
| Chạy `make help`, `make doctor`, `make vivado-check`, `make check` | P1-02 | 30–60 phút | Ghi exit status và path report; chia detected/tested/unknown |
| So sánh khả năng tiếp cận board và upstream target | P1-01/08 | 1–2 giờ | Shortlist có tiêu chí, chưa mua/chọn ngầm |
| Đọc hướng dẫn pin, xác minh URL/SHA/license và acquire khi được phép | P1-03 | 45–90 phút + tải/build tùy mạng | Checkout pin, không dùng nhánh main làm bằng chứng immutable |
| Thực hiện [simulation runbook](../../docs/guides/simulation.md) khi đủ prerequisites | P1-04 | 2–4 giờ dự phòng lỗi | Build và firmware output hoặc blocker kèm thông báo thật |
| Giải bài [fetch/decode/execute](../../knowledge/ibex-microarchitecture/rv32i-fetch-decode-execute.md) | P1-05 | 1–2 giờ | Bảng register/PC trước-sau, xác nhận giới hạn mô hình |
| Review tuần và chọn tối đa 3 việc W2 | P0-01 | 30 phút | Evidence, blockers, kế hoạch tiếp |

## Checklist thực tế tại thời điểm ghi nhận

- [x] Đọc specification v1.1 và xác định board vẫn TBD, Phase 1 chưa làm accelerator.
- [x] Agent mở nguồn chính thức về Ibex pipeline/IF/LSU, RISC-V ISA và Demo System để soạn hai starter notes có citation.
- [x] Có kế hoạch WP1–WP6, W1–W8 và learning modules CA01–CA08 trong workspace.
- [ ] Học viên đọc note, giải bài và sửa bằng ngôn ngữ của mình.
- [ ] Hoàn tất kiểm kê tool của máy sẽ build thực; xem handoff cuối phiên để biết lệnh agent đã chạy.
- [ ] Xác nhận pin bằng checkout thực và licenses.
- [ ] Có simulator build log và firmware execution log đáp ứng P1-04.
- [ ] Xác nhận board có thể dùng; ghi ADR trước FPGA build.

Không ghi lại trạng thái doctor/check ở đây để tránh lệch báo cáo cuối phiên; bằng chứng chạy được dẫn từ backlog/handoff. Các ô học viên và hardware chưa được tick thay người dùng.

## Câu hỏi cần giải quyết

1. Vivado ở server của người dùng; version/edition/path để TBD, ghi khi bắt đầu build.
2. Board nào người dùng đã có hoặc có thể mượn, và upstream target tương ứng có mức hỗ trợ nào?
3. Toolchain/FuseSoC/Verilator nào tương thích với revision Demo System được pin?

## Review cuối tuần — người học điền sau

Kết quả tự giải thích được: chưa ghi nhận. Evidence mới: bổ sung link run/note thật. Blocker còn lại và thay đổi lịch: đối chiếu backlog. Việc nhỏ đầu W2: gỡ prerequisite đầu tiên của P1-04 theo [next actions](../../ai/next-actions.md).
