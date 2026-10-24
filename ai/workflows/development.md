# Development workflow

1. Đọc AGENTS/context/state, chọn task trong tracker và viết acceptance criterion quan sát được.
2. Đọc source/ADR liên quan; kiểm tra working tree và pin trước sửa. Không đoán memory map.
3. Thực hiện một thay đổi nhỏ trong source của workspace; upstream có patch riêng và provenance.
4. Học viên tự cài môi trường. Chỉ chạy test/build khi người dùng yêu cầu rõ; không tự chạy
   các target Make để làm việc tài liệu. Ghi NOT RUN nếu chưa có kết quả thực thi.
5. Ghi kết quả/minh chứng thật; cập nhật tracker/state/next actions/handoff khi cần.
   Tạo commit bằng identity đã có nếu phù hợp; không push khi chưa có quyền.
