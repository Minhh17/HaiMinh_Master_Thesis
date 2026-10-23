# Tiêu chí test simulation

Thứ tự: compile firmware → compile RTL model → load ELF → kiểm tra output/PC →
self-checking UART/GPIO/timer test → lưu manifest. Phân biệt build PASS, quan sát
smoke và behavioral PASS. Timeout của hello-world vô hạn là dừng phiên, không
phải assertion pass. Theo dõi ở [verification matrix](../../docs/verification/verification-matrix.md).
