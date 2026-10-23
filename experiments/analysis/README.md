# Phân tích

Chưa có số liệu hoặc script phân tích. Khi có run, thêm script đọc metadata/results ở chế độ read-only và sinh bảng/hình từ lệnh được ghi lại. Pin dependency khi thêm thư viện; không yêu cầu notebook hoặc dashboard để chạy Phase 1.

Đơn vị, sample count, các run bị loại và quy tắc tổng hợp phải hiện trong output. Báo median/range hoặc uncertainty phù hợp thiết kế đo, không chọn một run thuận lợi. Speedup cần cùng boundary và tiêu chí correctness; time = cycles / clock chỉ hợp lệ khi clock và cách đếm đã được kiểm chứng.

Nguồn dữ liệu duy nhất: [results](../results/README.md). Report ghi script commit, input/output SHA-256 và command; hình luận văn dùng output đã truy vết.
