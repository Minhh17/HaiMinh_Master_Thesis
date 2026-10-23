# Thiết kế nghiên cứu

Nơi này dành cho lập luận phương pháp nối [research questions](../research-questions.md) với phép kiểm tra: vì sao chọn baseline, biến độc lập, metric, cách kiểm soát sai số và điều kiện bác bỏ giả thuyết.

Chưa có nghiên cứu thực nghiệm được thực hiện. Kế hoạch chạy, run IDs, cấu hình và kết quả lưu duy nhất ở [experiments](../../experiments/README.md). Dùng [experiment template](../../experiments/configurations/experiment-template.yaml), không tạo bản sao kết quả trong thư mục này.

Khi so sánh kiến trúc ở giai đoạn sau, chốt trước correctness tolerance, latency boundary, data-transfer inclusion, clock/tài nguyên, compiler, input split và cách báo cáo độ biến thiên. Ghi rõ phép đo FPGA khác simulation; không ghép chúng thành một bảng “đã xác thực” chung.
