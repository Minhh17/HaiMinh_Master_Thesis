# Đề cương luận văn — PROVISIONAL

Ngày lập: 2026-10-23. Tên đề tài cuối cùng và đóng góp chưa chốt. Không dùng tên đề tài khẳng định accelerator thành công trước khi có bằng chứng.

| Chương | Câu hỏi phải trả lời | Bằng chứng cần có |
|---|---|---|
| 1. Bối cảnh và mục tiêu | Vấn đề kỹ thuật, phạm vi và tiêu chí hoàn thành là gì? | Scope, RQ, constraints, nguồn gốc yêu cầu |
| 2. Cơ sở và công trình liên quan | ISA/core/SoC, FPGA và phương pháp hiện có liên quan thế nào? | Nguồn chính thức, literature matrix, notes toàn văn |
| 3. Nền tảng Ibex SoC và phương pháp | Vì sao chọn cấu hình/board; baseline được tái tạo thế nào? | ADR, upstream pins, memory map, tool versions, scripts |
| 4. Bring-up và xác thực baseline | Firmware/ngoại vi/debug hoạt động dưới điều kiện nào? | Verification matrix, logs trên board, build/timing/resource reports |
| 5. Khảo sát và đề xuất kiến trúc (có điều kiện) | Bottleneck hẹp nào đã được đo; thay đổi nào có căn cứ? | Profile baseline, gap review, hypothesis, design trade-offs |
| 6. Thực nghiệm so sánh (có điều kiện) | Kết quả đúng không, cải thiện bao nhiêu và giới hạn ở đâu? | Controlled runs, ablations, uncertainty, data provenance |
| 7. Kết luận và hướng tiếp | Điều nào đã được chứng minh, điều nào còn mở? | Claim-to-evidence, limitations, unresolved questions |

Chương 5–6 chỉ mở khi gate nghiên cứu được đáp ứng. Trong bản nháp ban đầu, ghi `CHƯA THỰC HIỆN`; không biến kế hoạch thành kết quả. Thống nhất cấu trúc chính thức với yêu cầu trường/người hướng dẫn trước khi chuẩn hóa định dạng.

Phụ lục dự kiến: tái lập môi trường, lệnh build/run, test matrix, dataset manifest, giới hạn truy cập artifact. Nội dung dài hoặc nhạy cảm không sao chép vào luận văn khi chưa có quyền.
