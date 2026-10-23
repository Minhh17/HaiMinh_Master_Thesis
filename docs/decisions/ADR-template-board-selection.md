# ADR-XXXX — Chọn FPGA cho baseline Phase 1

Trạng thái: TEMPLATE / chưa approve. Ngày, người quyết định: TBD.

1. Board/model/revision thực, nguồn xác nhận và khả năng tiếp cận: TBD.
2. Device part, target FuseSoC, top module, XDC upstream và commit: TBD.
3. Vivado version/edition, device support và quyền dùng license: TBD.
4. USB/JTAG/UART route, điện áp I/O, clock/reset, GPIO sử dụng: TBD.
5. So sánh ít nhất hai ứng viên: công sức bring-up, hỗ trợ, headroom, giá
   có ngày/nguồn nếu dùng; không tự đặt mua.
6. Lý do quyết định, phương án loại và giới hạn: TBD.
7. Bằng chứng source check / simulation / timing / hardware: tách riêng;
   trước chạy ghi NOT RUN, không dùng 0 thay số đo thiếu.
8. Kế hoạch smoke test, tiêu chí dừng và rollback: TBD.

Sau quyết định thật: tạo ADR có số mới, cập nhật
`fpga/boards/selected-board.json` với `status: "approved"`,
`board` đúng ID trong candidates, `target` đúng target và `adr` là đường dẫn
từ root tới ADR vừa tạo. Không approve bằng cách sửa JSON một mình.
Nếu đổi clock/constraints so với upstream, cần review riêng và version hóa diff.
