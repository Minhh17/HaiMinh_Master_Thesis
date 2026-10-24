# Roadmap luận văn

> Cập nhật 24/10/2026: đây là bản tham chiếu lúc khởi tạo. Kế hoạch/trạng thái đang dùng nằm trong [tracker Excel](Project_Tracker_HK1_Nguyen_Hai_Minh.xlsx); báo cáo tuần dùng Word theo [planning index](README.md). Học viên tự cài môi trường, agent không tự chạy Make/test/build. Khi có khác biệt, ưu tiên tracker đã được học viên cập nhật.

Cập nhật: 2026-10-23. Trạng thái pha dưới đây mô tả phạm vi đang được mở; trạng thái từng việc chỉ ở [backlog](backlog.md). `VERIFIED` chỉ dùng khi gate có bằng chứng kiểm tra, không phải khi đã có tài liệu kế hoạch.

| Pha | Trạng thái | Mục tiêu và giới hạn | Gate để kết thúc/mở pha tiếp |
| --- | --- | --- | --- |
| Phase 0 — workspace | VERIFIED | Khung repo local, hướng dẫn, pin strategy, doctor, kiểm tra độc lập FPGA | P0-01 đã có [validation](../docs/reports/workspace-validation-2026-10-23.md); không bao gồm engineering build |
| Phase 1 — baseline Ibex FPGA | ACTIVE | SoC tối thiểu, bare-metal C, mô phỏng, GPIO/UART/timer/interrupt/debug, đo baseline | P1-16 có baseline tái dựng, trace kiểm chứng, giới hạn và báo cáo phần cứng |
| Phase 2 — software DSP baseline | PLANNED | Kernel đại diện, reference model, dataset hợp lệ, quy trình đo có kiểm soát | Sai số đúng ngưỡng định trước; baseline, provenance và bottleneck đo được |
| Phase 3 — accelerator comparison | DEFERRED | Chỉ thử custom instruction/tightly coupled hoặc MMIO khi có câu hỏi đủ hẹp | So sánh cùng workload, độ chính xác, cấu hình, chi phí và overhead |
| Phase 4 — đóng góp kiến trúc | DEFERRED | Giả thuyết có thể bác bỏ; gap đối chiếu bài gốc | Bằng chứng lặp lại, đối chứng đủ mạnh, giới hạn và threats to validity |
| Phase 5 — luận văn/paper | PLANNED | Lập dàn ý từ đầu, bản thảo kết quả sau khi có evidence | Kết luận truy ngược đến run/source, kiểm tra trích dẫn và phản biện |

**Phase 1 không triển khai accelerator, custom DSP instruction, ADC/RF chain hoặc ứng dụng radar.** Tạo cấu trúc cho pha sau không phải kích hoạt pha đó. Ibex là lựa chọn ưu tiên cần kiểm chứng; board vẫn TBD. Vivado **CONFIRMED BY USER**, khả năng chạy trong môi trường agent phải dựa trên doctor/check thực tế.

Các gate quan trọng: môi trường → simulation/firmware → board/constraints → implementation/timing → physical bring-up → baseline tái dựng. Nút board có thể nghiên cứu song song với simulation nhưng không được bỏ qua trước build FPGA.

Thời gian W1–W8 là mục tiêu kế hoạch 2026-10-21 đến 2026-12-15, xem [Phase 1](phase1-plan.md). Khi thiếu board hoặc tool, tiếp tục phần học, nguồn và simulation được phép; không chuyển kết quả BLOCKED thành PASS để giữ lịch.
