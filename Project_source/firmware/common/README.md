# Startup, linker và hỗ trợ dùng chung

Chưa fork startup/linker. Baseline dùng `sw/common/link.ld` và support library
upstream. Nếu cần thay, ghi boot/entry, RAM/stack regions, vector/CSR setup và
ISA/ABI rồi kiểm tra map/disassembly; không tạo linker script bằng suy đoán.
