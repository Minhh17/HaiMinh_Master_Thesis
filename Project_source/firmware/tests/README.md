# Test firmware

Thiết kế test độc lập cho UART TX/RX, GPIO input/output, timer và IRQ: mỗi test
ghi expected vs observed, firmware hash và môi trường sim/hardware. Test cần
timeout/kết thúc xác định; hello-world vô hạn chỉ là smoke observation.
Các test này chưa được viết/chạy; trạng thái ở verification matrix là NOT RUN.
