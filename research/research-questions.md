# Câu hỏi nghiên cứu — PROVISIONAL

Ngày lập: 2026-10-23. Đây là câu hỏi để kiểm tra sau baseline, chưa là tuyên bố novelty. Phase 1 chưa triển khai DSP, custom instruction hay MMIO accelerator.

| ID | Câu hỏi | Giai đoạn và phép kiểm tra | Điều chưa biết |
|---|---|---|---|
| RQ-00 | Có thể tái tạo một baseline Ibex SoC chạy bare-metal và kiểm thử ngoại vi trên board đã chọn không? | Phase 1: build từ revision cố định; đối chiếu [verification matrix](../docs/verification/verification-matrix.md) và log trên board | Board, toolchain và trạng thái bring-up |
| RQ-01 | Trong kernel DSP đã xác định, chu kỳ chủ yếu nằm ở tính toán hay di chuyển dữ liệu? | Phase 2: profile baseline phần mềm, tách compute, copy và điều khiển; kiểm tra tính đúng | Kernel, kích thước dữ liệu, định dạng số và overhead đo |
| RQ-02 | Với cùng thuật toán và tiêu chí sai số, custom instruction hay MMIO cho độ trễ toàn tác vụ tốt hơn ở từng kích thước đầu vào? | Phase 3: hai thiết kế được chọn sau review; đo cả truyền dữ liệu, setup, tính toán và đọc kết quả | Chi phí tích hợp, tần số đạt được, bus và vùng nhớ |
| RQ-03 | Một thay đổi cụ thể vào data movement có giảm bottleneck đã đo mà vẫn đáp ứng tài nguyên/timing không? | Phase 4: ablation so với baseline và cấu hình chỉ thay đổi một yếu tố | Bottleneck chưa được xác định; chưa có đề xuất đóng góp |

Gate cho RQ-01–03: baseline Phase 1 có bằng chứng, bài liên quan đã kiểm tra toàn văn, dataset có quyền sử dụng rõ ràng và phương pháp đo tái lập được. Nếu dữ liệu không cho thấy bottleneck hoặc tài liệu đã giải quyết câu hỏi trong cùng điều kiện, thu hẹp hoặc bỏ câu hỏi.
