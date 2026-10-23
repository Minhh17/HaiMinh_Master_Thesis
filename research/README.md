# Nghiên cứu và bằng chứng

Trạng thái 2026-10-23: **PROVISIONAL**. Phase 1 tập trung đưa SoC Ibex lên FPGA và xác lập baseline; chưa có đóng góp kiến trúc hoặc kết quả DSP được chứng minh.

| Cần làm | Nguồn chuẩn |
|---|---|
| Đặt câu hỏi có thể kiểm chứng | [Research questions](research-questions.md) |
| Chuyển ý tưởng thành giả thuyết có thể bác bỏ | [Hypotheses](hypotheses.md) |
| Phân biệt thiếu hiểu biết với khoảng trống nghiên cứu | [Gap register](research-gaps.md) |
| Tra cứu bài đã đọc, danh tính và độ chắc chắn | [Literature workflow](literature/README.md) |
| Lập kế hoạch rồi ghi nhận thí nghiệm | [Experimental runs](../experiments/README.md) |
| Viết luận văn từ bằng chứng | [Thesis outline](../thesis/outline/outline.md) |

Quy trình: xác định câu hỏi → tìm nguồn gốc → ghi note có vị trí bằng chứng → đối chiếu literature matrix → đăng ký phương pháp đo trước khi chạy → lưu run và checksum → viết kết luận giới hạn theo dữ liệu. Mọi kết luận phải phân loại `EXTERNAL CITATION`, `HYPOTHESIS`, `SIMULATION`, `FPGA MEASUREMENT` hoặc `INFERENCE`.

`research/experiments/` chỉ mô tả thiết kế nghiên cứu; cấu hình, dữ liệu và kết quả từng lần chạy có một nơi lưu duy nhất trong `experiments/`. Không chép PDF có bản quyền vào Git. Việc có URL công khai không chứng minh quyền phân phối lại.
