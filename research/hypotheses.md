# Giả thuyết — PROVISIONAL

Chưa có giả thuyết nào được kiểm chứng. Ngày lập: 2026-10-23. Mỗi giả thuyết cần ngưỡng hiệu ứng, số lần lặp và quy tắc loại mẫu được chốt trong kế hoạch trước khi thu dữ liệu.

| ID | Phát biểu có điều kiện | Cách bác bỏ / điều kiện kết luận | Yếu tố cần kiểm soát |
|---|---|---|---|
| H-01 / RQ-01 | Với một kernel/kích thước được chọn sau profile, tỷ lệ chu kỳ data movement đủ lớn để đáng nghiên cứu | Không đạt ngưỡng tỷ lệ đăng ký trước hoặc hiệu ứng không tách khỏi overhead đo | Compiler/flags, định dạng số, memory placement, workload hash |
| H-02 / RQ-02 | Có một miền kích thước đầu vào mà latency toàn tác vụ của MMIO nhỏ hơn phương án tightly coupled | Không tìm thấy miền đó trong phạm vi đã đăng ký; khoảng bất định chồng lấp ngưỡng hiệu ứng | Thuật toán, độ đúng, clock thực, số lần truyền, completion protocol |
| H-03 / RQ-03 | Thay đổi data movement giảm latency toàn tác vụ so với baseline tại ngân sách tài nguyên đã đặt | Giảm không đủ ngưỡng, vi phạm timing/tài nguyên hoặc làm sai kết quả | Cùng đầu vào/split, build seeds, đo compute và transfer riêng |

Ngưỡng số hiện để TBD có chủ ý; không chọn ngưỡng sau khi nhìn kết quả. Kết quả âm cũng được lưu. Không chuyển cycle giảm thành thời gian giảm khi tần số hai thiết kế khác nhau; không suy ra năng lượng từ latency nếu chưa đo hoặc có mô hình được kiểm chứng.

Liên kết: [questions](research-questions.md), [gaps](research-gaps.md), [experiment procedure](../experiments/README.md).
