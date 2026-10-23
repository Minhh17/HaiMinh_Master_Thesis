# Development workflow

1. Đọc AGENTS/context/state, chọn task backlog và viết acceptance criterion quan sát được.
2. Đọc source/ADR liên quan; kiểm tra working tree và pin trước sửa. Không đoán memory map.
3. Thực hiện một thay đổi nhỏ trong source của workspace; upstream có patch riêng và provenance.
4. Chạy `make check` cùng test chuyên biệt. Khi RTL/tool thiếu, ghi BLOCKED; unit tests của
   workspace không thay thế simulation/hardware tests.
5. Ghi command, exit status, log, source revision; cập nhật backlog/state/next actions/handoff.
   Tạo commit bằng identity đã có nếu phù hợp; không push khi chưa có quyền.
