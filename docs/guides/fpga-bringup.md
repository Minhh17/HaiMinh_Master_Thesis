# Lab runbook: FPGA bring-up

Trạng thái: **BLOCKED — board TBD**. Checklist này dùng sau khi có ADR board,
môi trường build và bitstream đúng target; không ghi bước nào đã pass khi chưa chạy.

1. Ghi board/model/revision, clock/reset, nguồn cấp và interface dự kiến trong ADR;
   đối chiếu schematic/manual chính thức với XDC upstream. Kiểm tra USB/JTAG/UART
   route, quyền thiết bị và điện áp ngoại vi trước nối dây.
2. Chạy `make doctor`, `make vivado-check`, build firmware/simulation trước;
   resolve lỗi compile rồi mới chạy `make fpga BOARD=<approved-board-id>`.
3. Đọc timing/DRC/utilization theo [Vivado workflow](vivado-workflow.md).
   Lưu hash bitstream và source revision; không dùng bitstream không rõ nguồn.
4. Xác nhận đúng board đang nối, rồi program **chủ động** từ demo checkout:

```sh
fusesoc --cores-root=. run --target="$TARGET" --run lowrisc:ibex:demo_system
```

TARGET phải lấy từ JSON approved; `make fpga` chỉ build, không tự program.
Upstream cũng có Makefile target `pgm`; dùng chỉ khi đã xác định build directory
đúng target. Không chạy programming trong tool-independent CI.

5. Load firmware với OpenOCD config đúng board, tránh mặc định Arty trên board khác:

```sh
./util/load_demo_system.sh run ./sw/c/build/demo/hello_world/demo "$OPENOCD_CFG"
screen "$UART_DEVICE" 115200
```

Điền OPENOCD_CFG và UART_DEVICE từ thiết bị thực. Arty A7 upstream dùng
`util/arty-a7-openocd-cfg.tcl`; Sonata dùng `util/sonata-openocd-cfg.tcl`.
Không mặc định mọi `/dev/ttyUSB1` là board. Quyền USB nên xử lý bằng rule/group
phù hợp; không cần chạy toàn bộ flow như root.

6. Quan sát UART hello-world và timer value, gửi ký tự để kiểm tra RX/interrupt,
   thao tác GPIO input/output theo pinout, rồi chạy phiên GDB halt/step.
   Hello-world gộp nhiều chức năng; cần test riêng để kết luận từng yêu cầu.
7. Reset/power-cycle và tái nạp để kiểm tra baseline lặp lại. Ghi kết quả thực,
   expected/observed, firmware revision và điều kiện trong verification matrix.
   Dừng nếu JTAG ID/part/pinout không khớp, timing không đạt, hoặc log báo lỗi.

Nguồn lệnh: [README upstream tại pin](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/README.md),
[loader](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/util/load_demo_system.sh).
Debug chi tiết: [debugging.md](debugging.md). Bằng chứng:
[verification matrix](../verification/verification-matrix.md). Không có board
thì chỉ dừng tại preparation, không thay hardware observation bằng screenshot mô phỏng.
