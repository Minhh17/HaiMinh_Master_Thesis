# Memory map tham chiếu

Nguồn được đọc ngày 2026-10-23 tại demo commit
`d37beb753e19482eb054aefac73a27289bf72e47`; **source-derived, chưa đo hoặc mô phỏng**.

| Vùng | Base | Kích thước decode | Ghi chú |
| --- | --- | --- | --- |
| Simulation control | `0x00020000` | 1 KiB | Module chỉ instantiate dưới `VERILATOR` |
| RAM | `0x00100000` | 128 KiB | Code/data; boot input đặt tại base này |
| Debug | `0x1A110000` | 64 KiB | Debug module |
| GPIO | `0x80000000` | 4 KiB | Đọc input, ghi output; kiểm tra offsets ở driver |
| UART | `0x80001000` | 4 KiB | Baud parameter default 115200 |
| Timer | `0x80002000` | 4 KiB | Machine timer interrupt |
| PWM | `0x80003000` | 4 KiB | Không phải mục tiêu đo bắt buộc Phase 1 |
| SPI | `0x80004000` | 1 KiB | Không phải chuỗi ADC/RF |

Kích thước cửa sổ decode không bằng dung lượng thanh ghi thực. Không truy cập tùy
ý các địa chỉ chưa được định nghĩa; đọc RTL register map và C driver cùng revision.
Địa chỉ không hợp lệ và quyền truy cập cần test riêng.

Nguồn: [ibex_demo_system.sv](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/rtl/system/ibex_demo_system.sv).
Default clock parameter 50 MHz là tham số source, không phải kết quả timing.
Trước firmware riêng, đối chiếu `sw/common/link.ld`, startup và
`sw/c/common` trong checkout; không ghi lại linker script phỏng đoán.
