# ADR-0002 — Ưu tiên Ibex Demo System; FPGA chưa chọn

- Ngày: 2026-10-23
- Trạng thái: ACCEPTED như hướng chuẩn bị; core và board cuối cùng vẫn có thể đổi
- Quyết định board: **TBD**, chưa mua, chưa approve

**Bối cảnh.** Phase 1 cần học CPU/SoC, C bare-metal, peripherals và debug trên FPGA.
Người dùng xác nhận Vivado ở server; không cần cài local trong giai đoạn này.
Agent chưa truy cập server, đường dẫn/version/license trên server chưa được ghi.

**Quyết định.** Dùng Ibex Demo System làm ứng viên baseline vì tài liệu chính thức
có flow Verilator/Vivado, UART/GPIO/timer và OpenOCD/GDB. Pin demo và Ibex đi kèm;
không lấy master của core mới thay vào demo. Lý do này là tính phù hợp với mục tiêu
học/bring-up, chưa phải chứng minh Ibex có hiệu năng hoặc diện tích tối ưu.

Arty A7-35T và Sonata được README upstream xếp nhóm hỗ trợ tốt; các board khác
được liệt kê là community/experimental. Không suy từ tên họ board rằng mọi
dung lượng FPGA/pinout đều được hỗ trợ.

**Phương án khác.** Ibex Simple System hữu ích cho simulation tối giản nhưng
không thay nhiệm vụ FPGA/debug của demo. Các core RISC-V khác có thể nghiên cứu
khi câu hỏi Phase 2/3 yêu cầu; hiện chưa có bảng đo công bằng để chọn theo performance.
Không triển khai song song nhiều SoC trong Phase 1.

**Điều kiện chọn board.** Board thực có thể tiếp cận, đúng revision/device;
target+XDC upstream phù hợp; Vivado có device support; JTAG/UART dùng được;
GPIO đủ cho test; chi phí/thời gian mua và headroom cho hướng tương lai được ghi.
Xem [candidate matrix](../../fpga/boards/README.md) và
[template ADR board](ADR-template-board-selection.md).
Chỉ khi có quyết định thật mới đổi `selected-board.json` thành approved.

Nguồn: [demo README cố định](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/README.md),
[Ibex example scope tại pin](https://github.com/lowRISC/ibex/blob/594ea976c9dad793f87edf91ec1c4c1df447e6dc/README.md).
