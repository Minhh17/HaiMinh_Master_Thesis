# Hardware do workspace sở hữu

Phase 1 tái sử dụng RTL ở checkout demo theo [lock](../third_party/upstream.lock.json);
chưa có RTL tùy biến. Tài liệu implementation ở [system context](../docs/architecture/system-context.md).

- `rtl/`: module do luận văn viết khi có task/test rõ.
- `ip/`: mô tả IP tích hợp và provenance; không copy vendor IP.
- `constraints/`: diff constraints đã review sau quyết định board.
- `integration/`: hợp đồng nối bus/interrupt/reset và checklist thay đổi.

Thêm RTL phải có yêu cầu, interface, test và ảnh hưởng baseline; không thêm
accelerator/custom instruction ở Phase 1.
