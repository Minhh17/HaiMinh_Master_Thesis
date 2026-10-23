# Debug firmware và SoC

Trạng thái: **NOT RUN**. Cần board approved, bitstream phù hợp, OpenOCD >=0.12,
RISC-V GDB, firmware ELF còn symbols và USB/JTAG được host truy cập.

Tại demo checkout, chọn OPENOCD_CFG đúng board rồi mở terminal thứ nhất:

```sh
./util/load_demo_system.sh halt ./sw/c/build/demo/hello_world/demo "$OPENOCD_CFG"
```

Loader ở chế độ halt giữ phiên OpenOCD. Nếu mở OpenOCD thủ công,
`openocd -f "$OPENOCD_CFG"` là lựa chọn thay thế; không mở hai process cùng JTAG.
Terminal thứ hai:

```sh
riscv32-unknown-elf-gdb ./sw/c/build/demo/hello_world/demo
```

Trong GDB:

```text
target extended-remote localhost:3333
monitor reset halt
load
break main
continue
info registers
x/8i $pc
stepi
```

Lưu transcript cho reset/halt, breakpoint, PC/register trước-sau và lệnh thành công.
`load` ghi RAM trên board, chỉ chạy khi đã chọn đúng thiết bị/ELF.
Kết quả UART không tự chứng minh breakpoint hoặc single-step hoạt động.

| Hiện tượng | Kiểm tra tiếp |
| --- | --- |
| Không thấy adapter | Cable, USB passthrough, quyền device, config đúng board |
| TAP/ID không khớp | Board/FPGA target thực, bitstream, JTAG chain; dừng trước ghi tiếp |
| ELF không load | Linker map, RAM range, firmware build revision, OpenOCD log |
| PC không tới main | Reset/boot vector, startup/linker, symbols, clock/reset |
| UART lỗi ký tự | Clock/baud, đúng UART route và device |
| Timer đứng | Clock/reset, interrupt enables, vector/handler, wfi wakeup |
| Sim đúng nhưng board sai | XDC/pinout, CDC/reset, timing, init image; không sửa ISA vội |

Trong simulation, dùng FST để xem request/grant/response, PC và MMIO; grant là
nhận request, rvalid mới là response. Cần đối chiếu pin của core, tránh lấy
interface docs mới làm đặc tả cho revision cũ.

Nguồn: [upstream debug](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/README.md),
[loader source](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/util/load_demo_system.sh).
