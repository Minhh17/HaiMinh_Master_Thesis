# Thiết lập local

Chạy từ root `riscv-ibex-thesis`. Mục tiêu trước tiên là kiểm tra workspace,
sau đó mới có môi trường build. [Tool report](../../tools/tool-versions.md) là
nguồn trạng thái: **Vivado trên server — CONFIRMED BY USER**. Agent chưa truy cập
server hay kiểm chứng executable/license/build; người dùng cho phép giữ placeholder
server trong giai đoạn này.

```sh
make help
make doctor
make check
make vivado-check
```

Doctor liệt kê tool thiếu; không tự cài. Các check không cần FPGA có thể chạy
khi board TBD. Với host khác, ghi lại versions thay vì giữ kết quả host khởi tạo.

Môi trường build upstream cần Python/venv, Git, CMake, make, compiler C++,
Verilator và libelf headers; GCC bare-metal RV32IMC, objcopy, srecord.
OpenOCD >= 0.12.0 và RISC-V GDB phục vụ board debug; GTKWave dùng xem FST.
Nguồn: [prerequisites upstream](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/README.md),
[Verilator core configuration](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/ibex_demo_system.core).

Chỉ chạy các lệnh cài/tải sau khi đã sẵn sàng cho network/download trên máy local:

```sh
make upstream
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r third_party/python-requirements.in
python -m pip freeze > .venv/resolved-packages.txt
```

Giữ file freeze local, review trước khi đưa bản đã lọc vào báo cáo. Requirement
đã pin hai VCS refs; PyPI/transitive chưa khóa hoàn toàn, compatibility chưa
được build thử. Nếu venv thiếu, cài package venv theo hệ điều hành đang dùng;
không dùng `sudo pip`.

Demo `sw/c/gcc_toolchain.cmake` gọi **riscv32-unknown-elf-gcc** và
**riscv32-unknown-elf-objcopy**, với `-march=rv32imc -mabi=ilp32`.
Có riscv64 compiler + RV32 multilib chưa đủ để mặc định flow này chạy.
Cài toolchain có prefix được demo hỗ trợ, hoặc tạo toolchain CMake override
được review/test riêng; không tạo symlink giả chỉ để doctor xanh.

Chạy Vivado trên server của người dùng theo
[vivado-workflow](vivado-workflow.md); không cần cài Vivado vào host agent.
Server/đường dẫn/access vẫn TBD, không tự login hoặc giả định quyền. Linux native là đường đi đầu tiên;
WSL2 cần kiểm tra riêng USB passthrough/driver khi tới board debug. Không suy
từ simulation trong WSL2 ra JTAG truy cập được.

Sau setup: [simulation](simulation.md) → ADR board →
[FPGA bring-up](fpga-bringup.md). Nếu chưa có board, vẫn làm được học kiến trúc,
kiểm tra pins, firmware build và simulator sau khi có tools.
